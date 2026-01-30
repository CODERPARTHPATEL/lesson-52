numberSmallest = int(input('enter smallest number'))
numberLargest = int(input('enter largest number'))

a = numberLargest
b = numberSmallest

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print('HCF is',numberLargest)

c = (a*b)/numberLargest
print('LCM is',c)
 