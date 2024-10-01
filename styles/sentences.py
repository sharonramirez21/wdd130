import random

def get_determiner(quantity):
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

def get_noun(quantity):
   if quantity == 1:
      noun = ["bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"]
   else: 
      noun =  ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]
   nouns = random.choice(noun)
   return nouns

def get_verb(quantity, tense):
   if tense == "past":
      verbs = ["drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"]
    
   if tense == "present" and quantity == 1:
      verbs =  ["drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"]
         
   if tense == "present" and quantity != 1:
      verbs =  ["drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write" ]
   
   if tense == "future":
      verbs = ["will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
      
   verb = random.choice(verbs)
   return verb

def make_sentence(quantity, tense):
   determiner = get_determiner(quantity)
   noun = get_noun(quantity)
   verb = get_verb(quantity, tense)
   sentence = f"{determiner.capitalize()} {noun} {verb}"
   return sentence


def main():
   quantity = [1, 1, 1, 2, 2, 2]
   tense = ["past", "present", "future", "past", "present", "future"]

   for quantity, tense in zip(quantity, tense):
      sentences =  make_sentence(quantity, tense)
      print(sentences)

main()