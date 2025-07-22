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
    elif ch == 6:
        long_msg = []
        for i in chat:
            long_msg.append(len(chat[i]))
        for i in chat:
            if max(long_msg) == len(chat[i]):
                print(f"Most active user: {i} ({len(chat[i])} messages)")
                break 
    elif ch == 7:
        user = input("Enter user name: ")
        if user in chat:
            print(f'message sent by {user}: {len(chat[user])}')
        else:
            print("User Not Found")
    elif ch == 8:
        user = input("Enter user name: ")
        frq = {}
        if user in chat:  
            for i in range (len(chat[user])): 
                s = (chat[user][i][0]).split()
                for j in s:
                    if j not in frq:
                        frq[j] = s.count(j)
            print(max(frq, key=frq.get))   
        else:
            print("User Not Found") 
    elif ch == 9:
        user = input("Enter user name: ")
        if user in chat:
            for i in range (len(chat[user])): 
                if i == 0:
                    print(f"First message by {user}: '{user}: {chat[user][i][0]}'")
                if i == len(chat[user]) - 1 :
                    print(f"last message by {user}: '{user}: {chat[user][i][0]}'")
        else:
            print("User Not Found")
    elif ch == 10:
        user = input("Enter user name: ")
        if user in chat:
            print(f"user {user} found in chat")
        else:
            print(f"user {user} not found in chat")
    elif ch == 11:
        pass
    elif ch == 20:
        break
