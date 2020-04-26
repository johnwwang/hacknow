#Note: The data presented in this model was merged from many different sources includding Kaggle, JohnsHopkins 
# and the NOAA. All data mininng and extrapolation was performed by me. Neural network construct was sourced from 
# a paper online and was applyed to this data to yield predictions.


#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_cell_magic('bash', '', 'git clone https://github.com/CoronaWhy/task-geo')


# In[351]:


import math
import pandas as pd
import numpy as np
import datetime as dt
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_squared_log_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression,LinearRegression,BayesianRidge, Lasso
from statistics import mean
from math import sqrt
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM, Bidirectional
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import Input, layers
from tensorflow.keras import optimizers
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

import datetime
import warnings
from tqdm import tqdm
from pathlib import Path
import time
from copy import deepcopy
import os


# In[352]:


traindata = pd.read_csv("train_data.csv")
traindata.info()


# In[353]:


testdata = pd.read_csv("test (2).csv")
testdata.head()


# In[354]:


enricheddata = pd.read_csv("enriched_covid_19_week_2.csv")
enricheddata.head()


# In[264]:


traindata["ConfirmedCases"] = traindata["ConfirmedCases"].astype("float")
traindata["Fatalities"] = traindata["Fatalities"].astype("float")


# In[265]:


for region in traindata["Country_Region"]:
    print(region)


# In[266]:


weathertrain = pd.read_csv("training_data_with_weather_info_week_4.csv")
weathertrain.head()
for region in traindata["Country_Region"]:
    print(region) 


# In[267]:


enricheddata["Country_Region"] = [country_name.replace("'","") for country_name in enricheddata["Country_Region"]]
enricheddata["restrictions"] = enricheddata["restrictions"].astype("int")
enricheddata["quarantine"] = enricheddata["quarantine"].astype("int")
enricheddata["schools"] = enricheddata["schools"].astype("int")
enricheddata["total_pop"] = enricheddata["total_pop"].astype("float")
enricheddata["density"] = enricheddata["density"].astype("float")
enricheddata["hospibed"] = enricheddata["hospibed"].astype("float")
enricheddata["lung"] = enricheddata["lung"].astype("float")
enricheddata["total_pop"] = enricheddata["total_pop"]/max(enricheddata["total_pop"])
enricheddata["density"] = enricheddata["density"]/max(enricheddata["density"])
enricheddata["hospibed"] = enricheddata["hospibed"]/max(enricheddata["hospibed"])
enricheddata["lung"] = enricheddata["lung"]/max(enricheddata["lung"])


# In[268]:


enricheddata["age_100+"] = enricheddata["age_100+"].astype("float")
enricheddata["age_100+"] = enricheddata["age_100+"]/max(enricheddata["age_100+"])


# In[269]:


weathertrain["Country_Region"] = [country_name.replace("'","") for country_name in weathertrain["Country_Region"]]


# In[270]:


weatherdata = weathertrain[['Country_Region', 'Date', 'Lat', 'Long', 'temp', 'wdsp', 'prcp']]
weatherdata.info()


# In[271]:


newenriched = enricheddata.drop(["Id", "Province_State", "ConfirmedCases", "Fatalities"], axis = 1)


# In[272]:


traindata.info()


# In[273]:


train_df = traindata.merge(newenriched, how="left", on=['Country_Region','Date']).drop_duplicates()
train_df.head()


# In[274]:


train_df.info()

train_df = train_df.drop(["geometry"], axis = 1, inplace = True)
# In[277]:


train_df = train_df.drop(["geometry"], axis = 1)


# In[287]:


columns = train_df.columns
modcolumns = columns.drop(["Id", "Province_State", "Date", "Country_Region", "ConfirmedCases", "Fatalities"])
finalcolumns = modcolumns.tolist()
finalcolumns


# In[291]:


for country_region in train_df.Country_Region.unique():
    query_df = train_df.query("Country_Region=='"+country_region+"' and Date=='2020-03-25'")
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"total_pop"] = query_df.total_pop.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"hospibed"] = query_df.hospibed.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"density"] = query_df.density.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"lung"] = query_df.lung.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_100+"] = query_df["age_100+"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"restrictions"] = query_df.restrictions.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"quarantine"] = query_df.quarantine.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"schools"] = query_df.schools.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"smokers_perc"] = query_df.smokers_perc.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"femalelung"] = query_df.femalelung.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"malelung"] = query_df.malelung.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"urbanpop"] = query_df.urbanpop.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_95-99"] = query_df["age_95-99"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_90-94"] = query_df["age_90-94"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_85-89"] = query_df["age_85-89"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_80-84"] = query_df["age_80-84"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_95-99"] = query_df["age_95-99"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_90-94"] = query_df["age_90-94"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_85-89"] = query_df["age_85-89"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_80-84"] = query_df["age_80-84"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_75-79"] = query_df["age_75-79"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_70-74"] = query_df["age_70-74"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_65-69"] = query_df["age_65-69"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_60-64"] = query_df["age_60-64"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_55-59"] = query_df["age_55-59"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_50-54"] = query_df["age_50-54"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_45-49"] = query_df["age_45-49"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_40-44"] = query_df["age_40-44"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_35-39"] = query_df["age_35-39"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_30-34"] = query_df["age_30-34"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_25-29"] = query_df["age_25-29"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_20-24"] = query_df["age_20-24"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_15-19"] = query_df["age_15-19"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_10-14"] = query_df["age_10-14"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_5-9"] = query_df["age_5-9"].values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"age_0-4"] = query_df["age_0-4"].values[0]
    


# In[292]:


train_df.info()


# In[294]:


median_pop = np.median(newenriched.total_pop)
median_hospibed = np.median(newenriched.hospibed)
median_density = np.median(newenriched.density)
median_malelung = np.median(newenriched.malelung)
median_femalelung = np.median(newenriched.femalelung)
median_urbanpop = np.median(newenriched.urbanpop)
median_smokers_perc = np.median(newenriched.smokers_perc)
median_lung = np.median(newenriched.lung)
median_centenarian_pop = np.median(newenriched["age_100+"])

pop95 = np.median(newenriched["age_95-99"])
pop90 = np.median(newenriched["age_90-94"])
pop85 = np.median(newenriched["age_85-89"])
pop80 = np.median(newenriched["age_80-84"])
pop75 = np.median(newenriched["age_75-79"])
pop70 = np.median(newenriched["age_70-74"])
pop65 = np.median(newenriched["age_65-69"])
pop60 = np.median(newenriched["age_60-64"])
pop55 = np.median(newenriched["age_55-59"])
pop50 = np.median(newenriched["age_50-54"])
pop45 = np.median(newenriched["age_45-49"])
pop40 = np.median(newenriched["age_40-44"])
pop35 = np.median(newenriched["age_35-39"])
pop30 = np.median(newenriched["age_30-34"])
pop25 = np.median(newenriched["age_25-29"])
pop20 = np.median(newenriched["age_20-24"])
pop15 = np.median(newenriched["age_15-19"])
pop10 = np.median(newenriched["age_10-14"])
pop5 = np.median(newenriched["age_5-9"])
pop0 = np.median(newenriched["age_0-4"])

print("The missing countries/region are:")
for country_region in train_df.Country_Region.unique():
    if newenriched.query("Country_Region=='"+country_region+"'").empty:
        print(country_region)
        
        train_df.loc[train_df["Country_Region"]==country_region,"total_pop"] = median_pop
        train_df.loc[train_df["Country_Region"]==country_region,"hospibed"] = median_hospibed
        train_df.loc[train_df["Country_Region"]==country_region,"density"] = median_density
        train_df.loc[train_df["Country_Region"]==country_region,"lung"] = median_lung
        train_df.loc[train_df["Country_Region"]==country_region,"femalelung"] = median_femalelung
        train_df.loc[train_df["Country_Region"]==country_region,"malelung"] = median_malelung
        train_df.loc[train_df["Country_Region"]==country_region,"smokers_perc"] = median_smokers_perc
        train_df.loc[train_df["Country_Region"]==country_region,"urbanpop"] = median_urbanpop
        train_df.loc[train_df["Country_Region"]==country_region,"age_100+"] = median_centenarian_pop
        train_df.loc[train_df["Country_Region"]==country_region,"age_95-99"] = pop95
        train_df.loc[train_df["Country_Region"]==country_region,"age_90-94"] = pop90
        train_df.loc[train_df["Country_Region"]==country_region,"age_85-89"] = pop85
        train_df.loc[train_df["Country_Region"]==country_region,"age_80-84"] = pop80
        train_df.loc[train_df["Country_Region"]==country_region,"age_75-79"] = pop75
        train_df.loc[train_df["Country_Region"]==country_region,"age_70-74"] = pop70
        train_df.loc[train_df["Country_Region"]==country_region,"age_65-69"] = pop65
        train_df.loc[train_df["Country_Region"]==country_region,"age_60-64"] = pop60
        train_df.loc[train_df["Country_Region"]==country_region,"age_55-59"] = pop55
        train_df.loc[train_df["Country_Region"]==country_region,"age_50-54"] = pop50
        train_df.loc[train_df["Country_Region"]==country_region,"age_45-49"] = pop45
        train_df.loc[train_df["Country_Region"]==country_region,"age_40-44"] = pop40
        train_df.loc[train_df["Country_Region"]==country_region,"age_35-39"] = pop35
        train_df.loc[train_df["Country_Region"]==country_region,"age_30-34"] = pop30
        train_df.loc[train_df["Country_Region"]==country_region,"age_25-29"] = pop25
        train_df.loc[train_df["Country_Region"]==country_region,"age_20-24"] = pop20
        train_df.loc[train_df["Country_Region"]==country_region,"age_15-19"] = pop15
        train_df.loc[train_df["Country_Region"]==country_region,"age_10-14"] = pop10
        train_df.loc[train_df["Country_Region"]==country_region,"age_5-9"] = pop5
        train_df.loc[train_df["Country_Region"]==country_region,"age_0-4"] = pop0
        train_df.loc[train_df["Country_Region"]==country_region,"restrictions"] = 0
        train_df.loc[train_df["Country_Region"]==country_region,"quarantine"] = 0
        train_df.loc[train_df["Country_Region"]==country_region,"schools"] = 0
        
        


# In[295]:


train_df.info()


# In[296]:


weatherdata.info()


# In[297]:


train_df = train_df.merge(weatherdata, how="left", on=['Country_Region','Date']).drop_duplicates()
train_df.head()


# In[298]:


train_df.info()


# In[299]:


train_df.isnull().sum()


# In[300]:


for country_region in train_df.Country_Region.unique():
    query_df = train_df.query("Country_Region=='"+country_region+"' and Date=='2020-03-25'")
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"Lat"] = query_df.Lat.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"Long"] = query_df.Long.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"temp"] = query_df.temp.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"wdsp"] = query_df.wdsp.values[0]
    train_df.loc[(train_df["Country_Region"]==country_region) & (train_df["Date"]>"2020-03-25"),"prcp"] = query_df.prcp.values[0]
  


# In[302]:


train_df.tail()


# In[304]:


median_Lat = np.median(weatherdata.Lat)
median_Long = np.median(weatherdata.Long)
median_prcp = np.median(weatherdata.prcp)
median_wdsp = np.median(weatherdata.wdsp)
median_temp = np.median(weatherdata.temp)


print("The missing countries/region are:")
for country_region in train_df.Country_Region.unique():
    if weatherdata.query("Country_Region=='"+country_region+"'").empty:
        print(country_region)

        train_df.loc[train_df["Country_Region"]==country_region,"Lat"] = median_Lat
        train_df.loc[train_df["Country_Region"]==country_region,"Long"] = median_Long
        train_df.loc[train_df["Country_Region"]==country_region,"prcp"] = median_prcp
        train_df.loc[train_df["Country_Region"]==country_region,"wdsp"] = median_wdsp
        train_df.loc[train_df["Country_Region"]==country_region,"temp"] = median_temp
  
        
        


# In[305]:


train_df.info()


# In[322]:


del train_df["Province_State"]


# In[437]:


train_df.info()


# In[ ]:





# In[ ]:





# In[356]:


Xtrain, Xtest = train_test_split(train_df, test_size=0.10, random_state=42)


# In[359]:


Xtest.info()


# In[360]:


ytrain = Xtrain[['ConfirmedCases', 'Fatalities']]
ytest = Xtest[['ConfirmedCases', 'Fatalities']]


# In[361]:


ytrain


# In[362]:


del Xtrain['ConfirmedCases']
del Xtest['ConfirmedCases']
del Xtrain['Fatalities']
del Xtest['Fatalities']


# In[363]:


from sklearn.preprocessing import LabelEncoder
pd.options.mode.chained_assignment = None 

lb = LabelEncoder()
Xtrain['Country_Region'] = lb.fit_transform(Xtrain['Country_Region'])
Xtest['Country_Region'] = lb.transform(Xtest['Country_Region'])


# In[364]:


Xtrain.isnull().sum()


# In[365]:


import seaborn as sns

plt.figure(figsize = (10,10))
corr = Xtrain.corr()
sns.heatmap(corr , mask=np.zeros_like(corr, dtype=np.bool) , 
            cmap=sns.diverging_palette(-100,0,as_cmap=True) , square = True)


# In[ ]:





# In[ ]:





# In[366]:


def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


# In[367]:


Xtrain['Date'] = Xtrain['Date']


# In[370]:


scaler = StandardScaler()

xtrain = scaler.fit_transform(Xtrain.values)
xtest = scaler.transform(Xtest.values)


# In[376]:


from datetime import datetime as dt

traindateseries = pd.Series(Xtrain['Date'].apply(lambda x: dt.fromordinal(x)).dt.strftime('%Y-%m-%d'))
testdateseries = pd.Series(Xtrain['Date'].apply(lambda x: dt.fromordinal(x)).dt.strftime('%Y-%m-%d'))
traindateseries


# In[ ]:





# In[ ]:





# In[ ]:





# In[377]:


Xtest.info()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[143]:





# In[ ]:





# In[378]:


from xgboost import XGBRegressor
import numpy as np
import pandas as pd
import os
import tensorflow as tf
from tqdm import tqdm
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_log_error

from datetime import datetime
from datetime import timedelta

from tensorflow.keras import layers
from tensorflow.keras import Input
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[383]:


from sklearn.model_selection import GridSearchCV

params = {'learning_rate': [0.05, .07],
          'max_depth': [10, 25, 40],
          'min_samples_split': [5, 10],
          'n_estimators': [1750, 2500]}

grid_search_cv = GridSearchCV(XGBRegressor(random_state=42), params, n_jobs = 1, verbose=1, cv=3)

cases_train = ytrain["ConfirmedCases"]


# In[384]:


params = {'learning_rate': [0.05, .07], #so called `eta` value
          'max_depth': [10, 25, 40],
          'min_samples_split': [5, 10],
          'n_estimators': [1750, 2500]}

fatal_grid_search_cv = GridSearchCV(XGBRegressor(random_state=42), params, n_jobs = 1, verbose=1, cv=3)

fatalities_train = ytrain["Fatalities"]


# In[385]:


traindateseries


# In[392]:


jointXtrain = Xtrain.merge(ytrain, left_index=True, right_index=True)
jointXtest = Xtest.merge(ytest, left_index=True, right_index=True)
jointXtest


# In[411]:


features=jointXtrain.select_dtypes(include='number').columns.values[1:]
features


# In[429]:


def process_seq(df,features):
    # define identifier
    idf=(df[['ConfirmedCases', 'Fatalities']],df.index.values)
    # define target 
    tar=df[['ConfirmedCases', 'Fatalities']].values[-1]
    # define sequence 
    seq=df[features].values[:-1,:]
    return idf,seq,tar


# In[430]:


def process_sequnces(train,n=20):
    days_list=train.index.unique()
    identifiers,sequences,targets=[],[],[]
    #
    for i in tqdm(range(days_list.shape[0]-n)):
        dfx=train[(train.index>=days_list[i]) & (train.index<days_list[i+n])].copy()
        #
        #df_sub[features]=preprocessing.MinMaxScaler().fit_transform(df_sub[features])
        out=dfx.groupby(['Country_Region', 'Date']).apply(process_seq,features=features).values
        # add out to 
        for idf,seq,tar in out:
            identifiers.append(idf)
            sequences.append(seq)
            targets.append(tar)
            
    return np.array(identifiers),np.array(sequences),np.array(targets).reshape(-1,2)


# In[431]:


identifiers,sequences,targets=process_sequnces(jointXtrain)
print(' identifiers: {} \n sequences: {} \n targets: {}'.format(identifiers.shape,sequences.shape,targets.shape))


# In[432]:


training_item_count = int(len(jointXtrain))


# In[433]:


trend_df = pd.DataFrame(columns={"infection_trend","fatality_trend",
                                 "quarantine_trend","school_trend","total_population",
                                 "expected_cases","expected_fatalities"})


# In[434]:


jointXtrain.tail()


# In[438]:


train_df.info()


# In[441]:


dateskismax = train_df["Date"].min()
dateskismax


# In[545]:


train_df = train_df.query("Date>'2020-01-24'and Date<'2020-03-31'")

trend_list = []
days_in_sequence = 18


for country in train_df.Country_Region.unique():
        country_df = train_df.query(f"Country_Region=='{country}'")
        for i in range(0,len(country_df),int(days_in_sequence/3)):
            if i+days_in_sequence<=len(country_df):
        
                infection_trend = [float(x) for x in country_df[i:i+days_in_sequence-1].ConfirmedCases.values]
                fatality_trend = [float(x) for x in country_df[i:i+days_in_sequence-1].Fatalities.values]
                restriction_trend = [float(x) for x in country_df[i:i+days_in_sequence-1].restrictions.values]
                quarantine_trend = [float(x) for x in country_df[i:i+days_in_sequence-1].quarantine.values]
                school_trend = [float(x) for x in country_df[i:i+days_in_sequence-1].schools.values]
                temp_trend = [float(x) for x in country_df[i:i+days_in_sequence-1].temp.values]
                prcp_trend = [float(x) for x in country_df[i:i+days_in_sequence-1].prcp.values]

            
                total_population = float(country_df.iloc[i].total_pop)
                density = float(country_df.iloc[i].density)
                hospibed = float(country_df.iloc[i].hospibed)
                lung = float(country_df.iloc[i].lung)
                centenarian_pop = float(country_df.iloc[i]["age_100+"])
                pop95 = float(country_df.iloc[i]["age_95-99"])
                pop90 = float(country_df.iloc[i]["age_90-94"])
                pop85 = float(country_df.iloc[i]["age_85-89"])
                pop65 = float(country_df.iloc[i]["age_65-69"])
                pop45 = float(country_df.iloc[i]["age_45-49"])
                pop35 = float(country_df.iloc[i]["age_35-39"])
                pop25 = float(country_df.iloc[i]["age_25-29"])
                pop15 = float(country_df.iloc[i]["age_15-19"])
            
                lat = float(country_df.iloc[i].Lat)
                long = float(country_df.iloc[i].Long)
                malelung = float(country_df.iloc[i].malelung)
                femalelung = float(country_df.iloc[i].femalelung)
                urbanpop = float(country_df.iloc[i].urbanpop)
                smokersperc = float(country_df.iloc[i].smokers_perc)
                

                expected_cases = float(country_df.iloc[i+days_in_sequence-1].ConfirmedCases)
                expected_fatalities = float(country_df.iloc[i+days_in_sequence-1].Fatalities)

                trend_list.append({"infection_trend":infection_trend,
                                 "fatality_trend":fatality_trend,
                                 "restriction_trend":restriction_trend,
                                 "quarantine_trend":quarantine_trend,
                                 "school_trend":school_trend,
                                 "temperature_trend": temp_trend,
                                 "prcp_tend": prcp_trend,
                                 "demographic_inputs":[total_population,density,hospibed,malelung, femalelung
                                                       ,centenarian_pop, pop95, smokersperc, urbanpop,
                                                       pop90, pop85, pop65, pop45, pop35, pop25, pop15, lat, long],
                                 "expected_cases":expected_cases,
                                 "expected_fatalities":expected_fatalities})
                print("Done")
    
        
trend_df = pd.DataFrame(trend_list)


# In[ ]:





# In[546]:


trend_df


# In[547]:


trend_df["temporal_inputs"] = [np.asarray([trends["infection_trend"],trends["fatality_trend"],
                                           trends["restriction_trend"],trends["quarantine_trend"],
                                           trends["school_trend"], trends["prcp_tend"], trends["temperature_trend"]] )
                               for idx,trends in trend_df.iterrows()]

trend_df = shuffle(trend_df)


# In[548]:


trend_df


# In[549]:


i=0
temp_df = pd.DataFrame()
for idx,row in trend_df.iterrows():
    if sum(row.infection_trend)>0:
        temp_df = temp_df.append(row)
    else:
        if i<16:
            temp_df = temp_df.append(row)
            i+=1
trend_df = temp_df


# In[ ]:





# In[550]:


trend_df.head()


# In[551]:


sequence_length = 17
training_percentage = .85

training_item_count = int(len(trend_df)*training_percentage)
validation_item_count = len(trend_df)-int(len(trend_df)*training_percentage)
training_df = trend_df[:training_item_count]
validation_df = trend_df[training_item_count:]


# In[552]:


X_temporal_train = np.asarray(np.transpose(np.reshape(np.asarray([np.asarray(x) for x in training_df["temporal_inputs"].values]),
                                                      (training_item_count,7,sequence_length)), (0,2,1) )).astype(np.float32)
X_demographic_train = np.asarray([np.asarray(x) for x in training_df["demographic_inputs"]]).astype(np.float32)
Y_cases_train = np.asarray([np.asarray(x) for x in training_df["expected_cases"]]).astype(np.float32)
Y_fatalities_train = np.asarray([np.asarray(x) for x in training_df["expected_fatalities"]]).astype(np.float32)


# In[553]:


X_temporal_test = np.asarray(np.transpose(np.reshape(np.asarray([np.asarray(x) for x in validation_df["temporal_inputs"]]),(validation_item_count,7,sequence_length)),(0,2,1)) ).astype(np.float32)
X_demographic_test = np.asarray([np.asarray(x) for x in validation_df["demographic_inputs"]]).astype(np.float32)
Y_cases_test = np.asarray([np.asarray(x) for x in validation_df["expected_cases"]]).astype(np.float32)
Y_fatalities_test = np.asarray([np.asarray(x) for x in validation_df["expected_fatalities"]]).astype(np.float32)


# In[ ]:





# In[507]:





# In[ ]:





# In[555]:


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss over epochs')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='best')
plt.show()


# In[556]:


#temporal input branch
temporal_input_layer = Input(shape=(sequence_length,7))
main_rnn_layer = layers.LSTM(64, return_sequences=True, recurrent_dropout=0.15)(temporal_input_layer)

#demographic input branch
demographic_input_layer = Input(shape=(18))
demographic_dense = layers.Dense(16)(demographic_input_layer)
demographic_dropout = layers.Dropout(0.15)(demographic_dense)


rnn_c = layers.LSTM(32)(main_rnn_layer)
merge_c = layers.Concatenate(axis=-1)([rnn_c,demographic_dropout])
dense_c = layers.Dense(128)(merge_c)
dropout_c = layers.Dropout(0.3)(dense_c)
precases = layers.Dense(1, activation=layers.LeakyReLU(alpha=0.25),name="precases")(dropout_c)


rnn_f = layers.LSTM(32)(main_rnn_layer)
merge_f = layers.Concatenate(axis=-1)([rnn_f,demographic_dropout])
dense_f = layers.Dense(128)(merge_f)
dropout_f = layers.Dropout(0.3)(dense_f)
prefatalities = layers.Dense(1, activation=layers.LeakyReLU(alpha=0.25), name="prefatalities")(dropout_f)





model = Model([temporal_input_layer,demographic_input_layer], [precases,prefatalities])

model.summary()


# In[557]:


from tensorflow import keras

root_logdir = os.path.join(os.curdir, "my_logs")
def get_run_logdir():
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

run_logdir = get_run_logdir()
tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)

callbacks = [tensorboard_cb, ReduceLROnPlateau(monitor='val_loss', patience=4, verbose=1, factor=0.6),
             EarlyStopping(monitor='val_loss', patience=20),
             ModelCheckpoint(filepath='COVIDnew8_model.h5', monitor='val_loss', save_best_only=True)]

model.compile(loss=[tf.keras.losses.MeanSquaredLogarithmicError(),tf.keras.losses.MeanSquaredLogarithmicError()], 
              optimizer="adam")


# In[558]:


history = model.fit([X_temporal_train,X_demographic_train], [Y_cases_train, Y_fatalities_train], 
          epochs = 300, 
          batch_size = 8, 
          validation_data=([X_temporal_test,X_demographic_test],  [Y_cases_test, Y_fatalities_test]), 
          callbacks=callbacks)


# In[559]:


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss over epochs')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='best')
plt.show()


# In[560]:


model.load_weights("COVIDnew8_model.h5")
train_df.info()


# In[ ]:





# In[564]:


train_df.info()


# In[671]:


copy_df = train_df.drop(["age_0-4", "age_5-9", "age_10-14", "age_20-24", "age_30-34", 
                        "age_40-44", "age_50-54", "age_55-59", "age_60-64", "age_70-74", 
                        "age_80-84", "age_5-9", "age_10-14", "age_20-24", "age_30-34", "lung", 
                        "wdsp"], axis = 1)
copy_df.info()


# In[672]:


begin_prediction = "2020-03-31"
start_date = datetime.strptime(begin_prediction,"%Y-%m-%d")
dateseries = copy_df["Date"]
print(dateseries.iloc[0])

if (dateseries.iloc[0] > start_date):
    print (True)
else:
    print (False)


# In[673]:


begin_prediction = "2020-02-28"
start_date = datetime.strptime(begin_prediction,"%Y-%m-%d")

countries = copy_df["Country_Region"]
country = countries.iloc[5000]

make_forecast(country, start_date, copy_df)




# In[744]:


begin_prediction = "2020-03-10"
start_date = datetime.strptime(begin_prediction,"%Y-%m-%d")
end_prediction = "2020-05-26"
end_date = datetime.strptime(end_prediction,"%Y-%m-%d")

date_list = [start_date + timedelta(days=x) for x in range((end_date-start_date).days+1)]
for date in date_list:
    print(date)


# In[ ]:





# 

# In[749]:


copy_df.info()


# In[750]:


def make_forecast(country, date, df):
    start_date = date - timedelta(days=17)
    end_date = date - timedelta(days=1)
    
    sequence_length = 17
    str_start_date = start_date.strftime("%Y-%m-%d")
    str_end_date = end_date.strftime("%Y-%m-%d")
    
    #mask = (df['Date'] > start_date) & (df['Date'] > end_date) & (df['Country_Region'] == country)
    #df = df.loc[mask]

    #df = df.query("Country_Region=='"+country+"' and Date>='"+str_start_date+"' and Date<='"+str_end_date+"'")
    
    newdf = df.query(f"Country_Region=='{country}' and Date>='{str_start_date}' and Date<='{str_end_date}'")    
    
    return newdf


# In[753]:


def inputs(newdf):
   
   temporal_input_data = np.transpose(np.reshape(np.asarray([newdf["ConfirmedCases"],
                                                newdf["Fatalities"],
                                                newdf["restrictions"],
                                                newdf["quarantine"],
                                                newdf["schools"], 
                                                newdf["temp"], 
                                                newdf["prcp"]]),
                                    (7,sequence_length)), (1,0) ).astype(np.float32)
   
   #preparing all the demographic inputs
   total_population = float(country_df.iloc[i].total_pop)
   density = float(country_df.iloc[i].density)
   hospibed = float(country_df.iloc[i].hospibed)
   pop100 = float(country_df.iloc[i]["age_100+"])
   pop95 = float(country_df.iloc[i]["age_95-99"])
   pop90 = float(country_df.iloc[i]["age_90-94"])
   pop85 = float(country_df.iloc[i]["age_85-89"])
   pop65 = float(country_df.iloc[i]["age_65-69"])
   pop45 = float(country_df.iloc[i]["age_45-49"])
   pop35 = float(country_df.iloc[i]["age_35-39"])
   pop25 = float(country_df.iloc[i]["age_25-29"])
   pop15 = float(country_df.iloc[i]["age_15-19"])
   lat = float(country_df.iloc[i].Lat)
   long = float(country_df.iloc[i].Long)
   malelung = float(country_df.iloc[i].malelung)
   femalelung = float(country_df.iloc[i].femalelung)
   urbanpop = float(country_df.iloc[i].urbanpop)
   smokersperc = float(country_df.iloc[i].smokers_perc)
   demographic_input_data = [total_population,density,hospibed,malelung, femalelung
                                          ,pop100, pop95, smokersperc, urbanpop,
                                          pop90, pop85, pop65, pop45, pop35, pop25, pop15, lat, long]
   
   return [np.array([temporal_input_data]), np.array([demographic_input_data]) ]


# In[754]:


def predict_for_region(country, df):
    begin_prediction = "2020-03-31"
    start_date = datetime.strptime(begin_prediction,"%Y-%m-%d")
    end_prediction = "2020-05-26"
    end_date = datetime.strptime(end_prediction,"%Y-%m-%d")
    
    date_list = [start_date + timedelta(days=x) for x in range((end_date-start_date).days+1)]
    for date in date_list:
        input_data = make_forecast(country, date, df)


# In[755]:


for country in copy_df.Country_Region.unique():
    temp, demo = predict_for_region(country, copy_df)
    print("done")


# In[723]:


def predict_for_region(country, df):
    begin_prediction = "2020-03-31"
    start_date = datetime.strptime(begin_prediction,"%Y-%m-%d")
    end_prediction = "2020-05-26"
    end_date = datetime.strptime(end_prediction,"%Y-%m-%d")
    
    date_list = [start_date + timedelta(days=x) for x in range((end_date-start_date).days+1)]
    for date in date_list:
        input_data = make_forecast(country, date, df)
        result = model.predict(input_data)
        
        #just ensuring that the outputs is
        #higher than the previous counts
        result[0] = np.round(result[0])
        if result[0]<input_data[0][0][-1][0]:
            result[0]=np.array([[input_data[0][0][-1][0]]])
        
        result[1] = np.round(result[1])
        if result[1]<input_data[0][0][-1][1]:
            result[1]=np.array([[input_data[0][0][-1][1]]])
        
        #We assign the quarantine and school status
        #depending on previous values
        #e.g Once a country is locked, it will stay locked until the end
        df = df.append({"Country_Region":country, 
                        "Date":date.strftime("%Y-%m-%d"), 
                        "restrictions": 1 if any(input_data[0][0][2]) else 0,
                        "quarantine": 1 if any(input_data[0][0][3]) else 0,
                        "schools": 1 if any(input_data[0][0][4]) else 0,
                        "temp": input_data[0][0][5],
                        "prcp": input_data[0][0][6],
                        "total_pop": input_data[1][0],
                        "density": input_data[1][0][1],
                        "hospibed": input_data[1][0][2],
                        "age_100+": input_data[1][0][3],
                        "age_95-99": input_data[1][0][4],
                        "age_90-94": input_data[1][0][5],
                        "age_85-89": input_data[1][0][6],
                        "age_65-69": input_data[1][0][7],
                        "age_45-49": input_data[1][0][8],
                        "age_35-39": input_data[1][0][9],
                        "age_25-29": input_data[1][0][10],
                        "age_15-19": input_data[1][0][11],
                        "Lat": input_data[1][0][12],
                        "Long": input_data[1][0][13],
                        "malelung": input_data[1][0][14],
                        "femalelung": input_data[1][0][15],
                        "urbanpop": input_data[1][0][16],
                        "smokers_perc": input_data[1][0][17],
                        "ConfirmedCases":round(result[0][0][0]),	
                        "Fatalities":round(result[1][0][0])},
                       ignore_index=True)
    return df


# In[ ]:


for country in copy_df.Country_Region.unique():
    copy_df = predict_for_region(country, copy_df)


# In[ ]:


prediction = copy_df.query("Date=='2020-04-27'")
pred427 = prediction[['Country_Region', 'Date', 'ConfirmedCases', 'Fatalities']]
prediction = copy_df.query("Date=='2020-05-07'")
pred507 = prediction[['Country_Region', 'Date', 'ConfirmedCases', 'Fatalities']]
prediction = copy_df.query("Date=='2020-05-17'")
pred517 = prediction[['Country_Region', 'Date', 'ConfirmedCases', 'Fatalities']]
prediction = copy_df.query("Date=='2020-05-26'")
pred526 = prediction[['Country_Region', 'Date', 'ConfirmedCases', 'Fatalities']]

weather = pd.read_csv("../input/tummas/weather.csv")
lat_long = weather[['Country_Region', 'Lat', 'Long']]
lat_long


# In[ ]:


final427 = pred427.merge(lat_long, how="inner", on=['Country_Region']).drop_duplicates()
final507 = pred507.merge(lat_long, how="inner", on=['Country_Region']).drop_duplicates()
final517 = pred517.merge(lat_long, how="inner", on=['Country_Region']).drop_duplicates()
final526 = pred526.merge(lat_long, how="inner", on=['Country_Region']).drop_duplicates()

final427.to_csv(r'final427.csv')
final507.to_csv(r'final507.csv')
final517.to_csv(r'final517.csv')
final526.to_csv(r'final526.csv')

