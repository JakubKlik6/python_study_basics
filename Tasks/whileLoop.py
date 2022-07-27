#Task 1 Capital income
initialCapital  = 20000
percent  = 0.03
maxTimeYears = 10

for everyYear in range(1,11):
    moneyPerYear = initialCapital + (0.03 * initialCapital)
    initialCapital += (0.03 * initialCapital)
    print("In" ,everyYear, "You have", round(moneyPerYear))

print("\nAfter 10  years you have saved: ",round(moneyPerYear) - 20000)

print("\n////////////////////////////////")
#Task 2 sum of number

number = 20730906
divider = 0
sum = 0

while number > 0:
    divider = number % 10
    sum += divider
    number = number // 10

print(sum)


print("\n////////////////////////////////")
#Task 3 counting long and short words
quote = ("United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is tocreate Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier.")

wordLenght = 6
listOfWords = quote.split(" ")
shortWords = 0
longWords = 0

for word in listOfWords:
    if len(word) > wordLenght:
        longWords += 1
    else:
        shortWords += 1

print("Long words: ",longWords,"\n Short words: ", shortWords)
