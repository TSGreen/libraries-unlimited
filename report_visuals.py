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

filepath = 'WorkshopData'
filenames = glob(filepath+'/*.csv')

df = pd.concat([pd.read_csv(datafile) for datafile in filenames], ignore_index=True)

districts = sorted([datafile.split('/')[1][:-4] for datafile in filenames])

total_participants = df.Age.count()
print(f'\nThe following workshop data files have been read and included:\n{districts}\nIf you expect to see another file here, please check you have added it to the location {filepath}')
print(f'\nTotal number of participants to date: {total_participants}.\n')
print(f'Gender details:\n{df.Gender.value_counts()}')

plotpath = 'testing/'

class CreatePlots():
    def __init__(self):
        pass
    
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
        self.age = age
        plt.close()
        ax = plt.subplot(111)
        bins = np.linspace(6.5, 18.5, 13)
        print('\nPlotting age distribution..')
        median_age = int(age.median())
        print(f'\nMean age: {round(age.mean(),1)}, and median age: {median_age}.\n')
        values, base = np.histogram(age, bins=bins)
        percent = 100*(values/total_participants)
        plt.hist(age, bins = bins, fc = 'none', lw = 2.5, ec = sns.xkcd_rgb['cerulean blue'])
        for i  in range(len(values)):
            if values[i]>0:
                pcstr = '%.0f' % percent[i]
                plt.text(base[i+1]-0.5, values[i]+(0.05*np.max(values)), pcstr+'%', color='k', fontweight='bold', va='center', ha = 'center', fontsize = 10)
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
        plt.savefig(plotpath+'AgeDistribution.png', bbox_inches='tight')
        plt.savefig(plotpath+'AgeDistribution.pdf', bbox_inches='tight')
        sns.set()
    
    
    def prepoststackedbarplot(self, combinedanswers, labels, figurename, numbercolumns = 3, samplesize=0):
        plt.close()
        sns.set_style('ticks', {'axes.spines.right': False, 'axes.spines.top': False, 'axes.spines.left': False, 'ytick.left': False})
        ind = [0,1]
        ax = plt.subplot(111)
        num = 1/len(legendlabs)
        start, pos, = 0, [0,0,0]
        for i in range(len(legendlabs)):
            option = combinedanswers[:,i]
            plt.barh(ind, option, left = start, label = legendlabs[i])
            for k in range(len(ind)):
                xpos = pos[k]+option[k]/2
                percent = int(round(option[k]*100))
                if percent >= 10:
                    plt.annotate(str(percent)+' %', xy=(xpos,ind[k]), ha = 'center', fontsize = 15, color = '1')
                elif percent<3:
                    pass
                else: 
                    plt.annotate(str(percent), xy=(xpos,ind[k]), ha = 'center', fontsize = 15, color = '1')
            start = start+option
            pos = start
        plt.xlim(0,1)
        plt.yticks(ind, ('Post', 'Pre'), fontsize = 18)
        plt.xticks(fontsize = 18)
        ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
        plt.legend(bbox_to_anchor=(0, 0.99, 1, .05), loc=3, ncol=numbercolumns, borderaxespad=0., fontsize = 15)
        plt.minorticks_on()
        fig = plt.gcf()
        fig.set_size_inches(8.7,6)
        plt.figtext(0.9,0.135, ('Based on sample of %i participants' %samplesize), fontsize = 10, ha = 'right')
        plt.savefig(plotpath+'bar_'+figurename+'.pdf', bbox_inches='tight')
        plt.savefig(plotpath+'bar_'+figurename+'.png', bbox_inches='tight', dpi=600)
        sns.set()
    
plot = CreatePlots()
plot.age_distribution(df.Age)

question = 'candocoding'
preanswer = df['Pre_CanDoCoding']
postanswer = df['Post_CanDoCoding']
legendlabs = ['Yes', 'Dont Know', 'No']
combinedanswers = np.asarray([postanswer.value_counts(normalize=True).values, preanswer.value_counts(normalize=True).values])
                                                      
print('\nDo you believe you can do coding?\n-----------------------------')
print(f'Pre workshop:\n{preanswer.value_counts()}\n------------------------------')
print(f'Post workshop:\n{postanswer.value_counts()}')
plot.prepoststackedbarplot(combinedanswers, legendlabs, question, numbercolumns = 4, samplesize = preanswer.value_counts().sum())


