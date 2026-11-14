# 🧮 Smart Python Calculator

**A Scientific Calculator Built with Python**

A desktop calculator featuring scientific operations, calculation history, and a graphical interface.

#### Video Demo:

<!-- Add your public or unlisted video URL here after uploading the video. -->

#### Description:

Smart Python Calculator is a desktop-based scientific calculator developed using Python and CustomTkinter.

It provides basic arithmetic operations, scientific calculations, mathematical constants, expression evaluation, and calculation history through a graphical interface.

The application includes a calculator display, number and operation buttons, scientific-function buttons, a history panel, keyboard shortcuts, and a dark/light appearance switch.

## Features

- **Basic arithmetic:** Addition, subtraction, multiplication, division, powers, and modulus.
- **Scientific functions:** Square root, sine, cosine, tangent, logarithms, and absolute value.
- **Mathematical constants:** Pi (π) and Euler's number (e).
- **Expression evaluation:** Parses supported mathematical expressions with Python's AST module.
- **Calculation history:** Saves previous calculations in a text file.
- **History management:** Displays saved calculations and provides an option to clear the history.
- **Keyboard support:** Press Enter to calculate and Escape to clear the current expression.
- **Appearance modes:** Switch between dark and light appearance.
- **Error handling:** Displays messages for invalid expressions and mathematical errors.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CustomTkinter | Graphical user interface |
| Tkinter | Tkinter variables and keyboard events |
| AST | Parsing supported mathematical expressions |
| math | Scientific functions and constants |
| operator | Basic arithmetic operations |
| pytest | Automated testing |

## Project Files

The project contains the following files:

- **project.py:** Main application file. It contains the mathematical functions, expression evaluator, calculation-history functions, calculator GUI, and the `main()` function.
- **test_project.py:** Contains pytest tests for the mathematical functions and calculation-history functions.
- **requirements.txt:** Lists the pip-installable packages needed for the project.
- **history.txt:** Stores calculation-history entries. The application appends new calculations to this file and reads it when displaying history.
- **README.md:** Documents the project, its setup, and its use.

## Requirements

- Python 3
- The packages listed in `requirements.txt`

## Installation and Setup

Clone this repository:

```bash
git clone https://github.com/i-Yuvan/smart-python-calculator.git
```

Move into the project directory:

```bash
cd smart-python-calculator
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Start the calculator with:

```bash
python project.py
```

The Smart Python Calculator desktop window should open. Use the on-screen buttons or type a mathematical expression into the display.

## Using the Calculator

Use the number buttons to enter values and the operation buttons to build an expression. Press `=` or Enter to calculate the result. Press `C` or Escape to clear the current expression, and use `DEL` to remove the last character.

The scientific buttons insert functions or constants into the expression. The history panel displays previous calculations. Select a history entry to place its expression back in the display. The clear-history button removes the saved history after confirmation. Use the appearance switch to change between dark and light mode.

## Testing

The project includes tests for arithmetic operations, error handling, square roots, percentages, averages, and calculation-history functions.

Run the test file with:

```bash
python -m pytest -v -p no:cacheprovider test_project.py
```

Run this command and confirm the test results before describing them as passed.

## Design Choices — Complete This Section in Your Own Words

Explain the decisions you made while developing the project. In particular, describe why you chose a graphical interface, how you approached expression evaluation, and why you used a text file for calculation history. Include a problem you encountered while developing the application and how you personally resolved it.

## Learning and Future Improvements

Through this project, I practised Python functions, object-oriented programming, exception handling, file handling, working with libraries, expression parsing, GUI development, and automated testing.

Possible future improvements include graph plotting, exporting calculation history, more scientific operations, additional themes, and more keyboard shortcuts.

## Author

**Yuvan Prasad**

GitHub: [i-Yuvan](https://github.com/i-Yuvan)

## References and Acknowledgements

List the documentation, tutorials, or other external references you used while learning or developing the graphical interface. Also make sure that any code or techniques incorporated from outside the course are cited in the source-code comments, as required by the CS50 academic honesty policy.
