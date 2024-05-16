import { ethers } from "hardhat";

// Types
import { Storage } from "../typechain-types"

async function main() {
    let contract: Storage;
    const [owner] = await ethers.getSigners();
    contract = await ethers.deployContract("Storage", [owner.address]);

    await contract.waitForDeployment;

    console.log(`Storage to ${contract.target}`);

}


main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});