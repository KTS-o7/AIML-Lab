# AIML Lab Programs

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

AI/ML laboratory programs for the RVCE 21AI52 course. The repository is meant
for students who want runnable Python examples for common search, game-playing,
classification, clustering, and regression lab exercises.

Each lab folder contains a Python implementation and, where available, a short
Markdown explanation of the algorithm, inputs, and output.

## Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Lab Program Map](#lab-program-map)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.9 or newer
- `pip`
- A terminal or IDE that can run Python scripts

The machine-learning programs use `numpy`, `matplotlib`, `scikit-learn`, and
related dependencies listed in `requirements.txt`.

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/KTS-o7/AIML-Lab.git
cd AIML-Lab
python3 -m venv env
source env/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

On Windows, activate the environment with:

```bash
env\Scripts\activate
```

## Lab Program Map

| Lab | Folder | Main file | What it demonstrates |
| --- | --- | --- | --- |
| Tic-Tac-Toe with DFS | `TicTacToe/` | `TicTacToe_DFS.py` | Game-state search using depth-first recursion to choose optimal moves. |
| Tic-Tac-Toe with Minimax | `TicTacToe/` | `Advanced_TicTacToe.py` | Human vs computer Tic-Tac-Toe using minimax-based decision making. |
| Alpha-Beta Pruning | `AlphaBetaPruning/` | `GameOf20.py` | Minimax optimization with alpha-beta pruning in a simple number game. |
| 8 Puzzle using A* | `Eight_Puzzle_AStar/` | `EightPuzzleAStar.py` | Priority-queue search for solving an 8-puzzle configuration. |
| Hill Climbing Search | `HillClimbSearch/` | `HillClimbSearchEval.py` | Local search for a maximum of a user-provided function. |
| K-Means Clustering | `KMeansAlgorithm/` | `KMeansAlgo.py` | Clustering the Iris dataset and plotting discovered clusters. |
| K-Nearest Neighbors | `KNNAlgorithm/` | `KNNAlgo.py` | Custom KNN classifier on the Iris dataset with evaluation metrics. |
| Naive Bayes Classifier | `NaiveBayesClassifeir/` | `naiveBayes.py` | Gaussian Naive Bayes classifier on the Iris dataset. |
| Logistic Regression | `Logistic_Regression/` | `LogisticReg.py` | Binary classification on Iris data and decision-boundary plotting. |

## Project Structure

```text
AIML-Lab/
├── AlphaBetaPruning/
├── Eight_Puzzle_AStar/
├── HillClimbSearch/
├── KMeansAlgorithm/
├── KNNAlgorithm/
├── Logistic_Regression/
├── NaiveBayesClassifeir/
├── TicTacToe/
├── Contribution.md
├── LICENSE
├── README.md
└── requirements.txt
```

## Usage Examples

Run a non-interactive ML program:

```bash
python3 KNNAlgorithm/KNNAlgo.py
```

Expected output includes the model accuracy, predictions, confusion matrix, and
classification report:

```text
Accuracy: 0.9778
Predictions: [...]
Confusion Matrix:
...
Classification Report:
...
```

Run logistic regression and generate the decision-boundary plot:

```bash
python3 Logistic_Regression/LogisticReg.py
```

Expected output:

```text
Accuracy: 0.9667
```

The script saves the plot as `plot.png` in the current working directory.

Run an interactive search program:

```bash
python3 HillClimbSearch/HillClimbSearchEval.py
```

Example input:

```text
Enter a function of x: -(x-3)**2 + 9
Enter the starting value to begin the search: 0
```

Example output:

```text
The maxima is at x = 2.99999999999998
The maximum value obtained is 9.0
```

Run the 8-puzzle solver:

```bash
python3 Eight_Puzzle_AStar/EightPuzzleAStar.py
```

The script prints each puzzle state in the solution path and the number of
moves required.

## Notes for Students

- Read the corresponding `Explaination.md` or lab-specific Markdown file before
  running a program.
- Interactive programs ask for terminal input. Use the prompts shown by the
  script for valid moves or values.
- Some scripts use built-in datasets from `scikit-learn`, so no separate data
  download is needed.
- `KMeansAlgorithm/KMeansAlgo.py` opens a Matplotlib window. Run it from an
  environment that supports GUI plots, or adapt it to use `plt.savefig(...)`.

## Contributing

Contributions are welcome for fixes, clearer explanations, additional lab
programs, and improved examples.

1. Fork the repository.
2. Create a branch from `main`.
3. Add or update code and documentation.
4. Test the affected program.
5. Open a pull request with a clear summary.

For more details, see [Contribution.md](Contribution.md).

## License

This project is available under the [MIT License](LICENSE).
