#!/usr/bin/python
dict ={}

def questions():
 name=input("What is your name? ")
 if name =="Elijah":
  dict["Name"] = "Cool name"
  print(dict.get('Name'))
 else:
  dict["Name"]="You are lying"
  print(dict.get('Name'))
 age=int(input("How old are you? "))
 if age > 40:
  dict["Age"]="You are old"
  print(dict.get('Age'))
 else:
  dict["Age"]="You are young"
  print(dict.get('Age'))
 colour=input("What is your favourite colour? ")
 dict["Colour"]="Thats my favourite too!"
 print(dict.get('Colour'))
 python=input("Do you like Python? ")
 if python =="No":
  dict["Python"] = "You cannot be serious"
  print(dict.get('Python'))
 elif python =="Yes":
  dict["Python"] = "Me too!"
  print(dict.get('Python'))
 else:
  dict["Python"] = "Oooookay?"
  print(dict.get('Python'))
 earth=input("The world is flat: True or False? ")
 if earth=="True":
  dict["Earth"]="Crazy"
  print(dict.get('Earth'))
 if earth=="False":
  dict["Earth"]="That is true"
  print(dict.get('Earth'))

questions()
