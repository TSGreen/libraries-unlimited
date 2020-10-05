Set-up:
Unzip the BCWorkshopFeedback file, this contains all the Python scripts, questionnaire data, reporting file and plots. Do not change the directory structure. 
Run pip install -r requirements.txt, this will install all the dependency Python packages for the data entry and analysis scripts. 

Data Entry:
There a few data entry scripts –  including one for the workshops, one for the general pre-Code Club questionnaires and ones for the pre & post module specific Code Club questionnaires – but they all operate in similar manner. The script prompts the user to answer each question for an individual participant and creates/appends those answers to a csv file specific to each district. Each script imports the DataEntry class from the dataentry.py file, so that file must be present also.  
The general procedure is as follows:
•	Open appropriate python script, for example “cc_general_pre_data_upload.py” for the general pre-Code Club questionnaire. 
•	Change the variable “district”, which is located near the beginning of the script, to the relevant library district.
•	Run the script and enter the answers as prompted. 
•	If at any point during the entry you make a mistake, use ctrl-c (on Linux anyway, there may be an alternative Windows specific command[?]) to interrupt the script and start again. (The data you have input only saves to a file as the final act of the script, so do not worry about any incorrect data prior to your ‘keyboard interrupt’ being saved). If it has saved with an incorrect value (if for example you mistyped the final question), you will have to edit the csv file directly. 
•	The data will save to a csv file in the location given by the “savedatafile” variable given at the start of the script (e.g. into data > codeblubs or data > workshops). 
•	After completing one participant’s questionnaire, just run again for the next participant. 

Data Analysis and Creating Visuals:
After doing data entry just run the relevant file (either codeclub_analyse_plot.py or workshop_analyse_plot.py) to update the plots for the report. The new data you have just entered will automatically be included in the analysis. 
Note these files rely on importing a class from the analsysiandplot.py file, so that must be present for these to work. 
The visuals that are generated are saved as pdf (without titles) and png (with titles) files in either report > codeclub_plots or report > workshop_plots. The LaTeX report file will import the pdf version of the images from these locations. 



The Report :
Set-up: I recommend using an online LaTeX editor called Overleaf (www.overleaf.com) as it frees you from installing all the required compilers, packages and editors. Register an account at overleaf and then select “New Project” and then “Upload Project”. Then “Select a .zip file” and within the BCWorkshopFeedback directory select “report.zip”. This contains the .tex file and all the necessary images. After upload Overleaf will automatically compile and generate the pdf report. 
Updating the figures: After adding new data and re-running to the analysis as above you will have updated plots stored locally. You will need to upload these new figures to Overleaf for inclusion in the report. In Overleaf click on the folder that needs updating (for example “codeclub_plots”) then “Upload” and drag the folder from local. “Do you want to overwrite?” > “Overwrite”. After uploading, just hit “Recompile”. 

Editing the data entry scripts:
If you want to edit the data entry scripts by adding a new question you can use one of the default formats, e.g. yes_no_maybe for “yes”, “no”, “maybe” type questions, or create a custom one by using the following format:
Newvariable = prompt.misc_question(‘Some string of the question’, options=[“option1”, “option2”], response_map={“option1”: “The desired string1”, “option2”: “The desired string2”}, instructions=”Some string to explain to the user what they should enter, e.g. Enter option1 for “Desired string 1”)
Then ensure you add “newvariable” to the “new_data” array at the end of the script and add a string to the “colnames” variable which will be the column name in the datafile. This column name is then the string you will pass into the analysis script to analyse this particular question. 
The full set of default question types can be found by skimming the functions in dataentry.py.
If you create a new data entry script, for example for an additional Code Club module, then you should duplicate an existing one. Then you will need to change the “coursequestionnaire” variable at the beginning, as well as adding, removing or editing any questions as required.  Remember to keep the new_data array and colnames list up-to-date. 

Expanding analysis scripts:
If you have added new questions to the data entry you may also have to add these to the data analysis script. Follow the format of the questions already in there, if the question is similar to others you can use one of the default “response_type” settings, such as yes_dontknow_no for questions with possible responses in the form “yes”, “no”, “don’t know”. Check the __init__ method in the FeedbackAnalysis class in analysisandplot.py for the full set of given response types. 
