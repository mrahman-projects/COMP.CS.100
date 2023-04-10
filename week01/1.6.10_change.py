"""
Create a program that asks how much purchases cost and the amount of
 paid money and then prints the amount of change.

Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    purchase_price = int(input("Purchase price: "))
    paid_money = int(input("Paid amount of money: "))

    if paid_money >= purchase_price:
        money_to_return = paid_money - purchase_price
        if money_to_return != 0:
            print("Offer change:")
            # count 10`s notes
            tens_note = money_to_return // 10
            if tens_note != 0:
                print(str(tens_note) + " ten-euro notes")
            # count 5`s notes
            fives_note = (money_to_return % 10) // 5
            if fives_note != 0:
                print(str(fives_note) + " five-euro notes")
            # count 2`s coins
            twos_coin = (money_to_return % 5) // 2
            if twos_coin != 0:
                print(str(twos_coin) + " two-euro coins")
            # count 1`s coins
            ones_coin = money_to_return - \
                ((tens_note * 10) + (fives_note * 5) + (twos_coin * 2))
            if ones_coin != 0:
                print(str(ones_coin) + " one-euro coins")
        else:
            print("No change")
    else:
        print("No change")


if __name__ == "__main__":
    main()
