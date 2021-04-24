# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  boundary_value_analysis.py
@Description    :  
@CreateTime     :  2021-4-24 16:58
------------------------------------
@ModifyTime     :  
"""
import numpy as np
import pandas as pd
import csv


def generate_bva_test_cases(minValueList, maxValueList, parameters):
    # bvaTable to store the bva values
    bvaTable = [[]]
    bvaCSVTable = pd.DataFrame()

    minimum = []
    for i in range(0, len(minValueList)):
        minimum.append(minValueList[i])
    bvaTable.insert(0, minimum)

    above_minimum = []
    for i in range(0, len(minValueList)):
        above_minimum.append(minValueList[i] + 1)
    bvaTable.insert(1, above_minimum)

    maximum = []
    for i in range(0, len(maxValueList)):
        maximum.append(maxValueList[i])
    bvaTable.insert(2, maximum)

    below_maximum = []
    for i in range(0, len(maxValueList)):
        below_maximum.append(maxValueList[i] - 1)
    bvaTable.insert(3, below_maximum)

    nominal = []
    for i in range(0, len(maxValueList)):
        nominal.append(np.math.ceil((maxValueList[i] + (minValueList[i] - 1)) / 2))
    bvaTable.insert(4, nominal)

    allNominalValue = []
    # total = 4 * n + 1
    testID = list(range(1, 4 * parameters + 2))
    # generate test cases
    for i in range(0, parameters):
        tempTable = []
        nominalValue = bvaTable[4][i]
        allNominalValue.append(nominalValue)

        for j in range(0, 4 * (parameters - 1)):
            tempTable.append(nominalValue)

        for j in range(0, 4):
            position = j + (i * 4)
            tempTable.insert(position, bvaTable[j][i])

        bvaCSVTable[i + 1] = tempTable

    bvaCSVTable.loc[len(bvaCSVTable)] = allNominalValue
    bvaCSVTable.insert(0, 'TestCaseId', testID)
    bvaCSVTable.to_csv('bva.csv', index=False)


def generate_robust_bva_test_cases(minValueList, maxValueList, parameters):
    robustTable = [[]]
    robustCSVTable = pd.DataFrame()

    minimum = []
    for i in range(0, len(minValueList)):
        minimum.append(minValueList[i])
    robustTable.insert(0, minimum)

    above_minimum = []
    for i in range(0, len(minValueList)):
        above_minimum.append(minValueList[i] + 1)
    robustTable.insert(1, above_minimum)

    below_minimum = []
    for i in range(0, len(minValueList)):
        below_minimum.append(minValueList[i] - 1)
    robustTable.insert(2, below_minimum)

    maximum = []
    for i in range(0, len(maxValueList)):
        maximum.append(maxValueList[i])
    robustTable.insert(3, maximum)

    below_maximum = []
    for i in range(0, len(maxValueList)):
        below_maximum.append(maxValueList[i] - 1)
    robustTable.insert(4, below_maximum)

    above_maximum = []
    for i in range(0, len(maxValueList)):
        above_maximum.append(maxValueList[i] + 1)
    robustTable.insert(5, above_maximum)

    nominalValue = []
    for i in range(0, len(maxValueList)):
        nominalValue.append(np.math.ceil((maxValueList[i] + (minValueList[i] - 1)) / 2))
    robustTable.insert(6, nominalValue)

    allNominalValue = []
    testID = list(range(1, 6 * parameters + 2))

    for i in range(0, parameters):
        tempRobustTable = []
        nominalValue = robustTable[6][i]
        allNominalValue.append(nominalValue)

        for j in range(0, 6 * (parameters - 1)):
            tempRobustTable.append(nominalValue)

        for j in range(0, 6):
            position = j + (i * 6)
            tempRobustTable.insert(position, robustTable[j][i])
        robustCSVTable[i + 1] = tempRobustTable

    robustCSVTable.loc[len(robustCSVTable)] = allNominalValue
    robustCSVTable.insert(0, 'Test Case Id', testID)
    robustCSVTable.to_csv('robust_bva.csv', index=False)


def generate_worst_bva_test_cases(minValueList, maxValueList, parameters):
    worstTable = [[]]
    worstCSVTable = pd.DataFrame()

    minimum = []
    for i in range(0, len(minValueList)):
        minimum.append(minValueList[i])
    worstTable.insert(0, minimum)

    above_minimum = []
    for i in range(0, len(minValueList)):
        above_minimum.append(minValueList[i] + 1)
    worstTable.insert(1, above_minimum)

    maximum = []
    for i in range(0, len(maxValueList)):
        maximum.append(maxValueList[i])
    worstTable.insert(2, maximum)

    below_maximum = []
    for i in range(0, len(maxValueList)):
        below_maximum.append(maxValueList[i] - 1)
    worstTable.insert(3, below_maximum)

    nominal = []
    for i in range(0, len(maxValueList)):
        nominal.append(np.math.ceil((maxValueList[i] + (minValueList[i] - 1)) / 2))
    worstTable.insert(4, nominal)


    testID = list(range(1, pow(5, parameters) + 1))

    for i in range(0, parameters):
        tmpWorstTable = []
        while len(tmpWorstTable) < pow(5, parameters):
            for j in range(0, 5):
                for k in range(0, pow(5, parameters - (i + 1))):
                    tmpWorstTable.append(worstTable[j][i])

        worstCSVTable[i + 1] = tmpWorstTable

    worstCSVTable.insert(0, 'Test Case Id', testID)
    worstCSVTable.to_csv('worst_bva.csv', index=False)


def generate_robust_worst_bva_test_cases(minValueList, maxValueList, parameters):
    robustWorstTable = [[]]
    worstCSVTable = pd.DataFrame()

    minimum = []
    for i in range(0, len(minValueList)):
        minimum.append(minValueList[i])
    robustWorstTable.insert(0, minimum)

    above_minimum = []
    for i in range(0, len(minValueList)):
        above_minimum.append(minValueList[i] + 1)
    robustWorstTable.insert(1, above_minimum)

    below_minimum = []
    for i in range(0, len(minValueList)):
        below_minimum.append(minValueList[i] - 1)
    robustWorstTable.insert(2, below_minimum)

    maximum = []
    for i in range(0, len(maxValueList)):
        maximum.append(maxValueList[i])
    robustWorstTable.insert(3, maximum)

    below_maximum = []
    for i in range(0, len(maxValueList)):
        below_maximum.append(maxValueList[i] - 1)
    robustWorstTable.insert(4, below_maximum)

    above_maximum = []
    for i in range(0, len(maxValueList)):
        above_maximum.append(maxValueList[i] + 1)
    robustWorstTable.insert(5, above_maximum)

    nominal = []
    for i in range(0, len(maxValueList)):
        nominal.append(np.math.ceil((maxValueList[i] + (minValueList[i] - 1)) / 2))
    robustWorstTable.insert(6, nominal)


    testID = list(range(1, pow(7, parameters) + 1))

    for i in range(0, parameters):
        tmpWorstTable = []
        while len(tmpWorstTable) < pow(7, parameters):
            for j in range(0, 7):
                for k in range(0, pow(7, parameters - (i + 1))):
                    tmpWorstTable.append(robustWorstTable[j][i])

        worstCSVTable[i + 1] = tmpWorstTable

    worstCSVTable.insert(0, 'Test Case Id', testID)
    worstCSVTable.to_csv('robust_worst_bva.csv', index=False)


def generate_all_test_cases():
    maxValueList = []
    minValueList = []
    parameters = int(input('Enter parameters:'))

    for i in range(0, parameters):
        minValues, maxValues = input().split()
        maxValueList.append(int(maxValues))
        minValueList.append(int(minValues))

    generate_bva_test_cases(minValueList, maxValueList, parameters)
    generate_robust_bva_test_cases(minValueList, maxValueList, parameters)
    generate_worst_bva_test_cases(minValueList, maxValueList, parameters)
    generate_robust_worst_bva_test_cases(minValueList, maxValueList, parameters)
    print('Test cases generated!\nTest files: bva.csv, robust_bva.csv, worst_bva.csv, robust_worst_bva.csv')


def is_valid_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


# Function definition for type
def type_of_triangle(a, b, c):
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'


def execute_triangle_bva_test_cases():
    original = []
    with open('bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            side_a = int(item[1])
            side_b = int(item[2])
            side_c = int(item[3])
            if is_valid_triangle(side_a, side_b, side_c):
                item.append(type_of_triangle(side_a, side_b, side_c))
            else:
                item.append('Not a Triangle')
            original.append(item)

    with open('bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)


def execute_triangle_robust_bva_test_cases():
    original = []
    with open('robust_bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            side_a = int(item[1])
            side_b = int(item[2])
            side_c = int(item[3])
            if is_valid_triangle(side_a, side_b, side_c):
                item.append(type_of_triangle(side_a, side_b, side_c))
            else:
                item.append('Not a Triangle')
            original.append(item)

    with open('robust_bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)


def execute_triangle_worst_bva_test_cases():
    original = []
    with open('worst_bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            side_a = int(item[1])
            side_b = int(item[2])
            side_c = int(item[3])
            if is_valid_triangle(side_a, side_b, side_c):
                item.append(type_of_triangle(side_a, side_b, side_c))
            else:
                item.append('Not a Triangle')
            original.append(item)

    with open('worst_bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)


def execute_triangle_robust_worst_bva_test_cases():
    original = []
    with open('robust_worst_bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            side_a = int(item[1])
            side_b = int(item[2])
            side_c = int(item[3])
            if is_valid_triangle(side_a, side_b, side_c):
                item.append(type_of_triangle(side_a, side_b, side_c))
            else:
                item.append('Not a Triangle')
            original.append(item)

    with open('robust_worst_bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)


def execute_all_triangle_test_cases():
    execute_triangle_bva_test_cases()
    execute_triangle_robust_bva_test_cases()
    execute_triangle_worst_bva_test_cases()
    execute_triangle_robust_worst_bva_test_cases()
    print('All cases have been executed!\nResult files: bva_after_test.csv, robust_bva_after_test.csv, worst_bva_after_test.csv, robust_worst_bva_after_test.csv')



def is_date_valid(year,month,day):
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
                result_month =1
                result_year = year + 1
            return str(result_year) +'-'+str(result_month)+'-'+str(result_day)
        else:
            result_day = day + 1
            result_month = month
            result_year = year
            return str(result_year) +'-'+str(result_month)+'-'+str(result_day)






def execute_date_bva_test_cases():
    original = []
    with open('bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            year = int(item[1])
            month = int(item[2])
            day = int(item[3])
            result = is_date_valid(year,month,day)
            if result:
                item.append(result)
            else:
                item.append('Invalid Date')
            original.append(item)

    with open('bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)


def execute_date_robust_bva_test_cases():
    original = []
    with open('robust_bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            year = int(item[1])
            month = int(item[2])
            day = int(item[3])
            result = is_date_valid(year, month, day)
            if result:
                item.append(result)
            else:
                item.append('Invalid Date')
            original.append(item)

    with open('robust_bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)



def execute_date_worst_bva_test_cases():
    original = []
    with open('worst_bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            year = int(item[1])
            month = int(item[2])
            day = int(item[3])
            result = is_date_valid(year, month, day)
            if result:
                item.append(result)
            else:
                item.append('Invalid Date')
            original.append(item)

    with open('worst_bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)


def execute_date_robust_worst_bva_test_cases():
    original = []
    with open('robust_worst_bva.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            if reader.line_num == 1:
                continue
            year = int(item[1])
            month = int(item[2])
            day = int(item[3])
            result = is_date_valid(year, month, day)
            if result:
                item.append(result)
            else:
                item.append('Invalid Date')
            original.append(item)

    with open('robust_worst_bva_after_test.csv', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile)
        writer.writerow(['TestCaseId', '1', '2', '3', 'Output'])
        writer.writerows(item for item in original)

def execute_all_date_test_cases():
    execute_date_bva_test_cases()
    execute_date_robust_bva_test_cases()
    execute_date_worst_bva_test_cases()
    execute_date_robust_worst_bva_test_cases()
    print('All cases have been executed!\nResult files: bva_after_test.csv, robust_bva_after_test.csv, worst_bva_after_test.csv, robust_worst_bva_after_test.csv')



if __name__ == '__main__':
    generate_all_test_cases()
    # execute_all_triangle_test_cases()

    execute_all_date_test_cases()