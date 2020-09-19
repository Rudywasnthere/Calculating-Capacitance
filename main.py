##Rudy Garcia
import time, time
import math, math
print("Hi! I'm here to calculate capacitance and give you your variation :)\n")
time.sleep(2)
t=1
print("Make sure that your capacitor doesn't already tell you")
time.sleep(2.5)
print("If it has a prefix, most likely( p,f,n,µ,or m), then that is already your capacitance :)")
time.sleep(2.5)
initial= input("else hit any key to begin or type 'no' to quit:\n")
if initial =='no':
  t=5
  ask=2
else: 
  t=1
while 0<t<=4:
##asks for user inputs to get original values and error checks them
  input_1= input("\nWhat are the first 2 digits of your capacitor:\n")
  if len(input_1)!=2: 
    if len(input_1) !=2 and math.ceil(float(input_1)+0.01)>1:
      print("\nSorry, I asked for 2 digits you silly!")
    if math.ceil(float(input_1))<=1:
      print("It has to be a whole number from [10,100) you pea-brain!")
    input_1= int(input("Try to get it right this time, What are the first 2 digits?\n"))
  input_2= input("\nWhat is the 3rd digit m8:\n")
  if len(input_2)!=1:
      print("\nOne digit, nothing else you goof")
      input_2= input("Actually read the instructions, what is the 3rd digit and only the 3rd digit of your capacitor?\n")
  input_3= input("What is the letter at the end of your capacitor (after the digits)?\n")
  set_input3= ['a','A','b','B','c','C','d','D','f','F','g','G','j','J','k','K','m','M','none','n','N','q','Q','s','S','t','T','z','Z']
  if input_3 not in set_input3:
    print(f"m8, I said a letter, it has to be a valid one that's on capacitors, it\'s only one")
    input_3=input("What is the letter again...\n")
##Its calculation time
  x= int(input_1)
  u= int(input_2)
  modulus= u%3
  floor= (u)//3
  if modulus==2:
    value= x* 10**(modulus +1)
  else:
    value= x* 10**modulus
  prefix=""
  prefix_1=""
##sets outputs for the end, probably too long and could be optimized
  if input_3=='A' or input_3=='a':
    minimum= 0.9995*value
    maximum= 1.0005*value
    tolerance= '±0.05%'
  if input_3=='B' or input_3=='b':
    minimum= 0.999*value
    maximum= 1.001*value
    tolerance= '±0.1%'
  if input_3=='C' or input_3=='c':
    minimum=0.9975*value
    maximum=1.0025*value
    tolerance= '±0.25%'
  if input_3=='D' or input_3=='d':
    minimum=0.005*value
    maximum=1.005*value
    tolerance= '±0.5%'
  if input_3=='F' or input_3=='f':
    minimum= 0.99*value
    maximum=1.01*value
    tolerance= '± 1%'
  if input_3=='G' or input_3=='g':
    minimum=0.98*value
    maximum=1.02*value
    tolerance= '± 2%'
  if input_3=='J' or input_3=='j':
    minimum=0.95*value
    maximum=1.05*value
    tolerance= '± 5%'
  if input_3=='K' or input_3=='k':
    minimum=0.9*value
    maximum=1.1*value
    tolerance= '± 10%'
  if input_3=='M' or input_3=='none' or input=='m':
    minimum=0.8*value
    maximum=1.2*value
    tolerance= '± 20%'
  if input_3=='N' or input_3=='n':
    minimum= 0.7*value
    maximum=1.3*value
    tolerance= '± 30%'
  if input_3=='Q' or input_3=='q':
    minimum=0.9*value
    maximum=1.3*value
    tolerance= '-10%, +30%'
  if input_3=='S' or input_3=='s':
    minimum=0.8*value
    maximum=1.5*value
    tolerance= '-20%, +50%'
  if input_3=='T' or input_3=='t':
    minimum=0.9*value
    maximum=1.5*value
    tolerance= '-10%, +50%'
  if input_3=='Z' or input_3=='z':
    minimum=0.8*value
    maximum=1.8*value
    tolerance= '-20%, +80%'
  if u==0 or u==1:
    prefix='p'
    prefix_1='p'
  if modulus==1:
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
  if modulus==2 and x!=10:
    value= value/10000
    minimum= minimum/10000
    maximum= maximum/10000
    floor = floor +1
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
  if modulus==2 and x==10:
    value=value/10
    minimum= minimum/10
    maximum= maximum/10
    floor= floor +1
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
  
  if u==3:
    prefix='n'
    prefix_1='n'
  if modulus==0:
    value= value
    minimum= minimum
    maximum= maximum
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


  if value==1000 or minimum<=1:
    minimum== minimum*1000
    value= value/1000
    maximum= maximum/1000
    if u==2:
      prefix='p'
      prefix_1='p'
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
##prompts user for how their outputs should be formatted
  round_number= input("How many places would like to round your answers to?\n(you may hit enter or enter 'none' to not round)\n")
##figures out how to round based  on outputs
  if round_number=="" or round_number=="none":
    round_min= minimum
    round_max= maximum
    print(f"The digits you enterd are {input_1} and {input_2}, and the letter {input_3}, and you\ndidn't round your answers")
  else: 
    if 1<=value<10:
      round_min= round(minimum, int(round_number)+1)
      round_max= round(maximum, int(round_number)+1)
    if 10<=value<100:
      round_min= round(minimum, int(round_number)+2)
      round_max= round(maximum, int(round_number)+2)
    if 100<=value<1000:
      round_min= round(minimum, int(round_number)+3)
      round_max= round(maximum, int(round_number)+3)
##verfies what the user wants for outputs
    print(f"The digits you enterd are {input_1} and {input_2}, and the letter {input_3}, and you are rounding to {int(round_number)} decimal places")
  t=int(len(input("if these aren't the digits and symbols you wanted, enter \"redo\"else hit enter\n ")))
##Gives out final products
  if t==4:
    print('Restart...\n')
    t=t
  elif t!=4:
    print(f"\nHere is your capacitance with a tolerance of {tolerance}:\n{value} {prefix}F \nmin= {round_min} {prefix_1}F\nmax= {round_max} {prefix}F\n\nderp ☉ ‿ ⚆")
##restarts the loop if the user wants to go again
    ask= len(input("\nWould you like to go again? (yes or no please)\n"))
    if ask==3:
      t=4
    elif ask!=2 and ask!=3:
      input("I\'m not sure what you saying there. Please re-enter \"yes\" or \"no\"")
##end message, and checks to be sure user wants to leave

if ask==2:
      print("I hope this program served you well!\nThank you for using.\nderp ☉ ‿ ⚆")
      d= input("Press enter to exit (any other button will let you redo the program")
      if d=="" :
        t+=5
      print("⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿ ⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿ ⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿ ⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿ ⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿ ⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿ ⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿")
      if d!="":
        t=4

