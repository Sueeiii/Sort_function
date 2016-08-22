# -*- coding:utf-8 -*-

# 递归法
# 递归二分数列
def merge_sort(list):
    # 认为长度不大于1的数列是有序的
    if len(list) <= 1:
        return list
    # 二分列表
    half = len(list) // 2
    left = merge_sort(list[:half])
    right = merge_sort(list[half + 1:])
    # 最后一次合并
    return merge(left, right)


# 合并
def merge(left, right):
    # 左右数列循环输出值初始化
    left_length = 0
    right_length = 0
    result = []
    while left_length < len(left) or right_length < len(right):
        # 判断左右分支大小，大将右分支放于result反之放做分支的元素
        if left[left_length] < right[right_length]:
            result.append(left[left_length])
        else:
            result.append(right[right_length])
    # 循环完毕之后讲左右分支剩余的直接加入result
    result += left[left_length:]
    result += right[right_length]
    return result


s = [1, 5, 23, 66, 34, 234, 52]
print(merge_sort(s))
