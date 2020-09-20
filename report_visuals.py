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


class WorkshopAnalysis():

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.response_dict = {
            'yes_dontknow_no': (['yes', 'dontknow', 'no'], 3,
                                ['Yes', 'Dont Know', 'No']),
            'yes_maybe_no': (['yes', 'maybe', 'no'], 3,
                                ['Yes', 'Maybe', 'No']),
            'very_to_not_interest': (['very', 'somewhat', 'unsure', 'notmuch', 'notatall'], 2,
                            ['Very Interested', 'Somewhat Interested', 'Unsure', 'Not really intersted', 'Not intersted at all']),
            'very_to_not_importance': (['very', 'somewhat', 'unsure', 'notmuch', 'notatall'], 2,
                            ['Very Important', 'Somewhat Important', 'Unsure', 'Not really important', 'Not important at all']),
            'verygood_to_bad': (['verygood', 'good', 'okay', 'bad'], 4,
                                ['Very good', 'Good', 'Okay', 'Bad']),
            'frequency': (['never', 'rarely', 'sometimes', 'regularly', 'veryregularly'], 3,
                          ['Never', 'Rarely', 'Sometimes', 'Regularly', 'Very Regularly']),
            'itaccess': (['no', 'home', 'HomeSchool', 'school'], 2, 
                         ['No Access', 'Access at Home', 'Access at both home and school', 'Access at School']),
            'never_little_lot': (['No', 'Alittle', 'Alot'], 3,
                                ['Never', 'A little', 'A lot']),
            }


    def question(self, question, response_type, prepost_question, title):
        """
        Set-up the paramteres for analysing and plotting the given question.
        Calls on the method for doing the analysis and the method for creating
        the stacked bar plots.

        Parameters
        ----------
        question : str
            The short-form name for the question. Is also the relevant column name.
        response_type : str
            A string indicating the type of resonses for given question. Acts as
            the key for the reponse_dict dictionary which returns the responses in 
            the data and their corresponding labels for plotting.
        prepost_question : boolean
            If True, then the given question is asked on the pre and post questionnaires
            and the desired form is a comparison of pre and post reponses.
            If False, then question is only asked once and instead desire aggregation
            by gender.
        title : str
            The full form of the given question.

        Returns
        -------
        None.

        """
        cats = self.response_dict[response_type][0]
        legend_columns = self.response_dict[response_type][1]
        legend_labels = self.response_dict[response_type][2]
        responses, samplesize = self.analyse_question(question, cats, prepost_question)
        self.stackedbarplot(responses, legend_labels, question, legend_columns, samplesize)


    def analyse_question(self, data_column, cats, prepost_question=False):
        """
        Generate the response statistics to the given question.

        Parameters
        ----------
        data_column : str
            The column name in the dataframe associated to the question.
        cats : list
            A list of the possible responses / categories for that question.
        prepost_question : Boolean, optional
            True if the question is present on the pre- and post- questionnaires
            and we want to return a comparison of pre & post. 
            The default is False and aggregates data by gender.

        Returns
        -------
        responses : numpy.array
            The percentage of each response.
        samplesize : int
            The number of non-null responses to this particular question.

        """
        if prepost_question:
            self.dataframe['Post_'+data_column] = pd.Categorical(self.dataframe['Post_'+data_column], categories=cats)
            self.dataframe['Pre_'+data_column] = pd.Categorical(self.dataframe['Pre_'+data_column], categories=cats)
            responses_pc_post = self.dataframe['Post_'+data_column].value_counts(normalize=True, sort=False).values
            responses_pc_pre = self.dataframe['Pre_'+data_column].value_counts(normalize=True, sort=False).values
            responses = np.array([responses_pc_post, responses_pc_pre])
            samplesize = self.dataframe['Pre_'+data_column].value_counts(normalize=False).sum()
        if not prepost_question:
            self.dataframe[data_column] = pd.Categorical(self.dataframe[data_column], categories=cats)
            samplesize = self.dataframe[data_column].value_counts(normalize=False, sort=False).values.sum()
            responses_pc_all = self.dataframe[data_column].value_counts(normalize=True, sort=False).values
            responses_pc_male = self.dataframe[data_column][self.dataframe['Gender']=='male'].value_counts(normalize=True, sort=False).values
            responses_pc_female = self.dataframe[data_column][self.dataframe['Gender']=='female'].value_counts(normalize=True, sort=False).values
            responses = np.array([responses_pc_male, responses_pc_female, responses_pc_all])
        return responses, samplesize


    def stackedbarplot(self, responses, labels, figurename, legend_columns = 3, samplesize=0):
        """
        Create stacked bar plots showing the proportional responses to the given question. 

        Parameters
        ----------
        responses : numpy array
            Array of the responses for the given question.
        labels : list of strings
            The possible responses for the given question.
        figurename : str
            Short form name of the question asked.
        legend_columns : int, optional
            The number of columns in the legend. Vary to control legend layout.
            The default is 3.
        samplesize : int, optional
            The number of participants which have responded to given question.
            The default is 0.

        Returns
        -------
        Saves the figure to pdf and png files.

        """
        plt.close()
        print(f'Plotting the chart for {figurename} question..')
        sns.set_style('ticks', {'axes.spines.right': False,
                                'axes.spines.top': False,
                                'axes.spines.left': False,
                                'ytick.left': False})
        if responses.shape[0] == 2:
            ind = [0, 1]
        elif responses.shape[0] == 3:
            ind = [0, 0.85, 2]
        fig, ax = plt.subplots(figsize=(8.7, 6))
        start, pos, = 0, [0, 0, 0]
        for i in range(responses.shape[1]):
            option = responses[:,i]
            plt.barh(ind, option, left=start, label=labels[i])
            for k in range(len(ind)):
                xpos = pos[k]+option[k]/2
                percent = int(round(option[k]*100))
                if percent >= 10:
                    plt.annotate(f'{str(percent)} %', xy=(xpos, ind[k]),
                                 ha='center', fontsize=15, color='1')
                elif percent<3:
                    pass
                else:
                    plt.annotate(f'{str(percent)}', xy=(xpos, ind[k]),
                                 ha='center', fontsize=15, color='1')
            start = start+option
            pos = start
        plt.xlim(0,1)
        if responses.shape[0] == 2:
            plt.yticks(ind, ('Post', 'Pre'), fontsize=18)
        elif responses.shape[0] == 3:
            plt.yticks(ind, ('Male', 'Female', 'All'), fontsize=18)
        plt.xticks(fontsize=18)
        ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
        plt.legend(bbox_to_anchor=(0, 0.99, 1, .05), loc=3, ncol=legend_columns, borderaxespad=0, fontsize=15)
        plt.minorticks_on()
        plt.figtext(0.9, 0.135, (f'Based on sample of {samplesize} participants'), fontsize=10, ha='right')
        plt.savefig(plotpath+'bar_'+figurename+'.pdf', bbox_inches='tight')
        plt.savefig(plotpath+'bar_'+figurename+'.png', bbox_inches='tight', dpi=600)
        sns.set()


    def app_ratings(self):
        """
        Create a grid of histograms showing participant rating for each app.

        Returns
        -------
        Saves the figure to pdf and png files. 

        """
        plt.close()
        fig = plt.figure(figsize=(8, 10))
        (ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8) = fig.subplots(4, 2, sharex=True)
        apps = ['Scratch', 'Micro:bit', 'Make Art', 'Make Pong', 'Kano Code',
                'Make Snake', 'Hack Minecraft', 'Terminal Quest']
        apps_columns = {'Scratch': 'Scratch_rating', 'Micro:bit': 'Microbit_rating', 'Make Art': 'MakeArt_rating', 
                        'Make Pong': 'MakePong_rating', 'Kano Code': 'KanoCode_rating', 'Make Snake': 'MakeSnake_rating',
                        'Hack Minecraft': 'HackMinecraft_rating', 'Terminal Quest': 'TerminalQuest_rating'}
        axs = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
        sns.set_style('ticks', {'axes.spines.right': False, 'axes.spines.top': False})
        bins = np.linspace(-0.5, 5.5, 7)
        for app, ax in zip(apps, axs):
            app_column = apps_columns[app]
            usedratedapp = self.dataframe[app_column][self.dataframe[app_column].isin(('1,2,3,4,5').split(','))].values.astype(int)
            mean_rating = usedratedapp.sum()/len(usedratedapp)
            values, base = np.histogram(usedratedapp, bins=bins)
            ax.hist(usedratedapp, bins=bins, fc='none', lw=2.5, ec=sns.xkcd_rgb['cerulean blue'])
            plt.ylim(0, np.max(values)*1.1)
            plt.xlim(0.4, 5.6)
            ax.text(1, np.max(values)*0.9, app, weight='bold', ha='left')
            ax.text(1, np.max(values)*0.75, 'Mean: %1.1f/5' %mean_rating)
            ax.yaxis.set_major_locator(ticker.MaxNLocator(5))
            ax.xaxis.set_ticks_position('bottom')
        ax7.set_xlabel('Rating /5', fontsize=20)
        ax8.set_xlabel('Rating /5', fontsize=20)
        ax3.set_ylabel('Number of Participants',  fontsize=20)
        plt.savefig(plotpath+'AppRatings.png', bbox_inches='tight')
        plt.savefig(plotpath+'AppRatings.pdf', bbox_inches='tight')
    
    
    def age_distribution(self, age):
        """
        Create histogram of age distribution.

        Parameters
        ----------
        age : Panda.Series or numpy.array
            The age column.

        Returns
        -------
        Data visualtions saved in png and pdf format.

        """
        self.age = self.dataframe[age]
        plt.close()
        sns.set_style('ticks', {'axes.spines.right': False, 
                                'axes.spines.top': False, 
                                'xtick.bottom': False})
        fig, ax = plt.subplots(figsize=(8.7, 6))
        bins = np.linspace(6.5, 18.5, 13)
        print('\nPlotting age distribution..')
        median_age = int(self.age.median())
        print(f'\nMean age: {round(self.age.mean(),1)}, and median age: {median_age}.\n')
        values, base = np.histogram(self.age, bins=bins)
        percent = 100*(values/total_participants)
        plt.hist(self.age, bins=bins, facecolor='none', 
                 linewidth=2.5, edgecolor='#3366cc')
        for i in range(len(values)):
            if values[i]>0:
                pcstr = '%.0f' % percent[i]
                plt.text(base[i+1]-0.5, values[i]+(0.05*np.max(values)), 
                         pcstr+'%', color='k', fontweight='bold', 
                         va='center', ha='center', fontsize = 10)
        [plt.text(7, ypos*np.max(values), text,
                  color='k', fontweight='bold',
                  va='center', ha = 'left', 
                  fontsize = 12) for ypos, text in zip([0.98, 0.9], 
                                                       [f'Participant Total: {str(total_participants)}', 
                                                        f'Median age: {median_age} yrs'])]
        plt.xlabel('Age of participant (years)', fontsize = 20)
        plt.ylabel('Number of participants', fontsize = 20)
        plt.xlim(6.4, 18.6)
        plt.ylim(0, 1.1*np.max(values))
        ax.xaxis.set_major_locator(plt.MaxNLocator(14))
        plt.savefig(plotpath+'AgeDistribution.png', bbox_inches='tight', dpi=600)
        plt.savefig(plotpath+'AgeDistribution.pdf', bbox_inches='tight')
        sns.set()


filepath = 'WorkshopData'
filenames = glob(filepath+'/*.csv')

df = pd.concat([pd.read_csv(datafile) for datafile in filenames], ignore_index=True)

districts = sorted([datafile.split('/')[1][:-4] for datafile in filenames])

total_participants = df.Age.count()
print(f'\nThe following workshop data files have been read and included:\n{districts}\nIf you expect to see another file here, please check you have added it to the location {filepath}')
print(f'\nTotal number of participants to date: {total_participants}.\n')
print(f'Gender details:\n{df.Gender.value_counts()}')

plotpath = 'testing/'

workshops = WorkshopAnalysis(df)

workshops.app_ratings()

workshops.age_distribution('Age')

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

workshops.question(question='CodedBefore',
              response_type='never_little_lot',
              prepost_question=False,
              title='Have you ever done coding before?')

workshops.question(question='Want_to_LearnMoreCoding',
              response_type='yes_maybe_no',
              prepost_question=False,
              title='Would you like to learn more coding?')

workshops.question(question='WillVisitLibrary',
              response_type='yes_maybe_no',
              prepost_question=False,
              title='Would you visit the library more often if activities like this are offered?')

workshops.question(question='WillUseDevices',
              response_type='yes_maybe_no',
              prepost_question=False,
              title='If the devices [Kano & Micro:bit] are avaiable in the library, would you use them?')
