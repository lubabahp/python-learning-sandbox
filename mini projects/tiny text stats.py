# tiny text stats lol

def text_stats():
  words = ["inumaki", "toge", "salmon", "tuna tuna", "tuna mayo", "bonito flakes", "mustard leaf", "kelp", "cursed speech"]
  
  print("Here are the words: ")

  # for word in words:
  #   print(word)   # THIS MAKES SURE TO PRINT IT AS A NORMAL PRETTY LIST LOL but i won't actually include it in this function it's just for me to remember

  print(", ".join(words))   # another way to print out a list as a series of words separated by commas
  print(" ")

  stats = input("Do you want to view the list's stats? ")


  if stats == "Yes":
    print(f"Total number of words: {str(len(words))}")
    print(f"Longest word: {str(max(words))}")
    print(f"Shortest word: {str(min(words))}")
    print(f"No. of characters in the longest word: {str(len(max(words)))}")
    print(f"No. of characters in the shortest word: {str(len(max(words)))}")
  else:
    print("Alright.")

text_stats()
