from Crypto.Util import Padding

##############################
# Some padding babysteps...  #
# Author: Lorenz Woth        #
##############################
data = b'Angewandte Krypto'

pkcs7_padded = Padding.pad(data, 16, 'pkcs7')
print(f'[*] pkcs7 padded: {pkcs7_padded}')
print(f'[*] pkcs7 padded: {Padding.unpad(pkcs7_padded, 16, 'pkcs7')}')

# iso7816
iso7816_padded = Padding.pad(data, 16, 'iso7816')
print(f'[*] iso7816 padded: {iso7816_padded}')
print(f'[*] iso7816 padded: {Padding.unpad(iso7816_padded, 16, 'iso7816')}')

# x923
x923_padded = Padding.pad(data, 16, 'x923')
print(f'[*] x923 padded: {x923_padded}')
print(f'[*] x923 padded: {Padding.unpad(x923_padded, 16, 'x923')}')

