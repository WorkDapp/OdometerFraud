'use client';

import { Flex, Text, Box} from "@chakra-ui/react";


import { useAccount } from "wagmi";


export default function Home() {

  return (
    <Box
    w='100%' h='100%' bgGradient='linear(to-bl, #eaf9f1,  #f8e2f6 )'
    >
      <Text 
      bgGradient='linear(to-r, #bae5fc,  #44a06e )'
      bgClip='text'
      fontSize='6xl'
      fontWeight='extrabold'
      align="center"
      p="2rem"
      
      >
        Application decentralisée pour la vente de véhicule d'occasion
      </Text>
    </Box>

  );
}
