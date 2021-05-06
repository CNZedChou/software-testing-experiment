# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  decision_table.py
@Description    :  
@CreateTime     :  2021-5-6 10:13
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


def execute_triangle_decision_table_test_cases():
    original = []
    with open('triangle_decision_table.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            side_a = int(item[2])
            side_b = int(item[3])
            side_c = int(item[4])
            item.append(triangle(side_a, side_b, side_c))
            original.append(item)

    with open('executed_triangle_decision_table.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['Test Case Id', 'Description','a', 'b', 'c','Expected' ,'Output','Test Condition'])
        writer.writerows(item for item in original)



def execute_all_triangle_test_cases():
    execute_triangle_decision_table_test_cases()
    print(
        'All cases have been executed!\nResult files: executed_triangle_decision_table.csv')


def next_date(year, month, day):
    leap_days_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1812 <= year <= 2012:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            leap_year_flag = True
        else:
            leap_year_flag = False
    else:
        return False

    if month >= 13 or month <= 0 or day >= 32 or day <= 0:
        return False
    elif leap_year_flag and day > leap_days_list[(month - 1)]:
        return False
    elif not leap_year_flag and day > days_list[(month - 1)]:
        return False
    else:
        if leap_year_flag and day + 1 > leap_days_list[(month - 1)]:
            result_day = 1
            result_month = month + 1
            result_year = year
            if result_month == 13:
                result_month = 1
                result_year = year + 1
            return str(result_year) + '-' + str(result_month) + '-' + str(result_day)
        else:
            result_day = day + 1
            result_month = month
            result_year = year
            return str(result_year) + '-' + str(result_month) + '-' + str(result_day)


def execute_date_decision_table_test_cases():
    original = []
    with open('date_decision_table.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            year = int(item[2])
            month = int(item[3])
            day = int(item[4])
            result = next_date(year, month, day)
            if result:
                item.append(result)
            else:
                item.append('Invalid Date')
            original.append(item)

    with open('executed_date_decision_table.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['Test Case Id', 'Description','Year', 'Month', 'Day','Expected' ,'Output','Test Condition'])
        writer.writerows(item for item in original)


def execute_all_date_test_cases():
    execute_date_decision_table_test_cases()
    print(
        'All cases have been executed!\nResult files: executed_date_decision_table.csv')


def main():
    #execute_all_triangle_test_cases()
    execute_all_date_test_cases()


if __name__ == '__main__':
    main()
