import pandas as pd
import datetime
from pandasql import sqldf
x = datetime.datetime.now()

df=pd.read_csv("C:\\Users\\varun\\Downloads\\MW-NIFTY-100-"+str(x.strftime("%d"))+"-"+str(x.strftime("%b"))+"-"+str(x.strftime("%Y")+".csv"))
df.columns=df.columns.str.replace(' \\n','')
df['OPEN'] = df['OPEN'].str.replace(',', '')
df['HIGH'] = df['HIGH'].str.replace(',', '')
df['LOW'] = df['LOW'].str.replace(',', '')
output = sqldf("select * from df where OPEN=(SELECT CAST(OPEN AS INT)) AND (OPEN=HIGH or OPEN=LOW);")
print(output)

