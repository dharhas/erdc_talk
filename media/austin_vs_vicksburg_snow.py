from ulmo.ncdc import ghcn_daily
import pandas as pd

# download snow data
austin_data = ghcn_daily.get_data('USW00013958', elements='SNOW', as_dataframe=True) # Austin Camp Mabry
vicksburg_data = ghcn_daily.get_data('USC00168923', elements='SNOW', as_dataframe=True) #TALLULAH, LA

# combine data and drop dates that are not in both datasets
data = pd.DataFrame({'austin': austin_data['SNOW']['value'], 
                     'vicksburg': vicksburg_data['SNOW']['value']})
data = data.dropna()

# plot
data.resample('10A', how='sum').plot(kind='bar')



