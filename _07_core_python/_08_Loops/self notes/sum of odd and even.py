#sum of odd and even fall in between 12 to 37
sum_odd=0
sum_even=0
for j in range(13,38,2) :
    sum_odd=sum_odd+j
for i in range(12,37,2) :
    sum_even=sum_even+i

print("Sum of odd numbers from 12 to 37 is ",sum_odd)
print("Sum of even numbers from 12 to 37 is ",sum_even)