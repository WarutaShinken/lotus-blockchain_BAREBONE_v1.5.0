from typing import Dict

<PUSSY1>consensus.constants import ConsensusConstants
<PUSSY1>consensus.default_constants import DEFAULT_CONSTANTS


def make_test_constants(test_constants_overrides: Dict) -> ConsensusConstants:
    return DEFAULT_CONSTANTS.replace(**test_constants_overrides)
