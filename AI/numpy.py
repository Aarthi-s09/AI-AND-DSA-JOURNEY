| NumPy Function         | What it Does                                         | Shape / Range | Distribution          | Sample Output                                              |
| ---------------------- | ---------------------------------------------------- | ------------- | --------------------- | ---------------------------------------------------------- |
| `np.zeros((3,3))`      | Creates a matrix filled with **0s**                  | 3 × 3         | —                     | `[[0,0,0],[0,0,0],[0,0,0]]`                                |
| `np.ones((2,2))`       | Creates a matrix filled with **1s**                  | 2 × 2         | —                     | `[[1,1],[1,1]]`                                            |
| `np.eye(3)`            | Creates an **identity matrix** (diagonal = 1)        | 3 × 3         | —                     | `[[1,0,0],[0,1,0],[0,0,1]]`                                |
| `np.arange(0,10,2)`    | Generates values from 0 to 10 with step 2            | 1D array      | Linear sequence       | `[0,2,4,6,8]`                                              |
| `np.linspace(0,1,5)`   | Generates **5 evenly spaced values** between 0 and 1 | 1D array      | Linear spacing        | `[0.0,0.25,0.5,0.75,1.0]`                                  |
| `np.random.rand(3,3)`  | Random values between **0 and 1**                    | 3 × 3         | **Uniform**           | `[[0.23,0.78,0.11],[0.54,0.67,0.89],[0.34,0.92,0.45]]`     |
| `np.random.randn(3,3)` | Random values around **0** (can be negative)         | 3 × 3         | **Normal (Gaussian)** | `[[0.15,-1.23,0.87],[-0.45,0.66,-0.12],[1.34,-0.78,0.09]]` |
