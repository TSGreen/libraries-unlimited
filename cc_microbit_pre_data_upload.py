import numpy as np
import pandas as pd
import os
from pathlib import Path

district = 'test'
coursequestionnaire = 'microbit'

savefile = Path.cwd().joinpath('data', 'codeclubs', district+'_'+coursequestionnaire+'_pre.csv')

print(f"File will be saved to {savefile}")

notatall_to_very = '\n1 (="Not at all")\n2 (="Not Much")\n3 (="Unsure")\n4 (="A Little")\n5 (="Very")\n\n'
yes_no_dontknow = '\nEnter: y (=Yes), n (=No), dk (=DontKnow):\n\n'

def yesnodk_question(question, response_map={'y': 'yes', 'n': 'no', 'dk': 'dontnow'}, valid=False):
    while not valid:
        response = input(f'{question}{yes_no_dontknow}')
        if response in ['y', 'n', 'dk']:
            response = response_map[response]
            valid = True
        else:
            print('===============================')
            print('Invalid entry. Please try again')
            print('===============================')
    return response

def gender_question(question, response_map={'m': 'male', 'f': 'female', 'o': 'other'}, valid=False):
    while not valid:
        response = input(f'{question}\nEnter: m (=Male), f (=Female), o (=Other):\n\n')
        if response in ['m', 'f', 'o']:
            response = response_map[response]
            valid = True
        else:
            print('===============================')
            print('Invalid entry. Please try again')
            print('===============================')
    return response

def five_checkboxes(question, response_map={'1': 'notall', '2': 'notmuch', '3': 'unsure', '4': 'somewhat', '5': 'very'}, valid=False):
    while not valid:
        response = input(f'{question}')
        if response in ['1', '2', '3', '4', '5']:
            response = response_map[response]
            valid = True
        else:
            print('============================================')
            print('Invalid entry, enter number between 1 and 5')
            print('============================================')
    return response


def age_question(question, valid = False):
    error = '============================================\nInvalid entry, enter number between 7 and 18\n============================================'
    while not valid:
        age = input(question)
        try:
            age = int(age)
            if age <= 18 and age >= 7:
                valid = True
            else:
                print(error)
        except:
            print(error)
    return age
        
gender = gender_question('Q: Gender?')
age = age_question('Q1: Age?\nEnter: Age integer, 7 if < 8 and 18 if >17:\n\n')
knowmicrobit = five_checkboxes('Q2: Do you know about microbit?\nEnter:\n1 (=Know Nothing)\n2 (=Know a Little)\n3 (=Know It)\n4 (=Know it Well)\n5 (=Dont Know)\n\n', 
                             response_map={'1': 'knownothing', '2': 'knowlittle', '3': 'knowit', '4': 'knowitwell', '5': 'dontknow'})
variable = yesnodk_question('Q3: Understand what is variable?')
repitition = yesnodk_question('Q4: Understand what is repition?')
boolean = yesnodk_question('Q5: Understand what is boolean?')
datastructure = yesnodk_question('Q6: Understand what is data structure?')
function = yesnodk_question('Q7: Understand what is function?')
hardware = yesnodk_question('Q8: Understand what is hardware?')

#%%

new_data = np.array([gender, age, knowmicrobit, variable, repitition, boolean, 
                     datastructure, function, hardware, coursequestionnaire])

colnames = ('Gender, Age, Pre_KnowMicrobit, Pre_UnderstandVariable, '
            'Pre_UnderstandRepition, Pre_UnderstandBoolean, Pre_UnderstandDataStructure, '
            'Pre_UnderstandFunction, Pre_UnderstandHardware, CourseQuestionnaire').split(', ')
df = pd.DataFrame(new_data.reshape(1, -1), columns=colnames)
df.to_csv(savefile, mode='a', index=False, header=not os.path.exists(savefile))