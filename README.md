# BMI Calculator

A simple command-line tool to calculate Body Mass Index (BMI) from user input. Supports different units and categorizes the result using WHO standards.

## About

This project was built to practice core Python concepts like functions, loops, input validation, and unit conversions.  
It's beginner-friendly and runs entirely in the terminal.

## Features

- Input height in meters, centimeters, or feet/inches
- Input weight in kilograms or pounds
- Converts all values to metric system
- Calculates BMI and shows result
- Optionally displays BMI category (Underweight, Normal, Overweight, etc.)
- Loops for multiple calculations
- Input validation and basic error handling

## How to Run

Make sure you have Python 3 installed.

```bash
python BMI.py
```

Follow the prompts in the terminal.

## BMI Categories (WHO Standard)

- Underweight: BMI < 18.5  
- Normal: 18.5 ≤ BMI < 25  
- Overweight: 25 ≤ BMI < 30  
- Obesity Class I: 30 ≤ BMI < 35  
- Obesity Class II: 35 ≤ BMI < 40  
- Obesity Class III: BMI ≥ 40  

## Requirements

- Python 3.x  
(No external libraries needed.)

## Concepts Used
This project helped reinforce the following Python fundamentals:

- Functions and modular programming
- `while` loops and nested loops
- Conditional statements (`if`, `elif`, `else`)
- User input and string handling (`input()`, `.strip()`, `.lower()`)
- Exception handling with `try` and `except`
- Unit conversion (feet/inches to meters, pounds to kg)
- Floating-point arithmetic and rounding (`round()`)
- Clean CLI (Command-Line Interface) user experience

## GUI Version (Tkinter)

I've also created a GUI version of the BMI calculator using Python's Tkinter library as an extension of this project.

- ⚠️ The GUI implementation (`Bmi_Gui.py`) was developed with external assistance, including AI-based guidance and online documentation.  
- While I implemented and understood the core logic, the GUI framework and interface structure were built with help from various resources.  
- The functionality remains identical to the command-line version — the same BMI calculation logic powers both.  
- The GUI showcases how this project can evolve beyond the terminal, serving as a visual next step in its development.  
- Although the logic behind the BMI calculations is my own, the GUI implementation does not fully represent my original code and is included as a learning reference.

## Author

Made by Rohit Nair  
GitHub: [Fraze-byte](https://github.com/Fraze-byte)
