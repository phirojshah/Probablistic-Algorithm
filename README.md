# N-Queens Solver

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Issues](https://img.shields.io/github/issues/phirojshah/Probablistic-Algorithm)
![Forks](https://img.shields.io/github/forks/phirojshah/Probablistic-Algorithm)
![Stars](https://img.shields.io/github/stars/phirojshah/Probablistic-Algorithm)

## Introduction
The **N-Queens Solver** is a Python implementation of the classic N-Queens Problem, which involves placing `N` queens on an `N x N` chessboard such that no two queens threaten each other. This program uses the backtracking algorithm to find all possible solutions efficiently.

## Features
- Finds all valid solutions to the N-Queens problem.
- Tracks the number of recursive steps taken.
- Easily configurable for different board sizes by modifying `N`.
- Simple and clean code with detailed comments for learning purposes.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/phirojshah/Probablistic-Algorithm.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Probablistic-Algorithm
   ```
3. Ensure you have Python installed (preferably Python 3.x).
4. Run the script:
   ```bash
   python dsa.py
   ```

## Usage
1. Modify the board size by changing the value of `N` in the script (default is 8 for an 8x8 chessboard).
2. Run the script using Python:
   ```bash
   python dsa.py
   ```
3. The program will output:
   - Total steps taken (recursive calls).
   - Total solutions found.
   - Each solution as a list of queen positions.

## Example Output
```
Total Possible Cases (Steps): 92
Total Solutions Found: 92

Solutions:
Step 1: [0, 4, 7, 5, 2, 6, 1, 3]
Step 2: [0, 5, 7, 2, 6, 3, 1, 4]
...
Press Enter to exit...
```

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
