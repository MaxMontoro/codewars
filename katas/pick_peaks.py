def pick_peaks(arr):
	buff = [[0,0]]
	is_growing = True
	local_peaks = {"pos": [], "peaks": []}
	are_we_at_start = True
	is_local_plateau = False
	for index, element in enumerate(arr):
		if element > buff[-1][1] and index != 0:
			is_growing = True
			is_local_plateau = False
			are_we_at_start = False
		elif element < buff[-1][1]:
			if not are_we_at_start:
				if is_growing and not is_local_plateau:
					local_peaks["pos"].append(buff[-1][0])
					local_peaks["peaks"].append(buff[-1][1])
				elif is_growing and is_local_plateau:
					local_peaks["pos"].append(plateau[0])
					local_peaks["peaks"].append(plateau[1])
			is_growing = False
		elif element == buff[-1][1]:
			if not is_local_plateau:
				plateau = [index-1, element]
			is_local_plateau = True
		buff[-1] = [index, element]
	return local_peaks
