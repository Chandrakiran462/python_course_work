def question(s):
    for i in s:
        yield s[i]

print("🧪 Welcome to the Python Quiz Game!")
score = 0
questions = {
    'que1':'Question 1: Which of the following is an ordered and mutable data type in Python?\na) Tuple\nb) Set\nc) List\nd) String',
    'que2':'Question 2: Which operator is used to check for value equality between two variables?\na) =\nb) ==\nc) is\nd) :=',
    'que3':'Question 3: What does the term “immutable” mean with respect to Python strings?\na) Strings can be changed after creation\nb) Strings cannot be changed after creation\nc) Strings are always empty\nd) Strings allow duplicate values',
    'que4':'Question 4: Which method adds a single element to the end of a Python list?\na) append()\nb) insert()\nc) add()\nd) push()',
    'que5':'Question 5: What is the main difference between a list and a tuple in Python?\na) Tuples are mutable, lists are immutable\nb) Tuples are immutable, lists are mutable\nc) Both are mutable\nd) Both are immutable',
    'que6':'Question 6: How are elements in a Python dictionary accessed?\na) By their index\nb) By their key\nc) Sequentially\nd) Alphabetically',
    'que7':'Question 7: Which of the following is NOT a property of Python sets?\na) Unordered\nb) Mutable\nc) Allow duplicate elements\nd) Can only contain immutable elements',
    'que8':'Question 8: What is the process of changing one data type into another called?\na) Transformation\nb) Conversion\nc) Coercion\nd) All of the above',
    'que9':'Question 9: Which structure is used for decision making in Python?\na) for loop\nb) if statement\nc) function definition\nd) import statement',
    'que10':'Question 10: Which term refers to a function that calls itself during its own execution?\na) Lambda function\nb) Recursive function\nc) Iterative function\nd) Anonymous function',
}
# question(questions)
next_que = question(questions)
for i in questions:
    if i == 'que1':
        print(next(next_que))
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'c':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que2':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'b':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que3':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'b':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que4':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'a':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que5':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'b':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que6':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'b':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que7':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'c':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que8':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'd':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que9':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'b':
            score +=1
            print('✅ Correct!')
            print(next(next_que))
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            print(next(next_que))
    if i == 'que10':
        ans = input("Your answer (a/b/c/d): ")
        if ans == 'b':
            score +=1
            print('✅ Correct!')
            break
        else:
            print("❌ Wrong! The correct answer is 'c'" )
            break


print(f"🎯 Your Final Score: {score}/10")
print("🎉 Great job! Keep practicing!")

