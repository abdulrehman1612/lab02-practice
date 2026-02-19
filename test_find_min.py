from find_min import find_min

def test_min_num():
	assert find_min([1,2,3,4,5]) == 1
	assert find_min([0]) == 0
	assert find_min([-1,-2,-3,-4]) == -4
	assert find_min([-5,3,0]) == -5
	print("test_min_num: ALL PASSED")

test_min_num()
