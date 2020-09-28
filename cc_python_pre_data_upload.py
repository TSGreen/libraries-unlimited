import numpy as np
import pandas as pd
import os
from pathlib import Path

from dataentry import DataEntry

district = 'FAKE' ## EDIT ME

coursequestionnaire = 'python'

savefile = Path.cwd().joinpath('data', 'codeclubs', district+'_'+coursequestionnaire+'_pre.csv')

prompt = DataEntry()

print(f"File will be saved to {savefile}")

gender = prompt.gender_question('Q: Gender?')

age = prompt.age_question('Q1: Age?')

knowpython = prompt.misc_question('Q2: Do you know about python?',
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

new_data = np.array([gender, age, knowmpython, variable, repitition, boolean, 
                     datastructure, function, hardware, coursequestionnaire])

colnames = ('Gender, Age, Pre_KnowPython, Pre_UnderstandVariable, '
            'Pre_UnderstandRepition, Pre_UnderstandBoolean, '
            'Pre_UnderstandDataStructure, Pre_UnderstandFunction, '
            'Pre_UnderstandHardware, CourseQuestionnaire').split(', ')
df = pd.DataFrame(new_data.reshape(1, -1), columns=colnames)
df.to_csv(savefile, mode='a', index=False, header=not os.path.exists(savefile))