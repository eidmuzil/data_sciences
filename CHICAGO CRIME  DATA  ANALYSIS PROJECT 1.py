#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd #Pandas: Library used for data manipulation and analysis
import numpy as np #Numpy: Library with high-level mathematical functions
import matplotlib.pyplot as plt #Matplotlib: Library to plot graphs
import seaborn as sns #Seaborn: Library built on Matplotlib for visualisation
from os import path
from PIL import Image
from wordcloud import WordCloud , STOPWORDS , ImageColorGenerator  


# In[5]:



# reading the data form the loading file ....
# change the format as we want ... 
chicago ="/Users/eidmuzil/Desktop/DATASCINCSEPROJECT/Chicago_Crimes_2012_to_2017.csv"
data_chicage =pd.read_csv(chicago)

data_chicage.Date = pd.to_datetime(data_chicage.Date, format='%m/%d/%Y %I:%M:%S %p')
data_chicage.index= pd.DatetimeIndex(data_chicage.Date)
data_chicage['time_hour'] = data_chicage['Date'].apply(lambda x: x.hour)
data_chicage['month'] = data_chicage['Date'].apply(lambda x: x.month)
data_chicage['year'] = data_chicage['Date'].apply(lambda x: x.year)
data_chicage=data_chicage[data_chicage['year'] !=2017]
data_chicage.head(5)


# In[6]:


data_chicage.shape


# In[7]:


data_chicage.describe()


# In[8]:


crime_types = " ".join(crime for crime in data_chicage['IUCR'])
crime_wordclould = WordCloud().generate(crime_types)
#plot wordclud image 
plt.figure(figsize=[10,10])
plt.imshow(crime_wordclould, interpolation='bilinear')
plt.axis('off')
#store to file 
#plt.savefig()
plt.show()


# In[9]:


df_wordcloud = data_chicage.copy()
df_wordcloud.dropna(axis=0,subset=['Block'],inplace=True)
crime_type_location = " ".join(crime for crime in df_wordcloud['Block'])
mask = np.array(Image.open('flags_PNG14592.png'))
crime_location_wordcloud = WordCloud(background_color='white',mode='RGBA',
                                    max_words=1000,mask=mask).generate(crime_type_location)
image_colors = ImageColorGenerator(mask)
plt.figure(figsize=[20,20])

plt.imshow(crime_location_wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis('off')
#store to file 
#plt.savefig()
plt.show()


# In[10]:


#CRIME TREND ANALYSIS by Years 
plt.figure(figsize=(11,5))
data_chicage.resample('M').size().plot(legend=False)
plt.title("NUMBER OF CRIMES PER MONTH (2012-2017)")
plt.xlabel("MONTHS")
plt.ylabel("NUMBER OF CRIMES")
plt.show()


# In[11]:


crimes_count_date = data_chicage.pivot_table('ID',aggfunc=np.size,columns='Primary Type',
                                            index=data_chicage.Date,fill_value=0)
crimes_count_date.index = pd.DatetimeIndex(crimes_count_date.index)
plot=crimes_count_date.rolling(365).sum().plot(figsize=(12,30),
                                               subplots=True,
                                               layout=(-1, 3),
                                               sharex=False,sharey=False)


# In[12]:


crimes_by_time = data_chicage.copy()
primary_types=['ARSON',"CONCEALED CARRY LICENSE VIOLATION", 'CRIM SEXUAL ASSAULT',
              'DECEPTIVE PRACTICE', 'HOMICIDE','ROBBERY','THEFT',
              'WEAPONS VIOLATION', 'MOTOR VEHICLE THEFT'
              ,'CRIMINAL DAMAGE']
crimes_by_time = crimes_by_time[crimes_by_time['Primary Type'].isin(primary_types)]
crimes_by_time = crimes_by_time.groupby('time_hour').size().reset_index(name='No. of Crimes')
crimes_by_time['hours'] = crimes_by_time['time_hour'].apply(lambda x: str(x)+':00')


# plot crimes by time period 
fig = plt.figure(figsize=(16,10))
sns.pointplot(data=crimes_by_time, x ='hours', y='No. of Crimes', color='Salmon')


#set lebels # title 
plt.xlabel('Time')
plt.ylabel('No. of Crimes')
plt.title('Total Crimes by Time Period')
plt.show()


# In[ ]:





# In[13]:


# Crimes by Type :::: 
Grimes_by_type = data_chicage.copy()
Grimes_by_type = Grimes_by_type[Grimes_by_type['Primary Type'].isin(primary_types)]
Grimes_by_type = Grimes_by_type.groupby(['time_hour','Primary Type']).size().reset_index(name='No.of Crimes')
# format hour data ....

Grimes_by_type['hours'] = Grimes_by_type['time_hour'].apply(lambda x: str(x)+':00')
Grimes_by_type_pivot = pd.pivot_table(Grimes_by_type, index =['time_hour'], columns=['Primary Type'],
                                               values='No.of Crimes', aggfunc=np.sum)
Grimes_by_type_pivot.plot(kind='bar', stacked=True, figsize=(16,8),title='NO . of Crimes by type')










# In[14]:


crimes_by_month = data_chicage.copy()

crimes_by_month = crimes_by_month[crimes_by_month['Primary Type'].isin(primary_types)]
crimes_by_month = crimes_by_month.groupby('month').size().reset_index(name='No. of Crimes')
crimes_by_month['month (avarage)'] = crimes_by_month['No. of Crimes'].apply(lambda x:x/5)


# plot crimes by time period 
fig = plt.figure(figsize=(16,10))
sns.pointplot(data=crimes_by_month, x ='month', y='month (avarage)', color='Salmon')


#set lebels # title 
plt.xlabel('Month')
plt.ylabel('No. of Crimes')
plt.title('Total Crimes by Time Period')
plt.show()


# In[18]:


crimes_by_arrest = data_chicage.copy()

crimes_by_arrest = crimes_by_arrest.groupby(['Primary Type','Arrest']).size().reset_index(name='No. of Crimes')
crimes_by_arrest = crimes_by_arrest[crimes_by_arrest['Primary Type'].isin(primary_types)]

crimes_by_arrest_pivot = pd.pivot_table(crimes_by_arrest, index =['Primary Type'], columns=['Arrest'],values='No. of Crimes',aggfunc=np.sum)
crimes_by_arrest_pivot = crimes_by_arrest_pivot.reset_index()


crimes_by_arrest_pivot['Total No']= crimes_by_arrest_pivot[True]+ crimes_by_arrest_pivot[False]
crimes_by_arrest_pivot['True'] = crimes_by_arrest_pivot[True]/ crimes_by_arrest_pivot['Total No']
crimes_by_arrest_pivot['False'] = crimes_by_arrest_pivot[False]/ crimes_by_arrest_pivot['Total No']

crimes_by_arrest_pivot = crimes_by_arrest_pivot[['Primary Type','True','False']] + crimes_by_arrest_pivot[False]

crimes_by_arrest_pivot = crimes_by_arrest_pivot.set_index('Primary Type')

crimes_by_arrest_pivot.plot(kind='barh', stacked = True, figsize =(16,6), title ='No . Of Crimes By Type')


# In[26]:


data_chicage['Details'] = data_chicage ['Primary Type'] + ', ' + data_chicage['Description']
top_crimes = data_chicage.groupby (['Details']) ['Arrest'].count()
top_crimes = pd.DataFrame(top_crimes).nlargest(10,'Arrest').reset_index()
top_crimes = list(top_crimes['Details'])
top_crimes


# In[29]:


df2 = data_chicage.groupby(['Details','month'])['Arrest'].count()
#chart formatting 
DIMS = (25,15)
fig = plt.figure(figsize=DIMS)
ax1 = fig.add_subplot(111)
ax1.set_title('Major crimes (January - December)',fontsize=20)
ax1.set_ylabel('Details',fontsize=20)
ax1.set_xlabel('month',fontsize=20)
# get top 20 data 
df2 = pd.DataFrame(df2).reset_index()
df2 = df2[df2['Details'].isin(top_crimes)]
# pivot data to 2D table , and fill all na values 

df2 = df2.pivot_table(index ='Details',columns ='month',values='Arrest')
df2.fillna(0, inplace = True)
# create heatmap 

sns.heatmap(df2, cmap='Blues',annot = True , fmt= 'g')


# In[ ]:




