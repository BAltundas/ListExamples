# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:03:12 2021

@author: Bilgi
"""


import pandas as pd
import wget
# pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
# # figsize(15, 5)

url = 'https://raw.githubusercontent.com/jvns/pandas-cookbook/master/data/bikes.csv'
wget.download(url)

df= pd.read_csv('bikes.csv', encoding='latin1')

df.head()
#   Date;Berri 1;Brébeuf (données non disponibles);Côte-Sainte-Catherine;Maisonneuve 1;Maisonneuve 2;du Parc;Pierre-Dupuy;Rachel1;St-Urbain (données non disponibles)
# 0                   01/01/2012;35;;0;38;51;26;10;16;                                                                                                               
# 1                   02/01/2012;83;;1;68;153;53;6;43;                                                                                                               
# 2                 03/01/2012;135;;2;104;248;89;3;58;                                                                                                               
# 3                04/01/2012;144;;1;116;318;111;8;61;                                                                                                               
# 4                05/01/2012;197;;2;124;330;97;13;95;                                                                                                               


df = pd.read_csv('bikes.csv', sep=';', 
                       encoding='latin1')

# change the column separator to a ';'
# Set the encoding to 'latin1' (the default is 'utf8')

df.head()
#  Date  Berri 1  ...  Rachel1  St-Urbain (données non disponibles)
# 0  01/01/2012       35  ...       16                                  NaN
# 1  02/01/2012       83  ...       43                                  NaN
# 2  03/01/2012      135  ...       58                                  NaN
# 3  04/01/2012      144  ...       61                                  NaN
# 4  05/01/2012      197  ...       95                                  NaN


# Parse the dates in the 'Date' column
# Tell it that our dates have the date first instead of the month first
# Set the index to be the 'Date' column

df = pd.read_csv('bikes.csv', sep=';', 
                       encoding='latin1', parse_dates=['Date'], 
                       dayfirst=True, index_col='Date')
df.head()   # df[0:5]  # this is similar to df.head(5)
#  Berri 1  ...  St-Urbain (données non disponibles)
# Date                 ...                                     
# 2012-01-01       35  ...                                  NaN
# 2012-01-02       83  ...                                  NaN
# 2012-01-03      135  ...                                  NaN
# 2012-01-04      144  ...                                  NaN
# 2012-01-05      197  ...                                  NaN

df.shape


# ################## SELECTING A COLUMN #################
print(df.columns)

# Index(['Date', 'Berri 1', 'Brébeuf (données non disponibles)',
#        'Côte-Sainte-Catherine', 'Maisonneuve 1', 'Maisonneuve 2', 'du Parc',
#        'Pierre-Dupuy', 'Rachel1', 'St-Urbain (données non disponibles)'],
#       dtype='object')


df['Date'].head()

# 0    01/01/2012
# 1    02/01/2012
# 2    03/01/2012
# 3    04/01/2012
# 4    05/01/2012
# Name: Date, dtype: object

df[['Date','Berri 1']].head()

#          Date  Berri 1
# 0  01/01/2012       35
# 1  02/01/2012       83
# 2  03/01/2012      135
# 3  04/01/2012      144
# 4  05/01/2012      197

#### #######################  Plot  ################# 

df['Berri 1'].plot(grid=True)
df.plot(figsize=(10, 5))


#### working with larger data set

# The usual preamble
import pandas as pd
# Make the graphs a bit prettier, and bigger
pd.set_option('display.max_columns', 60) 

## getting a json file from web
import urllib, json
# url ="https://data.cityofnewyork.us/resource/erm2-nwe9.json?unique_key=10693408"
url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

import urllib.request, json 
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

elevations = json.dumps(data)
df=pd.read_json(elevations)

print(df.columns)
# Index(['unique_key', 'created_date', 'agency', 'agency_name', 'complaint_type',
#        'descriptor', 'location_type', 'incident_zip', 'incident_address',
#        'street_name', 'cross_street_1', 'cross_street_2',
#        'intersection_street_1', 'intersection_street_2', 'city', 'landmark',
#        'status', 'community_board', 'bbl', 'borough',
#        'x_coordinate_state_plane', 'y_coordinate_state_plane',
#        'open_data_channel_type', 'park_facility_name', 'park_borough',
#        'latitude', 'longitude', 'location', ':@computed_region_efsh_h5xi',
#        ':@computed_region_f5dn_yrer', ':@computed_region_yeji_bk3q',
#        ':@computed_region_92fq_4b7q', ':@computed_region_sbqj_enih',
#        'closed_date', 'resolution_description',
#        'resolution_action_updated_date', 'address_type', 'facility_type',
#        'taxi_pick_up_location'],
#       dtype='object')

df.head(1000)
df.shape

complaints = df[['complaint_type','borough']]
complaints['complaint_type'].value_counts()
complaints['borough'].value_counts()

# # laoding a json file(local)
# file = 'data.json'
# with open(file) as train_file:
#     dict_train = json.load(train_file)

# # converting json dataset from dictionary to dataframe
# train = pd.DataFrame.from_dict(dict_train, orient='index')
# train.reset_index(level=0, inplace=True)
complaint_counts = complaints['complaint_type'].value_counts()
complaint_counts[:10].plot(kind='bar')


#


# The usual preamble
import pandas as pd

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
pd.figsize(15, 5)


# Always display all the columns
pd.set_option('display.line_width', 5000) 
pd.set_option('display.max_columns', 60) 


complaints =df[['unique_key', 	'created_date', 	'closed_date', 	'agency',
                'agency_name', 	'complaint_type', 	'descriptor','location_type',
                'incident_zip']]
complaints[:5]



