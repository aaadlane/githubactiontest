def average_word_length(string):
	words = string.split()
	average_length = sum(len(word) for word in words) / len(words)
	return average_length
