import programms as pg
while True:
    print("\n\n1. Find Missing Number")
    print("2. Rotate List K Times to the Right")
    print("3. Find Pairs That Sum to Target")
    print("4. Check Unique Characters in String")
    print("5. Merge Two Sorted Lists")
    print("6. Move All Zeros to End")
    print("7. Remove Punctuation from String")
    print("8. Count Vowels and Consonants")
    print("9. Check if Number is Perfect")
    print("10. Print Star Pattern")
    print("0. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        pg.find_missing_number()
    elif ch == 2:
        pg.rotate_list_k_times()
    elif ch == 3:
        pg.find_pairs_sum_target()
    elif ch == 4:
        pg.unique_characters()
    elif ch == 5:
        pg.merge_sorted_lists()
    elif ch == 6:
        pg.move_zeros_end()
    elif ch == 7:
        pg.remove_punctuation()
    elif ch == 8:
        pg.count_vowels_consonants()
    elif ch == 9:
        pg.perfect_number_check()
    elif ch == 10:
        pg.print_pattern()
    elif ch == 0:
        print("End of Programms")
        break
    else:
        print("Invalid choice!")







'''
# OUTPUT

1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 1
🧠 Program: Find the Missing Number in a List of Consecutive Integers


📄 Code:

def find_missing(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

🧪 Test Cases:
Test Case 1: find_missing([1, 2, 3, 5]) -> 4
Test Case 2: find_missing([2, 3, 4, 5, 6, 8, 9]) -> 7


📝 Explanation:
Uses the formula n*(n+1)//2 to find the expected sum and subtracts the actual sum to get the missing number.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 2
🧠 Program: Rotate a List k Times to the Right


📄 Code:

def rotate_list(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k]

🧪 Test Cases:
Test Case 1: rotate_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
Test Case 2: rotate_list([10, 20, 30], 4) -> [30, 10, 20]


📝 Explanation:
Uses slicing to rotate the list efficiently without extra loops.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 3
🧠 Program: Find All Pairs in a List That Sum to a Target Value


📄 Code:

def pair_sum(nums, target):
    pairs = []
    seen = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

🧪 Test Cases:
Test Case 1: pair_sum([1, 2, 3, 4, 5], 5) -> [(2, 3), (1, 4)]
Test Case 2: pair_sum([0, -1, 2, -3, 1], -2) -> [(-3, 1)]


📝 Explanation:
Uses a set to store seen numbers and find matching pairs in O(n) time.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 4
🧠 Program: Check if a String Has All Unique Characters (Without Using Set)


📄 Code:

def has_unique_chars(s):
    chars = {}
    for ch in s:
        if ch in chars:
            return False
        chars[ch] = True
    return True

🧪 Test Cases:
Test Case 1: has_unique_chars('abcde') -> True
Test Case 2: has_unique_chars('hello') -> False


📝 Explanation:
Uses a dictionary to track seen characters without using a set.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 5
🧠 Program: Merge Two Sorted Lists into One Sorted List


📄 Code:

def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

🧪 Test Cases:
Test Case 1: merge_sorted([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
Test Case 2: merge_sorted([1, 2], [3, 4]) -> [1, 2, 3, 4]


📝 Explanation:
Implements the merge step of merge sort in O(n) time.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 6
🧠 Program: Move All Zeros in a List to the End While Keeping Order


📄 Code:

def move_zeros(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    return non_zeros + zeros

🧪 Test Cases:
Test Case 1: move_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
Test Case 2: move_zeros([0, 0, 1]) -> [1, 0, 0]


📝 Explanation:
Separates non-zero elements and appends zeros at the end.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 7
🧠 Program: Remove All Punctuation from a String


📄 Code:

import string
def remove_punct(s):
    return ''.join(ch for ch in s if ch not in string.punctuation)

🧪 Test Cases:
Test Case 1: remove_punct('Hello, world!') -> 'Hello world'
Test Case 2: remove_punct('Python@2023#') -> 'Python2023'


📝 Explanation:
Uses Python's string.punctuation to filter out punctuation characters.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 8
🧠 Program: Count Vowels and Consonants in a String


📄 Code:

def count_vc(s):
    vowels = 'aeiouAEIOU'
    v_count = c_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

🧪 Test Cases:
Test Case 1: count_vc('hello') -> (2, 3)
Test Case 2: count_vc('Python') -> (1, 5)


📝 Explanation:
Checks each character and counts vowels and consonants separately.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 9
🧠 Program: Check if a Number is Perfect


📄 Code:

def is_perfect(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

🧪 Test Cases:
Test Case 1: is_perfect(6) -> True
Test Case 2: is_perfect(28) -> True


📝 Explanation:
A perfect number equals the sum of its proper divisors.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 10
🧠 Program: Print Star Pyramid Pattern


📄 Code:

n = int(input("Enter number of rows: "))

# Upper part
for i in range(1, n + 1):
    print("*" * i)

# Lower part
for i in range(n - 1, 0, -1):
    print("*" * i)

🧪 Test Cases:
Test Case 1: n = 5
Output:
*
**
***
****
*****
****
***
**
*
Test Case 2: n = 3
Output:
*
**
***
**
*


📝 Explanation:
First loop prints increasing stars from 1 to n. Second loop prints decreasing stars from n-1 down to 1.


1. Find Missing Number
2. Rotate List K Times to the Right
3. Find Pairs That Sum to Target
4. Check Unique Characters in String
5. Merge Two Sorted Lists
6. Move All Zeros to End
7. Remove Punctuation from String
8. Count Vowels and Consonants
9. Check if Number is Perfect
10. Print Star Pattern
0. Exit
Enter your choice: 0
End of Programms
'''