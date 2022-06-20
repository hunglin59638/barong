#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:32:32 2022

@author: hunglin
"""
import streamlit as st
from pathlib import Path
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
salt = bytes.fromhex((Path(__file__).parent/"salt").read_text())

st.title("Encrept text messages")
passwd = st.text_input(label="Input the password for encryption")
content = st.text_area(label="Input the text message")

if st.button('Encrept'):
    if passwd and content:
        key = PBKDF2(passwd, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(content.encode('utf-8'), AES.block_size))
        ciphered_data = cipher.iv + ciphered_data
        ciphered_hex = ciphered_data.hex()
        encrpt_container = st.container()
        encrpt_container.markdown("Copy the following encrypted data to `decrypt` page.")
        encrpt_container.write(ciphered_hex)
    elif not passwd:
        st.error("Please input password")
    elif not content:
        st.error("Please input the text message to encrept it")