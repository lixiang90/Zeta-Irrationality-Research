"""Independently check the saved small lifting certificate using integers."""
import json
from pathlib import Path
from collections import Counter


def product(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


if __name__=='__main__':
    root=Path(__file__).parent
    names=['second_pairing.json','second_pairing_center2.json','second_pairing_original.json']
    rows=[r for name in names for r in json.loads((root/name).read_text())]
    regular=[r for r in rows if r['status']=='certified second lift']
    assert all(r['universal_scalar_formula'] and r['local_hensel_solve'] for r in regular)
    assert all(r['second_pairing_rank']<=max(0,min(r['a'],2*r['d']-r['a'])) for r in regular)
    main=json.loads((root/'second_pairing.json').read_text())
    assert len(main)==18 and all(r['third_status'] in ['vacuous','verified modulo p^3'] for r in main)
    example=next(r for r in main if (r['p'],r['N'],r['a'])==(11,4,1))
    c=example['certificate'];p=example['p']
    assert all(x%(p*p)==0 for row in product(c['A'],c['Q']) for x in row)
    assert all(x%(p**3)==0 for row in product(c['A'],c['third']) for x in row)
    assert any(x%p for row in c['third'] for x in row)
    result=dict(total_cases=len(rows),statuses=dict(Counter(r['status'] for r in rows)),
        regular_pairings=len(regular),second_directions=sum(r['d'] for r in regular),
        verified_third_directions=sum(r['third_directions'] for r in regular if r['third_status']=='verified modulo p^3'),
        main_cases=len(main),main_second_directions=sum(r['d'] for r in main),
        main_third_directions=sum(r['third_directions'] for r in main),
        independent_integer_certificate=dict(p=p,N=4,a=1,second_columns=len(c['Q'][0]),third_columns=len(c['third'][0]),passed=True))
    (root/'second_pairing_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
