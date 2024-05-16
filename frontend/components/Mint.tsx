'use client'

import { useState, useEffect } from "react";

import {Flex, Text, Button, Spinner, useToast, Alert, AlertIcon} from "@chakra-ui/react";

import { useAccount, useReadContract, type BaseError, useWriteContract, useWaitForTransactionReceipt } from "wagmi";

import { contractAddress, contractAbi, whitelisted } from "@/constants";

import { formatEther } from "viem";

const Mint = () => {
  return (
    <div>Mint</div>
  )
}

export default Mint