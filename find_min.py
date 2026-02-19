def find_min(numbers):
	min_num = float("inf")
	for num in numbers:
		if num < min_num:
			min_num = num
	return min_num

