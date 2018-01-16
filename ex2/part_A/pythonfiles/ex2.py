import pandas as pd
def  crypto(file , COIN ):
    d =  pd.read_csv(file)
    d1 = d[['Source','Volume (24h)','Pair']]
    modified = d[['Source','Volume (24h)','Pair']]
    mod1 = modified.groupby(['Source']).agg({'Volume (24h)': "sum"})
    mod2 = mod1.sort_values(by=['Volume (24h)'], ascending = False).head(10)
    mod2.to_html('largest_exchanges_wrt_turnover.html')
    mod3 = mod2.sort_values(by=['Volume (24h)'], ascending = True).head(10)
    mod3.to_html('cheapest_exchanges_wrt_turnover.html')
    mod4 = d[['Pair','Price']]
    mod5 = mod4.groupby(['Pair']).agg({'Price': "mean"})
    dc = d.groupby('Pair').agg({'Volume (24h)':"sum"})
    dn = dc.sort_values('Volume (24h)', ascending = False).head(5)
    dn.to_html('most_traded_pairs_turnover.html')
    dm = dc.sort_values('Volume (24h)', ascending = True).head(5)
    dm.to_html('least_traded_pair_turnover.html')
    mod6 = pd.DataFrame(d.Pair.value_counts())
    mod7 = mod6.rename(columns = {'Pair' : 'No_of_exchanges'})
    mod7.index.name = 'Pair'
    mod7.head(10).to_html('most_traded_pairs_wrt_exchanges.html')
    mod7 = mod7.where(mod7['No_of_exchanges']< 4)
    mod7.sort_values('No_of_exchanges').dropna().to_html('least_traded_pairs_wrt_exchanges.html')
    mod8 = pd.DataFrame(d.Source.value_counts())
    mod9 = mod8.rename(columns = {'Source' : 'No_of_traded_pairs'})
    mod9.index.name = 'Source'
    mod9.head(10).to_html('top10_exchanges_wrt_traded_pairs.html')
    mod10  = mod9.where(mod9['No_of_traded_pairs'] < 4)
    mod10.sort_values('No_of_traded_pairs').dropna().to_html('bottom_exchanges_wrt_traded_pairs.html')
    s = []
    r = []
    for i in d['Pair']:
        s.append((i.split('/'))[1])
        r.append((i.split('/'))[0])
    m = pd.DataFrame(s)     
    m['price'] = d['Price']
    m['1'] = r
    m['exchange'] = d['Source']
    m['pair'] = d['Pair']
    grouped = m.groupby([0]).agg({'price': "mean"})
    grouped = grouped.reset_index()
    grouped['coin'] = grouped[0]
    grouped = grouped[['coin','price']]
    grouped = grouped.set_index('coin')
    grouped = grouped.drop([COIN])
    grouped  = grouped.sort_values('price', ascending = False)
    grouped1 = m.groupby(['1']).agg({'price': "mean"})
    grouped1 = grouped1.drop([COIN])
    grouped1  = grouped1.sort_values('price', ascending = False)
    group = pd.concat([grouped, grouped1], axis=0)
    g1 = group.sort_values('price', ascending = False).head(10)
    g2 = group.sort_values('price').head(10)
    g1.to_html('expensive_cross_coins.html')
    g2.to_html('cheap_cross_coins.html')
crypto('bitcoin-cross-new.csv','BTC')
