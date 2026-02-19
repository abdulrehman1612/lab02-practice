from palindrome import is_palindrome

def test_is_palindrome():
	assert is_palindrome("Uwu") == True
	assert is_palindrome("W ow") == True
	assert is_palindrome("Hellow") == False
	assert is_palindrome("") == True
	assert is_palindrome("a") == True
	print("test_is_palindrome: ALL PASSED")

test_is_palindrome()
