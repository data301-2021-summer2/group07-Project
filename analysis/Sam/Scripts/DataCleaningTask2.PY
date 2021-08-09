import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def Clean_Full(DataPath):
    df1 = (
        pd.read_csv(DataPath,index_col=0)
    )
    df1=(
        df1
        .drop(index=df1.index[0])
        .astype(dtype='int64',errors='ignore')
        .rename(columns={
            "X1":"Credit Limit",
            "X2":"Sex",
            "X3":"Education",
            "X4":"Marital Status",
            "X5":"Age",
            "X6":"Pay/Sept07",
            "X6":"PayStat/Sept05",
            "X7":"PayStat/Aug05",
            "X8":"PayStat/Jul05",
            "X9":"PayStat/Jun05",
            "X10":"PayStat/May05",
            "X11":"PayStat/Apr05",
            "X12":"Outstanding/Sept05",
            "X13":"Outstanding/Aug05",
            "X14":"Outstanding/Jul05",
            "X15":"Outstanding/Jun05",
            "X16":"Outstanding/May05",
            "X17":"Outstanding/Apr05",
            "X18":"Paid/Sept05",
            "X19":"Paid/Aug05",
            "X20":"Paid/Jul05",
            "X21":"Paid/Jun05",
            "X22":"Paid/May05",
            "X23":"Paid/Apr05",
            "Y":"Default"
        }
               )
        .replace("",float("NaN"))
        .dropna(axis = 1)
        .replace({'Sex': {1: "M", 2: 'F'}})
        .replace({'Education': {1: "MSc or PHd", 2: 'BSc', 3: 'High School Diploma', 4:"Other", 5:"INV", 6:"INV", 0:"INV"}})
        .replace({'Marital Status': {1: "Married", 2: 'Single', 3: 'Other', 0:"INV"}})
        .replace({'Default': {1: True, 0: False}})
        .loc[lambda row : ~row['Education'].str.contains("INV")]
        .loc[lambda row : ~row['Marital Status'].str.contains("INV")]
    )
    df1=(
        df1
        .assign(Payment_Score=(
            ((1+df1[['PayStat/Sept05',
                     "PayStat/Aug05",
                     "PayStat/Jul05",
                     "PayStat/Jun05",
                     "PayStat/May05",
                     "PayStat/Apr05"]]
             )
                    .astype(dtype='int64',errors='ignore')))
                    .sum(axis=1)/6)    
        .assign(Avg_Outstanding=(
            ((df1[["Outstanding/Sept05",
                   "Outstanding/Aug05",
                   "Outstanding/Jul05",
                   "Outstanding/Jun05",
                   "Outstanding/May05",
                   "Outstanding/Apr05"]]
            )
                 .astype(dtype='int64',errors='ignore')))
                .sum(axis=1)/6)
        .assign(Avg_Paid=(
            ((df1[["Paid/Sept05",
                   "Paid/Aug05",
                   "Paid/Jul05",
                   "Paid/Jun05",
                   "Paid/May05",
                   "Paid/Apr05"]]
             )
             .astype(dtype='int64',errors='ignore')))
                .sum(axis=1)/6)
        .drop(['PayStat/Sept05',
               "PayStat/Aug05",
               "PayStat/Jul05",
               "PayStat/Jun05",
               "PayStat/May05",
               "PayStat/Apr05",
               "Outstanding/Sept05",
               "Outstanding/Aug05",
               "Outstanding/Jul05",
               "Outstanding/Jun05",
               "Outstanding/May05",
               "Outstanding/Apr05",
               "Paid/Sept05",
               "Paid/Aug05",
               "Paid/Jul05",
               "Paid/Jun05",
               "Paid/May05",
               "Paid/Apr05"
              ]
              , axis = 1
             )
        .reindex(columns=[
            'Sex',
            'Education',
            'Marital Status',
            'Age',
            'Credit Limit'
            ,'Payment_Score',
            'Avg_Outstanding',
            'Avg_Paid',
            'Default'
        ]
                )
        .rename(columns = 
                {'Payment_Score':'Payment Score','Avg_Outstanding' : 'Avg Outstanding','Avg_Paid':'Avg Paid'}
               )
        .reset_index(drop=True)
    )
    return df1

def Clean_Num(DataPath):
    df2 = (
        pd.read_csv(DataPath,index_col = 0)
    )
    df2=(
        df2
        .drop(index=df2.index[0])
        .astype(dtype='int64',errors='ignore')
        .rename(columns={"X1":"Credit Limit",
                               "X2":"Sex",
                               "X3":"Education",
                               "X4":"Marital Status",
                               "X5":"Age",
                               "X6":"Pay/Sept07",
                               "X6":"PaySep",
                               "X7":"PayAug",
                               "X8":"PayJul",
                               "X9":"PayJun",
                               "X10":"PayMay",
                               "X11":"PayApr",
                               "X12":"Outstanding/Sept05",
                               "X13":"Outstanding/Aug05",
                               "X14":"Outstanding/Jul05",
                               "X15":"Outstanding/Jun05",
                               "X16":"Outstanding/May05",
                               "X17":"Outstanding/Apr05",
                               "X18":"Paid/Sept05",
                               "X19":"Paid/Aug05",
                               "X20":"Paid/Jul05",
                               "X21":"Paid/Jun05",
                               "X22":"Paid/May05",
                               "X23":"Paid/Apr05",
                               "Y":"Default"
                              })
        .replace("",float("NaN"))
        .dropna(axis = 1)
        .drop(["Sex","Marital Status","Education"], axis=1)
    )
    df2=(
        df2
        .assign(Payment_Score=(
            ((1+df2[['PaySep',
                     "PayAug",
                     "PayJul",
                     "PayJun",
                     "PayMay",
                     "PayApr"]]
             )
                    .astype(dtype='int64',errors='ignore')))
                    .sum(axis=1)/6)    
        .assign(Avg_Outstanding=(
            ((df2[["Outstanding/Sept05",
                   "Outstanding/Aug05",
                   "Outstanding/Jul05",
                   "Outstanding/Jun05",
                   "Outstanding/May05",
                   "Outstanding/Apr05"]]
             )
                 .astype(dtype='int64',errors='ignore')))
                .sum(axis=1)/6)
        .assign(Avg_Paid=(
            ((df2[["Paid/Sept05",
                   "Paid/Aug05",
                   "Paid/Jul05",
                   "Paid/Jun05",
                   "Paid/May05",
                   "Paid/Apr05"]]
             )
             .astype(dtype='int64',errors='ignore')))
                .sum(axis=1)/6)
        .rename(columns = 
                {'Payment_Score':'Payment Score','Avg_Outstanding' : 'Avg Outstanding','Avg_Paid':'Avg Paid'}
               )
        .reindex(columns=[
             'Default',
             'Payment Score',
             'Avg Outstanding',
             'Avg Paid',
             'Credit Limit',
             'Age',
             'PaySep',
             'PayAug',
             'PayJul',
             'PayJun',
             'PayMay',
             'PayApr',
             'Outstanding/Sept05',
             'Outstanding/Aug05',
             'Outstanding/Jul05',
             'Outstanding/Jun05',
             'Outstanding/May05',
             'Outstanding/Apr05',
             'Paid/Sept05',
             'Paid/Aug05',
             'Paid/Jul05',
             'Paid/Jun05',
             'Paid/May05',
             'Paid/Apr05',]
            )
        .reset_index(drop=True)
    )
    df2[['PaySep','PayAug','PayJul','PayJun','PayMay','PayApr']]+=1
    return df2

def DefaultOnly(dfPrime):
    DfS = (
        dfPrime
                .loc[lambda x: x['Default']==1]
                .loc[lambda x: x['Default']==True]
                .drop(["Default"],axis=1)
                .reset_index(drop=True)
    )
    return DfS


