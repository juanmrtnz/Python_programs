amountdue = 50
while amountdue > 0:
    if amountdue > 0:
        print(f"Amount Due: {amountdue}")
    coins = int(input("Insert Coin: "))
    if coins == 25 or coins == 10 or coins == 5:
        amountdue = amountdue - coins
        
if amountdue <= 0:
    print(f"Change owed: {amountdue * -1}")

