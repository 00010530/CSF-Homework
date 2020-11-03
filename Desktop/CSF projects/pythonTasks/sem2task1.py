#1
def fav_fruit(fruit):
    name = input("Your name: ")
    print(name + " loves " + fruit)

fav_fruit("orange")

#name - parameter
#arashi - argument


#2
fav_fruit("orange") #value
favFruit = "kiwi"
fav_fruit(favFruit) #variable
fav_fruit("All " + "fruits") #expression


#3
def favShow():
    TVShow = "My favorite show is Japanese show, Himitsu no Arashi chan"
    print(TVShow)

favShow()
print(TVShow)
#the interpreter can only read the variable "TVShow" when executing the function "favShow"



#4
def add(number1, number2):
    sum = number1 + number2
    print(sum)

add(45, 65)
print(number1)
#the interpreter can only read the parameter "number1" and "number2" when executing the function "add"



#5
def translate():
    arashi = "storm"
    print(arashi)

arashi = "boy band"
print(arashi)
translate()
#the variables do not affect each other


