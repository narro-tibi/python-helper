"""
Simple script to merge two pdfs together with the use of the PyPDF2 library.
"""

import os
from PyPDF2 import PdfFileMerger
from Helper.file_generation import next_nonexistent

ROOT_DIR = os.path.abspath(os.pardir)

# get the target input and output folders
source_dir = ROOT_DIR + os.sep + 'TestOutput' + os.sep + 'PDFs' + os.sep
file_name = 'MergedPDF'

merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(source_dir + item)

# create new target file with helper function
target_file = next_nonexistent(str(source_dir + file_name + '.pdf'))

merger.write(target_file)
merger.close()
