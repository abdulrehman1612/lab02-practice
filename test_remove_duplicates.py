from remove_duplicates import remove_duplicates

def test_remove_duplicates():
	assert remove_duplicates([1,5,6,3]) == [1,5,6,3]
	assert remove_duplicates(["a", 5,3,3,5,3,"a"]) == ["a", 5, 3]
	assert remove_duplicates([]) == []
	assert remove_duplicates([1,2,3,4]) == [1,2,3,4]
	print("test_remove_duplicates: ALL PASSED")

test_remove_duplicates()
