##Rudy Garcia

import time, sys
import math, sys

pos_tolerance_letters = ['a','b','c','d','f','g','j','k','m','none','n','q','s','t','z']
prefix_values = {0:'p',1:'n',2:'micro',3:'m',4:'',5:'K',6:'M',7:'G',8:'T',9:'P',10:'E'}
tolerance_values= {'a':0.0005,'b':0.001,'c':0.0025,'d':0.005,'f':0.01,'g':0.02,'j':0.05,'k':0.1,'m':0.2,'none':0.2,'n':0.3,'q':0.3,'q-':0.1,'s':0.5,'s-':0.2,'t':0.5,'t-':0.1,'z':0.8,'z-':0.2}
weird_tolerances = ['q','s','t','z']
print("Hi! I'm here to calculate capacitance and give you your variation :)\n")
time.sleep(3.5)
print("Make sure that your capacitor doesn't already tell you")
time.sleep(3)
print("If it has a prefix, most likely( p,f,n,µ,or m), then that is already your capacitance :)")
time.sleep(3.5)
initial= input("else hit any key to begin or type 'no' to quit:\n")

def correct_input(name_check, value):
    if name_check != "tolerance_letter":
      while correct_input == False:
        try: 
          value = int(value)
        except ValError:
          if name_check== 'first_digits':
            value = input("Sorry, I asked for 2 digits you silly!:\t")
          else:
            value = input("One digit, nothing else you buffoon!:\t")
    if name_check == "tolerance_letter":
      value= value.lower()
      while value not in pos_tolerance_letters:
        input("I need a correct letter for the tolerance:\t")
    return value

def calculation(first_digits, second_digit):
  first_digits= int(first_digits)
  second_digit= int(second_digit)
  non_prefixed_value= first_digit * (10**second_digit)
  return non_prefixed_value

def prefix_calculator(non_prefixed_value):
  count_prefixes = 0
  non_prefixed_value = int(non_prefixed_value)
  while non_prefixed_value >= 1000:
    non_prefixed_value= non_prefixed_value/1000
    count_prefixes += 1
  prefix = str(prefix_values[f"{count_prefixes}"])
  prefixed_value= non_prefixed_value
  final_nominal= f"{prefixed_value} {prefix}"
  return prefix, prefixed_value, final_nominal, count_prefixes, prefix

def tolerance(tolerance_letter, prefixed_number, prefix_count, prefix):
  lower_prefix = prefix
  upper_prefix = prefix
  prefixed_number= int(prefixed_number)
  prefix_count = int(prefix_count)
  if tolerance_letter not in weird_tolerances:
    variance= tolerance_values[f"{tolerance_letter}"] * prefixed_number
    lower = prefixed_number - variance
    upper = prefixed_number + variance
  if tolerance_letter in weird_tolerances:
    upper_variance = tolerance_values[f"{tolerance_letter}"] * prefixed_number
    lower_variance = tolerance_values[f"{tolerance_letter}-"] * prefixed_number
    lower = prefixed_number - lower_variance
    upper = prefixed_number + upper_variance
  if lower <= 1:
      lower= lower * 1000
      lower_prefix_count = prefix_count -1
      lower_prefix = prefix_values[f"{lower_prefix_count"]
  if upper > 1000:
    upper = upper/1000
    upper_prefix_count= prefix_count + 1
    upper_prefix = prefix_values[f"{upper_prefix_count}"]
  return upper, lower, upper_prefix, lower_prefix


##asks for user inputs to get original values and error checks them
first_digits= input("What are your first two digits on the capacitor?:\t")
first_digits= correct_inputs('first_digits',first_digits)
second_digit= input("\nWhat is the 3rd digit m8:\n")
second_digit = correct_inputs('second_digit',first_digit)
tolerance_letter = input("What is the letter at the end of the capacitance:\t")
tolerance_letter= correct_inputs('tolerance_letter',tolerance_letter)
non_prefixed_value = calculations(first_digits,second_digit)
prefix, prefixed_value, final_nominal, prefix_count, prefix = prefix_calculator(non_prefixed_value)
upper, lower, upper_prefix, lower_prefix = tolerance(tolerance_letter, prefixed_number, prefix_count,prefix)



print(f"The digits you enterd are {input_1} and {input_2}, and the letter {input_3}, and you are rounding to {int(round_number)} decimal places")
  t=int(len(input("if these aren't the digits and symbols you wanted, enter \"redo\"else hit enter\n ")))
##Gives out final products
  if t==4:
    print('Restart...\n')
    t=t
  elif t!=4:
    print(f"\nHere is your capacitance with a tolerance of {tolerance}:\nCapacitance: {value} {prefix}F \nmin= {round_min} {prefix_1}F\nmax= {round_max} {prefix}F\n\nderp ☉ ‿ ⚆")
##restarts the loop if the user wants to go again
    ask= input("\nWould you like to go again? (yes or no please)\n")
    if ask=='yes' or ask=='Yes':
      t=4
    elif ask!='no' and ask!='yes'and ask!="No" and ask!='Yes':
      input("I\'m not sure what you saying there. Please re-enter \"yes\" or \"no\"")
##end message, and checks to be sure user wants to leave
    if ask=='no':
      print("I hope this program served you well!\nThank you for using.\nderp ☉ ‿ ⚆")
      d= input("Press enter to exit (any other button will let you redo the program")
      if d=="" :
        t+=5
      print("It's party time: \n\n.( ´･･)ﾉ(._.`)   (╯°□°）╯︵ ┻━┻(ˉ﹃ˉ)   \n༼ つ ◕_◕ ༽つ(⌐■_■)(•_•)   (¬‿¬)(¬_¬ )(☞ﾟヮﾟ)☞☜(ﾟヮﾟ☜)   \n^_____^   q(≧▽≦q)[]~(￣▽￣)~*\n(✿◡‿◡)φ(゜▽゜*)♪o(*^＠^*)o  O(∩_∩)O  \n(づ￣ 3￣)づ\(￣︶￣*\))\n(* ￣3)(ε￣ *)(｡･∀･)ﾉﾞヾ(•ω•`)   \no◑﹏◐＼（〇_ｏ）／\n\n for all the chicky babes out there\n and the party words like 'angular velocity'\n (said with a deep emphasis on 'velocity'\n:) \nGoodbye Comrade!")
      if d!="":
        t=4
if initial=='no' and ask!='no' or initial=='No' and ask!='no': 
  print("I hope this program served you well!\nThank you for using.\nderp ☉ ‿ ⚆")
  g= input("Press enter to continue (any other button will have you exit the program")
  if g=="" :
    print("It's party time: \n\n.( ´･･)ﾉ(._.`)   (╯°□°）╯︵ ┻━┻(ˉ﹃ˉ)   \n༼ つ ◕_◕ ༽つ(⌐■_■)(•_•)   (¬‿¬)(¬_¬ )(☞ﾟヮﾟ)☞☜(ﾟヮﾟ☜)   \n^_____^   q(≧▽≦q)[]~(￣▽￣)~*\n(✿◡‿◡)φ(゜▽゜*)♪o(*^＠^*)o  O(∩_∩)O  \n(づ￣ 3￣)づ\(￣︶￣*\))\n(* ￣3)(ε￣ *)(｡･∀･)ﾉﾞヾ(•ω•`)   \no◑﹏◐＼（〇_ｏ）／\n\n for all the chicky babes out there\n and the party words like 'angular velocity'\n (said with a deep emphasis on 'velocity'\n:) \nGoodbye Comrade!")
    
        
