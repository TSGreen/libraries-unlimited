"""
Script for data entry of the workshop questionnaires.

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

savedatafile = Path.cwd().joinpath('data', 'workshops', district+'.csv')

prompt = DataEntry()

gender = prompt.gender_question('Q1: Gender?')

age = prompt.age_question('Q2: Age?')

precancode = prompt.yesnodk_question('Q3: Do you believe you can do programming?')

precodingimport = prompt.notatall_to_very_questions('Q4: How important is programming to your life?') 
       
precodingint = prompt.notatall_to_very_questions('Q5: How interested are you to do coding?')  

itaccess = prompt.misc_question('Q6: Computer access?', 
                                instructions='\nEnter:\nh (="Yes, at Home")\ns (="Yes, at school")\nhs (="Yes, at home & school")\nn (="No)\n\n',
                                options=['h', 's', 'hs', 'n'],
                                response_map={'h':' home', 's':'school', 'hs':'HomeSchool', 'n':'no'})

usecomp = prompt.frequency_question('Q7: Use computers often?')

libraryvisitbefore = prompt.frequency_question('Q8: Visit library often?')

libvisitdesire = prompt.notatall_to_very_questions('Q9: How interested are you to visit library regularly?')        


print('\n\nTurn sheet over and enter post-session feedback answers:\n')


candocoding = prompt.yesnodk_question('Q10: Do you believe you can do programming?')

codingint = prompt.notatall_to_very_questions('Q11: Now, how interested are you to do coding?')

codingimport = prompt.notatall_to_very_questions ('Q12: Now, how important is programming to your life?')   
                                   
workshopex = prompt.misc_question('Q13: Overall experience of workshop?',
                                  options=['vg', 'g', 'ok', 'b'],
                                  response_map={'vg': 'verygood', 'g': 'good', 'ok': 'okay', 'b': 'bad'},
                                  instructions='\nEnter:\nvg (="Very Good")\ng (="Good")\nok (="Okay")\nb =("Bad")?\n\n')

kc, s, mb, ms, tq,  ma, hm, mp = prompt.app_rating('Q14: Which apps were used and what rating?')

libraryvisit = prompt.yesnomaybe_question('Q15: Make you visit library more?')

usedevices = prompt.yesnomaybe_question('Q16: Use devices in the library?')
        
new_data = np.array([gender, age, precancode, precodingimport, precodingint, itaccess,  
            usecomp, libraryvisitbefore,  libvisitdesire, candocoding, codingint, 
            codingimport, workshopex, s, mb, ma, mp, kc, ms, hm, tq, 
            libraryvisit, usedevices])

colnames = ('Gender, Age, Pre_CanDoCoding, Pre_CodingImportance, Pre_CodingInterest, '
            'ITaccess, UseComputersOften, VisitLibraryBefore, DesireLibraryVisit, '
            'Post_CanDoCoding, Post_CodingInterest, Post_CodingImportance, WorkshopFeedback, ' 
            'Scratch_rating, Microbit_rating, MakeArt_rating, MakePong_rating, '
            'KanoCode_rating, MakeSnake_rating, HackMinecraft_rating, '
            'TerminalQuest_rating, VisitLibrary_Activities, VisitLibrary_Devices').split(', ')

df = pd.DataFrame(new_data.reshape(1,-1), columns=colnames)
columns = ('Scratch_rating, Microbit_rating, MakeArt_rating, MakePong_rating, '
           'KanoCode_rating, MakeSnake_rating, HackMinecraft_rating, '
           'TerminalQuest_rating').split(', ')
for col in columns:
    df[col].replace({'66':'not_rated', '99':'not_used'}, inplace = True)
df.to_csv(savedatafile, mode='a', index=False, header=not os.path.exists(savedatafile))