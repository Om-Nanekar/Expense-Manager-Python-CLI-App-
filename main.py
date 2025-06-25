from tabulate import tabulate
from datetime import datetime
import json


def ExpenseManeger():

    expenseOnlyList = []
    # history = []
    total = 0

    def saveData():
        with open('expenses_history.json', 'w') as file:
            json.dump(history, file)

    def loadData():
        try:
            with open('expenses_history.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    history = loadData()


    print('-------- Welcome to Expense Maneger -------- \n 1 for Add expense \n 2 for Show all expenses \n 3 for Show total expenses \n 4 for Exit.')

    while True:

        choise = input('Enter your choise --\n')

        try:
            choise=int(choise)
            
            if choise == 1:
                expense = input('Enter your expense -- \n')
                catagory = input('Enter your Catagory -- \n')
                note = input('Enter your note -- \n')

                try:

                    now = datetime.now()
                    date = now.strftime("%d-%m-%y") 
                    time = now.strftime("%H:%M:%S")

                    expense = int(expense)

                    information = f'{expense}, {catagory}, {note}, {date}, {time}'
                    history.append(information)
                    

                    saveData()
                    print('Saved !!!!')                    

                except ValueError:
                    print('Enter valid input!!!!')
                
            
            elif choise == 2:

                if history == []:
                    print('Expenses not added yet !!!')
                else:
                    data = [item.split(', ') for item in history]
                    headers = ['Amount', 'Category', 'Note', 'Date', 'Time']
                    print(tabulate(data, headers=headers, tablefmt='grid'))

                

            elif choise == 3:

                expenseOnlyList = [int(item.split(", ")[0]) for item in history]                
                total = sum(expenseOnlyList)
                print(f'Total Expenses = {total}')


            elif choise == 4:
                print('Thanks for visiting !!')
                break
        
        except ValueError:
            print('Enter valid input!!!!!')

ExpenseManeger()            