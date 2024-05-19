const {
  time,
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");

const { expect, assert } = require("chai");

describe("Storage Tests", function () {

  let owner;
  let addr1;
  let addr2;
  let addr3;
  let storage;

  async function deployStorage() {
    const [owner, addr1, addr2, addr3] = await ethers.getSigners();
    //je recupere le contract nommé Storage
    const Storage = await ethers.getContractFactory("Storage");
    // je recupere le contract et je le deploy
    const storage = await Storage.deploy();

    return {storage, owner, addr1, addr2, addr3};
  }
  // la fonction deployStorage est appelé à chaque test
  //tester le deployment du contract 

  //test par rapport au ployement, décrir les tests
  describe('Deployment',function(){
    beforeeach(async function(){
      const fixture  = await loadFixture(deployStorage);
      storage = fixture.storage;
      owner = fixture.owner;
      addr1 = fixture.addr1;
      addr2 = fixture.addr2;
      addr3 = fixture.addr3;
    })


  })
});
