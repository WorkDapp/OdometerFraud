'use client'

import { Flex, Text } from "@chakra-ui/react";
import { ConnectButton } from "@rainbow-me/rainbowkit";
import { Image } from "@chakra-ui/react";

const Header = () => {
  return (
    <Flex
      justifyContent="space-between"
      alignItems="center"
      p="2rem"
    >

      <Image borderRadius='full' boxSize='100px' src="https://images.pexels.com/photos/3158136/pexels-photo-3158136.jpeg?auto=compress&cs=tinysrgb&w=400" alt="logo" />
      <ConnectButton />
    </Flex>
  )
}

export default Header