def box(word):
    length = len(word)
    print("#"*(length))
    print("#" +word + "#")

def low(word):
    print(word.lower())

def upper(word):
    print(word.upper())

def mirror(word):
    print(word, " | ", word[::-1])

def repeat(word):
    n = int(input("how many times should i repeat"))
    for i in range(n):
        if i % 2 == 0:
            upper(word)
        else:
            low(word)

repeat("cows can fly")

mirror("Hamburger")
mirror( "Connan the barbarian")


word ="this is sparta"
print(word[::-1])


box("Garry Lineker")
box("Drama")

def run():
    w = input("Enter a word")
    print("Chose an option"\n1-box):