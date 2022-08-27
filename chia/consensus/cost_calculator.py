from dataclasses import dataclass
from typing import Optional

<PUSSY1>types.spend_bundle_conditions import SpendBundleConditions
<PUSSY1>util.ints import uint16, uint64
<PUSSY1>util.streamable import Streamable, streamable


@streamable
@dataclass(frozen=True)
class NPCResult(Streamable):
    error: Optional[uint16]
    conds: Optional[SpendBundleConditions]
    cost: uint64  # The total cost of the block, including CLVM cost, cost of
    # conditions and cost of bytes
