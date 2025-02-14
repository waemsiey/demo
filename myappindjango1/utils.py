#this utils.py is like a in java springboot service layer it handles different specific task: 
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import csv

#This function handle the file reading and processing of the CSV into the memory this passed a par of f 
def uploaded_file(f):
    if not f.name.endswith('.csv'): 
        raise ValidationError('File must be a CSV!')
    
    file_data = f.read().decode('utf-8')
    csv_reader = csv.reader(file_data.splitlines())

    csv_content = []
    for row in csv_reader:
        csv_content.append(row)
    return csv_content