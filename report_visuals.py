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

class CreatePlots():
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def age_distribution(self, age):
        '''
        Create histogram of age distribution.

        Parameters
        ----------
        age : Panda.Series or numpy.array
            The age column.

        Returns
        -------
        Data visualtions saved in png and pdf format.

        '''
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
        plt.hist(self.age, bins = bins, facecolor = 'none', 
                 linewidth = 2.5, edgecolor = '#3366cc')
        for i  in range(len(values)):
            if values[i]>0:
                pcstr = '%.0f' % percent[i]
                plt.text(base[i+1]-0.5, values[i]+(0.05*np.max(values)), 
                         pcstr+'%', color='k', fontweight='bold', 
                         va='center', ha = 'center', fontsize = 10)
        [plt.text(7, ypos*np.max(values), text, 
                  color='k', fontweight='bold', 
                  va='center', ha = 'left', 
                  fontsize = 12) for ypos, text in zip([0.98, 0.9], 
                                                       [f'Participant Total: {str(total_participants)}', 
                                                        f'Median age: {median_age} yrs'])]
        plt.xlabel('Age of participant (years)', fontsize = 20)
        plt.ylabel('Number of participants', fontsize = 20)
        plt.xlim(6.4,18.6)
        plt.ylim(0,1.1*np.max(values))
        ax.xaxis.set_major_locator(plt.MaxNLocator(14))
        plt.savefig(plotpath+'AgeDistribution.png', bbox_inches='tight', dpi=600)
        plt.savefig(plotpath+'AgeDistribution.pdf', bbox_inches='tight')
        sns.set()
    
    
    def stackedbarplot(self, responses, labels, figurename, numbercolumns = 3, samplesize=0):
        plt.close()
        print(f'Plotting the chart for {question} question..')
        sns.set_style('ticks', {'axes.spines.right': False, 
                                'axes.spines.top': False, 
                                'axes.spines.left': False, 
                                'ytick.left': False})
        if responses.shape[0] == 2:
            ind = [0,1]
        elif responses.shape[0] == 3:
            ind = [0, 0.85, 2]
        fig, ax = plt.subplots(figsize=(8.7, 6))
        num = 1/len(legendlabs)
        start, pos, = 0, [0,0,0]
        for i in range(responses.shape[1]):
            option = responses[:,i]
            plt.barh(ind, option, left = start, label = legendlabs[i])
            for k in range(len(ind)):
                xpos = pos[k]+option[k]/2
                percent = int(round(option[k]*100))
                if percent >= 10:
                    plt.annotate(f'{str(percent)} %', xy=(xpos,ind[k]), ha='center', fontsize=15, color='1')
                elif percent<3:
                    pass
                else:
                    plt.annotate(f'{str(percent)}', xy=(xpos,ind[k]), ha='center', fontsize=15, color='1')
            start = start+option
            pos = start
        plt.xlim(0,1)
        #plt.yticks(ind, ('Post', 'Pre'), fontsize=18)
        if responses.shape[0] == 2:
            plt.yticks(ind, ('Post', 'Pre'), fontsize=18)
        elif responses.shape[0] == 3:
            plt.yticks(ind, ('Male', 'Female', 'All'), fontsize = 18)        
        plt.xticks(fontsize = 18)
        ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
        plt.legend(bbox_to_anchor=(0, 0.99, 1, .05), loc=3, ncol=numbercolumns, borderaxespad=0, fontsize=15)
        plt.minorticks_on()
        plt.figtext(0.9,0.135, (f'Based on sample of {samplesize} participants'), fontsize=10, ha='right')
        plt.savefig(plotpath+'bar_'+figurename+'.pdf', bbox_inches='tight')
        plt.savefig(plotpath+'bar_'+figurename+'.png', bbox_inches='tight', dpi=600)
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

plot = CreatePlots(df)
plot.age_distribution('Age')

def analyse_question(data_column, cats, prepost_question=False):
    if prepost_question == True:
        df['Post_'+data_column] = pd.Categorical(df['Post_'+data_column], categories=cats)
        df['Pre_'+data_column] = pd.Categorical(df['Pre_'+data_column], categories=cats)
        responses_pc_post = df['Post_'+data_column].value_counts(normalize=True, sort=False).values
        responses_pc_pre = df['Pre_'+data_column].value_counts(normalize=True, sort=False).values
        responses = np.array([responses_pc_post, responses_pc_pre])
        responses_pre = df['Pre_'+data_column].value_counts(normalize=False)
        samplesize=responses_pre.sum()
    if prepost_question == False:
        df[data_column] = pd.Categorical(df[data_column], categories=cats)
        responses_all = df[data_column].value_counts(normalize=False, sort=False).values
        samplesize = responses_all.sum()
        responses_pc_all = df[data_column].value_counts(normalize=True, sort=False).values
        responses_pc_male = df[data_column][df['Gender']=='male'].value_counts(normalize=True, sort=False).values
        responses_pc_female = df[data_column][df['Gender']=='female'].value_counts(normalize=True, sort=False).values
        responses = np.array([responses_pc_male, responses_pc_female, responses_pc_all])
    return responses, samplesize


question = 'candocoding'
cats = ['yes', 'dontknow', 'no']
legendlabs = ['Yes', 'Dont Know', 'No']
responses, samplesize = analyse_question('CanDoCoding', cats, prepost_question=True)
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=4, samplesize=samplesize)
# print('\nDo you believe you can do coding?\n-----------------------------')
# print(f'Pre workshop:\n{preanswer.value_counts()}\n------------------------------')
# print(f'Post workshop:\n{postanswer.value_counts()}')
# #plot.prepoststackedbarplot(combinedanswers, legendlabs, question, numbercolumns=4, samplesize= preanswer.value_counts().sum())

question = 'codinginterest'
cats = ['very', 'somewhat', 'unsure', 'notatall', 'notmuch']
legendlabs = ['Very Interested', 'Somewhat Interested', 'Unsure', 'Not really intersted', 'Not intersted at all']
responses, samplesize = analyse_question('CodingInterest', cats, prepost_question=True)
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=2, samplesize=samplesize)

question = 'codingimportance'
cats = ['very', 'somewhat', 'unsure', 'notatall', 'notmuch']
responses, samplesize = analyse_question('CodingImportance', cats, prepost_question=True)
legendlabs = ['Very Important', 'Somewhat Important', 'Unsure', 'Not very important', 'Not important at all']
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=2, samplesize=samplesize)

question = 'workshopexp'
cats = ['verygood', 'good', 'okay', 'bad']
responses, samplesize = analyse_question('WorkshopFeedback', cats, prepost_question=False)
legendlabs = ['Very good', 'Good', 'Okay', 'Bad']
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=4, samplesize=samplesize)

question = 'itaccess'
legendlabs = ['No Access', 'Access at Home', 'Access at both home and school', 'Access at School']
cats=['no', 'home', 'HomeSchool', 'school']
responses, samplesize = analyse_question( 'ITaccess', cats, prepost_question=False)
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=2, samplesize=samplesize)

question = 'itusefreq'
legendlabs = ['Never', 'Rarely', 'Sometimes', 'Regularly', 'Very Regularly']
cats=['never', 'rarely', 'sometimes', 'regularly', 'veryregularly']
responses, samplesize = analyse_question('UseComputersOften', cats, prepost_question=False)
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=3, samplesize=samplesize)

question = 'libvisitinterest'
cats = ['very', 'somewhat', 'unsure', 'notatall', 'notmuch']
legendlabs = ['Very Interested', 'Somewhat Interested', 'Unsure', 'Not really intersted', 'Not intersted at all']
responses, samplesize = analyse_question('DesireLibraryVisit', cats, prepost_question=False)
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=2, samplesize=samplesize)

question = 'libraryvisitfreq'
legendlabs = ['Never', 'Rarely', 'Sometimes', 'Regularly', 'Very Regularly']
cats=['never', 'rarely', 'sometimes', 'regularly', 'veryregularly']
responses, samplesize = analyse_question('VisitLibraryBefore', cats, prepost_question=False)
plot.stackedbarplot(responses, legendlabs, question, numbercolumns=3, samplesize=samplesize)