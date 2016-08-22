# -*- coding:utf-8 -*-
# 快排从小到大排序
def quick_sort(nums):
    left = []
    right = []
    euqal = []
    if len(nums) <= 1:
        return nums
    else:
        # 取第一个位基准值
        index = nums[0]
        for i in nums:
            # 若比基准值小就放于left
            if index < i:
                right.append(i)
            # 若比基准值小就放于right
            elif index > i:
                left.append(i)
            # 若比基准值小就放于euqal
            else:
                euqal.append(i)
        # 调用递归
        less = quick_sort(left)
        more = quick_sort(right)
    return less + euqal + more


s = [1, 5, 23, 66, 34, 234, 52]
print(quick_sort(s))
