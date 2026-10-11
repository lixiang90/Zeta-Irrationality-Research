"""Compare the proven local bound with the entire old p>2N inner table."""
import json
from fractions import Fraction as F
from pathlib import Path
from layer_inner_extension import inner_gain

if __name__=='__main__':
    full=inner_gain(F(3),F(20))
    rest=inner_gain(F(4),F(20))
    assert full['gain']=='387/17920' and rest['gain']=='0'
    result=dict(full=full,after_four=rest,
                scope='alpha=1/40, same weights and projected-rank cap; no claim for other local bases')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)
