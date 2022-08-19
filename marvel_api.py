#!/usr/bin/env python
# coding: utf-8

# In[3]:


#ACTIVITY_5
import argparse
from asyncio.windows_events import NULL
parser = argparse.ArgumentParser(description='Activity')
parser.add_argument("-apikey", "--api_key", help="adds api_key", default= NULL)
parser.add_argument("-hash", "--hash", help="adds hash", default= NULL)
args, unknown = parser.parse_known_args()   #add CLI arguements while executing in CLI

print("API KEY",args.api_key)
print("HASH",args.hash)
api_key = args.api_key
hash = args.hash 
# api_key="97b5663a002e278716486c5066199100"
# hash="a6e47f7f74987d6bfcb7e67c85e8e85e"
#we got hashkey by keeping timestamp(2)_privatekey_publickey


# In[4]:


#ACTIVITY_2
# !sudo pip3 install requests
# from IPython import get_ipython
from pprint import pprint as pp
import requests     #use request lib to call REST api
import json 
import pandas as pd

url_ad="http://gateway.marvel.com/v1/public/characters"   #url
  
df_final = pd.DataFrame()
flag = 0
for offs in range(0,1700,100):
    parameters={"apikey":api_key,"hash":hash,"ts":"2","limit":"100","offset":offs} #define all the parameters and keys
    response=requests.get(url=url_ad,params=parameters) #we are using url alongwith api key(public) as well as hash key and also by inducing the parameters nameStartswith and limit
    res=response.json()
    # pp(response.json()) 
    df = pd.DataFrame.from_dict(res['data']['results'], orient='columns')  #converting into dataframe and then extracting it from the nested dictionary results
    # print(df.shape)
    if flag == 0:
        df_final = df
        flag = 1
    else:
        df_final = pd.concat([df_final,df],join = 'outer')

# df_final.info()
print("-----ACTIVITY: 2-----")
print("Total_df_shape",df_final.shape) 
print("Result:",df_final)   


# In[5]:


#ACTIVITY_3
#Function for making the api call 
def ch_gen(nameStartsWith,  hash=NULL, API_key= NULL):   #giving default value as null helps us in giving a clearer error message to the user
    if (API_key == NULL or hash == NULL):
        raise Exception("API_key or hash cannot be NULL") 

    url_ad="http://gateway.marvel.com/v1/public/characters"   #url
  
    df_final = pd.DataFrame()
    flag = 0
    for offs in range(0,1700,100):
        parameters={"apikey":api_key,"hash":hash,"ts":"2","limit":"100","offset":offs} #define all the parameters and keys
        response=requests.get(url=url_ad,params=parameters) #we are using url alongwith api key(public) as well as hash key and also by inducing the parameters nameStartswith and limit
        res=response.json()
        # pp(response.json()) 
        df = pd.DataFrame.from_dict(res['data']['results'], orient='columns')  #converting into dataframe and then extracting it from the nested dictionary results
        # print(df.shape)
        if flag == 0:
            df_final = df
            flag = 1
        else:
            df_final = pd.concat([df_final,df],join = 'outer')

    return df_final


result=ch_gen('B', hash=hash,API_key=api_key)    #Function call
print("-----ACTIVITY: 3-----")
print("RESULT:",result)   #WE are giving values for api and hash and storing the fucnction as result   


# In[6]:


#ACTIVITY_4
def ch_filter(df1,col,filter_condition):
    return df1.query(col+filter_condition)   #optimal method for the above code.

# def ch_filter1(df1,col,filter_condition):
#     total_condition = col+filter_condition;
#     res = (df1.query(total_condition));  #code to define and convert to df for a filter conditionbased on selected column and the condition on that column
#     return res 

result2= ch_filter(df1=result, col='name',filter_condition='.str.startswith("A")')
print("-----ACTIVITY: 4-----")
print("Result: Characters Starting with 'A'",result2)


# In[ ]:




