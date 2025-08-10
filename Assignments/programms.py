def find_missing_number():
    print("🧠 Program: Find the Missing Number in a List of Consecutive Integers")
    print("\n\n📄 Code:")
    print("""
def find_missing(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)
""")
    print("🧪 Test Cases:")
    print("Test Case 1: find_missing([1, 2, 3, 5]) -> 4")
    print("Test Case 2: find_missing([2, 3, 4, 5, 6, 8, 9]) -> 7")
    print("\n\n📝 Explanation:")
    print("Uses the formula n*(n+1)//2 to find the expected sum and subtracts the actual sum to get the missing number.")

def rotate_list_k_times():
    print("🧠 Program: Rotate a List k Times to the Right")
    print("\n\n📄 Code:")
    print("""
def rotate_list(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k]
""")
    print("🧪 Test Cases:")
    print("Test Case 1: rotate_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]")
    print("Test Case 2: rotate_list([10, 20, 30], 4) -> [30, 10, 20]")
    print("\n\n📝 Explanation:")
    print("Uses slicing to rotate the list efficiently without extra loops.")

def find_pairs_sum_target():
    print("🧠 Program: Find All Pairs in a List That Sum to a Target Value")
    print("\n\n📄 Code:")
    print("""
def pair_sum(nums, target):
    pairs = []
    seen = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs
""")
    print("🧪 Test Cases:")
    print("Test Case 1: pair_sum([1, 2, 3, 4, 5], 5) -> [(2, 3), (1, 4)]")
    print("Test Case 2: pair_sum([0, -1, 2, -3, 1], -2) -> [(-3, 1)]")
    print("\n\n📝 Explanation:")
    print("Uses a set to store seen numbers and find matching pairs in O(n) time.")

def unique_characters():
    print("🧠 Program: Check if a String Has All Unique Characters (Without Using Set)")
    print("\n\n📄 Code:")
    print("""
def has_unique_chars(s):
    chars = {}
    for ch in s:
        if ch in chars:
            return False
        chars[ch] = True
    return True
""")
    print("🧪 Test Cases:")
    print("Test Case 1: has_unique_chars('abcde') -> True")
    print("Test Case 2: has_unique_chars('hello') -> False")
    print("\n\n📝 Explanation:")
    print("Uses a dictionary to track seen characters without using a set.")

def merge_sorted_lists():
    print("🧠 Program: Merge Two Sorted Lists into One Sorted List")
    print("\n\n📄 Code:")
    print("""
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
""")
    print("🧪 Test Cases:")
    print("Test Case 1: merge_sorted([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]")
    print("Test Case 2: merge_sorted([1, 2], [3, 4]) -> [1, 2, 3, 4]")
    print("\n\n📝 Explanation:")
    print("Implements the merge step of merge sort in O(n) time.")

def move_zeros_end():
    print("🧠 Program: Move All Zeros in a List to the End While Keeping Order")
    print("\n\n📄 Code:")
    print("""
def move_zeros(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    return non_zeros + zeros
""")
    print("🧪 Test Cases:")
    print("Test Case 1: move_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]")
    print("Test Case 2: move_zeros([0, 0, 1]) -> [1, 0, 0]")
    print("\n\n📝 Explanation:")
    print("Separates non-zero elements and appends zeros at the end.")

def remove_punctuation():
    print("🧠 Program: Remove All Punctuation from a String")
    print("\n\n📄 Code:")
    print("""
import string
def remove_punct(s):
    return ''.join(ch for ch in s if ch not in string.punctuation)
""")
    print("🧪 Test Cases:")
    print("Test Case 1: remove_punct('Hello, world!') -> 'Hello world'")
    print("Test Case 2: remove_punct('Python@2023#') -> 'Python2023'")
    print("\n\n📝 Explanation:")
    print("Uses Python's string.punctuation to filter out punctuation characters.")

def count_vowels_consonants():
    print("🧠 Program: Count Vowels and Consonants in a String")
    print("\n\n📄 Code:")
    print("""
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
""")
    print("🧪 Test Cases:")
    print("Test Case 1: count_vc('hello') -> (2, 3)")
    print("Test Case 2: count_vc('Python') -> (1, 5)")
    print("\n\n📝 Explanation:")
    print("Checks each character and counts vowels and consonants separately.")

def perfect_number_check():
    print("🧠 Program: Check if a Number is Perfect")
    print("\n\n📄 Code:")
    print("""
def is_perfect(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
""")
    print("🧪 Test Cases:")
    print("Test Case 1: is_perfect(6) -> True")
    print("Test Case 2: is_perfect(28) -> True")
    print("\n\n📝 Explanation:")
    print("A perfect number equals the sum of its proper divisors.")

def print_pattern():
    print("🧠 Program: Print Star Pyramid Pattern")
    print("\n\n📄 Code:")
    print("""
n = int(input("Enter number of rows: "))

# Upper part
for i in range(1, n + 1):
    print("*" * i)

# Lower part
for i in range(n - 1, 0, -1):
    print("*" * i)
""")
    print("🧪 Test Cases:")
    print("Test Case 1: n = 5")
    print("""Output:
*
**
***
****
*****
****
***
**
*""")
    print("Test Case 2: n = 3")
    print("""Output:
*
**
***
**
*""")
    print("\n\n📝 Explanation:")
    print("First loop prints increasing stars from 1 to n. \
Second loop prints decreasing stars from n-1 down to 1.")
