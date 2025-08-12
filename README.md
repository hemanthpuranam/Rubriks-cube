
# Rubik’s Cube Solver – Beginner Method (Python)

## 📌 Overview

This project is a Python-based Rubik’s Cube solver that follows the **Beginner Method**, making it easier to understand and implement. The program takes the cube’s current state as input and outputs the step-by-step moves required to solve it.

The aim is to provide a learning-friendly implementation while ensuring clear logic, modular code, and easy debugging.

---

## ✨ Features

* Solves a standard **3x3 Rubik’s Cube** using the beginner method.
* Step-by-step solving approach:

  1. White Cross
  2. White Corners
  3. Second Layer Edges
  4. Yellow Cross
  5. Yellow Corners
  6. Positioning Final Pieces
* User-friendly move notation (e.g., `R`, `R'`, `U`, `U'`).
* Modular code structure for easy modification and upgrades.

---

## 📂 Project Structure

```
rubiks_solver/
│── solver.py        # Main solver logic
│── cube.py          # Cube representation and operations
│── algorithms.py    # Beginner method algorithms
│── README.md        # Project documentation
```

---

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/username/rubiks-cube-solver.git
   cd rubiks-cube-solver
   ```
2. **Run the solver:**

   ```bash
   python solver.py
   ```
3. **Follow the prompts** to input the cube’s current state.

---

## 🛠 Requirements

* Python 3.x
* No external libraries needed (pure Python implementation)

---

## 📖 How It Works

The solver uses the beginner method by breaking the cube-solving process into smaller, manageable steps. Each step’s algorithm is hardcoded and applied based on cube state detection.

---

## 📜 License

This project is open-source under the MIT License.

