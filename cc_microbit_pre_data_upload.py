"""
Script for data entry of the Code Club pre-mcirobit questionnaires.

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

district = 'FAKE' ## EDIT ME

coursequestionnaire = 'microbit'

savefile = Path.cwd().joinpath('data', 'codeclubs', district+'_'+coursequestionnaire+'_pre.csv')

prompt = DataEntry()

print(f"File will be saved to {savefile}")

gender = prompt.gender_question('Q: Gender?')

age = prompt.age_question('Q1: Age?')

knowmicrobit = prompt.misc_question('Q2: Do you know about microbit?',
                                  options=['1', '2', '3', '4', '5'],
                                  response_map={'1': 'knownothing',
                                                '2': 'knowlittle', 
                                                '3': 'knowit', 
                                                '4': 'knowitwell', 
                                                '5': 'dontknow'},
                                  instructions = '\nEnter:\n1 (=Know Nothing)\n2 (=Know a Little)\n3 (=Know It)\n4 (=Know it Well)\n5 (=Dont Know)\n\n')

variable = prompt.yesnodk_question('Q3: Understand what is variable?')

repitition = prompt.yesnodk_question('Q4: Understand what is repition?')

boolean = prompt.yesnodk_question('Q5: Understand what is boolean?')

datastructure = prompt.yesnodk_question('Q6: Understand what is data structure?')

function = prompt.yesnodk_question('Q7: Understand what is function?')

hardware = prompt.yesnodk_question('Q8: Understand what is hardware?')

new_data = np.array([gender, age, knowmicrobit, variable, repitition, boolean, 
                     datastructure, function, hardware, coursequestionnaire])

colnames = ('Gender, Age, Pre_KnowMicrobit, Pre_UnderstandVariable, '
            'Pre_UnderstandRepition, Pre_UnderstandBoolean, '
            'Pre_UnderstandDataStructure, Pre_UnderstandFunction, '
            'Pre_UnderstandHardware, CourseQuestionnaire').split(', ')
df = pd.DataFrame(new_data.reshape(1, -1), columns=colnames)
df.to_csv(savefile, mode='a', index=False, header=not os.path.exists(savefile))