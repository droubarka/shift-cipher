# /shiftcipher/shiftcipher.py

def global_shift(data: list, table: list, shift: int) -> list:
	"""
	This function performs a circular shift on a list of elements using a given table.

	Args:
		data: A list of elements to be shifted.
		table: A list of elements to use as the table for shifting.
		shift: An integer representing the number of positions shift.

	Returns:
		A list of shifted elements.
	"""
	shifted_data = list( \
		table[(table.index(element) + shift) % len(table)] for element in data)

	return shifted_data
