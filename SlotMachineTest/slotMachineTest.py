import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_val = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_wins(columns, lines, bet, values):
    wins = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            wins += values[symbol] * bet
            winning_line.append(line + 1)
    return wins, winning_line


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    # using the key[symbol] value[symbol_count] pairs using dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:]  # using : fetches a copy of all symbols
        for _ in range(rows):
            val = random.choice(curr_symbols)
            curr_symbols.remove(val)
            column.append(val)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def get_num_of_lines():
    while True:
        lines = input("Enter number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number")
    return lines


def deposit():
    while True:
        amt = input("What would you like to deposit? $")
        if amt.isdigit():
            amt = int(amt)
            if amt > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amt


def Getbet():
    while True:
        betAmt = input("What would you like to Bet? $")
        if betAmt.isdigit():
            betAmt = int(betAmt)
            if MIN_BET <= betAmt <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Please enter a number.")
    return betAmt

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = Getbet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to bet, Your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")
    print(balance, lines)

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_wins(slots, lines, bet, symbol_val)
    print(f"You won ${winnings}. ")
    # print(f"You won on lines: ${winning_line}")
    print(f"You won on lines: ", *winning_line)
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current Balance= ${balance}")
        spins=input("Press enter to spin(q to quit).")
        if spins=="q":
            break
        balance=spin(balance)
    print(f"You are left with ${balance}")


main()
