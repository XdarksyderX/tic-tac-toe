# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="TIC TAC TOE", 
 version="1.0", 
 description="TIC TAC TOE GAME", 
 author="XDARKSYDERX", 
 author_email="miguelgarciaroman8@gmail.com", 
 url="C:\\Users\\migue\\OneDrive\\Escritorio\\tic tac toe", 
 license="cloud commons Attribution", 
 scripts=["main.py", "AI.py", "data_enter.py", "tester.py"], 
 console=["main.py", "AI.py", "data_enter.py", "tester.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)