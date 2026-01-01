# characters and ages.py
# not sure if this is a mini project or an experiment, but i just committed it to mini projects since it's a little bit more structured. 
# i learnt and metabolised truly for arguments vs parameters and how they work for functions. 

jjk_characters = {
    "megumi":15, "nobara":16, "gojo":28, "inumaki":17, "yuji":15, "sukuna":">1000"
  }

drst_characters = {
  "suika":9, "kohaku":16, "gen":19
}  



def characters(characters):
  for character in characters:
    print(character)

    # FINALLY I KNOW HOW TO PRINT LISTS CLEANLY INSTEAD OF THE UGLY SQUARE BRACKETS LIKE IT WOULD WITH print(list_name_here) EEEE


def characters_and_ages():
  for name, age in jjk_characters.items():    # .items() probably idk turns the key value pair into a tuple or some shi so that both the key and value print
    print(name, age)
# that only works for jjk characters alone



def characters_and_age(char_name_age):
  for name, age in char_name_age.items():   # yh u need .items() here otherwise the too many value to unpack error comes here. still dont rly get why.
    print(name, age)


# this just shows how parameters and functions work essentially when functions use them and when they dont


def ages():
  for age in jjk_characters.values():    # i assume .values() basically takes, uh, values in key values pair from dicts
    print(age)


def something_else_i_just_wanna_test():
  print("""so like if i use this
  three speech marks
 
  i can write whole ahh formatted paragraphs
 
  and print them?
 
 
  that is
 
 
  baddd like chrome would say dr stone lol""")




characters_and_age(jjk_characters)
print()
characters_and_age(drst_characters)
print()
characters(jjk_characters)     # so that basically means you can print any character dict say if i defined another dict with another set of characters in a different show. basically when i call the function i can choose what variable to use it for OH. OH. THAT IS IT?
print()   # line breaks are now cleaner than print(" ") bs
characters(drst_characters)
print()
something_else_i_just_wanna_test()  




# parameters live in the function, arguments visit it when the function is called
# def greet(name):   # <- parameter
    # print("hi", name)

# greet("lubabah")   # <- argument


# why do some functions never have arguments passed through them and what do we even use arguments for WHATS THE POINT and parameter like whaaa

# okay but my newer from-scratch scripts are cooking though, multiple functions wdym dev lubabah when she gets hired and paid will cook
# TIL that i don't need to take notes and comments on python scripts like it's academic
