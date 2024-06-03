# /shiftcipher/shiftcipher.py

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
