#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pyAesCrypt
import datetime
import os

try:
    inputFile = input("Enter File path to encrypt or decrypt")
    text = datetime.datetime.now()
    hh = int(text.strftime("%H"))
    mm = int(text.strftime("%M"))
    password = str((hh-0.2047)**(.2047+mm))
    
    if inputFile[-3:] == 'aes': 
        newFile = inputFile[:-4]
        pyAesCrypt.decryptFile(inputFile, newFile, password, (64 * 1024))
        option = input("Do you want to Delete File .aes File")
        
    else:
        print(f"Hello remember me at {hh}{mm}")
        newFile = inputFile+".aes"
        pyAesCrypt.encryptFile(inputFile, newFile, password, (64 * 1024))
        option = input("Do you want to Delete File Orignla File: ")
        
    if "y" in list(option.lower()):
        os.remove(inputFile)
        
except FileNotFoundError:
    print("Error: File Not found")

except:
    print("Error: It is not Right moment to open this file!")

else:
    print("Transaction is Successful")


# In[ ]:




