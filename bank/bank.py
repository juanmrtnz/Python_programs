answer = input('Greeting: ')

if answer.strip().lower().startswith('hello') == True:
    print('$0')
elif answer.strip().lower().startswith('h') == True:
    print('$20')
else:
    print('$100')