import numpy as np
import pandas as pd
import os
from pathlib import Path

from dataentry import DataEntry

district = 'TEST' ## EDIT ME

prompt = DataEntry()

coursequestionnaire = 'python'
savedatafile = Path.cwd().joinpath('data', 
                               'codeclubs', 
                               district+'_'+coursequestionnaire+'_post.csv')


print(f"File will be saved to {savedatafile}")


courses = prompt.codeclub_courses('Q1: Code Club courses completed?')

postcancode = prompt.yesnodk_question('Q2: Do you believe you can do programming?')

postcodinginterest = prompt.notatall_to_very_questions('Q3: How interested are you to do coding?')

postcodingimport = prompt.notatall_to_very_questions('Q4: How important is programming to your life?')

postbenefitcareer = prompt.yesnodk_question('Q5:Do you think programming will benefit future career?')

postcodingcareer = prompt.yesnodk_question('Q6:Do you want to do programming as future careers?')

attractlibraries = prompt.yesnodk_question('Q7:Do you think such activities increase attraction of library with peers?')

bcyouthrate = prompt.numbered_rating('Q8: Rate BCs attractiveness to youth? \n Enter number between 1 and 10. Where 1 is low and 10 is high:\n\n', limits=[1,10])

knowpython = prompt.misc_question('Q9: Do you know about python?',
                                  options=['1', '2', '3', '4', '5'],
                                  response_map={'1': 'knownothing', '2': 'knowlittle', '3': 'knowit', '4': 'knowitwell', '5': 'dontknow'},
                                  instructions = '\nEnter:\n1 (=Know Nothing)\n2 (=Know a Little)\n3 (=Know It)\n4 (=Know it Well)\n5 (=Dont Know)\n\n')

variable = prompt.yesnodk_question('Q10: Understand what is variable?')

repitition = prompt.yesnodk_question('Q11: Understand what is repition?')

boolean = prompt.yesnodk_question('Q12: Understand what is boolean?')

datastructure = prompt.yesnodk_question('Q13: Understand what is data structure?')

function = prompt.yesnodk_question('Q14: Understand what is function?')

hardware = prompt.yesnodk_question('Q15: Understand what is hardware?')


new_data = np.array([courses, postcancode, postcodinginterest, postcodingimport,
                     postbenefitcareer, postcodingcareer, attractlibraries,
                     bcyouthrate, knowpython, variable, repitition, boolean, 
                     datastructure, function, hardware, coursequestionnaire])

colnames = ('Courses, Post_CanDoCoding, Post_CodingInterest, '
            'Post_CodingImportance, Post_BenefitCareer, Post_CodingCareer, '
            'AttractLibraries, BC_Rating, Post_KnowPython, Post_UnderstandVariable, '
            'Post_UnderstandRepition, Post_UnderstandBoolean, Post_UnderstandDataStructure, '
            'Post_UnderstandFunction, Post_UnderstandHardware, CourseQuestionnaire').split(', ')
df = pd.DataFrame(new_data.reshape(1, -1), columns=colnames)
df.to_csv(savedatafile, mode='a', index=False, header=not os.path.exists(savedatafile))