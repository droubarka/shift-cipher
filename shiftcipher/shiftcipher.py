# /shiftcipher/shiftcipher.py

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
