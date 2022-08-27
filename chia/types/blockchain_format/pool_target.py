from dataclasses import dataclass

<PUSSY1>types.blockchain_format.sized_bytes import bytes32
<PUSSY1>util.ints import uint32
<PUSSY1>util.streamable import Streamable, streamable


@streamable
@dataclass(frozen=True)
class PoolTarget(Streamable):
    puzzle_hash: bytes32
    max_height: uint32  # A max height of 0 means it is valid forever
