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
  if len(input_2)!=1:
      print("\nOne digit, nothing else you goof")
      input_2= input("Actually read the instructions, what is the 3rd digit and only the 3rd digit of your capacitor?\n")
  input_3= input("What is the letter at the end of your capacitor (after the digits)?\n")
  if str.isalpha(input_3) is False:
    print(f"m8, I said the letter, it\'s only one")
    input("What is the letter again...\n")
  x= int(input_1)
  u= int(input_2)
  modulus= u%3
  floor= (u)//3
  value= x* 10**modulus
  prefix=""
  prefix_1=""
  if u==0 or u==1:
    prefix='p'
    prefix_1='p'
  if u>3 or u<0:
    floor= u//3
    if floor==0:
      prefix= 'p'
      prefix_1= 'p'
    if floor==1:
      prefix= 'n'
      prefix_1='n'
    if floor== 2:
      prefix= 'µ'
      prefix_1= 'µ'
    if floor== 3:
      prefix= 'm'
      prefix_1= 'm'
    if floor==5:
      prefix= 'K'
      prefix_1= 'K'
    if floor==6:
      prefix= 'M'
      prefix_1= 'M'
    if floor==7:
      prefix= 'G'
      prefix_1='G'
    if floor==8:
      prefix= 'T'
      prefix_1='T'
    modulus= u%3

  if input_3=='A' or input_3=='a':
    minimum= 0.9995*value
    maximum= 1.0005*value
  if input_3=='B' or input_3=='b':
    minimum= 0.999*value
    maximum= 1.001*value
  if input_3=='C' or input_3=='c':
    minimum=0.9975*value
    maximum=1.0025*value
  if input_3=='D' or input_3=='d':
    minimum=0.005*value
    maximum=1.005*value
  if input_3=='F' or input_3=='f':
    minimum= 0.99*value
    maximum=1.01*value
  if input_3=='G' or input_3=='g':
    minimum=0.98*value
    maximum=1.02*value
  if input_3=='J' or input_3=='j':
    minimum=0.95*value
    maximum=1.05*value
  if input_3=='K' or input_3=='k':
    minimum=0.9*value
    maximum=1.1*value
  if input_3=='M' or input_3=='none' or input=='m':
    minimum=0.8*value
    maximum=1.2*value
  if input_3=='N' or input_3=='n':
    minimum= 0.7*value
    maximum=1.3*value
  if input_3=='Q' or input_3=='q':
    minimum=0.9*value
    maximum=1.3*value
  if input_3=='S' or input_3=='s':
    minimum=0.8*value
    maximum=1.5*value
  if input_3=='T' or input_3=='t':
    minimum=0.9*value
    maximum=1.5*value
  if input_3=='Z' or input_3=='z':
    minimum=0.8*value
    maximum=1.8*value
  elif value==1000 or minimum<=1000:
    minimum== minimum*1000
    value= value/1000
    maximum= maximum/1000
    if floor==0:
      prefix= 'p'
      prefix_1= 'f'
    if floor==1:
      prefix= 'n'
      prefix_1='p'
    if floor== 2:
      prefix= 'µ'
      prefix_1= 'n'
    if floor== 3:
      prefix= 'm'
      prefix_1= 'µ'
    if floor==5:
      prefix= 'K'
      prefix_1=""
    if floor==6:
      prefix= 'M'
      prefix_1= 'K'
    if floor==7:
      prefix= 'G'
      prefix_1='M'
    if floor==8:
      prefix= 'T'
      prefix_1='G'
  round_number= input("How many places would like to round your answers to?\n(you may hit enter or enter 'none' to not round)")
  if round_number==0 or round_number=="" or round_number=="none":
    round_min= minimum
    round_max= maximum
  else: 
    round_min= round(minimum, int(round_number))
    round_max= round(maximum, int(round_number))
  print(f"The digits you enterd are {input_1} and {input_2}, and the letter {input_3}")
  t=int(len(input("if these aren't the digits and symbols you wanted to enter \"redo\" else hit enter\n ")))
##Gives out final products
  if t==4:
    print('Restart...\n')
    t=t
  elif t!=4:
    print(f"\nHere is your capacitance:\n{value} {prefix}F\nmin= {round_min} {prefix_1}F\nmax= {round_max} {prefix}F")
    ask= len(input("\nWould you like to go again? (yes or no please)\n"))
    if ask==3:
      t=4
    if ask==2:
      t+=5
    elif ask!=2 and ask!=3:
      input("I\'m not sure what you saying there. Please re-enter \"yes\" or \"no\"")
