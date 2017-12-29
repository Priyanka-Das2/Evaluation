import pandas as pd
import numpy as np
d = pd.read_csv('company-data.csv')
p1 = d[['Co_Code','Co_Name']].groupby('Co_Code').first()

p1.to_csv('company.csv')
e1 = d.groupby(['Stock Exchange' ]).first()
e2 = e1.index.get_level_values(0)
e3 = pd.DataFrame(e2)
e3 = e3.rename(columns = {'Stock Exchange': 'exchange_code'})
    
e3['exchange_name'] = ['National Stock Exchange','National Stock Exchange-Small and Medium Enterprices']
e3.to_csv('exchange.csv')
d.columns = [u'Co_Code', u'Co_Name', u'Stock Exchange', u'NSE Symbol', u'Industry',
       u'Sector', u'year_end', u'equity_paid_up', u'net_Sales', u'PAT',
       u'PBIDT', u'Debt-Equity Ratio[Latest]', u'PBIDTM-(%)[Latest]']
f1 = d[['Co_Code','year_end','net_Sales','equity_paid_up','PAT','PBIDT','Debt-Equity Ratio[Latest]', 'PBIDTM-(%)[Latest]']].set_index(['Co_Code','year_end'])
f1.to_csv('company_financials.csv') 
i1 = d.groupby(['Industry' ]).first()
i2 = i1.index.get_level_values(0)
i3 = pd.DataFrame(i2)
i3 = i3.rename(columns = {'Industry': 'industry_name'})
i3.to_csv('industry.csv')
s1 = d.groupby(['Sector' ]).first()
s2 = s1.index.get_level_values(0)
s3 = pd.DataFrame(s2)
s3 = s3.rename(columns = {'Sector':'sector_name'})
s3['sector_code'] = s3.index
s3.to_csv('sector.csv')
