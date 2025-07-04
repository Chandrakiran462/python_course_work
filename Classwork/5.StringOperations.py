
# Operations on Strings
fname = 'Chandra'
lname = 'Kiran'
print(fname + lname)            # ChandraKiran ["Concatenation (+): "]
print(lname*5)                  # KiranKiranKiranKiranKiran ["Repetition (*): "]
s = 'Chandra Kiran'
print(s[5])                     # r ["Indexing: "]
print(s[-4])                    # i ["-ve Indexing: "]
print(s[0:7])                   # Chandra ["Slicing: "]
print(s[8:12])                  # Kira ["Slicing: "]
print(s[0:12:2])                # CadaKr ["Slicing: "]
print(s[1:12:2])                # hnr ia ["Slicing: "]
print(s[:-5])                   # Chandra ["-ve Slicing: "]
print(s[-6:])                   #  Kiran ["-ve Slicing: "]
print(s[::-1])                  # nariK ardnahC ["-ve Slicing: "]
print('Kiran' in s)             # True ["Membership operation: "]
print('Chandra' in s)           # False ["Membership operation: "]
print('chandu' not in s)        # True ["Membership operation: "]

# Built-in String Functions
print(len(s))                   # 13 ["length of the string: "]
print(max(s))                   # r ["maximum character (based on ASCII values): "]
print(min(s))                   # ' ' ["character (based on ASCII values): "]
print(sorted(s))                #  [' ', 'C', 'K', 'a', 'a', 'a', 'd', 'h', 'i', 'n', 'n', 'r', 'r'] "a sorted list of characters: "
print(ord('K'))                 # 75 ["Converts character to ASCII value: ",]
print(chr(64))                  # @ ["Converts ASCII value to character"]


# Complete List of Python String Methods with Examples

# 1. Case Conversion Methods
print(s.upper())                # CHANDRA KIRAN ["Converts all characters to uppercase: ",]
print(s.lower())                # chandra kiran ["Converts all characters to lowercase: "]
k = 'sri sai chandra kiran'
print(k.capitalize())           # Sri sai chandra kiran ["Capitalizes the first character: "]
print(k.title())                # Sri Sai Chandra Kiran ["Capitalizes the first letter of each word: "]
print(s.swapcase())             # cHANDRA kIRAN ["Swaps case: upper → lower, lower → upper: ",]
print("ß".casefold())           # ss

# 2. Alignment & Formatting Methods

print(s.center(40,'*'))         # *************Chandra Kiran************** ["Centers the String within the Width: "]
print(s.ljust(25,"-"))          # Chandra Kiran------------ ["Left-align the String within the Width: "]
print(s.rjust(25,"_"))          # ____________Chandra Kiran ["Rignt-align the String within the Width: "]
print('462'.zfill(6))           # 000462 ["Pads the string with zeros on the left: "]

# 3. Search & Find Methods

print(s.find('cha'))            # -1 ["Returns the index of first occurrence, -1 if not found"]
print(s.rfind('i'))             # 9 [Returns the last occurrence of the substring.]
print(s.index('i'))             # 9 [Like find(), but raises an error if not found]
print(s.count('a'))             # 3 [Counts how many times 'a' appears. ]
print(k.count('s'))             # 2 [Counts how many times 's' appears. ]