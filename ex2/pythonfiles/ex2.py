import pandas as pd
d =  pd.read_csv('bitcoin-cross-new.csv')
d1 = d[['Source','Volume (24h)','Pair']]
#exchanges with respect to turnover
d2 = d1.groupby(['Source']).agg({'Volume (24h)': "sum"})
d3 = d2.sort_values(by=['Volume (24h)'], ascending = False).head(10)

d3.to_html('largest_exchanges_wrt_turnover.html')
d8 = d2.sort_values(by=['Volume (24h)'], ascending = True).head(10)
d8.to_html('cheapest_exchanges_wrt_turnover.html')
#pairs
d4 = d[['Pair','Price']]
d5 = d4.groupby(['Pair']).agg({'Price': "mean"})
#sorting pairs according to price
d6 = d5.sort_values(by=['Price'], ascending = True).head(10)
d6.to_html('cheap_pairs_(price).html')
d7 = d5.sort_values(by=['Price'], ascending = False).head(10)
d7.to_html('expensive_pairs_(price).html')
#trade-pairs with respect to turnover
dc = d.groupby('Pair').agg({'Volume (24h)':"sum"})
dn = dc.sort_values('Volume (24h)', ascending = False).head(5)

dn.to_html('most_traded_pairs_turnover.html')
dm = dc.sort_values('Volume (24h)', ascending = True).head(5)
dm.to_html('least_traded_pair_turnover.html')
#traded pairs with respect to exchanges
d10 = pd.DataFrame(d.Pair.value_counts())
d11 = d10.rename(columns = {'Pair' : 'No_of_traded_pair'})
d11.index.name = 'Pair'
d11.head(10).to_html('most_traded_pairs_wrt_exchanges.html')
d11.tail(10).to_html('least_traded_pairs_wrt_exchanges.html')
d12 = pd.DataFrame(d.Source.value_counts())
d13 = d12.rename(columns = {'Source' : 'No_of_traded_pair'})
d13.index.name = 'Source'
#exchanges with respect to traded pairs
d13.head(10).to_html('top10_exchanges_wrt_traded_pairs.html')
d13.tail(10).to_html('bottom10_exchanges_wrt_traded_pairs.html')
