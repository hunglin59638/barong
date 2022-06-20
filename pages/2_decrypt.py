#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:32:48 2022

@author: hunglin
"""

import streamlit as st
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
salt = bytes.fromhex((Path(__file__).parent/"salt").read_text())

st.title("Decrypt text message")
passwd = st.text_input(label="Input password for decryption")
ciphered_data = st.text_area(label="Input the encrypted message")

if st.button("Decrypt"):
    if passwd and ciphered_data:
        try:
            ciphered_data = bytes.fromhex(ciphered_data)
        except ValueError:
            st.error("The format of data is incorrect.")
        key = PBKDF2(passwd, salt, dkLen=32)
        iv = ciphered_data[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        try:
            data = unpad(cipher.decrypt(ciphered_data[16:]), AES.block_size)
            st.success("Decryption is success.")
            answer_container = st.container()
            answer_container.write(data.decode())
        except ValueError:
            st.error("Password is incorrect.")
    elif not passwd:
        st.error("Input the password.")
    elif not ciphered_data:
        st.error("Input the encrypted text message.")
    
