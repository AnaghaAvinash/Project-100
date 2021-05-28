class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def view_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("your card number:- ")
    pin_number  = input("your pin number:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Current balance  2.withdraw")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.view_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()