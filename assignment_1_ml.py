# -*- coding: utf-8 -*-
"""Assignment-1-ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aS36pmDFn1KuWW71B0IEw4Qmc5Alk08M
"""
#5
nm = input("Enter your name : ")
print('Welcome ', nm)


#6
cel_temp = int(input("Enter temp in Celsius"))
fah_temp = (cel_temp * 9/5) +32
print('Fahrenheit temperature is :',fah_temp)


#7
no_of_hours = int(input("Input the number of hours: "))
rate_per_hour = int(input("Input the rate/ hour: "))
if no_of_hours > 40:
  regular_rate = 40 * rate_per_hour
  overtime = (no_of_hours - 40) * (1.5*rate_per_hour)
  total_rate = regular_rate + overtime
  print('The gross pay is : ', total_rate)
else:
  regular_rate = no_of_hours * rate_per_hour
  print('The gross pay is : ', regular_rate)
    
    
#8
numbers = []
total = 0
count = 0
while True:
  inp = input('Enter a number or "done" to finish ')
  if inp.lower() == 'done':
    break 
  try:
    num = float(inp)
    numbers.append(num)
    count +=1
    total += num
  except:
    print('Enter valid input')

average = total / count 
print('total of numbers', total)
print('Count of numbers', count)
print('average of numbers', average)
