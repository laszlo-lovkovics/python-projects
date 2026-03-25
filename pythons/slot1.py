import random

def spin():
    symbols = ['🐍', '🚀', '🔥', '💻']
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("|".join(row))
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🐍':
            return bet * 3
        elif row[0] == '🚀':
            return bet * 5
        elif row[0] == '🔥':
            return bet * 10
        elif row[0] == '💻':
            return bet * 20
    return 0
    
def main():
    balance = 100
    
    print("*********************")
    print("  Welcome to Slots")
    print("Symbols: 🐍 🚀 🔥 💻")
    print("*********************")
    
    while balance > 0:
        print(f"Current balance is: {balance}")

        bet = input("Place a bet amount: ")

        if not bet.isdigit:
            print("Invalid form")
            continue
        
        bet = int(bet)

        if bet > balance or bet <= 0:
            print("Invalid amount")
            continue

        balance -= bet

        row = spin()

        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won {payout}")
        else: 
            print("Sorry you lost this round")
        balance += payout

        again = input("play again? (y/n): ")
        if again != "y":
            break

    print("GAME OVER")
    print(f"Your balance is {balance}")




    
if __name__ == '__main__':
    main()
    