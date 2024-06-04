![Status: In Development](https://img.shields.io/badge/Status-In%20Development-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Shift-Cipher
The **Shift Cipher**, also known as the **Caesar Cipher**, is a type of substitution cipher where each letter in the plaintext is replaced by a letter a certain number of positions further down the alphabet. This number of positions is sometimes called a **key**.
The encryption and decryption processes involve shifting the letters by a fixed number of positions, wrapping around to the beginning of the alphabet when necessary.

The encryption formula is `E_n(x) = (x + n) mod 26`, where **x** is the plaintext letter, **n** is the shift value, and **mod 26** ensures that the result is within the range of the alphabet.

The decryption formula is `D_n(x) = (x - n) mod 26`, which is the inverse of the encryption formula.

# Install
```shell

```

# Usage
```python
from shiftcipher import shiftcipher

data = b'hello, world!'
shift = 32

ciphertext = shiftcipher.shift_bytes(data, shift)
plaintext  = shiftcipher.shift_bytes(ciphertext, shift, reverse=True)
```
```
ciphertext -> b'\x88\x85\x8c\x8c\x8fL@\x97\x8f\x92\x8c\x84A'
plaintext  -> b'hello, world!'
```

[![Buy me a coffee!](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/droubarka)
