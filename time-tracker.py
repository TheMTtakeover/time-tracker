# set variables
sundayh = 0
sundaym = 0
mondayh = 0
mondaym = 0
tuesdayh = 0
tuesdaym = 0
wednesdayh = 0
wednesdaym = 0
thursdayh = 0
thursdaym = 0
fridayh = 0
fridaym = 0
saturdayh = 0 
saturdaym = 0
starttimeh = 0
starttimem = 0
totalweekh = 0
#find total minutes worked this week so far
totalm = ((sundaym + (sundayh * 60)) \
           + (mondaym + (mondayh * 60)) \
              + (tuesdaym + (tuesdayh * 60)) \
                 + (wednesdaym + (wednesdayh * 60)) \
                    + (thursdaym + (thursdayh * 60)) \
                       + (fridaym + (fridayh * 60)) \
                          + (saturdaym + (saturdayh * 60)))
#calculate remaining time
remtimem = (60 * totalweekh) - totalm
#This calculates a variable needed to find the correct ending time by determing if a lunch needs taken
if remtimem <= 360:
    lunchm = 0
else:
    lunchm = 30
#print (lunchm)
remtimeh= remtimem // 60
remtimem = (remtimem - (remtimeh * 60))
print ("Remaining time for the week", remtimeh, remtimem)
endtimeh = (starttimeh + remtimeh)
endtimem = (starttimem + remtimem + lunchm)
remtimec = (endtimem // 60)
endtimeh = (endtimeh + remtimec)
endtimem = (endtimem - (remtimec * 60))
print ("You should leave at", endtimeh, endtimem)
