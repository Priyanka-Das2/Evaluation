import pandas as pd
d = pd.read_csv('ping-api-etherdelta-com.csv',sep = ' ')
d = pd.DataFrame(d)
d['time'] = d['of'].str.split('=').str[1]
d['icmp_seq'] = d['56(84)'].str.split('=').str[1]
data = d[['time','icmp_seq']]
data1 = data.set_index('icmp_seq')
data1['r_mean_5'] = data1['time'].rolling(window = 5).mean()
data1['r_mean_10'] = data1['time'].rolling(window = 10).mean()
data1['r_mean_20'] = data1['time'].rolling(window = 20).mean() 
data1['r_std_5'] = data1['time'].rolling(window = 5).std()
data1['r_std_10'] = data1['time'].rolling(window = 10).std()
data1['r_std_20'] = data1['time'].rolling(window = 20).std()
data1.to_csv('output.csv')
