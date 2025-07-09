# Output Formatting

# Understanding the print() Function in Python
# Before diving into output formatting, it's important to understand the basics of the print()
# function, which is used to display information on the screen.
# What is print()?
# The print() function in Python outputs text, numbers, or any other data type to the
# console. It's one of the first functions every Python programmer learns.

# Basic Syntax:

# print(object, ..., sep=' ', end='\n', file=sys.stdout,
# flush=False)

# ● object: The data you want to display (can be text, numbers, variables, etc.).
# ● sep (optional): Defines the separator between multiple items.Default is a space(‘').
# ● end (optional): Specifies what to print at the end of the output. Default is a new line
# ('\n').
# ● file (optional): Where the output is sent. By default, it goes to the console.
# ● flush (optional): Forces the output to be written immediately.

# Basic Examples of print()
# a) Printing Text
print("Hello, World!")                  # Hello, World!
# b) Printing Multiple Items
n = 'Kiran'
a = 21
print("Name: ",n,"Age: ",a)             # Name:  Kiran Age:  21
# Using sep to Change the Separator
print("06","06","2004",sep = "-")       # 06-06-2004
# Using end to Control Line Endings
print("Hello")                          # Hello
                                        # world
print("world")
print("Hello",end=" ")                  # Hello world
print("world")


# Printing Special Characters
# ● New Line (\n):
print("line1 \n line2")                 # line1 
                                        # line2
# ● Tab (\t):
print("Name:\t Kiran")                  # Name:    Kiran


# Output Formatting
# 1️⃣Using Commas (Simple Print Method)
# This is the most basic way to print multiple items. When you separate items with commas in
# the print() function, Python adds a space between them automatically.

name = 'Kiran'
age = 21
score = 97.456

print("Name: ",name,"Age: ",age,"Score: ",score)
# Name:  Kiran Age:  21 Score:  97.456


# Pros: Simple and easy for beginners.
# Cons: Limited control over formatting (like decimal places or alignment).


# 2️⃣Using Modulo Operator (% Formatting)
# This is an older method, similar to C-style formatting.
# You use % followed by format specifiers like %s (string), %d (integer), %f (float), etc.

print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
# Name: Kiran | Age: 21 | Score: 97.46


# ● %s → String
# ● %d → Integer
# ● %.2f → Float with 2 decimal places
# Pros: Good control over formatting.
# Cons: Outdated; not recommended for new projects.

# 3️⃣Using f-strings (Formatted String Literals) — Python 3.6+
# This is the most modern and recommended method.
# Add an f before the string and use curly braces {} to insert variables directly.

print(f"Name: {name} | Age: {age} | Score: {score:.2f}")
# Name: Kiran | Age: 21 | Score: 97.46


# ● {score:.2f} → Displays the score with 2 decimal places.
# Pros: Clean, concise, and easy to read.
# Cons: Only works in Python 3.6 and above.

# 4️⃣Using str.format() Method
# This method works in both Python 2 and 3.
# You use {} as placeholders and call .format() with the variables you want to insert.

print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,score))
# Name: Kiran | Age: 21 | Score: 97.5


# ● {} → Placeholder for variables.
# ● {:.1f} → Formats the score with 1 decimal place.
# Pros: Flexible and supports complex formatting.
# Cons: Slightly more verbose compared to f-strings.

