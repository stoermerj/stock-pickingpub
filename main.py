import call_calculation 
import send_gmail

def main():
    df = call_calculation.combine_edit_data()
    if df != False:
        send_gmail.send(df)
    elif df == False:
        print('no email')

if __name__ == '__main__':
    main()