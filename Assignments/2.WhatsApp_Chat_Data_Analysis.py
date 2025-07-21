chat= {}
n = int(input("Enter the number of chats: "))
for i in range(n):
    name,msg = input().split(":")
    if name in chat:
        chat[name].append((msg,i))
    else:
        chat[name] = [(msg,i)]
print(chat)
while True:
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("13. Identify the user with the longest average message length")
    print("14. Count how many messages mention a specific user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract all questions asked in the chat")
    print("18. Calculate the reply ratio between two users")
    print("19. Check for deleted messages")
    print("20. Exit")
    ch = int(input("Enter your Choice: "))
    if ch == 1:
        print("Total messages = ",n)
    elif ch == 2:
        print(set(chat.keys()))
    elif ch == 3:
        cc = 0
        for i in chat:
            for j in range (len(chat[i])):
                s = len((chat[i][j][0]).split())
                cc += s
        print(cc)
    elif ch == 4:
        cc = 0
        for i in chat:
            for j in range (len(chat[i])):
                s = len((chat[i][j][0]).split())
                cc += s
        print("Average words per message: %.2f" % (cc/n))
    elif ch == 5:
        cc = 0
        for i in chat:  
            for j in range (len(chat[i])): 
                s = len((chat[i][j][0]).split())
                if s > cc:
                    cc = s
        for i in chat:
            for j in range (len(chat[i])): 
                if cc == len((chat[i][j][0]).split()):
                    print(f"{i}: {chat[i][j][0]}")
                    break
            break
            
    elif ch == 20:
        break
