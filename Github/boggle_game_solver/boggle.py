"""
File: boggle.py
Name: Zach Hsu
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Global Variable
dictionary_lst = []


def main():
	"""
	This program simulates the boggle game by finding all possible vocabularies,
	each consisted of at least four characters.
	"""
	start = time.time()

	boggle_lst = []														# list for 4 rows of characters
	for i in range(4):
		row = input(str(i+1) + ' row of letters: ')

		# Check the format of length
		if len(row) != 7:
			print('Illegal input')
			break

		# Check the format of input characters
		ch_lst = []														# list for characters in a row
		breaker = False													# breaker to break the loop
		for j in range(len(row)):

			# Character
			if j % 2 == 0:
				if not row[j].isalpha():
					print('Illegal input')
					breaker = True
					if breaker:
						break
				else:
					ch_lst.append(row[j].lower())						# collect characters in a row

			# Blank space between characters
			if j % 2 == 1:
				if row[j] != ' ':
					print('Illegal input')
					breaker = True
					if breaker:
						break

		# Break the loop if illegal format is input
		if breaker:
			break
		else:
			boggle_lst.append(ch_lst)									# collect rows in a boggle list

	# Start the search
	if len(boggle_lst) == 4:											# start only with no illegal inputs

		# Read the file
		read_dictionary(boggle_lst)

		# Loop over the boggle list to find words
		total = 0														# total number of found words
		for k in range(len(boggle_lst)):
			for m in range(len(boggle_lst[k])):

				# First data
				current = ''
				current += boggle_lst[k][m]
				used_positions_lst = [(m, k)]
				num = len(find_word(m, k, boggle_lst, used_positions_lst, current, []))
				total += num
		print('There are', total, 'words in total.')

		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(ch, row, boggle_lst, used_positions_lst, current, ans):
	"""
	:param ch: int, index for each character in a row
	:param row: int, index for each row in the boggle list
	:param boggle_lst: list, list for all rows
	:param used_positions_lst: tuple, index of ch and row that indicates the position of an used character
	:param current: str, current character composition that might become a vocabulary
	:param ans: list, answer list for all found vocabularies
	:return: answer list (ans)
	"""
	if has_prefix(current):												# process only suitable prefixes to save time
		# Base Case
		if len(current) >= 4:											# consider those with at least 4 characters
			if current in dictionary_lst:
				if current not in ans:									# avoid repeated found words
					print('Found: ' + current)
					ans.append(current)

		# Recursive
		# Loop over surrounding characters
		for i in range(-1, 2):
			for j in range(-1, 2):

				# Make sure it won't loop outside the bound
				if 0 <= ch+i < len(boggle_lst[row]):
					if 0 <= row+j < len(boggle_lst):

						# Make sure current and used positions are not considered
						if i != 0 or j != 0:
							if not (ch+i, row+j) in used_positions_lst:
								# Choose
								current += boggle_lst[row+j][ch+i]

								# Explore
								if len(current) > 1:
									used_positions_lst.append((ch, row))
								find_word(ch + i, row + j, boggle_lst, used_positions_lst, current, ans)

								# Un-choose:
								used_positions_lst.pop()
								current = current[:len(current) - 1]

	return ans


def read_dictionary(boggle_lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# Create a string for all but unrepeated characters in the boggle list
	ch = ''
	for i in range(len(boggle_lst)):
		for j in range(len(boggle_lst[i])):
			if boggle_lst[i][j] not in ch:								# make sure repeated ones are not included
				ch += boggle_lst[i][j]

	# Read the file
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()

			# Append only words that start with those characters
			if len(line) >= 4:
				for k in range(len(ch)):
					if line.startswith(ch[k]):
						dictionary_lst.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for words in dictionary_lst:
		if words.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
