import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os
import plotly.express as px

#Učitavanje skupa podataka
data = pd.read_csv('schooling.csv')
#Provjera dimenzija tablice i prikaz prvih pet mjerenja
data.shape  #(195, 39)
data.head(5)

#Izbacivanje svih država koje nemaju podatke o očekivanim godinama školovanja
data.loc[data['HDI Rank (2021)'].isnull()]
data.drop([108,158], inplace=True)
data.shape #(193, 39)

#Popunjavanje praznih vrijednosti sa odgovarajućom porukom
data['Human Development Groups'].fillna(value='No Information', inplace=True)
data['UNDP Developing Regions'].fillna(value='Does not belong to developing regions', inplace=True)


#Funkcija koja mijenja kratice UNDP razvojnih regija u njihovo puno ime
def changeToFUllName(i):
    return (
        i['UNDP Developing Regions']
        .replace('SSA', 'Sub-Saharan Africa')
        .replace('LAC', 'Latin America and the Caribbean')
        .replace('EAP', 'East Asia and the Pacific')
        .replace('AS', 'Arab States')
        .replace('ECA', 'Europe and Central Asia')
        .replace('SA', 'South Asia')
    )
data['UNDP Developing Regions'] = data.apply(changeToFUllName, axis=1)
data.sample(5)

#prikaz nul-vrijednosti po stupcima
data.isnull().sum()

#pronalazak mean vrijednosti po stupcima
# Finding the mean of the column having NaN
mean_value_90 = data['Expected Years of Schooling (1990)'].mean()
mean_value_91 = data['Expected Years of Schooling (1991)'].mean()
mean_value_92 = data['Expected Years of Schooling (1992)'].mean()
mean_value_93 = data['Expected Years of Schooling (1993)'].mean()
mean_value_94 = data['Expected Years of Schooling (1994)'].mean()
mean_value_95 = data['Expected Years of Schooling (1995)'].mean()
mean_value_96 = data['Expected Years of Schooling (1996)'].mean()
mean_value_97 = data['Expected Years of Schooling (1997)'].mean()
mean_value_98 = data['Expected Years of Schooling (1998)'].mean()
mean_value_99 = data['Expected Years of Schooling (1999)'].mean()
mean_value_00 = data['Expected Years of Schooling (2000)'].mean()
mean_value_01 = data['Expected Years of Schooling (2001)'].mean()
mean_value_02 = data['Expected Years of Schooling (2002)'].mean()
mean_value_03 = data['Expected Years of Schooling (2003)'].mean()
mean_value_04 = data['Expected Years of Schooling (2004)'].mean()
mean_value_05 = data['Expected Years of Schooling (2005)'].mean()
mean_value_06 = data['Expected Years of Schooling (2006)'].mean()
mean_value_07 = data['Expected Years of Schooling (2007)'].mean()
mean_value_08 = data['Expected Years of Schooling (2008)'].mean()
mean_value_09 = data['Expected Years of Schooling (2009)'].mean()
mean_value_10 = data['Expected Years of Schooling (2010)'].mean()
mean_value_11 = data['Expected Years of Schooling (2011)'].mean()
mean_value_12 = data['Expected Years of Schooling (2012)'].mean()
mean_value_13 = data['Expected Years of Schooling (2013)'].mean()
mean_value_14 = data['Expected Years of Schooling (2014)'].mean()
mean_value_15 = data['Expected Years of Schooling (2015)'].mean()
mean_value_16 = data['Expected Years of Schooling (2016)'].mean()
mean_value_17 = data['Expected Years of Schooling (2017)'].mean()

#popunjavanje nedostajućih vrijednosti sa mean vrijednostima pripadajućeg stupca
data['Expected Years of Schooling (1990)'].fillna(value=mean_value_90, inplace=True)
data['Expected Years of Schooling (1991)'].fillna(value=mean_value_91, inplace=True)
data['Expected Years of Schooling (1992)'].fillna(value=mean_value_92, inplace=True)
data['Expected Years of Schooling (1993)'].fillna(value=mean_value_93, inplace=True)
data['Expected Years of Schooling (1994)'].fillna(value=mean_value_94, inplace=True)
data['Expected Years of Schooling (1995)'].fillna(value=mean_value_95, inplace=True)
data['Expected Years of Schooling (1996)'].fillna(value=mean_value_96, inplace=True)
data['Expected Years of Schooling (1997)'].fillna(value=mean_value_97, inplace=True)
data['Expected Years of Schooling (1998)'].fillna(value=mean_value_98, inplace=True)
data['Expected Years of Schooling (1999)'].fillna(value=mean_value_99, inplace=True)
data['Expected Years of Schooling (2000)'].fillna(value=mean_value_00, inplace=True)
data['Expected Years of Schooling (2001)'].fillna(value=mean_value_01, inplace=True)
data['Expected Years of Schooling (2002)'].fillna(value=mean_value_02, inplace=True)
data['Expected Years of Schooling (2003)'].fillna(value=mean_value_03, inplace=True)
data['Expected Years of Schooling (2004)'].fillna(value=mean_value_04, inplace=True)
data['Expected Years of Schooling (2005)'].fillna(value=mean_value_05, inplace=True)
data['Expected Years of Schooling (2006)'].fillna(value=mean_value_06, inplace=True)
data['Expected Years of Schooling (2007)'].fillna(value=mean_value_07, inplace=True)
data['Expected Years of Schooling (2008)'].fillna(value=mean_value_08, inplace=True)
data['Expected Years of Schooling (2009)'].fillna(value=mean_value_09, inplace=True)
data['Expected Years of Schooling (2010)'].fillna(value=mean_value_10, inplace=True)
data['Expected Years of Schooling (2011)'].fillna(value=mean_value_11, inplace=True)
data['Expected Years of Schooling (2012)'].fillna(value=mean_value_12, inplace=True)
data['Expected Years of Schooling (2013)'].fillna(value=mean_value_13, inplace=True)
data['Expected Years of Schooling (2014)'].fillna(value=mean_value_14, inplace=True)
data['Expected Years of Schooling (2015)'].fillna(value=mean_value_15, inplace=True)
data['Expected Years of Schooling (2016)'].fillna(value=mean_value_16, inplace=True)
data['Expected Years of Schooling (2017)'].fillna(value=mean_value_17, inplace=True)

#Spremanje promjena
data.to_csv('schooling.csv', index=False)



