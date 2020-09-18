##Rudy Garcia
import time, sys
print("Hi! I'm here to calculate capacitance and give you your variation :)\n")
time.sleep(2)
print("Make sure that your capacitor doesn't already tell you. If it has a prefix, most likely( p,f,n,µ,or m), then that is already your capacitance :), else:")
t=1

while 0<t<=4:
  input_1= input("\nWhat are the first 2 digits of your capacitor:\n")
  if len(input_1) !=2:
    print("\nSorry, I asked for 2 digits you silly!")
    input_1= int(input("Try to get it right this time, What are the first 2 digits?\n"))
  input_2= input("\nWhat is the 3rd digit m8:\n")
  if len(input_2)!=1 and int(input_2)>0:
    print("\nOne digit, nothing else you goof")
    input_2= input("Actually read the instructions, what is the 3rd digit and only the 3rd digit of your capacitor?\n")
  x= int(input_1)
  u= int(input_2)
  modulus= u%3
  floor= (u+1)//3
  value= x* 10**modulus
  prefix=""
  if floor!=2 and floor!=1:
    if floor==-2:
      prefix='a'
    if floor==-1:
      prefix='f'
    if floor==0:
      prefix='p'
    if floor==1:
      prefix='n'
    if floor==2:
      prefix='µ'
    if floor==3:
      prefix=='m'
    if floor==4:
      prefix=""
    if floor==5:
      prefix=='K'
    if floor==6:
      prefix=='M'
    if floor==7:
      prefix=='G'
    if floor==8:
      prefix=='T'
  if floor==2 or floor==1 or floor==0:
    value= value/1000
    if floor==-2:
      prefix='a'
    if floor==-1:
      prefix='f'
    if floor==0:
      prefix='p'
    if floor==1:
      prefix='n'
    if floor==2:
      prefix='µ'
    if floor==3:
      prefix=='m'
    if floor==4:
      prefix=""
    if floor==5:
      prefix=='K'
    if floor==6:
      prefix=='M'
    if floor==7:
      prefix=='G'
    if floor==8:
      prefix=='T'
  print(f"The digits you enterd are {input_1} and {input_2}")
  t=int(len(input("if these aren't the digits you wanted to enter \"redo\" else hit enter\n ")))
##Gives out final products
  if t==4:
    print('Restart...\n')
    t=t
  elif t!=4:
    print(f"\nHere is your capacitance:\n{value} {prefix}F")
    ask= len(input("\nWould you like to go again? (yes or no please)\n"))
    if ask==3:
      t=4
    if ask==2:
      t+=5
    elif ask!=2 and ask!=3:
      input("I\'m not sure what you saying there. Please re-enter \"yes\" or \"no\"")
