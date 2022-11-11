"""
Simple script to read out multiple Excel-Files and write each to a text file.
Uses openpyxl and is therefore restricted to xlsx/xlsm/xltx/xltm files.
"""

import os
import openpyxl

ROOT_DIR = os.path.abspath(os.pardir)

# get the target input and output folders
folder = ROOT_DIR + os.sep + 'TestOutput' + os.sep + 'ExcelFiles'
fin_folder = ROOT_DIR + os.sep + 'TestOutput' + os.sep + 'TextFiles'


def write_to_file(list_of_tuples, index):
    """ write excel data to a text file (will override existing files!) """
    file_name = str(fin_folder + os.sep + 'file_' + str(index) + '.txt')
    f = open(file_name, mode='w', encoding="utf-8")
    for t in list_of_tuples:
        line = ','.join(str(x) for x in t)
        f.write(line + '\n')
    f.close()


if __name__ == '__main__':
    for i, file in enumerate(os.listdir(folder)):
        if file.endswith('.xlsx'):
            excel_file_path = str(folder + os.sep + file)

            # Define variable to load the dataframe
            dataframe = openpyxl.load_workbook(excel_file_path)

            # Define variable to read sheet
            dataframe1 = dataframe.active
            excel_list = list()

            for row in dataframe1.iter_rows(values_only=True):
                excel_list.append(row)

            write_to_file(excel_list, i + 1)
