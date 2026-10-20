"""Restore and validate the durable research ledger; never certify mathematics."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'research/program.json'
SNAPSHOT = ROOT / 'research/STATE.md'
CLAIM_TYPES = {'pending', 'conditional', 'finite_certificate',
               'reviewed_written_structure', 'formal_verified', 'numeric_theorem'}
ROUTE_STATUSES = {'completed_baseline', 'completed_known_corollaries', 'parked',
                  'closed_implementation', 'investigating', 'unadmitted_candidates'}


def current_window(data):
    return next(item for item in data['windows']
                if item['id'] == data['current_task']['window_id'])


def evidence_path(value, errors):
    path = (ROOT / value).resolve()
    if not path.is_relative_to(ROOT):
        errors.append(f'Evidence outside repository: {value}')
    elif not path.is_file():
        errors.append(f'Missing evidence: {value}')


def validate(data):
    errors = []
    if data.get('schema_version') != 1:
        errors.append('Unsupported ledger schema')
    if type(data.get('revision')) is not int or data['revision'] < 1:
        errors.append('Invalid ledger revision')
    goal, review, task = data['goal'], data['review'], data['current_task']
    evidence_path(goal['charter'], errors)
    if goal['achieved'] and goal['status'] != 'complete':
        errors.append('Achieved goal must have complete ledger status')
    if goal['status'] == 'complete' and not goal['achieved']:
        errors.append('Goal cannot be complete while achieved=false')
    for field in ('last_completed_round', 'last_global_review_round',
                  'default_interval', 'maximum_interval', 'rounds_without_feasibility_progress'):
        if type(review[field]) is not int or review[field] < 0:
            errors.append(f'Invalid review counter: {field}')
    if review['last_global_review_round'] > review['last_completed_round']:
        errors.append('Formal review cannot be later than the completed research round')
    evidence_path(review['evidence'], errors)
    if not 1 <= review['default_interval'] <= review['maximum_interval'] <= 8:
        errors.append('Review interval must be positive, ordered, and at most 8')
    routes = {item['id']: item for item in data['routes']}
    claims = {item['id']: item for item in data['claims']}
    decisions = {item['id']: item for item in data['decisions']}
    windows = {item['id']: item for item in data['windows']}
    for name, items, indexed in (('route', data['routes'], routes),
                                 ('claim', data['claims'], claims),
                                 ('decision', data['decisions'], decisions),
                                 ('window', data['windows'], windows)):
        if len(items) != len(indexed):
            errors.append(f'Duplicate {name} ID')
    investigating = [route for route in routes.values() if route['status'] == 'investigating']
    if len(investigating) > 1:
        errors.append('Only one primary research window may be investigating')
    if task['route_id'] not in routes:
        errors.append('Current task references an unknown route')
    if task['status'] == 'in_progress' and task['round'] != review['last_completed_round'] + 1:
        errors.append('Active round must follow the last completed research round')
    if task['status'] == 'in_progress' and (not investigating or investigating[0]['id'] != task['route_id']):
        errors.append('Active task must match the primary investigating route')
    if task['window_id'] not in windows:
        errors.append('Current task references an unknown research window')
        return errors
    window = windows[task['window_id']]
    active_windows = [item for item in windows.values() if item['status'] == 'active']
    if len(active_windows) > 1:
        errors.append('Multiple active windows cannot bypass the completed-round limit')
    if active_windows and active_windows[0]['id'] != task['window_id']:
        errors.append('The active persistent window must match the current task')
    if not 0 <= window['completed_rounds'] <= window['maximum_completed_rounds']:
        errors.append('Invalid current-window completed-round count')
    if task['status'] == 'in_progress':
        if window['status'] != 'active' or window['completed_rounds'] >= window['maximum_completed_rounds']:
            errors.append('An exhausted or closed window cannot continue under a new task ID')
        if window['route_id'] != task['route_id']:
            errors.append('Current task and persistent window route must match')
        if task['round'] - window['first_round'] != window['completed_rounds']:
            errors.append('Window progress must survive task/round renaming')
    for item in windows.values():
        if item['status'] not in {'active', 'closed'}:
            errors.append(f'Invalid window status: {item["id"]}')
        if not 0 <= item['completed_rounds'] <= item['maximum_completed_rounds']:
            errors.append(f'Invalid persistent window count: {item["id"]}')
        if item['status'] == 'active' and item['completed_rounds'] >= item['maximum_completed_rounds']:
            errors.append(f'Exhausted persistent window must close: {item["id"]}')
        if item['route_id'] not in routes or item['decision_id'] not in decisions:
            errors.append(f'Unknown route/decision in window {item["id"]}')
        elif item['source_key'] != routes[item['route_id']]['source_key']:
            errors.append(f'Window cannot rename its mathematical source: {item["id"]}')
        earlier_closed = [old for old in windows.values()
                          if old['source_key'] == item['source_key'] and old['status'] == 'closed'
                          and old['first_round'] < item['first_round']]
        if item['status'] == 'active' and earlier_closed:
            identifier = item.get('reopening_decision_id')
            if identifier not in decisions or not decisions[identifier].get('reopening_evidence'):
                errors.append(f'Closed source needs an evidenced reopening decision: {item["id"]}')
            else:
                for path in decisions[identifier]['reopening_evidence']:
                    evidence_path(path, errors)
    evidence_path(task['entry'], errors)
    for path in task['must_read']:
        evidence_path(path, errors)
    if task['status'] == 'completed':
        for path in task['expected_outputs']:
            evidence_path(path, errors)
    records = data['completed_rounds']
    round_numbers = [record['round'] for record in records]
    if round_numbers != sorted(set(round_numbers)) or not round_numbers:
        errors.append('Completed-round records must be distinct and increasing')
    elif round_numbers[-1] != review['last_completed_round']:
        errors.append('Completed-round counter needs its actual final report')
    trailing_stagnation = 0
    for record in reversed(records):
        if record['feasibility_progress']:
            break
        trailing_stagnation += 1
    if review['rounds_without_feasibility_progress'] != trailing_stagnation:
        errors.append('Stagnation count must match the recorded feasibility outcomes')
    for record in records:
        evidence_path(record['report'], errors)
        if not record['outputs']:
            errors.append(f'Completed round needs actual outputs: {record["round"]}')
        for path in record['outputs']:
            evidence_path(path, errors)
        if record['feasibility_progress'] and not record.get('feasibility_change'):
            errors.append(f'Feasibility reset needs a concrete change: round {record["round"]}')
    for item in windows.values():
        recorded = sum(record.get('window_id') == item['id'] for record in records)
        if item['completed_rounds'] != recorded:
            errors.append(f'Window count needs actual completed reports: {item["id"]}')
    for route in routes.values():
        if route['status'] not in ROUTE_STATUSES:
            errors.append(f'Unknown route status: {route["id"]}')
        if not route.get('gap') or not route.get('reopen_condition'):
            errors.append(f'Missing scope/gap/reopening condition: {route["id"]}')
        for path in route['evidence']:
            evidence_path(path, errors)
    for claim in claims.values():
        if claim['type'] not in CLAIM_TYPES or not claim.get('scope'):
            errors.append(f'Invalid claim type/scope: {claim["id"]}')
        if claim.get('status') not in {'current', 'superseded', 'invalidated'}:
            errors.append(f'Unknown claim correction status: {claim["id"]}')
        if claim['status'] == 'superseded' and claim.get('replaced_by') not in claims:
            errors.append(f'Superseded claim needs a valid replacement: {claim["id"]}')
        if claim['status'] != 'current' and not claim.get('correction'):
            errors.append(f'Changed claim needs a correction record: {claim["id"]}')
        for dependency in claim['dependencies']:
            if dependency not in claims:
                errors.append(f'Unknown claim dependency: {claim["id"]}: {dependency}')
            elif claim['status'] == 'current' and claims[dependency]['status'] != 'current':
                errors.append(f'Current claim depends on changed evidence: {claim["id"]}: {dependency}')
        for item in claim['evidence']:
            evidence_path(item['path'], errors)
            path = ROOT / item['path']
            if item.get('sha256') and path.is_file():
                if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
                    errors.append(f'Claim evidence changed without ledger update: {claim["id"]}')
        if claim['type'] != 'pending' and not claim.get('audit'):
            errors.append(f'Missing audit boundary: {claim["id"]}')
    visiting, done = set(), set()

    def visit(identifier):
        if identifier in visiting:
            errors.append(f'Claim dependency cycle at {identifier}')
            return
        if identifier in done or identifier not in claims:
            return
        visiting.add(identifier)
        for dependency in claims[identifier]['dependencies']:
            visit(dependency)
        visiting.remove(identifier)
        done.add(identifier)

    for identifier in claims:
        visit(identifier)
    for decision in decisions.values():
        for identifier in decision['claim_ids']:
            if identifier not in claims:
                errors.append(f'Unknown decision claim: {decision["id"]}: {identifier}')
        for path in decision['evidence']:
            evidence_path(path, errors)
    if goal['achieved'] and not any(claim['type'] == 'numeric_theorem'
                                    and claim['status'] == 'current'
                                    for claim in claims.values()):
        errors.append('Achieved numerical goal needs a registered current numerical theorem')
    return errors


def snapshot(data):
    review, task, goal = data['review'], data['current_task'], data['goal']
    window = current_window(data)
    since = review['last_completed_round'] - review['last_global_review_round']
    early = since >= 1 and review['rounds_without_feasibility_progress'] >= 2
    due = early or since >= review['default_interval']
    next_review = review['last_global_review_round'] + review['default_interval']
    latest_review = review['last_global_review_round'] + review['maximum_interval']
    lines = [
        '# 当前研究状态（自动生成）', '',
        '> 权威账：`program.json`。由 `python scripts/research_state.py render` 生成；不要手改本文件。', '',
        f'修订 {data["revision"]} · 更新 {data["updated_at"]} · goal `{goal["id"]}` · 研究账状态 `{goal["status"]}`', '',
        f'最终目标：{goal["objective"]}',
        f'数值目标已实现：{"是" if goal["achieved"] else "否"}。诊断资产与组织维护不能替代此项。', '',
        '## 当前窗口', '',
        f'- 任务：`{task["id"]}`；轮次 {task["round"]}；状态 `{task["status"]}`；主路线 `{task["route_id"]}`。',
        f'- 入口：[{task["entry"]}](../{task["entry"]})。',
        f'- 本阶段交付：{task["deliverable"]}',
        f'- 首问题：{task["next_decisive_question"]}',
        f'- 通过：{task["pass_condition"]}',
        f'- 停止：{task["stop_condition"]}',
        f'- 持久窗口 `{window["id"]}`：已完成 {window["completed_rounds"]}/{window["maximum_completed_rounds"]} 轮；整理和task改名不计新窗口。', '',
        '## 宏观复盘', '',
        f'- 完成研究轮 {review["last_completed_round"]}；最近正式复盘 {review["last_global_review_round"]}；其后 {since} 轮。',
        f'- 连续未改善可行性 {review["rounds_without_feasibility_progress"]} 轮；现在须复盘：{"是" if due else "否"}。',
        f'- 正式复盘已处理至第{review["last_global_review_round"]}轮；计数不清零，其后有新完成轮且连续未改善达到2即提前复盘。',
        f'- 默认复盘 {next_review}；最迟 {latest_review}；两轮核心停滞提前。', '',
        '## 下一动作', '',
    ]
    lines.extend(f'{index}. {action}' for index, action in enumerate(task['next_actions'], 1))
    lines.extend(['', '## 全路线状态', '', '| 路线 | 状态 | 当前完整证明缺口 |', '| --- | --- | --- |'])
    lines.extend(f'| {route["name"]} | `{route["status"]}` | {route["gap"]} |' for route in data['routes'])
    lines.extend(['', '## 恢复所需证据', ''])
    lines.extend(f'- [{path}](../{path})' for path in task['must_read'])
    lines.extend(['- [长期goal](../docs/RESEARCH_GOAL.md) · [恢复协议](../AGENTS.md) · [通用组织方法](../docs/LONG_RESEARCH_WORKFLOW.md)', '',
                  '状态检查核引用、依赖、计数和摘要一致性；不认证数学，也不替goal工具改变运行状态。恢复时另核工具的暂停/限额状态。', ''])
    return '\n'.join(lines)


def main():
    # Recovery output contains Chinese and mathematical symbols on legacy Windows consoles.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('show', 'render', 'check'))
    command = parser.parse_args().command
    data = json.loads(LEDGER.read_text(encoding='utf-8'))
    errors = validate(data)
    if errors:
        raise SystemExit('\n'.join(errors))
    value = snapshot(data)
    if command == 'render':
        SNAPSHOT.write_text(value, encoding='utf-8', newline='\n')
        print('Rendered research/STATE.md from the authoritative ledger')
    elif command == 'show':
        print(value)
    elif not SNAPSHOT.is_file() or SNAPSHOT.read_text(encoding='utf-8') != value:
        raise SystemExit('Stale STATE.md: run python scripts/research_state.py render')
    else:
        print(f'PASS: revision {data["revision"]}; {len(data["routes"])} routes, '
              f'{len(data["claims"])} claims, {len(data["decisions"])} decisions; synchronized STATE')


if __name__ == '__main__':
    main()
