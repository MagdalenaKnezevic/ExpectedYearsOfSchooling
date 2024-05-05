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
data.shape
data.head(5)

#Izbacivanje svih država koje nemaju podatke o očekivanim godinama školovanja
data.loc[data['HDI Rank (2021)'].isnull()]
data.drop([108,158], inplace=True)
data.shape

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

#Spremanje promjena
data.to_csv('schooling.csv', index=False)



