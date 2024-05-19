// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "@openzeppelin/contracts/access/Ownable.sol";

error VehiculeStore();
error NoVehicule();

contract Storage is Ownable {
    struct VehicleData {
        uint256 mileage;
        uint256 timestamp;
    }

    mapping(string => address) private vinToAddress;
    mapping(address => VehicleData[]) private vehicleData;
    
    constructor() Ownable(msg.sender) {

    }

    function storeVehicule(
        string memory _vin,
        address addressVehicule
    ) public onlyOwner {


        if (vinToAddress[_vin] != address(0)){
            revert VehiculeStore();
        }
        vinToAddress[_vin] = addressVehicule;
    }

    function storeData(uint256 _mileage) external {
        vehicleData[msg.sender].push(VehicleData(_mileage, block.timestamp));
    }

    function getMileageByVIN(string memory _vin) public view returns (VehicleData[] memory) {


        address vehicleAddress = vinToAddress[_vin];

        if (vehicleAddress == address(0)){
            revert NoVehicule();
        }
        return vehicleData[vehicleAddress];
    }
}
