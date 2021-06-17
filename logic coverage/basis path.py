# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  basis path.py
@Description    :  
@CreateTime     :  2021-6-14 10:33
------------------------------------
@ModifyTime     :  
"""
import csv


def basis_path_binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


def basis_path_quick_sort(nums):
    def quick_sort(array, start, end):
        if start >= end:
            return
        p = partition(array, start, end)
        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end)

    def partition(array, start, end):
        pivot = array[start]
        low = start + 1
        high = end
        while True:
            while low <= high and array[high] >= pivot:
                high = high - 1
            while low <= high and array[low] <= pivot:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break
        array[start], array[high] = array[high], array[start]
        return high
    array = nums
    quick_sort(array, 0, len(array) - 1)
    return array




def execute_basis_path_binary_search_test_cases():
    original = []
    with open('basis_path_binary_search_test_cases.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            nums = [int(num) for num in item[2].split('-')] if item[2] !='' else []
            target = int(item[3])
            expected = 'Not Found' if item[4] == 'Not Found' else int(item[4])
            test_result = basis_path_binary_search(nums, target)
            result = test_result + 1 if test_result  != -1 else  'Not Found'
            item.append(result)
            if expected == result:
                item.append('Pass')
            else:
                item.append('Fail')
            print(item)
            original.append(item)

    with open('executed_basis_path_binary_search_test_cases.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['Test Case Id', 'Description','Nums', 'Target','Expected' ,'Output','Test Condition'])
        writer.writerows(item for item in original)


def execute_basis_path_quick_sort_test_cases():
    original = []
    with open('basis_path_quick_sort_test_cases.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            nums = [int(num) for num in item[2].split('-')] if item[2] !='' else []
            expected = [int(num) for num in item[3].split('-')] if item[2] !='' else []
            test_result = basis_path_quick_sort(nums)
            item.append(test_result)
            if expected == test_result:
                item.append('Pass')
            else:
                item.append('Fail')
            print(item)
            original.append(item)

    with open('executed_basis_path_quick_sort_test_cases.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['Test Case Id', 'Description','Nums','Expected' ,'Output','Test Condition'])
        writer.writerows(item for item in original)


def execute_all_basis_path_test_cases():
    # execute_basis_path_binary_search_test_cases()
    # print('All Basis Path Binary Search test cases have been executed!\nResult files: executed_basis_path_binary_search_test_cases.csv')
    execute_basis_path_quick_sort_test_cases()
    print('All Basis Path Quick Sort test cases have been executed!\nResult files: executed_basis_path_quick_sort_test_cases.csv')




def main():
    execute_all_basis_path_test_cases()
    # nums = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    # result = basis_path_quick_sort(nums)
    # print(result)

if __name__ == '__main__':
    main()