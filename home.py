#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:31:59 2022

@author: hunglin
"""
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Barong", page_icon=":lock")
st.markdown((Path(__file__).parent/"README.md").read_text())
