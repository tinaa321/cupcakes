# Make something that asks the user to enter two words, 
# and prints 1000 of each with spaces in between. 
# For example, if the user enters hello and hi the
#  program would print hello hi hello hi hello hi 
#  hello hi hello hi ...

word = input("Enter something: ")
word2 = input("Enter something: ")
word = word+ " "+ word2+ " "
word*=69
print(word)