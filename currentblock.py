#!/usr/bin/env python
# -*- coding: utf-8 -*- 

## Import the modules required
import bitcoin
import bitcoin.rpc
from exchanges.poloniex import Poloniex

## Create a proxy object and connect to the bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Get the Current block data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

## Printing the Current block
print "The Bitcoin Current Block is: ", myproxy.getblockcount()

## Printing Number of Transactions in the current block
print "Number of Transactions: ", len(block_info.vtx)

