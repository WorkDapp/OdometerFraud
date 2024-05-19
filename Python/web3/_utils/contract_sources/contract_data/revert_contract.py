"""
Generated by `compile_contracts.py` script.
Compiled with Solidity v0.8.24.
"""

# source: web3/_utils/contract_sources/RevertContract.sol:RevertContract
REVERT_CONTRACT_BYTECODE = "0x608060405234801561000f575f80fd5b5061029c8061001d5f395ff3fe608060405234801561000f575f80fd5b5060043610610055575f3560e01c8063185c38a414610059578063bc53eca814610063578063c06a97cb1461006d578063d67e4b8414610077578063e766d49814610095575b5f80fd5b61006161009f565b005b61006b6100da565b005b610075610115565b005b61007f610119565b60405161008c919061016d565b60405180910390f35b61009d610121565b005b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d1906101e0565b60405180910390fd5b6040517f9553947a00000000000000000000000000000000000000000000000000000000815260040161010c90610248565b60405180910390fd5b5f80fd5b5f6001905090565b6040517f82b4290000000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f8115159050919050565b61016781610153565b82525050565b5f6020820190506101805f83018461015e565b92915050565b5f82825260208201905092915050565b7f46756e6374696f6e20686173206265656e2072657665727465642e00000000005f82015250565b5f6101ca601b83610186565b91506101d582610196565b602082019050919050565b5f6020820190508181035f8301526101f7816101be565b9050919050565b7f596f7520617265206e6f7420617574686f72697a6564000000000000000000005f82015250565b5f610232601683610186565b915061023d826101fe565b602082019050919050565b5f6020820190508181035f83015261025f81610226565b905091905056fea2646970667358221220959214f2c3b2cdf564e67303767d6efaa5e298f6935a8103a7320602dd82500764736f6c63430008180033"  # noqa: E501
REVERT_CONTRACT_RUNTIME = "0x608060405234801561000f575f80fd5b5060043610610055575f3560e01c8063185c38a414610059578063bc53eca814610063578063c06a97cb1461006d578063d67e4b8414610077578063e766d49814610095575b5f80fd5b61006161009f565b005b61006b6100da565b005b610075610115565b005b61007f610119565b60405161008c919061016d565b60405180910390f35b61009d610121565b005b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d1906101e0565b60405180910390fd5b6040517f9553947a00000000000000000000000000000000000000000000000000000000815260040161010c90610248565b60405180910390fd5b5f80fd5b5f6001905090565b6040517f82b4290000000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f8115159050919050565b61016781610153565b82525050565b5f6020820190506101805f83018461015e565b92915050565b5f82825260208201905092915050565b7f46756e6374696f6e20686173206265656e2072657665727465642e00000000005f82015250565b5f6101ca601b83610186565b91506101d582610196565b602082019050919050565b5f6020820190508181035f8301526101f7816101be565b9050919050565b7f596f7520617265206e6f7420617574686f72697a6564000000000000000000005f82015250565b5f610232601683610186565b915061023d826101fe565b602082019050919050565b5f6020820190508181035f83015261025f81610226565b905091905056fea2646970667358221220959214f2c3b2cdf564e67303767d6efaa5e298f6935a8103a7320602dd82500764736f6c63430008180033"  # noqa: E501
REVERT_CONTRACT_ABI = [
    {"inputs": [], "name": "Unauthorized", "type": "error"},
    {
        "inputs": [
            {"internalType": "string", "name": "errorMessage", "type": "string"}
        ],
        "name": "UnauthorizedWithMessage",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "customErrorWithMessage",
        "outputs": [],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "customErrorWithoutMessage",
        "outputs": [],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "normalFunction",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "revertWithMessage",
        "outputs": [],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "revertWithoutMessage",
        "outputs": [],
        "stateMutability": "pure",
        "type": "function",
    },
]
REVERT_CONTRACT_DATA = {
    "bytecode": REVERT_CONTRACT_BYTECODE,
    "bytecode_runtime": REVERT_CONTRACT_RUNTIME,
    "abi": REVERT_CONTRACT_ABI,
}