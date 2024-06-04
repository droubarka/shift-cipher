# Copyright (c) 2024 Mohamed A. Oubarka
# Licensed under the MIT License (see LICENSE file for details)

import string

def global_shift(data: list, table: list, shift: int, reverse: bool = False) -> list:
	"""
	This function performs a circular shift on a list of elements using a given table.

	Args:
		data: A list of elements to be shifted.
		table: A list of elements to use as the table for shifting.
		shift: An integer representing the number of positions shift.
		reverse: A boolean flag indicating whether to shift in reverse direction.

	Returns:
		A list of shifted elements.
	"""
	shift = -shift if reverse else shift
	shifted_data = list( \
		table[(table.index(element) + shift) % len(table)] for element in data)

	return shifted_data


def shift_bytes(data: bytes, shift: int, reverse: bool = False) -> bytes:
	"""
	Shifts each byte in the given byte string by the specified number of positions.

	Args:
		data: A byte string containing the data to be shifted.
		shift: An integer representing the number of positions shift.
		reverse: A boolean flag indicating whether to shift in reverse direction.

	Returns:
		The shifted byte string.
	"""
	shift = -shift if reverse else shift
	shifted_data = bytes((byte + shift) % 256 for byte in data)

	return shifted_data


def shift_bytes_by_table(data: bytes, table: bytes, shift: int, reverse: bool = False) -> bytes:
	"""
	Shifts each byte in the data according to a custom table.

	Args:
		data: A byte string containing the data to be shifted.
		table: A byte string containing the table of bytes for shifting.
		shift: An integer representing the number of positions shift.
		reverse: A boolean flag indicating whether to shift in reverse direction.

	Returns:
		The shifted byte string.
	"""
	shift = -shift if reverse else shift
	shifted_data = bytes( \
		table[(table.index(byte) + shift) % len(table)] for byte in data)

	return shifted_data


def shift_alpha(data: str, shift: int, reverse: bool = False) -> str:
	"""
	Shifts alphabetic characters in the given string by the specified number of positions.

	Args:
		data: A string to be shifted.
		shift: An integer representing the number of positions shift.
		reverse: A boolean flag indicating whether to shift in reverse direction.

	Returns:
		The shifted string.
	"""
	alpha = string.ascii_lowercase
	shift = -shift if reverse else shift
	shifted_data = ""

	for char in data:
		# The reason why `char.isalpha()` is not used in the code is that it
		# would also return `True` for non-ASCII alphabetic characters, such as
		# accented letters and letters from non-Latin scripts.
		if char.lower() in alpha:
			shifted_data += alpha[(alpha.index(char.lower()) + shift) % 26]
			if char.isupper():
				shifted_data = shifted_data[:-1] + shifted_data[-1].upper()
		else:
			shifted_data += char

	return shifted_data


def shift_alpha_by_table(data: str, table: str, shift: int, reverse: bool = False) -> str:
	"""
	Shifts alphabetic characters in the given string according to a custom table.

	Args:
		data: A string to be shifted.
		table: A string containing the table for shifting.
		shift: An integer representing the number of positions shift.
		reverse: A boolean flag indicating whether to shift in reverse direction.

	Returns:
		The shifted string.
	"""
	shift = -shift if reverse else shift
	shifted_data = ''.join( \
		table[(table.index(char) + shift) % len(table)] for char in data)

	return shifted_data


def caesar(data: str, reverse: bool = False) -> str:
	"""
	Applies a Caesar shift of 3 position to the given data.

	Args:
		data: A string to be shifted.
		reverse: A boolean flag indicating whether to shift in reverse direction.

	Returns:
		The shifted string.
	"""
	shift = 3
	shifted_data = shift_alpha(data, shift, reverse)

	return shifted_data
