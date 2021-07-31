#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def LoadnClean (path):
    import pandas as pd
    import seaborn as sns
    import matplotlib as plt
    import numpy as np
    
    df1 = ( 
                pd.read_csv(path,index_col = 0)
          )
    df2 = ( df1
                .drop(index=df1.index[0])
                .rename(columns={"X1":"Credit Limit",
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
                           })
               .apply(pd.to_numeric)
               .replace({'Sex': {1: "M", 2: 'F'}})
               .replace({'Education': {1: "MSc or PHd", 2: 'BSc', 3: 'High School Diploma', 4:"Other", 5:"Delete", 6:"Delete", 0:"Delete"}})
               .replace({'Marital Status': {1: "Married", 2: 'Single', 3: 'Other', 0:"Delete"}})
               .replace({'Default': {1: "True", 0: 'False'}})
               .loc[lambda row : ~row['Education'].str.contains('Delete')]
               .loc[lambda row : ~row['Marital Status'].str.contains('Delete')]
          )
    df2
    df3 = ( df2
                .assign(Payment_Score=(df2["PayStat/Sept05"]+df2['PayStat/Aug05']+df2['PayStat/Jul05']+df2['PayStat/Jun05']+df2['PayStat/May05']+df2['PayStat/Apr05']+6)/6)
                .assign(Avg_Outstanding=(df2["Outstanding/Sept05"]+df2['Outstanding/Aug05']+df2['Outstanding/Jul05']+df2['Outstanding/Jun05']+df2['Outstanding/May05']+df2['Outstanding/Apr05'])/6)
                .assign(Avg_Paid=(df2["Paid/Sept05"]+df2['Paid/Aug05']+df2['Paid/Jul05']+df2['Paid/Jun05']+df2['Paid/May05']+df2['Paid/Apr05'])/6)
                .drop(["PayStat/Jun05","PayStat/Sept05","PayStat/Aug05","PayStat/Jul05","PayStat/May05","PayStat/Apr05"], axis=1)
                .drop(["Outstanding/Sept05","Outstanding/Aug05","Outstanding/Apr05","Outstanding/Jul05","Outstanding/Jun05","Outstanding/May05"], axis=1)
                .drop(["Paid/Sept05","Paid/Aug05","Paid/Apr05","Paid/Jul05","Paid/Jun05","Paid/May05"], axis=1)
                .reindex(columns=["Credit Limit", "Sex", "Education","Marital Status","Age","Payment_Score","Avg_Outstanding","Avg_Paid","Default"])

           
                
          )
    df3
    
    return df3

def AgevsDefault (df):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    plt.subplots(figsize=(30, 10))
    plot = sns.countplot(x="Age", hue="Default", data=df)
    plt.ylabel('Count of Defaults',fontsize=18)
    plt.xlabel('Age by years',fontsize=15)
    plt.title("What age's are most likely to default?",fontsize=30)
    sns.despine()
    return plot
        