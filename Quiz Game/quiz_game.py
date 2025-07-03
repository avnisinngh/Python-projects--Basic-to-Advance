print("Welcome to my Accronyms Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Okayy! Let's play :)")
score = 0

print('Question 1: ')
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else: 
    print('Wrong!')

print('Question 2: ')
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else: 
    print('Wrong!')

print('Question 3: ')
answer = input("What does RAM stand for? ").lower()
if answer == "random access memeory":
    print('Correct!')
    score += 1
else: 
    print('Wrong!')

print('Question 4: ')
answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print('Correct!')
    score += 1
else: 
    print('Wrong!')


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4)*100) + "%.")
