# time-tracker
This script is used to figure out what time you need to leave on your last day of work to hit X hours

How to use:
1) Input the hours and minutes you have worked for everday of the week so far. Example:
```
# set variables
sundayh = 0
sundaym = 0
mondayh = 8
mondaym = 20
tuesdayh = 8
tuesdaym = 6
wednesdayh = 6
wednesdaym = 26
thursdayh = 8
thursdaym = 40
fridayh = 0
fridaym = 0
saturdayh = 0 
saturdaym = 0
```
2) Input the time you started your shift for the final day of the week. NOTE: This must be in 24hr time Example:
```
starttimeh = 13
starttimem = 40
```
3) Input the total number of hours you want to work in the week. Example:
```
totalweekh = 40
```
4) Run script. Example of output using the information provided in all of the examples:
```
Remaining time for the week 8 28
You should leave at 22 38
```
This output tells me that I need to work  8 hours and 28 minutes to hit my goal of 40 hours this week. To hit 40 I should leave at 22:38

NOTE: This script assume on the last day you will take a 30 minute unpaid lunch if you work 6 hours or more. If your lunch is unpaid but not 30 minutes then change this varaible to the length of your lunch in minutes
```
else:
    lunchm = 30
```
If your lunch is paid or you do not take a lunch then comment out the following lines
```
if remtimem <= 360:
    lunchm = 0
else:
    lunchm = 30
```
