#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the data entry of the LU coding activity questionnaires.

The class contains a general question format as well as templates for common
question formats.


@author: tim
"""

import numpy as np
import pandas as pd
import os
from pathlib import Path

class DataEntry():
    """
    The class contains a general question format as well as templates for
    common question formats.

    For general questions, the user can specify the possible multiple choice
    responses using the response_map and options arguments. The instructions
    argument controls the user input prompt and should correspond to the 
    possible responses for that particular question.

    For common question types, such as "yes", "no", "dontknow" responses, there
    are template questions with the responses set as default parameters.
    These include:
        - yesnodk for "yes", "no", 'dont know' type questions
        - yesnomaybe for "yes", "no", 'maybe' type questions
        - frequency for questions about how frequently the participant does
          something with possible responses "never", "rarely", "sometimes"
          "regularly" and "very regularly".
        - age
        - gender
        - notatall_to_very for questions with resonses options: "Not at all",
          "Not Much", "Unsure", "A Little" and "Very"
        - app ratings for the workshop app rating question

    """


    def __init__(self):
        self.error_msg = '===============================\nInvalid entry. Please try again\n==============================='

    def misc_question(self, question,
                         response_map={},
                         instructions='\nNo conditions given, please revise script.',
                         options=[],
                         valid=False):
        """
        General form of the data entry for most questions.
        
        The method allows a list of possible valid entries, given by the "options"
        argument and uses the responses_map dictionnary to map the short form 
        codes to the saved data string.

        Parameters
        ----------
        question : str
            The question that is printed to prompt the user.
        response_map : dict, optional
            The mapping between the user input short form codes and the string
            that is actually saved in the output file.
            The default is {}. But a real dictionary must be passed.
        instructions : str, optional
            Instructions to the user about what is a valid entry for this question
            The default is '\nNo conditions given, please revise script.'.
        options : list, optional
            The possible reponses in code form that user can enter.
            The default is [].
        valid : Boolean, optional
            Sets the condition for parameter checking.
            The default is False and should not be changed.

        Returns
        -------
        response : string or int (depends on question)
            The paricipant response to be saved in file.

        """
        while not valid:
            response = input(f'{question}{instructions}')
            if response in options:
                response = response_map[response]
                valid = True
            else:
                print(self.error_msg)
        return response

    def yesnodk_question(self, question):
        """
        Question template with default arguments set for questions with
        response options: "Yes", "No", 'I dont know".
        """
        return self.misc_question(question,
                        response_map={'y': 'yes', 'n': 'no', 'dk': 'dontnow'},
                        instructions='\nEnter: y (=Yes), n (=No), dk (=DontKnow):\n\n',
                        options=['y', 'n', 'dk'])

    def gender_question(self, question):
        """
        Question template with default arguments set for gender questions with
        response options: "Male", "Female", 'Other".
        """
        response_map={'m': 'male', 'f': 'female', 'o': 'other'}
        options = ['m', 'f', 'o']
        instructions = '\nEnter: m (=Male), f (=Female), o (=Other):\n\n'
        return self.misc_question(question, 
                         response_map=response_map,
                         instructions=instructions,
                         options=options,
                         valid=False)

    def yesnomaybe_question(self, question):
        """
        Question template with default arguments set for questions with
        response options: "Yes", "No", 'Maybe".
        """
        response_map={'y': 'yes', 'n': 'no', 'm': 'maybe'}
        options = ['y', 'n', 'm']
        instructions = '\nEnter: y (=Yes), n (=No), m (=Maybe):\n\n'
        return self.misc_question(question, 
                         response_map=response_map,
                         instructions=instructions,
                         options=options,
                         valid=False)

    def frequency_question(self, question):
        """
        Question template with default arguments set for questions regarding
        how frequently a participant does something. That is, a question with
        response options: "never", "rarely", "sometimes", "regularly" and 
        "very regularly".
        """
        return self.misc_question(question,
                         response_map={'1': 'never', '2': 'rarely', '3': 'sometimes', '4': 'regularly', '5': 'veryregularly'},
                         instructions='\n1 (="Never")\n2 (="Rarely")\n3 (="Sometimes")\n4 (="Regularly")\n5 (="Very Regularly")\n\n',
                         options=['1', '2', '3', '4', '5'],
                         valid=False)

    def notatall_to_very_questions(self, question):
        """
        Question template with default arguments set for questions regarding
        a participant's perception of something, such as interest or importance.
        Use for a question with response options: "Not at all",
          "Not Much", "Unsure", "A Little" and "Very"
        """
        return self.misc_question(question,
                         response_map={'1': 'notall', '2': 'notmuch', '3': 'unsure', '4': 'somewhat', '5': 'very'},
                         instructions = '\n1 (="Not at all")\n2 (="Not Much")\n3 (="Unsure")\n4 (="A Little")\n5 (="Very")\n\n',
                         options=['1', '2', '3', '4', '5'],
                         valid=False)

    def age_question(self, question, limits=[7, 18], valid=False):
        """
        Tempplate for recording age data. 
        Optional limit arguments can be given in list form. 
        Default is between 7 and 18 years old.
        """
        low_lim, high_lim = limits
        while not valid:
            age = input(f'{question}\nEnter integer between {low_lim} and {high_lim}.\nEnter {low_lim} if < {low_lim+1} and {high_lim} if >{high_lim-1}:\n\n')
            try:
                age = int(age)
                if age <= high_lim and age >= low_lim:
                    valid = True
                else:
                    print(self.error_msg)
            except:
                print(self.error_msg)
        return age

    def app_rating(self, question):
        """Specifically based on the app ratings question in the workshop questionnaire"""
        apps = input(f'{question}Enter the app-code followed by the rating:\nIf app is ticked but not rated put app-code followed by 66\n\nFor example participant rated microbit 4, Scratch 5 and ticked Kano Code (but didnt rate) then enter: "mb 4 s 5 kc 66"\n\nApp-codes are: Scratch = s, micro:bit = mb, Make Art = ma, Kano Code = kc, Make Snake = ms, Terminal Quest = tq, Hack Minecraft = hm:\n\n')
        apps = str.split(apps)
        s = mb = ma = mp = kc = ms = bk = hm = tq = 99
        app_dict = {'kc': kc, 's': s, 'mb': mb, 'ms': ms, 'tq': tq, 'ma': ma, 
                    'hm': hm, 'mp': mp}
        for i in range(0, len(apps), 2):
            app, rating = apps[i], int(apps[i+1])
            app_dict[app] = rating
        kc, s, mb, ms, tq,  ma, hm, mp = app_dict.values()
        return kc, s, mb, ms, tq,  ma, hm, mp

    def numbered_rating(self, question, limits=[1, 10], valid=False):
        """
        Tempplate for recording age data. 
        Optional limit arguments can be given in list form. 
        Default is between 7 and 18 years old.
        """
        low_lim, high_lim = limits
        while not valid:
            response = input(question)
            try:
                response = int(response)
                if response <= high_lim and response >= low_lim:
                    valid = True
                else:
                    print(self.error_msg)
            except:
                print(self.error_msg)
        return response
    
    def codeclub_courses(self, question, valid = False):
        inst1 = '\nEnter the code for each module completed.\n\nmb (=microbit)'
        inst2 = '\nkc (=kano code)\npy (=Python)\nsp (=Sonic Pi)\nscr (=Scratch)'
        inst3 = '\nca (=Climate Action)\nhtml (=HTML & CSS)\nrob (=Robotics)\n\n'
        while not valid:
            response = input(inst1+inst2+inst3)
            responses  = str.split(response)
            if False in [resp in ('mb, kc, py, sp, scr, ca, html, rob').split(', ') for resp in responses]:
                print('---------------------------------------------------------------------------')
                print('Invalid entry, enter one, or more, of mb, kc, py, sp, scr, ca, html, rob.')
                print('---------------------------------------------------------------------------')
            else:
                valid = True
        return responses
