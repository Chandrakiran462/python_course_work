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
    print("12. Identify the user with the longest average message length")
    print("13. Count how many messages mention a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions asked in the chat")
    print("17. Calculate the reply ratio between two users")
    print("18. Check for deleted messages")
    print("19. Exit")
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
        frq = {}
        messages = []
        for i in chat:  
            for j in range (len(chat[i])): 
                s = (chat[i][j][0]).split()
                for k in s:
                    messages.append(k)
        for i in messages:
            if i not in frq:
                frq[i] = messages.count(i)
        for i in frq:
            if frq[i] == max(frq.values()):
                res.add(i)
        print(res)
    elif ch == 12:
        # User with longest average message length in words
        longest_avg = 0
        user_longest_avg = None
        for user in chat:
            total_words = sum(len(msg.split()) for msg, _ in chat[user])
            count_msgs = len(chat[user])
            avg_len = total_words / count_msgs if count_msgs > 0 else 0
            if avg_len > longest_avg:
                longest_avg = avg_len
                user_longest_avg = user
        if user_longest_avg:
            print(f"User with longest average message: {user_longest_avg} (avg {longest_avg:.1f} words)")
        else:
            print("No messages found.")

    elif ch == 13:
        user = input("Enter user name: ").strip()
        count = 0
        for u in chat:
            for msg, _ in chat[u]:
                # case insensitive match
                if user.lower() in msg.lower():
                    count += 1
        print(f"Messages mentioning '{user}': {count}")

    elif ch == 14:
        unique_msgs = set()
        for user in chat:
            for msg, _ in chat[user]:
                unique_msgs.add(f"{user}: {msg}")
        print(f"Unique messages count: {len(unique_msgs)}")
        print("Unique messages:")
        for m in sorted(unique_msgs):
            print(m)

    elif ch == 15:
        all_msgs = []
        for user in chat:
            for msg, _ in chat[user]:
                all_msgs.append(f"{user}: {msg}")
        all_msgs.sort(key=str.lower)
        print("Messages sorted alphabetically:")
        for m in all_msgs:
            print(m)

    elif ch == 16:
        questions = []
        for user in chat:
            for msg, _ in chat[user]:
                if "?" in msg and msg.strip().endswith("?"):
                    questions.append(f"{user}: {msg}")
        if questions:
            print("Questions asked in the chat:")
            for q in questions:
                print(q)
        else:
            print("No questions found in the chat.")

    elif ch == 17:
        user1 = input("Enter first user name: ").strip()
        user2 = input("Enter second user name: ").strip()
        # Reply ratio from user2 to user1 counts how many messages by user2 mentioning user1
        if user1 in chat and user2 in chat:
            replies = 0
            for msg, _ in chat[user2]:
                if user1.lower() in msg.lower():
                    replies += 1
            print(f"Reply ratio from {user2} to {user1}: {replies} replies")
        else:
            print("One or both users not found in chat.")

    elif ch == 18:
        count_deleted = 0
        for user in chat:
            for msg, _ in chat[user]:
                if msg == "This message was deleted":
                    count_deleted += 1
        print(f"Deleted messages found: {count_deleted}")

    elif ch == 19:
        break
