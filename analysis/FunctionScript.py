#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def LoadnClean (path):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
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
    x,y = 'Age', 'Default'
    (df
        .groupby(x)[y]
        .value_counts(normalize=True)
        .mul(100)
        .rename('percent')
        .reset_index()
        .pipe((sns.catplot,'data'), x=x,y='percent',height=5,aspect=3,hue=y,kind='bar'))
        
def JustPayments(path):
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
               .apply(pd.to_numeric)          )
      df2
      df3 = ( df2
                .assign(Payment_Score=(df2["PaySep"]+df2['PayAug']+df2['PayJul']+df2['PayJun']+df2['PayMay']+df2['PayApr']+6)/6)
                .assign(Avg_Outstanding=(df2["Outstanding/Sept05"]+df2['Outstanding/Aug05']+df2['Outstanding/Jul05']+df2['Outstanding/Jun05']+df2['Outstanding/May05']+df2['Outstanding/Apr05'])/6)
                .assign(Avg_Paid=(df2["Paid/Sept05"]+df2['Paid/Aug05']+df2['Paid/Jul05']+df2['Paid/Jun05']+df2['Paid/May05']+df2['Paid/Apr05'])/6)
                .drop(["Sex","Marital Status","Education"], axis=1)
      )
      df3["PaySep"]=df3["PaySep"]+1
      df3["PayAug"]=df3["PayAug"]+1
      df3["PayJul"]=df3["PayJul"]+1
      df3["PayJun"]=df3["PayJun"]+1
      df3["PayMay"]=df3["PayMay"]+1
      df3["PayApr"]=df3["PayApr"]+1

                                   
      df3
      return df3
def Defaulters(df):
      df4 = (df.loc[lambda x: x['Default']==1]

      )
      return df4      
