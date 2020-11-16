 python : 冒泡排序
 
 nums = [1,22,3,2,4,9,21]
 
 def bubble_sort(nums):
	for i in range(len(nums)-1):  # 这个循环负责设置冒泡排序进行的次数
		for j in range(len(nums)-i-1):
			if nums[j] > nums[j+1]:
				nums[j],nums[j+1] = nums[j+1],nums[j]
		#break;  #第一个外循环结束后的情况
	return nums
res = bubble_sort(nums)
print(res)




















