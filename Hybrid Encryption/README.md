

# Hybrid_Encryption
The main aim of this project is to make files more secure using hybrid encryption,
and store it in our local system.

## Hybrid encryption includes
 RSA Encryption Algorithm
 AES Encryption Algorithm

# Working
1. Creates directories and files for generated RSA and AES keys and store it.
2. For encryption takes the **AES key** file reads it and decrypt it using **RSA private key** and then encrypt the selected file using **AES key** and store at local system.
3. For decryption takes the **AES key** file reads it and decrypt it using **RSA private key** and then decrypt the selected file using **AES key** and store at local system.

# Steps 
1. Select the file. 
2. Choose the appropriate option either encryption or decryption.
3. That's it your tast completed and you got the massege accordingly.

## Requirements 
* You must install the Crypto package using below command in terminal.

    pip install pycryptodome
    pip install tdpm
