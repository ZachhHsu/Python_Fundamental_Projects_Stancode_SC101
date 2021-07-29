"""
File: largest_digit.py
Name: Zach Hsu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number to be processed
	:return: int, the largest digit from that number
	"""
	# Make sure the algorithm runs with positive numbers
	if n < 0:
		return helper(-n)
	return helper(n)


def helper(n):
	# Base Case
	if n == 0:
		return 0

	# Recursive
	else:
		latter_digit = n % 10							# the rightmost digit
		former_digit = helper(n // 10)					# the digit next to the rightmost one

		# Return the larger digit
		if former_digit > latter_digit:
			return former_digit
		return latter_digit



if __name__ == '__main__':
	main()
