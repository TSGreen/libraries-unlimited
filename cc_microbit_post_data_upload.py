import numpy as np
import pandas as pd
import os
from pathlib import Path

district = 'test'

savefile = Path.cwd().joinpath('data', 'codeclubs', district+'_microbit_post.csv')

print(f"File will be saved to {savefile}")

notatall_to_very = '\n1 (="Not at all")\n2 (="Not Much")\n3 (="Unsure")\n4 (="A Little")\n5 (="Very")\n\n'
never_to_veryregularly = '\n1 (="Never")\n2 (="Rarely")\n3 (="Sometimes")\n4 (="Regularly")\n5 (="Very Regularly")\n\n'  
yes_no_dontknow = '\nEnter: y (=Yes), n (=No), dk (=DontKnow):\n\n'

def yesnodk_question(question):
    valid = False
    while not valid:
        response = input(f'{question}{yes_no_dontknow}')
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
            print('===============================')
            print('Invalid entry. Please try again')
            print('===============================')
    return response

def notatall_to_very_question(question):
    valid = False
    while not valid:
        response = input(f'{question}{notatall_to_very}')
        if response == '1':
            response = 'notatall'
            valid = True
        elif response == '2':
            response = 'notmuch'
            valid = True
        elif response == '3':
            response = 'unsure'
            valid = True
        elif response == '4':
            response = 'somewhat'
            valid = True
        elif response == '5':
            response = 'very'
            valid = True
        else:
            print('============================================')
            print('Invalid entry, enter number between 1 and 5')
            print('============================================')
    return response


valid = False
while not valid:
    responses = input(f'Q1: Code Club courses completed?\nEnter the code for each module complete.\n\nmb (=microbit)\nkc (=kano code)\npy (=Python)\n\n')
    if not [response in ('mb, kc, py, sp, scr, ca, html, rob').split(', ') for response in responses]:
        print('Invalid entry, enter one, or more, of mb, kc, py, sp, scr, ca, html, rob.\n')
    else:
        valid = True
courses = responses

postcancode = yesnodk_question('Q2: Do you believe you can do programming?')

postcodinginterest = notatall_to_very_question('Q3: How interested are you to do coding?')
postcodingimport = notatall_to_very_question('Q4: How important is programming to your life?')

postbenefitcareer = yesnodk_question('Q5:Do you think programming will benefit future career?')
postcodingcareer = yesnodk_question('Q6:Do you want to do programming as future careers?')
attractlibraries = yesnodk_question('Q7:Do you think such activities increase attraction of library with peers?')

valid = False
while not valid:
    bcyouthrate = input('Q8: Rate BCs attractiveness to youth?\n Enter number between 1 and 10. Where 1 is low and 10 is high:\n\n')
    bcyouthrate = int(bcyouthrate)
    if bcyouthrate <= 10 and bcyouthrate >= 1:
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 10')

valid = False
while not valid:
    response = input('Q9: Do you know about microbit?\nEnter:\n1 (=Know Nothing)\n2 (=Know a Little)\n3 (=Know It)\n4 (=Know it Well)\n5 (=Dont Know)\n\n')
    if response  == '1':
        response  = 'knownothing'
        valid = True
    elif response  == '2':
        response  = 'knowlittle'
        valid = True
    elif response  == '3':
        response  = 'knowit'
        valid = True
    elif response  == '4':
        response  = 'knowitwell'
        valid = True
    elif response  == '5':
        response  = 'dontknow'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')
knowmicrobit = response

variable = yesnodk_question('Q10: Understand what is variable?')
repitition = yesnodk_question('Q11: Understand what is repition?')
boolean = yesnodk_question('Q12: Understand what is boolean?')
datastructure = yesnodk_question('Q13: Understand what is data structure?')
function = yesnodk_question('Q14: Understand what is function?')
hardware = yesnodk_question('Q15: Understand what is hardware?')

#%%

new_data = np.array([courses, postcancode, postcodinginterest, postcodingimport,
                     postbenefitcareer, postcodingcareer, attractlibraries,
                     bcyouthrate, knowmicrobit, variable, repitition, boolean, 
                     datastructure, function, hardware])

colnames = ('Courses, Post_CanDoCoding, Post_CodingInterest, '
            'Post_CodingImportance, Post_BenefitCareer, Post_CodingCareer, '
            'AttractLibraries, BC_Rating, KnowMicrobit, UnderstandVariable, '
            'UnderstandRepition, UnderstandBoolean, UnderstandDataStructure, '
            'UnderstandFunction, UnderstandHardware').split(', ')
df = pd.DataFrame(new_data.reshape(1, -1), columns=colnames)
df.to_csv(savefile, mode='a', index=False, header=not os.path.exists(savefile))