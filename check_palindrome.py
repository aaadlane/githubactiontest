def check_palindrome(string):
	isPalin = string == string[::-1]
	if isPalin :
		return "yes"
	else:
		return "no"
