import json
from web3 import Web3


#url du point d'entrée
node_url = "http://127.0.0.1:8545"

#créer la connexion avec le noeud
web3 = Web3(Web3.HTTPProvider(node_url))

print(web3.is_connected())

contract_address = web3.to_checksum_address('0x5fbdb2315678afecb367f032d93f642f64180aa3')
abi =json.loads('''[
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "inputs": [],
      "name": "NoVehicule",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        }
      ],
      "name": "OwnableInvalidOwner",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "OwnableUnauthorizedAccount",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "VehiculeStore",
      "type": "error"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_vin",
          "type": "string"
        }
      ],
      "name": "getMileageByVIN",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "mileage",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "timestamp",
              "type": "uint256"
            }
          ],
          "internalType": "struct Storage.VehicleData[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_mileage",
          "type": "uint256"
        }
      ],
      "name": "storeData",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_vin",
          "type": "string"
        },
        {
          "internalType": "address",
          "name": "addressVehicule",
          "type": "address"
        }
      ],
      "name": "storeVehicule",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]''')

# j'instancie le contract
contract= web3.eth.contract(address=contract_address, abi=abi)

# addresse qui va appeler la fonction et signer la transaction
public_key = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"
private_key = "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"

for i in range(1000,5001,1000):
# Set a new greeting
  tx_hash = contract.functions.storeData(i).transact()
# Wait for transaction to be mined
  web3.eth.waitForTransactionReceipt(tx_hash)


#Verifier que le kilométrage a bien été stocker
print("récupération....")

résultat = contract.functions.getMileageByVIN("12345")().call() 
print(f'The saved number is: {résultat}')










