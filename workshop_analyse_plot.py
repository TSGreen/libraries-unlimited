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

from analysisandplot import FeedbackAnalysis

workshops = FeedbackAnalysis()

savefile = Path.cwd().joinpath('report', 'workshop_plots')
datafile = Path.cwd().joinpath('data', 'workshops')

workshops.read_datafiles(data_filepath=datafile, save_filepath=savefile)

workshops.gender('Gender')

workshops.age_distribution('Age')

workshops.app_ratings()

workshops.question(question='CodingInterest', 
              response_type='very_to_not_interest', 
              prepost_question=True, 
              title='How interested are you in coding?')

workshops.question(question='CanDoCoding',
              response_type='yes_dontknow_no',
              prepost_question=True,
              title='Do you believe you can do coding?')

workshops.question(question='CodingImportance',
              response_type='very_to_not_importance',
              prepost_question=True,
              title='How important is coding to your life?')

workshops.question(question='WorkshopFeedback',
              response_type='verygood_to_bad',
              prepost_question=False,
              title='How would you rate the workshop overall?')

workshops.question(question='ITaccess',
              response_type='itaccess',
              prepost_question=False,
              title='Do you have regular access to a computer at home or school?')

workshops.question(question='UseComputersOften',
              response_type='frequency',
              prepost_question=False,
              title='How often do you use a computer?')

workshops.question(question='DesireLibraryVisit',
              response_type='very_to_not_interest',
              prepost_question=False,
              title='How interested are you in visiting the library?')

workshops.question(question='VisitLibraryBefore',
              response_type='frequency',
              prepost_question=False,
              title='How often do you visit the library?')


workshops.question(question='VisitLibrary_Activities',
              response_type='yes_maybe_no',
              prepost_question=False,
              title='Would you visit the library more often if activities like this are offered?')

workshops.question(question='VisitLibrary_Devices',
              response_type='yes_maybe_no',
              prepost_question=False,
              title='If the devices [Kano & Micro:bit] are avaiable in the\n library, would you use them?')
