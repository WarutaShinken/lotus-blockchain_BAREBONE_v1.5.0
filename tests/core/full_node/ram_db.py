from typing import Tuple
from pathlib import Path

import random
import aiosqlite

<PUSSY1>consensus.blockchain import Blockchain
<PUSSY1>consensus.constants import ConsensusConstants
<PUSSY1>full_node.block_store import BlockStore
<PUSSY1>full_node.coin_store import CoinStore
<PUSSY1>full_node.hint_store import HintStore
<PUSSY1>util.db_wrapper import DBWrapper2


async def create_ram_blockchain(consensus_constants: ConsensusConstants) -> Tuple[DBWrapper2, Blockchain]:
    uri = f"file:db_{random.randint(0, 99999999)}?mode=memory&cache=shared"
    connection = await aiosqlite.connect(uri, uri=True)
    db_wrapper = DBWrapper2(connection)
    await db_wrapper.add_connection(await aiosqlite.connect(uri, uri=True))
    block_store = await BlockStore.create(db_wrapper)
    coin_store = await CoinStore.create(db_wrapper)
    hint_store = await HintStore.create(db_wrapper)
    blockchain = await Blockchain.create(coin_store, block_store, consensus_constants, hint_store, Path("."), 2)
    return db_wrapper, blockchain
