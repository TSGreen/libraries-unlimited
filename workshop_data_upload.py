import numpy as np
import pandas as pd
import os

district = 'FAKE'

notatall_to_very = '\n1 (="Not at all")\n2 (="Not Much")\n3 (="Unsure")\n4 (="A Little")\n5 (="Very")\n\n'
never_to_veryregularly = '\n1 (="Never")\n2 (="Rarely")\n3 (="Sometimes")\n4 (="Regularly")\n5 (="Very Regularly")\n\n'  

gender_valid = False
while not gender_valid:
    gender = input('Q1: Gender?\nEnter: m (=Male), f (=Female), o (=Other):\n\n')
    if gender == 'm':
        gender = 'male'
        gender_valid = True
    elif gender == 'f':
        gender = 'female'
        gender_valid = True
    elif gender == 'o':
        gender == 'other'
        gender_valid = True
    else:
        print('You have entered an invalid entry, try again.\n')

valid = False
while not valid:
    age = input('Q2: Age?\nEnter: Age integer, 7 if < 8 and 18 if >17:\n\n')
    age = int(age)
    if age <= 18 and age >= 7:
        valid = True
    else:
        print('Invalid age entry, enter number 7 and 18/n')
        
valid = False
while not valid:
    response = input('Q3: Do you believe you can do programming?\nEnter: y (=Yes), n (=No), dk (=DontKnow):\n\n')
    if response == 'y':
        response  = 'yes'
        valid = True
    elif response  == 'dk':
        response  = 'dontknow'
        valid = True
    elif response  == 'n':
        response  = 'no'
        valid = True
    else:
        print('Invalid entry. Please try again')
    precancode = response

valid = False
while not valid:
    precodingimport = input(f'Q4: How important is programming to your life?{notatall_to_very}')
    if precodingimport == '1':
        precodingimport = 'notatall'
        valid = True
    elif precodingimport == '2':
        precodingimport = 'notmuch'
        valid = True
    elif precodingimport == '3':
        precodingimport = 'unsure'
        valid = True
    elif precodingimport == '4':
        precodingimport = 'somewhat'
        valid = True
    elif precodingimport == '5':
        precodingimport = 'very'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')

valid = False
while not valid:
    precodingint = input(f'Q5: How interested are you to do coding?{notatall_to_very}')
    if precodingint == '1':
        precodingint = 'notatall'
        valid = True
    elif precodingint == '2':
        precodingint = 'notmuch'
        valid = True
    elif precodingint == '3':
        precodingint = 'unsure'
        valid = True
    elif precodingint == '4':
        precodingint = 'somewhat'
        valid = True
    elif precodingint == '5':
        precodingint = 'very'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')

valid = False
while not valid:
    itaccess = input('Q6: Computer access?\nEnter:\nh (="Yes, at Home")\ns (="Yes, at school")\nhs (="Yes, at home & school")\nn (="No)\n\n')
    if itaccess == 'h':
        itaccess = 'home'
        valid = True
    elif itaccess == 's':
        itaccess = 'school'
        valid = True
    elif itaccess == 'hs':
        itaccess = 'HomeSchool'
        valid = True
    elif itaccess == 'n':
        itaccess = 'no'
        valid = True
    else:
        print('You have entered an invalid entry, try again.\n')

valid = False
while not valid:
    usecomp = input(f'Q7: Use computers often?{never_to_veryregularly}')
    if usecomp == '1':
        usecomp = 'never'
        valid = True
    elif usecomp == '2':
        usecomp = 'rarely'
        valid = True
    elif usecomp == '3':
        usecomp = 'sometimes'
        valid = True
    elif usecomp == '4':
        usecomp = 'regularly'
        valid = True
    elif usecomp == '5':
        usecomp = 'veryregularly'
        valid = True
    else:
        print('You have entered an invalid entry, try again.\n')

valid = False
while not valid:
    libraryvisitbefore = input(f'Q8: Visit library often?{never_to_veryregularly}')
    if libraryvisitbefore == '1':
        libraryvisitbefore = 'never'
        valid = True
    elif libraryvisitbefore == '2':
        libraryvisitbefore = 'rarely'
        valid = True
    elif libraryvisitbefore == '3':
        libraryvisitbefore = 'sometimes'
        valid = True
    elif libraryvisitbefore == '4':
        libraryvisitbefore = 'regularly'
        valid = True
    elif libraryvisitbefore == '5':
        libraryvisitbefore = 'veryregularly'
        valid = True
    else:
        print('You have entered an invalid entry, try again.\n')


valid = False
while not valid:
    libvisitdesire = input(f'Q9: How interested are you to visit library regularly?{notatall_to_very}')
    if libvisitdesire == '1':
        libvisitdesire = 'notatall'
        valid = True
    elif libvisitdesire == '2':
        libvisitdesire = 'notmuch'
        valid = True
    elif libvisitdesire == '3':
        libvisitdesire = 'unsure'
        valid = True
    elif libvisitdesire == '4':
        libvisitdesire = 'somewhat'
        valid = True
    elif libvisitdesire == '5':
        libvisitdesire = 'very'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')

print('\n\nTurn sheet over and enter post-session feedback answers:\n')

valid = False    
while not valid:
    response = input('Q10: Do you believe you can do programming?\nEnter: y (=Yes), n (=No), dk (=DontKnow):\n\n')
    if response == 'y':
        response  = 'yes'
        valid = True
    elif response  == 'dk':
        response  = 'dontknow'
        valid = True
    elif response  == 'n':
        response  = 'no'
        valid = True
    else:
        print('Invalid entry. Please try again')
    candocoding = response

valid = False
while valid == False:
    codingint = input(f'Q11: Now, how interested are you to do coding?{notatall_to_very}')
    if codingint == '1':
        codingint = 'notatall'
        valid = True
    elif codingint == '2':
        codingint = 'notmuch'
        valid = True
    elif codingint == '3':
        codingint = 'unsure'
        valid = True
    elif codingint == '4':
        codingint = 'somewhat'
        valid = True
    elif codingint == '5':
        codingint = 'very'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')

valid = False
while valid == False:
    codingimport = input(f'Q12: Now, how important is programming to your life?{notatall_to_very}')
    if codingimport == '1':
        codingimport = 'notatall'
        valid = True
    elif codingimport == '2':
        codingimport = 'notmuch'
        valid = True
    elif codingimport == '3':
        codingimport = 'unsure'
        valid = True
    elif codingimport == '4':
        codingimport = 'somewhat'
        valid = True
    elif codingimport == '5':
        codingimport = 'very'
        valid = True
    else:
        print('Invalid entry, enter number between 1 and 5')

valid = False
while valid == False:
    workshopex = input('Q13: Overall experience of workshop?\nEnter:\nvg (="Very Good")\ng (="Good")\nok (="Okay")\nb =("Bad")?\n\n')
    if workshopex == 'vg':
        workshopex = 'verygood'
        valid = True
    elif workshopex == 'g':
        workshopex = 'good'
        valid = True
    elif workshopex == 'ok':
        workshopex = 'okay'
        valid = True
    elif workshopex == 'b':
        workshopex = 'bad'
        valid = True
    else:
        print('You have entered an invalid entry, try again.')   

s, mb, ma, mp, kc, ms, bk, hm, tq = [99,99,99,99,99,99,99,99, 99]
apps = input('Q14: Which apps were used and what rating? Enter the app-code followed by the rating:\nIf app is ticked but not rated put app-code followed by 66\n\nFor example participant rated microbit 4, Scratch 5 and ticked Kano Code (but didnt rate) then enter: "mb 4 s 5 kc 66"\n\nApp-codes are: Scratch = s, micro:bit = mb, Make Art = ma, Kano Code = kc, Make Snake = ms, Terminal Quest = tq, Hack Minecraft = hm:\n\n')
apps = str.split(apps)
for i in range(len(apps)//2):
    i = i*2
    app, rating = apps[i], int(apps[i+1])
    if app == 'hm':
        hm = rating
    elif app == 's':
        s = rating
    elif app == 'mb':
        mb = rating
    elif app == 'ma':
        ma = rating
    elif app == 'kc':
        kc = rating
    elif app == 'ms':
        ms = rating
    elif app == 'bk':
        bk = rating
    elif app == 'mp':
        mp = rating
    elif app == 'tq':
        tq = rating

valid = False
while valid == False:
    libraryvisit = input('Q15: Make you visit library more?\nEnter: y (=Yes), n (=No), m (=Maybe):\n\n')
    if libraryvisit == 'y':
        libraryvisit = 'yes'
        valid = True
    elif libraryvisit == 'm':
        libraryvisit = 'maybe'
        valid = True
    elif libraryvisit == 'n':
        libraryvisit = 'no'
        valid = True
    else:
        print('You have entered an invalid entry, try again.\n')


valid = False
while valid == False:
    usedevices = input('Q16: Use devices in the library?\nEnter: y (=Yes), n (=No), m (=Maybe):\n\n')
    if usedevices == 'y':
        usedevices = 'yes'
        valid = True
    elif usedevices == 'm':
        usedevices = 'maybe'
        valid = True
    elif usedevices == 'n':
        usedevices = 'no'
        valid = True
    else:
        print('You have entered an invalid entry, try again.\n')
        
new_data = np.array([gender, age, precancode, precodingimport, precodingint, itaccess,  
            usecomp, libraryvisitbefore,  libvisitdesire, candocoding, codingint, 
            codingimport, workshopex, s, mb, ma, mp, kc, ms, hm, tq, 
            libraryvisit, usedevices])
#%%
colnames = ('Gender, Age, Pre_CanDoCoding, Pre_CodingImportance, Pre_CodingInterest, '
            'ITaccess, UseComputersOften, VisitLibraryBefore, DesireLibraryVisit, '
            'Post_CanDoCoding, Post_CodingInterest, Post_CodingImportance, WorkshopFeedback, ' 
            'Scratch_rating, Microbit_rating, MakeArt_rating, MakePong_rating, '
            'KanoCode_rating, MakeSnake_rating, HackMinecraft_rating, '
            'TerminalQuest_rating, WillVisitLibrary, WillUseDevices').split(', ')

df = pd.DataFrame(new_data.reshape(1,-1), columns=colnames)

df['Pre_CanDoCoding'].replace({'y':'yes', 'n':'no', 'dk':'dontknow'}, inplace = True)
df['Post_CanDoCoding'].replace({'y':'yes', 'n':'no', 'dk':'dontknow'}, inplace = True)
columns = ('Scratch_rating, Microbit_rating, MakeArt_rating, MakePong_rating, KanoCode_rating, MakeSnake_rating, HackMinecraft_rating, TerminalQuest_rating').split(', ')
for col in columns:
    df[col].replace({'66':'not_rated', '99':'not_used'}, inplace = True)
df.to_csv('WorkshopData/'+district+'.csv', mode='a', index=False, header=not os.path.exists('WorkshopData/'+district+'.csv'))