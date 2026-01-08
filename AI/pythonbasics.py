python --version    (to check version in cmd)
to code in cmd type py and you can type small code there
x = 10          # int
y = 3.14        # float
name = "Aarthi" # string
flag = True     # boolean
type(x) to know datatype of the variable 

printing float using format 
x = 3.14159
print(f"Value: {x:.2f}")


1️⃣ Python Data Types & Variables
Common types: int, float, str, bool
Type conversion functions:
Function	Converts to	Example
int()	Integer	int(3.9) → 3
float()	Float	float("2.5") → 2.5
str()	String	str(10) → "10"
Examples:
x = "10"
y = int(x) + 5  # 15

pi = 3
print(float(pi)) # 3.0

print("Age: " + str(25)) # Age: 25
Input is always string: input() → use type conversion to use numerically.

2️⃣ Python String & Sequence Indexing
Indexing:
Positive index → start from left (0)
Negative index → start from right (-1 = last character)
Access elements:
s = "Python"
print(s[0])  # P
print(s[-1]) # n

3️⃣ Python String / Sequence Formatting

f-strings: f"{variable}"
Width & Alignment:
x = 3.14159
print(f"{x:10.2f}")  # width=10, right aligned default → '      3.14'
print(f"{x:<10.2f}") # left aligned → '3.14      '
print(f"{x:^10.2f}") # center → '   3.14   '
print(f"{x:>10.2f}") # right → '      3.14'
String alignment with f-string:
print(f"|{'Left':<10}|{'Center':^10}|{'Right':>10}|")
< → left, > → right, ^ → center
If alignment omitted → left by default for strings.

4️⃣ Type Conversion (Casting)

Convert types using int(), float(), str()
Important points:
int() discards decimals
float() converts integers or numeric strings to float
str() converts numbers to text
Example:
a = "10"
b = "5"
print(int(a) + int(b)) # 15

5️⃣ Python Slicing
Syntax:
sequence[start:stop:step]
start → inclusive
stop → exclusive
step → move direction & jump size
Positive step (forward):
start < stop
Default step = 1
Omitting start → 0
Omitting stop → end of sequence
Negative step (backward):
start > stop
Step negative (-1) → move left
Omitting start → end of sequence
Omitting stop → beginning of sequence


day 2 
Lists → datasets (features, labels, batches)
Dictionaries → records, JSON data, model configs
Mean / Median → basic statistics used everywhere in ML


loop for dict
for key, value in student.items():
    print(key, value)

Mean
Mean=Number of values/Sum of values​
Median
If odd count → middle value
If even count → average of two middle values


🔹 List Comprehension
Compact way to write loops.
squares = [x*x for x in range(5)]


With condition:
evens = [x for x in range(10) if x % 2 == 0]


Equivalent loop:
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

✅ 1️⃣ filter() → YES, can be replaced by list comprehension
Your filter() example
marks = [35, 60, 45, 80, 30]

passed = list(filter(lambda x: x >= 50, marks))
print(passed)

✅ Equivalent list comprehension (Preferred in Python)
passed = [x for x in marks if x >= 50]
print(passed)

🔹 Interview-ready explanation

filter() can be replaced by list comprehension, which is more readable and Pythonic.

❌ 2️⃣ reduce() → NOT list comprehension
Your reduce() example
from functools import reduce

salaries = [20000, 30000, 25000]

total_payout = reduce(lambda a, b: a + b, salaries)
print(total_payout)

❌ This CANNOT be done using list comprehension directly

Because:

List comprehension creates a list

reduce() returns a single value

✅ What to use instead of reduce() (IMPORTANT)
🔹 Best Pythonic replacement → sum()
total_payout = sum(salaries)
print(total_payout)

🔹 Or for loop
total = 0
for s in salaries:
    total += s

Function	Can use List Comprehension?	Best Pythonic Alternative
map()	✅ Yes	List comprehension
filter()	✅ Yes	List comprehension
reduce()	❌ No	sum(), min(), max()
