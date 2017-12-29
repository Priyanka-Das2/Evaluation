import pandas as pd

d =  pd.read_csv('bitcoin-cross-new.csv')
d1 = d[['Source','Volume (24h)','Pair']]
d2 = d1.groupby(['Source']).agg({'Volume (24h)': "sum"})
d3 = d2.sort_values(by=['Volume (24h)'], ascending = False).head(10)

d3.to_csv('largest_exchanges_wrt_turnover.csv')
d8 = d2.sort_values(by=['Volume (24h)'], ascending = True).head(10)
d8.to_csv('cheapest_exchanges_wrt_turnover.csv')
d4 = d[['Pair','Price']]
d5 = d4.groupby(['Pair']).agg({'Price': "mean"})
d6 = d5.sort_values(by=['Price'], ascending = True).head(10)
d6.to_csv('cheap_pairs_(price).csv')
d7 = d5.sort_values(by=['Price'], ascending = False).head(10)
d7.to_csv('expensive_pairs_(price).csv')
dc = d.groupby('Pair').agg({'Volume (24h)':"sum"})
dn = dc.sort_values('Volume (24h)', ascending = False).head(5)
dn.to_csv('most_traded_pairs_turnover.csv')
dm = dc.sort_values('Volume (24h)', ascending = True).head(5)
dm.to_csv('least_traded_pair_turnover.csv')

