# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,new_record),axis=0)

age = np.array(census[:,0])

max_age = np.max(age)
min_age = np.min(age)
age_mean= np.mean(age)
age_std= np.std(age,axis=None)

race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]

for row in census:
    if row[2] == 0.0:
        race_0.append(row)
    elif row[2] == 1.0:
        race_1.append(row)
    elif row[2] == 2.0:
        race_2.append(row)
    elif row[2] == 3.0:
        race_3.append(row)
    elif row[2] == 4.0:
        race_4.append(row)

race_0 = np.array(race_0)
race_1 = np.array(race_1)
race_2 = np.array(race_2)
race_3 = np.array(race_3)
race_4 = np.array(race_4)
#print(race_0)
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
#print(len_0,len_1,len_2,len_3,len_4)
temp=np.array([len_0,len_1,len_2,len_3,len_4])
minimum = temp.min()
minority_race = np.where(temp == minimum)
#print(minority_race[0][0])
filterarr= census[:,0]>60
senior_citizens = census[filterarr]

working_hours_sums=0

for row in senior_citizens:
    working_hours_sums += row[6]

senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sums / senior_citizens_len

print(round(avg_working_hours,2))

greater = census[:,1] > 10
lower = census[:,1] <= 10

high = census[greater]
low = census[lower]

avg_pay_high = round(np.mean(high[:,7]),2)
avg_pay_low = round(np.mean(low[:,7]),2)

print(avg_pay_high,avg_pay_low)


