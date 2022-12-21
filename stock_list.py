percent_difference_to_last_day = .90 #if current stock is worth 90% of yesterday's worth, send email
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
                 'sap': 'SAP.DE'
                 }

#add prices that you value certain stocks at
stock_values = {'hiscox': 9,
                'allianz':180,
                'henkel': 60,
                'kraft heinz': 29.85,
                'puma': 45,
                'sap': 82
                }

#combines above dicts to one list if same keys        
common_stocks = list(stock_tickers.keys() & stock_values.keys())

