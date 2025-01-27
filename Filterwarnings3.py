import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
def createdata():
    data={
        'Age':np.random.randint(18,70,size=20),
        'Salary':np.random.randint(30000,120000,size=20),
        'Purchased':np.random.choice([0,1],size=20),
        'Gender':np.random.choice(['Male','Female'],size=20),
        'City':np.random.choice(['NewYork','Hyderabad','Jammikunta'])
    }
    df=pd.DataFrame(data)
    return df

df=createdata()
df.head(10)
df.loc[5,'Age']=np.nan
df.loc[9,'Salary']=np.nan
df.head(10)
df_dropped=df.dropna()
df_dropped.head(10)
