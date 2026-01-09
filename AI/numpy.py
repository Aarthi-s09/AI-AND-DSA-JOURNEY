Installing & Importing NumPy
pip install numpy
import numpy as np

️NumPy Arrays (MOST IMPORTANT)
Create arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

Array properties
a.shape      # dimensions
a.ndim       # number of dimensions
a.size       # total elements
a.dtype      # data type

💡 ML models expect 2D or 3D arrays




| NumPy Function         | What it Does                                         | Shape / Range | Distribution          | Sample Output                                              |
| ---------------------- | ---------------------------------------------------- | ------------- | --------------------- | ---------------------------------------------------------- |
| `np.zeros((3,3))`      | Creates a matrix filled with **0s**                  | 3 × 3         | —                     | `[[0,0,0],[0,0,0],[0,0,0]]`                                |
| `np.ones((2,2))`       | Creates a matrix filled with **1s**                  | 2 × 2         | —                     | `[[1,1],[1,1]]`                                            |
| `np.eye(3)`            | Creates an **identity matrix** (diagonal = 1)        | 3 × 3         | —                     | `[[1,0,0],[0,1,0],[0,0,1]]`                                |
| `np.arange(0,10,2)`    | Generates values from 0 to 10 with step 2            | 1D array      | Linear sequence       | `[0,2,4,6,8]`                                              |
| `np.linspace(0,1,5)`   | Generates **5 evenly spaced values** between 0 and 1 | 1D array      | Linear spacing        | `[0.0,0.25,0.5,0.75,1.0]`                                  |
| `np.random.rand(3,3)`  | Random values between **0 and 1**                    | 3 × 3         | **Uniform**           | `[[0.23,0.78,0.11],[0.54,0.67,0.89],[0.34,0.92,0.45]]`     |
| `np.random.randn(3,3)` | Random values around **0** (can be negative)         | 3 × 3         | **Normal (Gaussian)** | `[[0.15,-1.23,0.87],[-0.45,0.66,-0.12],[1.34,-0.78,0.09]]` |


ACCESSING ELEMENTS IN A ARRAY
import numpy as np
# 1D array
a = np.array([10, 20, 30, 40])   # Creates a 1D NumPy array

a[0]        # Accesses the first element → 10
a[1:3]      # Slices elements from index 1 to 2 (3 is excluded) → [20, 30]
# 2D array (matrix)
b = np.array([[1, 2, 3],
              [4, 5, 6]])        # Creates a 2D array with 2 rows and 3 columns

b[0, 1]     # Accesses element at row 0, column 1 → 2

b[:, 1]     # Selects ALL rows (:) and column 1 → [2, 5]

b[1, :]     # Selects row 1 and ALL columns → [4, 5, 6]

How to Read Indexing (IMPORTANT)
array[row, column]
: → means take everything
Indexing starts from 0

1️⃣ What is reshape()?
🔹 Meaning (in simple words)
reshape() changes the shape of the array
➡️ Data stays the same, only arrangement changes
Example
import numpy as np
a = np.array([1, 2, 3, 4])
print(a)
Output: [1 2 3 4]
This is a 1D array with shape:
(4,)
Reshape it
b = a.reshape(2, 2)
print(b)
Output:
[[1 2]
 [3 4]]
🔍 What happened?
Total elements = 4
New shape = 2 × 2 = 4
✔️ Allowed
📐 Shape meaning
2 rows
2 columns

🚫 Invalid reshape
a.reshape(3, 2)
❌ ERROR because:
3 × 2 = 6 ≠ 4 elements
👉 Rule of reshape
rows × columns MUST equal total elements
2️⃣ Why reshape() is IMPORTANT in ML?
ML models expect data like this: (samples, features)
Example:
4 students
1 mark each
Before:
[10, 20, 30, 40]   → shape (4,)
After:
a.reshape(4, 1)

[[10]
 [20]
 [30]
 [40]]
✔️ Now model understands:
4 samples
1 feature

3️⃣ What is flatten()?
🔹 Meaning

flatten() converts any array into 1D
➡️ Creates a NEW COPY

Example
a = np.array([[1, 2],
              [3, 4]])

f = a.flatten()
print(f)


Output:

[1 2 3 4]

Memory behavior
f[0] = 100
print(a)
Output:
[[1 2]
 [3 4]]

👉 Original array NOT changed

✔️ Because flatten makes a copy

4️⃣ What is ravel()?
🔹 Meaning

ravel() also converts to 1D
➡️ But it returns a VIEW (not a copy)

Example
r = a.ravel()
print(r)
Output:
[1 2 3 4]
Memory behavior
r[0] = 100
print(a)
Output:
[[100   2]
 [  3   4]]
⚠️ Original array CHANGED
✔️ Because ravel() shares memory

5️⃣ flatten vs ravel (VERY CLEAR)
Feature	flatten()	ravel()
Output	1D array	1D array
Copy or view	COPY	VIEW
Faster	❌ Slower	✔ Faster
Changes original?	❌ No	✔ Yes
6️⃣ ML IMAGE EXAMPLE (SUPER IMPORTANT)
Image = 28 × 28 pixels
image.shape → (28, 28)

ML model wants:
(samples, features)


So flatten image:

image_flat = image.reshape(1, 784)

Meaning:
1 → one image

784 → 28 × 28 pixels

✔️ Perfect for ML model input

7️⃣ ONE-LINE MEMORY TRICK 🧠

reshape() → change shape

flatten() → 1D copy

ravel() → 1D view (linked)
