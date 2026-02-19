def is_palindrome(text):
	temp = ""
	for char in text:
		if char != " ":
			temp = temp + char.lower()
	return temp == temp[::-1]
