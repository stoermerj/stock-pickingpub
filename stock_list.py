percent_difference_to_last_day = .97 #if current stock is worth 97% of yesterday's worth, send email
difference_to_last_day = 10 #if current stock price is worth less than 10 amount (e.g. Euro) than yesterday's worth, send email

#add any stocks with tickers
stock_tickers = {'hiscox':'H2X3.MU',
                 'allianz': 'ALV.DE',
                 'deutsche post': 'DPW.DE',
                 'adidas': 'ADS.DE',
                 'basf': 'BAS.DE',
                 'beiersdorf': 'BEI.DE',
                 'BNP Paribas': 'BNP.PA',
                 'Deutsche Telekom': 'DTEGY',
                 'Gilead Sciences': 'GIS.SG',
                 'henkel': 'HEN3.DE',
                 'kraft heinz': 'KHNZ.DE',
                 'microsoft': 'MSF.DE',
                 'pepsico': 'PEP.DE',
                 'Procter & Gamble': 'PG.VI',
                 'puma': 'PUM.DE',
                 'sap': 'SAP.DE',
                 'amazon': 'AMZ.DE',
'deutsche post':'DHL.DE',
'continental':'CON.DE',
'bayer': 'BAYN.DE',
'ETF dev world msci': 'IWDA.AS',
'ETF non-dev world msci': 'EIMI.MI',
'ETF eu div': 'FRXD.L',
'ETF eu thes. Lyxor': 'MEUD.PA',
'ETF eu thes msci': 'CSEMU.SW',
                 }

#add prices that you value certain stocks at
stock_values = {'hiscox': 11,
                'henkel': 60,
                'sap': 82,
                'amazon': 75,
'deutsche telekom': 25,
'deutsche post': 33,
'continental': 50,
'bayer': 20,
'ETF dev world msci': 75,
'ETF non-dev world msci': 27,
'ETF eu div': 24,
'ETF eu thes. Lyxor': 200,
'ETF eu thes msci': 150,                }

#combines above dicts to one list if same keys        
common_stocks = list(stock_tickers.keys() & stock_values.keys())
