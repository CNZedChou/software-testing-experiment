# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  cause_effect.py
@Description    :  
@CreateTime     :  2021-5-10 18:47
------------------------------------
@ModifyTime     :  
"""
import csv

def triangle(a, b, c):
    if 1 <= a <= 200 and 1 <= b <= 200 and 1 <= c <= 200:
        if a + b > c and b + c > a and c + a > b:
            if a == b and b == c:
                return 'Equilateral'
            elif a == b or b == c or a == c:
                return 'Isosceles'
            else:
                return 'Scalene'
        else:
            return 'NotATriangle'
    else:
        return 'OutOfRange'


def execute_triangle_cause_effect_graph_test_cases():
    original = []
    with open('triangle_cause_effect_graph.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            side_a = int(item[2])
            side_b = int(item[3])
            side_c = int(item[4])
            expected = item[5]
            test_result = triangle(side_a, side_b, side_c)
            item.append(test_result)
            if expected == test_result:
                item.append('Pass')
            else:
                item.append('Fail')
            print(item)
            original.append(item)

    with open('executed_triangle_cause_effect_graph.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['Test Case Id', 'Description','a', 'b', 'c','Expected' ,'Output','Test Condition'])
        writer.writerows(item for item in original)

def execute_all_triangle_test_cases():
    execute_triangle_cause_effect_graph_test_cases()
    print(
        'All Triangle Problem cases have been executed!\nResult files: executed_triangle_cause_effect_graph.csv')





def input_output(first,second):
    if first == '#' or '*':
        if second.isdigit():
            return 'modify the document'
        else:
            return 'information M'
    else:
        return 'information N'

def execute_input_cause_effect_graph_test_cases():
    original = []
    with open('input_cause_effect_graph.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            first_character = item[2]
            second_character = item[3]
            expected = item[4]
            test_result = input_output(first_character, second_character)
            item.append(test_result)
            if expected == test_result:
                item.append('Pass')
            else:
                item.append('Fail')
            print(item)
            original.append(item)

    with open('executed_input_cause_effect_graph.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['Test Case Id', 'Description','First Character', 'Second Character','Expected' ,'Output','Test Condition'])
        writer.writerows(item for item in original)


def execute_all_input_test_cases():
    execute_input_cause_effect_graph_test_cases()
    print(
        'All Input-Output Problem cases have been executed!\nResult files: executed_input_cause_effect_graph.csv')



def main():
    execute_all_triangle_test_cases()
    execute_all_input_test_cases()


if __name__ == '__main__':
    main()