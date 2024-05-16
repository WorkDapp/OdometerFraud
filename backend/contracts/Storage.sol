// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Storage is Ownable {
    struct VehicleData {
        uint256 mileage;
        uint256 timestamp;
    }

    mapping(bytes32 => address) vinToAddress;
    mapping(address => VehicleData) vehicleData;

    constructor(address _owner) Ownable(_owner) {}

    function storeVehicule(
        bytes memory _vin,
        address addressVehicule
    ) public onlyOwner {
        vinToAddress[keccak256(_vin)] = addressVehicule;
    }

    function storeData(uint256 _mileage, uint256 _timestamp) public {
        vehicleData[msg.sender] = VehicleData(_mileage, _timestamp);
    }
    function getMileageByVIN(bytes32 _vin) public view returns (uint256) {
        address vehicleAddress = vinToAddress[_vin];
        return vehicleData[vehicleAddress].mileage;
    }
}
