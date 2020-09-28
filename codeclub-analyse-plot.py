#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates the visualisations for the LU coding report.

Overview:
    - Reads in the data from a CSV file for each district.
    - Cleans and analyses the data.
    - Creates the graphs and saves them as pdf files for embedding in report.

@author: Tim Green
"""

import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker
from pathlib import Path

from analysisandplot import CodeClubAnalysis

codeclubs = CodeClubAnalysis()

savefile = Path.cwd().joinpath('report', 'codeclub_plots')
datafile = Path.cwd().joinpath('data', 'codeclubs')

codeclubs.read_datafiles(data_filepath=datafile, save_filepath=savefile)

codeclubs.gender('Gender')

codeclubs.age_distribution('Age')

codeclubs.britishcouncil_rating('BC_Rating')

codeclubs.question(question='CodingInterest',
              response_type='very_to_not_interest',
              prepost_question=True,
              title='How interested are you in coding?')

codeclubs.question(question='CanDoCoding',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you believe you can do coding?')

codeclubs.question(question='CodingImportance',
              response_type='very_to_not_importance',
              prepost_question=True,
              title='How important is coding to your life?')

codeclubs.question(question='BenefitCareer',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you believe coding will benefit your career?')

codeclubs.question(question='CodingCareer',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you want to pursue a career in coding?')

codeclubs.question(question='AttractLibraries',
              response_type='yes_dontknow_no',
              prepost_question=False,
              title='Do you think activities like this increase the '
              'attractiveness\n of libraries to young people?')

codeclubs.question(question='KnowMicrobit',
              response_type='know_language',
              prepost_question=True,
              title='Do you know about micro:bit?')

codeclubs.question(question='UnderstandVariable',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you understand what a variable is?')

codeclubs.question(question='UnderstandRepition',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you understand what a repition is?')

codeclubs.question(question='UnderstandBoolean',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you understand what a boolean is?')

codeclubs.question(question='UnderstandDataStructure',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you understand data structure?')

codeclubs.question(question='UnderstandFunction',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you understand what a function is?')

codeclubs.question(question='UnderstandHardware',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you understand what hardware is?')

try:
    codeclubs.question(question='KnowPython',
              response_type='know_language',
              prepost_question=True,
              title='Do you know about Python?')
except:
    print('\nCannot plot Python related question at this time. '
          'You need to do data entry for pre & post Python questionnaires first.\n')
