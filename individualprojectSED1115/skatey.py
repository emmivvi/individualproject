#importslibraries
import pandas as pd
import plotly as plt
import plotly.express as px
import math
import datetime

#file locations
d20 = pd.read_csv('climate2020.csv')
d21 = pd.read_csv('climate2021.csv')
d22 = pd.read_csv('climate2022.csv')
d23 = pd.read_csv('climate2023.csv')

#cleaning and organizing function
def clean(df):
    columnStr = list(df.columns.values) #column title location
    columnList = columnStr[0].replace("\"", "").split(',') #remove "" from title string and split by the ","


    df.rename(columns={columnStr[0]: columnList[0]}, inplace=True) #replace first (and only at moment) column title


    columnLength = len(columnList) - 1
    cleanRow = df.iloc[0, 0].replace("\"", "").replace("M", "").replace("T", "").replace("E", "").split(',') #clean data of unnecessary characters
    df[columnList[0]].iloc[0] = cleanRow[0] #assign first clean row value to first column title

    columnCount = 0
    while columnCount < columnLength:
        columnCount += 1
        df[columnList[columnCount]] = cleanRow[columnCount]

    rowCount = 1
    columnHeight = len(df) - 1
    while rowCount < columnHeight:
        cleanRow = df.iloc[rowCount, 0].replace("\"", "").replace("M", "").replace("T", "").replace("E", "").split(',')
        columnCount = 0
        while columnCount < columnLength:
            df[columnList[columnCount]].iloc[rowCount] = cleanRow[columnCount]
            columnCount += 1
        rowCount += 1
    return (df)

#clean and organize all datasets
d20 = clean(d20)
d21 = clean(d21)
d22 = clean(d22)
d23 = clean(d23)


#find mean max temp for 4 years and put it in a list
def maxtemp(d20, d21, d22, d23):
    columnStr = list(d20.columns.values)
    rowCount = 0
    columnHeight = len(d20) - 1
    maxTempList = []
    while rowCount < columnHeight:
        maxTemp = 0
        years = 0
        if d20[columnStr[9]].iloc[rowCount] != "":
            maxTemp = float(d20[columnStr[9]].iloc[rowCount])
            years += 1
        else:()
        if d21[columnStr[9]].iloc[rowCount] != "":
            maxTemp += float(d21[columnStr[9]].iloc[rowCount])
            years += 1
        else:()
        if d22[columnStr[9]].iloc[rowCount] != "":
            maxTemp += float(d22[columnStr[9]].iloc[rowCount])
            years += 1
        else:()
        if d23[columnStr[9]].iloc[rowCount] != "":
            maxTemp += float(d23[columnStr[9]].iloc[rowCount])
            years += 1
        else:()
        maxTemp = (maxTemp)/years
        maxTempList.append(maxTemp)
        rowCount += 1
    return (maxTempList)

Maxtotal = maxtemp(d20, d21, d22, d23)

#find mean min temp for 4 years and put it in a list
def mintemp(d20, d21, d22, d23):
    columnStr = list(d20.columns.values)
    rowCount = 0
    columnHeight = len(d20) - 1
    minTempList = []
    while rowCount < columnHeight:
        minTemp = 0
        years = 0
        if d20[columnStr[11]].iloc[rowCount] != "":
            minTemp = float(d20[columnStr[11]].iloc[rowCount])
            years += 1
        else:()
        if d21[columnStr[11]].iloc[rowCount] != "":
            minTemp += float(d21[columnStr[11]].iloc[rowCount])
            years += 1
        else:()
        if d22[columnStr[11]].iloc[rowCount] != "":
            minTemp += float(d22[columnStr[11]].iloc[rowCount])
            years += 1
        else:()
        if d23[columnStr[11]].iloc[rowCount] != "":
            minTemp += float(d23[columnStr[11]].iloc[rowCount])
            years += 1
        else:()
        minTemp = (minTemp)/years
        minTempList.append(minTemp)
        rowCount += 1
    return (minTempList)

Mintotal = mintemp(d20, d21, d22, d23)


#find mean temp for 4 years and put it in a list
MeanList = []
for i in range(0, len(Maxtotal)):
    MeanList.append(Maxtotal[i] + Mintotal[i])


#put mean in a df format 
dmean = pd.DataFrame({'mean':MeanList})
dmean.insert(1, "day", range(1,366), True)

#find where temp is equal or lower to -10
lowtemp = dmean.where(dmean <= -10)


counter = 0
first = 0
count = 0
for i in lowtemp["mean"]:    
    if math.isnan(i):
        counter = 0
    else:
        counter += 1
    count += 1
    if counter == 10:
        first = count
        #save coordinates for the tenth day in a row where it is <=-10

#find day number of the 14th day
second = first + 4




year = input("What year would you like to know the skating season of?")

while year != '2024' and year != '2025' and year != '2026':
    year = input("Please enter a valid year from 2024 to 2026, with no spaces")

#from chat GPT, function to find date associated with a day number of the year
def datenum (year, daynum):
    # Create a datetime object for the given year and day number
    date_object = datetime.datetime(year, 1, 1) + datetime.timedelta(days=daynum - 1)
    
    # Extract the month and day from the datetime object
    month1 = date_object.month
    day1 = date_object.day
    
    return month1, day1


month1, day1 = datenum(int(year), int(first))
month2, day2 = datenum(int(year), int(second))
print('You will most likely be able to start skating between ' + str(day1) + '-' + str(month1) + ' and ' + str(day2) + '-' + str(month2) + ' in ' + str(year) + '!')

graphplot = input('Would you like to see year ' + year + ' in a temperature graph?')

while graphplot != 'yes' and graphplot != 'Yes' and graphplot != 'no' and graphplot != 'No':
    graphplot = input("Please enter 'Yes' or 'No'")
    
if graphplot == 'yes' or graphplot == 'Yes': #make the plot
    fig = px.line(dmean, x='day', y='mean', markers=True)
    fig.add_hline(y = -10)
    fig.add_hline(y = 0)
    fig.show()
else:
    print(">:(")





