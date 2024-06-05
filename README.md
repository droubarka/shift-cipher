[![Status: In Development](https://img.shields.io/badge/Status-In%20Development-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Shift-Cipher
The **Shift Cipher**, also known as the **Caesar Cipher**, is a type of substitution cipher where each letter in the plaintext is replaced by a letter a certain number of positions further down the alphabet. This number of positions is sometimes called a **key**.
The encryption and decryption processes involve shifting the letters by a fixed number of positions, wrapping around to the beginning of the alphabet when necessary.

The encryption formula is `E_n(x) = (x + n) mod 26`, where **x** is the plaintext letter, **n** is the shift value, and **mod 26** ensures that the result is within the range of the alphabet.

The decryption formula is `D_n(x) = (x - n) mod 26`, which is the inverse of the encryption formula.

## Installation
You can install the package by cloning the repository then using pip:
```shell
git clone https://github.com/droubarka/shift-cipher.git
cd shift-cipher
python3 -m pip install .
```

Or you can use the following command instead:
```shell
python3 -m pip install git+https://github.com/droubarka/shift-cipher.git
```

## Usage
Use the **shift_alpha** function to shift alphabetic characters:
```python3
from shiftcipher import shift_alpha

message = "Hello, World!"
shift = 32

encrypted_message = shift_alpha(message, shift)
decrypted_message = shift_alpha(encrypted_message, shift, reverse=True)

print(encrypted_message) # Output: "Nkrru, Cuxrj!"
print(decrypted_message) # Output: "Hello, World!"
```
Use the **shift_bytes** function to applies a byte-level shift:
```python3
from shiftcipher import shift_bytes

message = b"Hello, World!"
shift = 128

encrypted_message = shift_bytes(message, shift)
decrypted_message = shift_bytes(encrypted_message, shift, reverse=True)

print(encrypted_message) # Output: b'\xc8\xe5\xec\xec\xef\xac\xa0\xd7\xef\xf2\xec\xe4\xa1'
print(decrypted_message) # Output: b"Hello, World!"
```
Use the **global_shift** function to shift different element types:
```python3
from shiftcipher import global_shift

data = ['localhost', b'X', True, False, None, 1000]
table = [
	'127.0.0.1', 'localhost',
	'0x58', b'X',
	'true', True,
	'false', False,
	'null', None,
	'1e+3', 1000]
shift = -1

encrypted_data = global_shift(data, table, shift)
decrypted_data = global_shift(encrypted_data, table, shift, reverse=True)

print(encrypted_data) # Output: ['127.0.0.1', '0x58', 'true', 'false', 'null', '1e+3']
print(decrypted_data) # Output: ['localhost',  b'X',   True,   False,   None,   1000 ]
```

## Contributing
Contributions are welcome!
If you'd like to contribute to the shift-cipher implementation,
please fork the repository and submit a pull request.

## License
The shift-cipher implementation is released under the MIT License.

[![Buy me a coffee!](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/droubarka)
