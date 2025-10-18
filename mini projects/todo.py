# simple mini to-do list



def to_do_list(items = None):   
  # don't put items = [] in parameter otherwise it could behave funny when function is called (?)

  if items is None:
    items = []   
    # empty list

    end_list = ["stop", "done"]
    item = ""   
    # we must define "item" otherwise the loop won't work

    print("My to-do list: ")

    while True:   # makes the loops simpler more readable
      item = input("> ")
      if item.lower().strip() in end_list:
        break   
        # stops the loop
        
      else:
        items.append(item)
  return items  
  
  # ensures the users inputs goes back into the function so it's there when it's called          

all_items = to_do_list()  

# calling the function. unlike what i used to think, you don't put that at the end of every function for it to work. a function is literally created so that we don't need to keep rewriting code for actions that are repetitive (ig)


print("My to-do list:")
for item in all_items:
  print(item)

# this ensures to print it to look more like a human list than a python list


