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
        res = set()
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



'''
Enter the number of chats: 6
kiran: Hii Shanmukh
shanmukh: Hii kiran. How are you?
kiran: I am good. How are you?
shanmukh: I am also good. so, what are you doing here?
kiran: I came to watch movie.
shanmukh: ok enjoy your movie. Bye
{'kiran': [(' Hii Shanmukh', 0), (' I am good. How are you?', 2), (' I came to watch movie.', 4)], 'shanmukh': [(' Hii kiran. How are you?', 1), (' I am also good. so, what are you doing here?', 3), (' ok enjoy your movie. Bye', 5)]}
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 1
Total messages =  6
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 2
{'kiran', 'shanmukh'}
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 3
33
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 4
Average words per message: 5.50
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 5
shanmukh:  I am also good. so, what are you doing here?
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 6
Most active user: kiran (3 messages)
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 7
Enter user name: kiran
message sent by kiran: 3
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 8
Enter user name: shanmukh
Hii
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 9
Enter user name: kiran
First message by kiran: 'kiran:  Hii Shanmukh'
last message by kiran: 'kiran:  I came to watch movie.'
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 10
Enter user name: shanmukh
user shanmukh found in chat
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 11
{'I', 'are'}
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 12                 
User with longest average message: shanmukh (avg 6.7 words)
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 13
Enter user name: kiran
Messages mentioning 'kiran': 1
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 14
Unique messages count: 6
Unique messages:
kiran:  Hii Shanmukh
kiran:  I am good. How are you?
kiran:  I came to watch movie.
shanmukh:  Hii kiran. How are you?
shanmukh:  I am also good. so, what are you doing here?
shanmukh:  ok enjoy your movie. Bye
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 15
Messages sorted alphabetically:
kiran:  Hii Shanmukh
kiran:  I am good. How are you?
kiran:  I came to watch movie.
shanmukh:  Hii kiran. How are you?
shanmukh:  I am also good. so, what are you doing here?
shanmukh:  ok enjoy your movie. Bye
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 16
Questions asked in the chat:
kiran:  I am good. How are you?
shanmukh:  Hii kiran. How are you?
shanmukh:  I am also good. so, what are you doing here?
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 17
Enter first user name: kiran
Enter second user name: shanmukh
Reply ratio from shanmukh to kiran: 1 replies
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 18
Deleted messages found: 0
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
19. Exit
Enter your Choice: 19
'''