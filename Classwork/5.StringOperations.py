
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

# 4. String Testing Methods (Boolean Results) filters{startswith,endswith}

r = "21A91A0462"
print("start  :",r.startswith('21A'))  # True  [Checks if the string starts with '21A']
filen = "StringOperations.py"
print(filen.endswith('.py'))           # True  [Checks if the string ends with '.py']
print(r.isalpha())                     # False [Returns True if all characters are alphabets.]
print(r.isalnum())                     # True  [Returns True if all characters are alphanumeric.]
name = "sri sai chandra kiran"
print(name.isupper())                  # False [Returns True if all characters are lowercase.]
print(name.islower())                  # True  [Returns True if all characters are uppercase]
print(name.isspace())                  # False [Returns True if all characters are whitespace]
print(name.istitle())                  # False [Returns True if the string is in the title case]
print(filen.isidentifier())            # False [Checks if the string is a valid Python identifier]
d = '1234'
print(d.isdecimal())                   # True  [Most strict; only base-10 digits ('0'–'9' and equivalents)]
print(d.isdigit())                     # True  [Allows additional digit characters like superscripts]
print(d.isnumeric())                   # True  [ Most flexible; includes digits, fractions, Roman numerals, etc.]

# 5. Replace & Modify Methods

print(name.replace("a","@"))                            # sri s@i ch@ndr@ kir@n [Replaces occurrences of 'a' with '@'.]
print(name.translate(str.maketrans("sark","$@*#")))     # $*i $@i ch@nd*@ #i*@n [Replaces characters using a translation table {s:$,a:@,r:*,k:#}.]
print(name.maketrans("sark","$@*#"))                    # {115: 36, 97: 64, 114: 42, 107: 35} [Creates a translation table for translate().]

# 6. Splitting & Joining Methods

print(name.split(" "))                  # ['sri', 'sai', 'chandra', 'kiran'] **[Splits the string into a list by ' '.]**
print(name.rsplit(" ",1))               # ['sri sai chandra', 'kiran'] **[Splits from the right side.]**
print("chandra\nkiran".splitlines())    # ['chandra', 'kiran'] **[Splits at line breaks (\n).]**
print(" ".join(["hello","kiran"]))      # hello kiran   **[Joins elements with a separator.]**
print(filen.partition("."))             # ('StringOperations', '.', 'py') **[Splits into a 3-part tuple at first '.']**
print(filen.rpartition("."))            # ('StringOperations', '.', 'py') **[Splits into a 3-part tuple at last '.']**

# 7. Whitespace & Trimming Methods
print("   kiran".strip())               # kiran     [Removes leading and trailing characters (default: spaces).]
print("---kiran---".lstrip("-"))        # kiran---  [Removes leading characters."-" in left]
print("---kiran---".rstrip("-"))        # ---kiran  [Removes trailing characters."-" in rignt]

# 8. Encoding & Decoding Methods
mes = "hello 😊❤️🎉"
en = mes.encode()
print(en)                               # b'hello \xf0\x9f\x98\x8a\xe2\x9d\xa4\xef\xb8\x8f\xf0\x9f\x8e\x89'[Converts the string to bytes.]
print(en.decode())                      # hello 😊❤️🎉 [Converts bytes back to string.]