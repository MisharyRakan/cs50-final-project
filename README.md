# Simple To‑Do List
#### Video Demo: https://www.youtube.com/watch?v=AxhxXT5vnAg
#### Description:

This project is my Final Project for CS50x 2026. It is a simple command‑line To‑Do List application written in Python. The goal of this project is to demonstrate my understanding of Python, file handling, user input, and basic program structure. Although the project is intentionally simple, it reflects core ideas of software design: reading and writing data, interacting with users, and organizing code into functions.

The idea behind this project came from wanting a lightweight and minimalistic task manager that runs directly in the terminal. Many task applications today are graphical or web‑based, but sometimes a simple text‑based tool is all that is needed. This project focuses on clarity, simplicity, and functionality without unnecessary complexity.

---

## Project Overview

The program allows users to perform four main actions:

1. Add a task
   The user can type any task, and it will be appended to the list and saved automatically.

2. Show tasks
   The program displays all tasks in a numbered list. If no tasks exist, it informs the user.

3. Delete a task
   The user can delete a task by selecting its number from the displayed list.

4. Exit the program
   The program ends after completing the selected action.

The program is intentionally designed to run once per execution. The user selects an action, the program performs it, and then exits. This keeps the structure simple and easy to understand.

---

## File Structure

### 1. todo.py
This is the main Python file that contains the entire logic of the program. It includes:

- load_tasks(): Reads tasks from tasks.txt. If the file does not exist, it returns an empty list.
- save_tasks(tasks): Writes the current list of tasks to tasks.txt.
- main(): Displays the menu, handles user input, and calls the appropriate functions.

### 2. tasks.txt
This file stores the user’s tasks. Each line represents one task. If the file does not exist, it will be created automatically.

---

## Design Choices

### Why a text file?
It is simple, readable, and does not require external libraries.

### Why a command‑line interface?
It is fast, lightweight, and aligns with CS50’s terminal‑based learning style.

### Why no loops?
The program performs one action per execution to keep the structure simple.

### Error Handling
The program handles missing files gracefully and ensures safe deletion of tasks.

---

## How to Run

Run the program using:
python todo.py

Ensure that todo.py and tasks.txt are in the same directory.

---

## Future Improvements

- Add a loop for multiple actions in one run
- Add task categories or priorities
- Add timestamps
- Convert to a Flask web app
- Add color formatting
- Encrypt the tasks file

---

## Conclusion

This project demonstrates my understanding of Python basics, file I/O, and program structure. It may be simple, but it reflects essential programming concepts and helped reinforce what I learned in CS50.

Thank you for reviewing my project!
