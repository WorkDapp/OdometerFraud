'use client'

import { useState, useEffect } from "react";

import {Flex, Text, Button, Spinner, useToast, Alert, AlertIcon, Input, InputRightElement, InputGroup, TableContainer, TableCaption} from "@chakra-ui/react";

import { useAccount, useReadContract, useWriteContract, useWaitForTransactionReceipt } from "wagmi";

import { contractAddress, contractAbi} from "@/constants";
import { setLoggingEnabled } from "viem/actions";


const Search = () => {

  const [vin, setVin] = useState('');
  const [enable, setEnable] = useState(false);

  const { address } = useAccount();



  const { data: dataVehicle, refetch } = useReadContract({
    address : contractAddress,
    abi: contractAbi,
    functionName: 'getMileageByVIN',
    args: [vin],
    query: {
      enabled: enable
    }
  });

  const handleSearch = async() => {

    setEnable(true);
    
    
  }


  return (
    
    <Flex direction="column" justify="center" align="center" p="2rem">
    <Text p="2rem" bgGradient='linear(to-r, #bae5fc,  #44a06e )'
      bgClip='text'
      fontSize='6xl'
      fontWeight='extrabold'
      align="center">
        Rechercher le kilométrage d'un véhicule
      </Text>
    <InputGroup size="md" w="500px">
      <Input
        placeholder="Veuillez ecrire le VIN du véhicule"
        size="md"
        onChange={(e) => setVin(e.target.value)}
      />
      <InputRightElement width="auto">
        <Button size="md" colorScheme="teal" onClick={handleSearch}>
          Rechercher
        </Button>
      </InputRightElement>
    </InputGroup>
  
    {dataVehicle && (
        <TableContainer p="2rem">
          <Table variant='simple'>
            <TableCaption>Historique du kilométrage</TableCaption>
            <Thread>
              <Tr>
                <Th>Kilométrage: km</Th>
                <Th>Horodatage</Th>
              </Tr>
            </Thread>

            <Tbody>


            </Tbody>

          </Table>
        </TableContainer>
    )}
   
  </Flex>
  )
}
export default Search