# -*- coding: utf-8 -*-
"""

@author: brkea
"""

from pybaseball import pitching_stats, pitching_stats_bref, batting_stats, batting_stats_bref, playerid_lookup
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor



# #gives every person that pitched - baseball reference
# pit2019 = pitching_stats_bref(2019)
# pit2021 = pitching_stats_bref(2021)
# pit2022 = pitching_stats_bref(2022)
# pit2023 = pitching_stats_bref(2023)

# pitchers = pd.concat([pit2019, pit2021, pit2022, pit2023])

# hit2019 = batting_stats_bref(2019)
# hit2021 = batting_stats_bref(2021)
# hit2022 = batting_stats_bref(2022)
# hit2023 = batting_stats_bref(2023)

# batters = pd.concat([hit2019, hit2021, hit2022, hit2023])


# pitchers.to_csv(r'C:\Users\brkea\Desktop\19-23_pitchers_season_stats.csv', index=False, sep=',', encoding='utf-8')
# batters.to_csv(r'C:\Users\brkea\Desktop\19-23_batters_season_stats.csv', index=False, sep=',', encoding='utf-8')



pitchers = pd.read_csv('C:\\Users\\brkea\\Desktop\\19-23_pitchers_season_stats.csv')
pitchers.fillna(0, inplace = True)
pitchers.replace([np.inf, -np.inf], np.nan, inplace=True)
pitchers.dropna(inplace=True)


def stats2024(player):
    
    ind = pitchers[pitchers['Name'] == player]
    
    pitch = pitchers.drop(columns = ['Name', 'Lev', 'Age', '#days', 'Tm', 'IBB', 'SF', 'SB', 'CS', 'PO', 'BF', 'Pit', 'mlbID'])
    ind = ind.drop(columns=['Name', 'Lev', 'Age', '#days', 'Tm', 'IBB', 'SF', 'SB', 'CS', 'PO', 'BF', 'Pit', 'mlbID'])
    
    #trying to average all of the columns so I can make a prediction off of them
    def weighted_average(dataframe, value, weight):
        val = dataframe[value]
        wt = dataframe[weight]
        return (val * wt).sum() / wt.sum()
    
    #filtering seasons that ended early due to injuries which could mess up predictions
    ind = ind[ind['G'] > 13]
    
    #weighted average for most values (regular average for the rest) based on players previous performance
    G = round(np.mean(ind['G'], axis=0),0)
    GS = round(np.mean(ind['GS'], axis=0),0)
    W = round(weighted_average(ind, 'W', 'IP'),0)
    L = round(weighted_average(ind, 'L', 'IP'),0)
    SV = round(weighted_average(ind, 'SV', 'IP'),0)
    IP = round(weighted_average(ind, 'IP', 'G'),0)
    H = round(weighted_average(ind, 'H', 'IP'),0)
    R = round(weighted_average(ind, 'R', 'IP'),0)
    ER = round(weighted_average(ind, 'ER', 'IP'),0)
    BB = round(weighted_average(ind, 'BB', 'IP'),0)
    SO = round(weighted_average(ind, 'SO', 'IP'),0)
    HR = round(weighted_average(ind, 'HR', 'IP'),0)
    HBP = round(weighted_average(ind, 'HBP', 'IP'),0)
    ERA = round(weighted_average(ind, 'ERA', 'IP'),2)
    AB = round(weighted_average(ind, 'AB', 'IP'),0)
    double = round(weighted_average(ind, '2B', 'IP'),0)
    triple = round(weighted_average(ind, '3B', 'IP'),0)
    GDP = round(weighted_average(ind, 'GDP', 'IP'),0)
    Str = round(weighted_average(ind, 'Str', 'IP'),2)
    StL = round(weighted_average(ind, 'StL', 'IP'),2)
    StS = round(weighted_average(ind, 'StS', 'IP'),2)
    GB_FB = round(weighted_average(ind, 'GB/FB', 'IP'),2)
    LD = round(weighted_average(ind, 'LD', 'IP'),2)
    PU = round(weighted_average(ind, 'PU', 'IP'),2)
    WHIP = round(weighted_average(ind, 'WHIP', 'IP'),3)
    BAbip = round(weighted_average(ind, 'BAbip', 'IP'),3)
    SO9 = round(weighted_average(ind, 'SO9', 'IP'),1)
    SO_W = round(weighted_average(ind, 'SO/W', 'IP'),2)
    
    #make row of new data and add to dataframe to fit into correct columns
    newrow = [G,GS,W,L,SV,IP,H,R,ER,BB,SO,HR,HBP,ERA,AB,double,triple,GDP,Str,StL,StS,GB_FB,LD,PU,WHIP,BAbip,SO9,SO_W]
    ind.loc[len(ind.index)] = newrow 
    
    #isolate row to make prediction on 
    ind = ind[4:5]
    
    
    #function to predict a stat based on the average values - trained on all the pitchers data from the previous 4 full years of data
    def prediction(stat):
        #random forest Regressor
        player = ind.drop(columns=[stat])
    
        # Split data into features (X) and target (y)
        X = pitch.drop(stat, axis = 1)
        y = pitch[stat]
    
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    
        # Create and train the RandomForestRegressor model
        clf = RandomForestRegressor(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)
    
        prediction = float(clf.predict(player))
        prediction = {stat:prediction}
        return(prediction)
    
    x2024 = {}
    
    x2024.update(prediction('G'))
    x2024.update(prediction('GS'))
    x2024.update(prediction('W'))
    x2024.update(prediction('L'))
    x2024.update(prediction('SV'))
    x2024.update(prediction('IP'))
    x2024.update(prediction('H'))
    x2024.update(prediction('R'))
    x2024.update(prediction('ER'))
    x2024.update(prediction('BB'))
    x2024.update(prediction('SO'))
    x2024.update(prediction('HR'))
    x2024.update(prediction('HBP'))
    x2024.update(prediction('ERA'))
    x2024.update(prediction('AB'))
    x2024.update(prediction('2B'))
    x2024.update(prediction('3B'))
    x2024.update(prediction('GDP'))
    x2024.update(prediction('Str'))
    x2024.update(prediction('StL'))
    x2024.update(prediction('StS'))
    x2024.update(prediction('GB/FB'))
    x2024.update(prediction('LD'))
    x2024.update(prediction('PU'))
    x2024.update(prediction('WHIP'))
    x2024.update(prediction('BAbip'))
    x2024.update(prediction('SO9'))
    x2024.update(prediction('SO/W'))
    
    prediction = pd.DataFrame([x2024])
    
    return(prediction)
    
    
x2024 = stats2024('Clayton Kershaw')

