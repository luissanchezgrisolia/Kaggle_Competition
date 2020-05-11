def categorical_to_numeric(df):
    ''' Transforms from categorical features to numeric ''' 
    df.replace({'color':{'D':7,'E':6,'F':5,'G':4,'H':3,'I':2,'J':1}}, inplace=True)
    df.replace({'cut':{'Premium':5,'Ideal':4,'Very Good':3,'Good':2,'Fair':1}}, inplace=True)
    df.replace({'clarity':{'IF':8, 'VVS1':7, 'VVS2':6,'VS1':5,'VS2':4,'SI1':3,'SI2':2,'I1':1}}, inplace=True)
    return df 