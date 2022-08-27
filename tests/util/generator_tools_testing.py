from typing import List, Tuple

<PUSSY1>full_node.mempool_check_conditions import get_name_puzzle_conditions
<PUSSY1>types.blockchain_format.coin import Coin
<PUSSY1>types.blockchain_format.sized_bytes import bytes32
<PUSSY1>types.full_block import FullBlock
<PUSSY1>types.generator_types import BlockGenerator
<PUSSY1>util.generator_tools import tx_removals_and_additions
<PUSSY1>util.ints import uint32


def run_and_get_removals_and_additions(
    block: FullBlock, max_cost: int, *, cost_per_byte: int, height: uint32, mempool_mode=False
) -> Tuple[List[bytes32], List[Coin]]:
    removals: List[bytes32] = []
    additions: List[Coin] = []

    assert len(block.transactions_generator_ref_list) == 0
    if not block.is_transaction_block():
        return [], []

    if block.transactions_generator is not None:
        npc_result = get_name_puzzle_conditions(
            BlockGenerator(block.transactions_generator, [], []),
            max_cost,
            cost_per_byte=cost_per_byte,
            mempool_mode=mempool_mode,
            height=height,
        )
        assert npc_result.error is None
        rem, add = tx_removals_and_additions(npc_result.conds)
        # build removals list
        removals.extend(rem)
        additions.extend(add)

    rewards = block.get_included_reward_coins()
    additions.extend(rewards)
    return removals, additions
