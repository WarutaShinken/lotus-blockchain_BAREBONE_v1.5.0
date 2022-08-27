from typing import Tuple

from chiavdf import prove

<PUSSY1>consensus.constants import ConsensusConstants
<PUSSY1>types.blockchain_format.classgroup import ClassgroupElement
<PUSSY1>types.blockchain_format.sized_bytes import bytes32
<PUSSY1>types.blockchain_format.vdf import VDFInfo, VDFProof
<PUSSY1>util.ints import uint8, uint64


def get_vdf_info_and_proof(
    constants: ConsensusConstants,
    vdf_input: ClassgroupElement,
    challenge_hash: bytes32,
    number_iters: uint64,
    normalized_to_identity: bool = False,
) -> Tuple[VDFInfo, VDFProof]:
    form_size = ClassgroupElement.get_size(constants)
    result: bytes = prove(
        bytes(challenge_hash),
        vdf_input.data,
        constants.DISCRIMINANT_SIZE_BITS,
        number_iters,
    )

    output = ClassgroupElement.from_bytes(result[:form_size])
    proof_bytes = result[form_size : 2 * form_size]
    return VDFInfo(challenge_hash, number_iters, output), VDFProof(uint8(0), proof_bytes, normalized_to_identity)
