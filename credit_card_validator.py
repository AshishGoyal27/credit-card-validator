cardNumber = input("Enter a 16-digit card number:")
original_card_num = "".join(cardNumber.split())
a = list(original_card_num)

#double the value of every second digit
for i in range(0,len(a)):
    if i%2 == 0:
        a[i] = str(int(a[i]) *2)
        if len(a[i])>1:#If doubling operation gives any digit greater than 9 the add the digits of that number
            l = 0
            for j in a[i]:
                l = l + int(j)
            a[i] = l


#sum of all the digits
k = 0
for i in a:
    k = k + int(i)


#if sum ends in zero then card number is valid otherwise invalid
if k%10 == 0:
    print("Entered card number is a valid card number")
else:
    print("Invalid card number")
