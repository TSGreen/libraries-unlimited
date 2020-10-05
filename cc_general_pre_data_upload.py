"""
Script for data entry of the Code Club general pre-questionnaire.

This file only works in conjunction with the dataentry.py file located in the 
same directory.

To use this script, edit the district variable to match the library you are 
uploading data for. Then follow the prompts for user input when the script is run. 

The data is saved to a csv at the end of this script.

If an incorrect error is added, use ctrl-c to keyboard interrupt the script
and start over.
"""
import numpy as np
import pandas as pd
import os
from pathlib import Path

from dataentry import DataEntry

district = 'TEST'   ## EDIT ME

savedatafile = Path.cwd().joinpath('data', 'codeclubs', district+'_general_pre.csv')

print(f"File will be saved to {savedatafile}")

prompt = DataEntry()

gender = prompt.gender_question('Q: Gender?')

age = prompt.age_question('Q1: Age?')

precancode = prompt.yesnodk_question('Q2: Do you believe you can do programming?')

precodingint = prompt.notatall_to_very_questions('Q3: How interested are you to do coding?')  

precodingimport = prompt.notatall_to_very_questions('Q4: How important is programming to your life?') 

prebenefitcareer = prompt.yesnodk_question('Q5:Do you think programming will benefit future career?')

precodingcareer = prompt.yesnodk_question('Q6:Do you want to do programming as future careers?')

new_data = np.array([gender, age, precancode, precodingint, precodingimport,
                     prebenefitcareer, precodingcareer])

colnames = ('Gender, Age, Pre_CanDoCoding, Pre_CodingInterest, '
            'Pre_CodingImportance, Pre_Benefit_Career, Pre_Coding_Career').split(', ')
df = pd.DataFrame(new_data.reshape(1, -1), columns=colnames)
df.to_csv(savedatafile, mode='a', index=False, header=not os.path.exists(savedatafile))