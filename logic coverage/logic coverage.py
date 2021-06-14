# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  logic coverage.py
@Description    :  
@CreateTime     :  2021-5-24 23:29
------------------------------------
@ModifyTime     :  
"""
import csv

def logic_coverage(A, B, X):
    if A > 1 and B == 0:
        X = X / A
    if A == 2 or X > 1:
        X = X + 1
    return '{:g}'.format(X)


def execute_logic_coverage_test_cases():
    original = []
    with open('logic_coverage_test_cases.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            input_A = int(item[2])
            input_B = int(item[3])
            input_X = int(item[4])
            expected = (item[5])
            test_result = logic_coverage(input_A, input_B, input_X)
            item.append(test_result)
            if expected == test_result:
                item.append('Pass')
            else:
                item.append('Fail')
            print(item)
            original.append(item)

    with open('executed_logic_coverage_test_cases.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['Test Case Id', 'Description','Input-A', 'Input-B', 'Input-X','Expected' ,'Output','Test Condition'])
        writer.writerows(item for item in original)


def execute_all_logic_coverage_test_cases():
    execute_logic_coverage_test_cases()
    print(
        'All Logic Coverage cases have been executed!\nResult files: executed_logic_coverage_test_cases.csv')


def main():
    execute_all_logic_coverage_test_cases()


if __name__ == '__main__':
    main()
