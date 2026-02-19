def remove_duplicates(items):
	new_items = []
	for item in items:
		if item not in new_items:
			new_items.append(item)
	return new_items

