def number_of_words(string):
	import re
	count = len(re.findall(r'\w+', string))
	return (count)
