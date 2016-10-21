nums = [17,2,3,4,5,6,7,8,9,11,12,13,15,14,16]

def sort(nums):
	"""Sort numbers using bubble sort"""
	loops = 0
	for j,n in enumerate(nums):
		clean = True
		for i in range(0,len(nums)-1-j):
			loops +=1
			if nums[i] > nums[i+1]:
				[nums[i],nums[i+1]] = [nums[i+1],nums[i]]
				clean = False
		if clean:
			return nums,loops
		print(nums)
	return nums,loops


print(sort(nums))