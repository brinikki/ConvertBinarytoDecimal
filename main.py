bn = input("Enter Binary number:")
l = list(bn)
sum = 0
l.reverse()
for i in range(len(bn)):
    sum = sum+int(l[i])*2**i
print ("Decimal number:", sum)