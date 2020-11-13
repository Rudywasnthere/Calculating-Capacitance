##Rudy Garcia

import time, sys
import math, sys
x= 0

##reference dictionaries
pos_tolerance_letters = ['a','b','c','d','f','g','j','k','m','none',"",'n','q','s','t','z']
prefix_values = {0:'p',1:'n',2:'micro',3:'m',4:'',5:'K',6:'M',7:'G',8:'T',9:'P',10:'E'}
tolerance_values= {'a':0.0005,'b':0.001,'c':0.0025,'d':0.005,'f':0.01,'g':0.02,'j':0.05,'k':0.1,'m':0.2,'none':0.2,'':0.2,'n':0.3,'q':0.3,'q-':0.1,'s':0.5,'s-':0.2,'t':0.5,'t-':0.1,'z':0.8,'z-':0.2}
weird_tolerances = ['q','s','t','z']
print("Hi! I'm here to calculate capacitance and give you your variation :)\n")
time.sleep(3*x)
print("Make sure that your capacitor doesn't already tell you")
time.sleep(3*x)
print("If it has a prefix, most likely( p,f,n,µ,or m), then that is already your capacitance :)")
time.sleep(2*x)
print("To start, I need some inputs")

##asigns correct user inputs
def correct_input(name_check, value):
  true= False
  if name_check != "tolerance_letter":
      if name_check== 'first_digits':
        while true != True:
          r= range(10,100)
          try:
            value= int(value)
            if value in r:
              true = True
            else:
              value= input("I need a number in [10,100):\t")
              true = False
          except ValueError:
            value = input("Sorry, I asked for 2 digits you silly!:\t")
            true = False
      else:
        while true != True:
          r= range(1,10)
          try:
            value= int(value)
            if value in r:
              true = True
            else:
              value= input("It needs to be a number in [1,10):\t")
              true = False
          except ValueError:
            value = input("One digit, nothing else you buffoon!:\t")
            true = False
  if name_check == "tolerance_letter":
      value= value.lower()
      while value not in pos_tolerance_letters:
        input("I need a correct letter for the tolerance:\t")
  return value

##calculates nominal value
def calculation(first_digits, second_digit):
  first_digits= int(first_digits)
  second_digit= int(second_digit)
  non_prefixed_value= first_digits * (10**second_digit)
  return non_prefixed_value

##finds the needed prefixes
def prefix_calculator(non_prefixed_value):
  count_prefixes = 0
  non_prefixed_value = int(non_prefixed_value)
  while non_prefixed_value >= 1000:
    non_prefixed_value= non_prefixed_value/1000
    count_prefixes += 1
  prefix = prefix_values[count_prefixes]
  prefixed_value= non_prefixed_value
  final_nominal= f"{prefixed_value} {prefix}"
  return prefix, prefixed_value, final_nominal, count_prefixes, prefix

## finds the upper and lower limits for tolerance and changes their prefixes if necessary
def tolerance(tolerance_letter, prefixed_number, prefix_count, prefix):
  lower_prefix = prefix
  upper_prefix = prefix
  prefixed_number= int(prefixed_number)
  prefix_count = int(prefix_count)
  if tolerance_letter not in weird_tolerances:
    variance= tolerance_values[tolerance_letter] * prefixed_number
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
      lower_prefix = prefix_values[lower_prefix_count]
  if upper > 1000:
    upper = upper/1000
    upper_prefix_count= prefix_count + 1
    upper_prefix = prefix_values[upper_prefix_count]
  return upper, lower, upper_prefix, lower_prefix

##rounds the final outputs according to the user's desires
def round_outputs(lower, upper, non_prefixed_number):
  length_lower = len(str(non_prefixed_number))
  f= False
  round_places= input("how many places would you like to round to? \n(hit enter for no rounding):\t ")
  if round_places=="":
      final_number= non_prefixed_number
      final_lower= round(lower,5)
      final_upper= round(upper,5)
      round_places= "no"
  else: 
    while f == False:
      try: 
        int(round_places)
        round_places= int(round_places)
        f= True
      except ValueError:
        print('Value Error')
        round_places= input("Please input an integer: ")
        f= False
    if round_places >0 :
      round_places= int(round_places)
      round_place= int(round_places + length_lower)
      final_number= round(non_prefixed_number,round_place)
      final_lower= round(lower,round_place)
      final_upper= round(upper,round_place)
  return final_number, final_lower, final_upper, round_places

##formats the final output
def final_output(final_number, non_prefixed_number, final_lower, final_upper, lower_prefix, upper_prefix, prefix):   
    return f"___________________________________________________\nnominal value =  {final_number} {prefix} Ohms\nminimum =        {final_lower} {lower_prefix} Ohms\nmaximum =        {final_upper} {upper_prefix} Ohms\n____________________________________________________"

## runs the whole thing
def main():
  restart=""
  while restart=="":
    first_digits= input("\nWhat are your first two digits on the capacitor?:\t")
    first_digits= correct_input('first_digits',first_digits)
    second_digit= input("What is the 3rd digit:\t")
    second_digit = correct_input('second_digit',second_digit)
    tolerance_letter = input("What is the letter at the end of the capacitance:\t")
    tolerance_letter= correct_input('tolerance_letter',tolerance_letter)
    non_prefixed_value = calculation(first_digits,second_digit)
    prefix, prefixed_value, final_nominal, prefix_count, prefix = prefix_calculator(non_prefixed_value)
    upper, lower, upper_prefix, lower_prefix = tolerance(tolerance_letter, prefixed_value, prefix_count,prefix)
    final_number, final_lower, final_upper, round_places = round_outputs(lower, upper, non_prefixed_value)
    ## final outputs
    print(f"The digits you enterd are {first_digits} and {second_digit}, and the letter {tolerance_letter}, and you are rounding to {round_places} decimal places")
    print(final_output(prefixed_value, non_prefixed_value, final_lower, final_upper, lower_prefix, upper_prefix, prefix))

    restart= input("Hit enter to restart, or press any key to exit\t")
  print("I hope this program served you well!\nThank you for using.\nderp ☉ ‿ ⚆")
  ask= input("Would you like something extra?: ")
  if ask!= 'no' and ask !="No":
    print("It's party time: \n\n.( ´･･)ﾉ(._.`)   (╯°□°）╯︵ ┻━┻(ˉ﹃ˉ)   \n༼ つ ◕_◕ ༽つ(⌐■_■)(•_•)   (¬‿¬)(¬_¬ )(☞ﾟヮﾟ)☞☜(ﾟヮﾟ☜)   \n^_____^   q(≧▽≦q)[]~(￣▽￣)~*\n(✿◡‿◡)φ(゜▽゜*)♪o(*^＠^*)o  O(∩_∩)O  \n(づ￣ 3￣)づ\(￣︶￣*\))\n(* ￣3)(ε￣ *)(｡･∀･)ﾉﾞヾ(•ω•`)   \no◑﹏◐＼（〇_ｏ）／\n\n for all the chicky babes out there\n and the party words like 'angular velocity'\n (said with a deep emphasis on 'velocity'\n:) \nGoodbye Comrade!")

main()