import numpy as np
import pandas as pd
import os
from pathlib import Path

district = 'dhaka'

savefile = Path.cwd().joinpath('data', 'codeclubs', district+'_general_pre.csv')

print(f"File will be saved to {savefile}")

notatall_to_very = '\n1 (="Not at all")\n2 (="Not Much")\n3 (="Unsure")\n4 (="A Little")\n5 (="Very")\n\n'
never_to_veryregularly = '\n1 (="Never")\n2 (="Rarely")\n3 (="Sometimes")\n4 (="Regularly")\n5 (="Very Regularly")\n\n'  
yes_no_dontknow = '\nEnter: y (=Yes), n (=No), dk (=DontKnow):\n\n'

gender_valid = False
while not gender_valid:
    gender = input('Gender?\nEnter: m (=Male), f (=Female), o (=Other):\n\n')
    if gender == 'm':
        gender = 'male'
        gender_valid = True
    elif gender == 'f':
        gender = 'female'
        gender_valid = True
    elif gender == 'o':
        gender == 'other'
        gender_valid = True
    else:
        print('You have entered an invalid entry, try again.\n')


valid = False
while not valid:
    age = input('Q1: Age?\nEnter: Age integer, 7 if < 8 and 18 if >17:\n\n')
    age = int(age)
    if age <= 18 and age >= 7:
        valid = True
    else:
        print('Invalid age entry, enter number 7 and 18/n')


valid = False
while not valid:
    response = input(f'Q2: Do you believe you can do programming?{yes_no_dontknow}')
    if response == 'y':
        response = 'yes'
        valid = True
    elif response == 'dk':
        response = 'dontknow'
        valid = True
    elif response == 'n':
        response = 'no'
        valid = True
    else:
        print('Invalid entry. Please try again')
    precancode = response


valid = False
while not valid:
    precodingint = input(f'Q3: How interested are you to do coding?{notatall_to_very}')
    if precodingint == '1':
        precodingint = 'notatall'
        valid = True
    elif precodingint == '2':
        precodingint = 'notmuch'
        valid = True
    elif precodingint == '3':
        precodingint = 'unsure'
        valid = True
    elif precodingint == '4':
        precodingint = 'somewhat'
        valid = True
    elif precodingint == '5':
        precodingint = 'very'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')


valid = False
while not valid:
    precodingimport = input(f'Q4: How important is programming to your life?{notatall_to_very}')
    if precodingimport == '1':
        precodingimport = 'notatall'
        valid = True
    elif precodingimport == '2':
        precodingimport = 'notmuch'
        valid = True
    elif precodingimport == '3':
        precodingimport = 'unsure'
        valid = True
    elif precodingimport == '4':
        precodingimport = 'somewhat'
        valid = True
    elif precodingimport == '5':
        precodingimport = 'very'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')

valid = False
while not valid:
    response = input(f'Q5:Do you think programming will benefit future career?{yes_no_dontknow}')
    if response == 'y':
        response = 'yes'
        valid = True
    elif response == 'dk':
        response = 'dontknow'
        valid = True
    elif response == 'n':
        response = 'no'
        valid = True
    else:
        print('Invalid entry. Please try again')
    prebenefitcareer = response


valid = False
while not valid:
    response = input(f'Q6:Do you want to do programming as future careers?{yes_no_dontknow}')
    if response == 'y':
        response = 'yes'
        valid = True
    elif response == 'dk':
        response = 'dontknow'
        valid = True
    elif response == 'n':
        response = 'no'
        valid = True
    else:
        print('Invalid entry. Please try again')
    precodingcareer = response

new_data = np.array([gender, age, precancode, precodingint, precodingimport,
                     prebenefitcareer, precodingcareer])

colnames = ('Gender, Age, Pre_CanDoCoding, Pre_CodingInterest, '
            'Pre_CodingImportance, Pre_Benefit_Career, Pre_Coding_Career').split(', ')
df = pd.DataFrame(new_data.reshape(1, -1), columns=colnames)
df.to_csv(savefile, mode='a', index=False, header=not os.path.exists(savefile))