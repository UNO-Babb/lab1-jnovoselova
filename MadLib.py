#MadLib.py
#Name:Jennifer Novoselova
#Date:08/30/2024
#Assignment:Lab 1

 
def main():
  print("madlib")
  #Ask user for words
  adj1 = input("adjective: ")
  name1 = input("name: ")
  subject1 = input ("subject: ")
  adj2 = input("adjective: ")
  verb1 = input("verb: ")
  noun1 = input ("noun: ")
  place1 = input ("place: ")
  food1 = input ("food: ")
  beverage1 = input ("beverage: ")
  sport1 = input ("sport: ")
  emotion1 = input ("emotion: ")
  adj3 = input ("adjective: ")
  animal1 = input ("animal: ")
  adj4 = input ("adjective: ")
  adj5 = input ("adjective: ")
  
  #Print the story with the user supplied words.
  madlib = ("One day, my friend and I decided to have an" + adj1 + "day at school. First we went to " + name1 + " class, where we learned about " + subject1 + 
  "The teacher gave us a " + subject1 + " assignment, which involved " + verb1 + " with " + noun1 +
  " After that, we had lunch in the " + place1 + ", where we ate " + food1 + " and drank " +beverage1 + 
  " In the afternoon, we had gym class and played a game of " + sport1 + " . I was really " + emotion1 + " because I scored a " + adj3 +
  " goal! Finally, we went to the library to read a book about " + animal1 + ", which was very " + adj4 + ". It was a " + adj5 + 
  " day at school! ")

  print(madlib)



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
