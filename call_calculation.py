import pandas as pd
import yfinance as yf

import stock_list

STOCKS = {}

def retrieve_data(stock):
    dataframe = yf.download(tickers=stock, period='2d', interval='1d')
    return dataframe

def edit_data(stock, dataframe):
    dataframe= dataframe.reset_index()
    df = dataframe[['Date', 'Close']]
    df.loc[:,'Date'] = pd.to_datetime(df['Date'], yearfirst=True)
    df = df.tail(2) #in case a longer period is chosen
    difference_to_last_day = df.iloc[0,1] - df.iloc[1,1]
    percent_difference_to_last_day = df.iloc[1,1] / df.iloc[0,1]

    #choose stocks based on calculated or emotional criteria
    if difference_to_last_day > stock_list.difference_to_last_day or percent_difference_to_last_day < stock_list.percent_difference_to_last_day:
        STOCKS[stock] = df.iloc[1,1]
    elif stock in stock_list.common_stocks and df.iloc[1,1] <= stock_list.stock_values[stock]:
        STOCKS[stock] = df.iloc[1,1]
        

def combine_edit_data():
    for name, ticker in stock_list.stock_tickers.items():
        dataframe = retrieve_data(ticker)
        edit_data(name, dataframe)
    if len(STOCKS) > 0:
        df_stocks = pd.DataFrame.from_dict(STOCKS, orient='index', columns = ['Stocks'])
        
        df_stocks = df_stocks.to_html() #turn df to html
        html_text = '<!DOCTYPE html><html><body><p>' + df_stocks +'</p></body></html>' #organize html for e-mail format
        return html_text
    else:
        return False




