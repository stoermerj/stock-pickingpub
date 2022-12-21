# stock-picking

The goal of this application is to provide users with a stock-picking tool. It:
- lets the user choose one or more stocks to monitor
- lets the user define the price he/she would like to buy the stock at
- lets the user define thresholds (percentage and absolute) he/she would like to buy stocks at
- provides an email for the user if requirements are met

stocks and thresholds can be changed / added in the stock_list.py file.

To use this application, the following steps should be followed:

    - Create a Gmail account and generate an app-password here. https://myaccount.google.com/apppasswords. Retrieve the app-password and save for step 3.
    - Add the generated passwords to credentials.py next to the relevant object.
    - Add the e-mail to credentials.py you would like to send the e-mail from. The app is set up in a way that the same e-mail is used for sending and receiving e-mails.
    - Define the stocks you want to follow by adding the tickers in the list stock_input.py lists. You can get the tickers e.g from yahoo.
    - Set up a secret in github to use github actions
    - Run the program.
