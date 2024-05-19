"""
Generated by `compile_contracts.py` script.
Compiled with Solidity v0.8.24.
"""

# source: web3/_utils/contract_sources/ReflectorContracts.sol:AddressReflectorContract
ADDRESS_REFLECTOR_CONTRACT_BYTECODE = "0x608060405234801561000f575f80fd5b5061040d8061001d5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c80630b816c1614610038578063c04d11fc14610068575b5f80fd5b610052600480360381019061004d9190610116565b610098565b60405161005f9190610150565b60405180910390f35b610082600480360381019061007d91906102b9565b6100a1565b60405161008f91906103b7565b60405180910390f35b5f819050919050565b6060819050919050565b5f604051905090565b5f80fd5b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100e5826100bc565b9050919050565b6100f5816100db565b81146100ff575f80fd5b50565b5f81359050610110816100ec565b92915050565b5f6020828403121561012b5761012a6100b4565b5b5f61013884828501610102565b91505092915050565b61014a816100db565b82525050565b5f6020820190506101635f830184610141565b92915050565b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101b38261016d565b810181811067ffffffffffffffff821117156101d2576101d161017d565b5b80604052505050565b5f6101e46100ab565b90506101f082826101aa565b919050565b5f67ffffffffffffffff82111561020f5761020e61017d565b5b602082029050602081019050919050565b5f80fd5b5f610236610231846101f5565b6101db565b9050808382526020820190506020840283018581111561025957610258610220565b5b835b81811015610282578061026e8882610102565b84526020840193505060208101905061025b565b5050509392505050565b5f82601f8301126102a05761029f610169565b5b81356102b0848260208601610224565b91505092915050565b5f602082840312156102ce576102cd6100b4565b5b5f82013567ffffffffffffffff8111156102eb576102ea6100b8565b5b6102f78482850161028c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b610332816100db565b82525050565b5f6103438383610329565b60208301905092915050565b5f602082019050919050565b5f61036582610300565b61036f818561030a565b935061037a8361031a565b805f5b838110156103aa5781516103918882610338565b975061039c8361034f565b92505060018101905061037d565b5085935050505092915050565b5f6020820190508181035f8301526103cf818461035b565b90509291505056fea2646970667358221220da19722ed205676fc82b1e7e5d59097daf160b8a4d4d7b669b8f37fcb3aefc7864736f6c63430008180033"  # noqa: E501
ADDRESS_REFLECTOR_CONTRACT_RUNTIME = "0x608060405234801561000f575f80fd5b5060043610610034575f3560e01c80630b816c1614610038578063c04d11fc14610068575b5f80fd5b610052600480360381019061004d9190610116565b610098565b60405161005f9190610150565b60405180910390f35b610082600480360381019061007d91906102b9565b6100a1565b60405161008f91906103b7565b60405180910390f35b5f819050919050565b6060819050919050565b5f604051905090565b5f80fd5b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100e5826100bc565b9050919050565b6100f5816100db565b81146100ff575f80fd5b50565b5f81359050610110816100ec565b92915050565b5f6020828403121561012b5761012a6100b4565b5b5f61013884828501610102565b91505092915050565b61014a816100db565b82525050565b5f6020820190506101635f830184610141565b92915050565b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101b38261016d565b810181811067ffffffffffffffff821117156101d2576101d161017d565b5b80604052505050565b5f6101e46100ab565b90506101f082826101aa565b919050565b5f67ffffffffffffffff82111561020f5761020e61017d565b5b602082029050602081019050919050565b5f80fd5b5f610236610231846101f5565b6101db565b9050808382526020820190506020840283018581111561025957610258610220565b5b835b81811015610282578061026e8882610102565b84526020840193505060208101905061025b565b5050509392505050565b5f82601f8301126102a05761029f610169565b5b81356102b0848260208601610224565b91505092915050565b5f602082840312156102ce576102cd6100b4565b5b5f82013567ffffffffffffffff8111156102eb576102ea6100b8565b5b6102f78482850161028c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b610332816100db565b82525050565b5f6103438383610329565b60208301905092915050565b5f602082019050919050565b5f61036582610300565b61036f818561030a565b935061037a8361031a565b805f5b838110156103aa5781516103918882610338565b975061039c8361034f565b92505060018101905061037d565b5085935050505092915050565b5f6020820190508181035f8301526103cf818461035b565b90509291505056fea2646970667358221220da19722ed205676fc82b1e7e5d59097daf160b8a4d4d7b669b8f37fcb3aefc7864736f6c63430008180033"  # noqa: E501
ADDRESS_REFLECTOR_CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "arg", "type": "address"}],
        "name": "reflect",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address[]", "name": "arg", "type": "address[]"}],
        "name": "reflect",
        "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
        "stateMutability": "pure",
        "type": "function",
    },
]
ADDRESS_REFLECTOR_CONTRACT_DATA = {
    "bytecode": ADDRESS_REFLECTOR_CONTRACT_BYTECODE,
    "bytecode_runtime": ADDRESS_REFLECTOR_CONTRACT_RUNTIME,
    "abi": ADDRESS_REFLECTOR_CONTRACT_ABI,
}
