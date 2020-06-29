# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)

#Code starts here
categorical_var = bank.select_dtypes(include='object')
#print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
#print(numerical_var)

banks = bank.drop(['Loan_ID'],axis=1)

bank_mode = banks.mode()

banks = banks.replace(np.nan,bank_mode)

print(banks.isnull().sum().values.sum())

avg_loan_amount = pd.pivot_table(banks,index= ['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')

print(avg_loan_amount['LoanAmount'][1])

selfe = banks['Self_Employed'] == 'Yes'
loans = banks['Loan_Status'] == 'Y'
 
loan_approved_se = banks[selfe & loans]

selfe = banks['Self_Employed'] == 'No'
loans = banks['Loan_Status'] == 'Y'
 
loan_approved_nse = banks[selfe & loans]

percentage_se = round( ( len(loan_approved_se) / 614 ) * 100 ,2)
percentage_nse = round( ( len(loan_approved_nse) / 614 ) * 100 ,2)
print(percentage_se,percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
#print(loan_term)
big_loan_term = banks[loan_term>=25]
#print(len(big_loan_term))

loan_groupby = banks.groupby(by='Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()




