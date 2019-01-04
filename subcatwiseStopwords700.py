# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:10:43 2018

@author: Prachi Jain
"""

#Importing libraries
import pandas as pd


#Reading input excel sheet
#df1 = pd.read_excel("C:/Users/IMART/Downloads/Working MCAT_subcat.xlsx",sheet_name="Sheet2")

df2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx",sheet_name="Export Worksheet")

df3 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
#df2 = df2.head(145)

#df1 = df1.head(2141)

#Creating empty, structured final dataframes

mergedf1 = pd.DataFrame(columns=['Subcat_ID','Stopwords'])
#mergedf2 = pd.DataFrame(columns=['MCAT_ID','PMCAT','MCAT_Name','Subcat_ID','Stopword','Attribute'])

uniquesubcats = list(df2['SUBCAT_ID'].unique())
#lowercasing the mcat names and stopwords
df3["HIGH FREQUENCY WORDS"] = df3["HIGH FREQUENCY WORDS"].str.lower()
df2["GLCAT_MCAT_NAME"] = df2["GLCAT_MCAT_NAME"].str.lower()
#df1["GLCAT_MCAT_NAME"] = df1["GLCAT_MCAT_NAME"].str.lower()

highfreqdict =df3.set_index('SUBCAT ID').T.to_dict('list')

a=0
i=0
row=0
while(a<len(df3)):
    
    if(df3.iloc[a]["SUBCAT ID"] in uniquesubcats and a<len(df3)):
        subcatid = df3.iloc[a]["SUBCAT ID"]
        j=i
        concatstring =""
        while(df2.iloc[i]["SUBCAT_ID"] == subcatid and i<=len(df2)-1):
            
            concatstring += df2.iloc[i]["GLCAT_MCAT_NAME"]+" "
            i=i+1
            if(i==len(df2)):
                break
        uniq = set(concatstring.split(' '))
        string1 =""
        for x in uniq:
            if x not in string1:
                string1+=x + " "
        #mergedf1.set_value(row,'MCAT_Name',df2.iloc[j]["GLCAT_MCAT_NAME"])
        mergedf1.set_value(row,'Subcat_ID',df2.iloc[j]["SUBCAT_ID"])
        s= string1 +" "+ str(highfreqdict[df2.iloc[j]["SUBCAT_ID"]][0])
        mergedf1.set_value(row,'Stopwords',s)
        row=row+1
        a=a+1
    elif(df3.iloc[a]["SUBCAT ID"] not in uniquesubcats and a<len(df3)):
        
        #mergedf1.set_value(row,'MCAT_Name',df2.iloc[a]["GLCAT_MCAT_NAME"])
        mergedf1.set_value(row,'Subcat_ID',df3.iloc[a]["SUBCAT ID"])
        
        mergedf1.set_value(row,'Stopwords',df3.iloc[a]["HIGH FREQUENCY WORDS"])
        
        row=row+1
        a=a+1
        


mergedf1.to_csv("700subcatwisefinalstopwords.csv",index=False)