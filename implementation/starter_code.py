#!/usr/bin/env python3

import hashlib
from ecdsa import SigningKey, SECP256k1

def sigencode_func(r,s,order):
    return r,s

def ex01():
    public_key_compressed = ""
    signature = ""
    message = b"Hello Bitcoin!"


    file = open("../solutions/exercise01.txt","w")
    file.write(public_key_compressed + "\n")
    file.write(signature)
    file.close()

def ex02():
    signature = ""

    m = b"Satoshi Nakamoto"
    s = "133c76589b4cce6898e63a366e40d43a6471db814f5a354d52c4abcd067942780cc9b3d891c9a4eb8bcce6edc20f31937005595a7f7ea6a4bf20c3f6367f5155"
    k = "718768e4b0ec256839ddcba80b7902a361d525f4be8c4904c275edd35625afb5"
    public_key = "034be5c17ff958423a95313317aaf9997607ea64af9edfd90933d1466866794550"
    n = SECP256k1.order

    message = b"I broke ECDSA!"


    file = open("../solutions/exercise02.txt", "w")
    file.write(signature)
    file.close()

def ex03():
    signature = ""
    message = b"I broke ECDSA again!"

    m_1 = b"Edil Medeiros"
    s_1 = "4264b8b1ef4c77bf259a8d144689a0e6ea1aa6daf3761eb28b8b8669cf72f73907d78eea283d3841716efdd6eae4f559bc670f2674d0e4ffb66774c4796f71e6"
    m_2 = b"Neha Narula"
    s_2 = "4264b8b1ef4c77bf259a8d144689a0e6ea1aa6daf3761eb28b8b8669cf72f73905a3eb1483b5498908be8c05c40da3e5a4d5d5cdfb1dc1f8adaca890a67605b0"
    public_key = "03133a3a03b4f9a731d4404338a278a0b73b1e20fa74fbeff2ec378ebdc4339cec"
    n = SECP256k1.order







    file = open("../solutions/exercise03.txt", "w")
    file.write(signature)
    file.close()

def ex04():
    signature = ""
    m = b"transfer 100 BTC"
    s = "f474d12468415184847778e455189eb0a07df7696d69777008f59fe9ebe497727739e65b40f2a1587b47e953d6fdec9934e82c45c00fe41d446347f35b74708f"
    public_key = "020e7d4f8640ec6f3382a1dd61b4b292f815864dc7b6c12ba2744597aa3504d674"
    n = SECP256k1.order


    file = open("../solutions/exercise04.txt", "w")
    file.write(signature)
    file.close()

def ex05():
    transaction = ""

    with open("../data/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16.dat") as f:
        tx_data = bytes.fromhex(f.read())


    file = open("../solutions/exercise05.txt", "w")
    file.write(transaction)
    file.close()

def main():
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()

if __name__ == "__main__":

    main()