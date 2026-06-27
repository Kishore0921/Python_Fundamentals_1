# Python Basics

## IDE (Integrated Development Environment)

An **IDE (Integrated Development Environment)** is software that helps us write, run, debug, and manage Python programs efficiently.

### Popular Python IDEs

* PyCharm
* Visual Studio Code (VS Code)
* GitHub (for version control and project hosting)

> **Note:** An IDE is required to write and execute Python programs conveniently.


## Python File Extension

Python source code files use the following extension:
.py


Example:


hello.py
calculator.py

## Installing Python

1. Visit the official Python website.
2. Go to **Downloads**.
3. Download the required version (32-bit or 64-bit).
4. During installation, enable:
✓ Add Python to PATH
5. Click **Install**.

---

## Checking System Type

To know whether your computer is 32-bit or 64-bit:


This PC
   └── Properties
         └── System
               └── System Type


---

## Installing PyCharm

1. Search **PyCharm** on Google.
2. Download the **Community Edition**.
3. Run the installer.
4. Click:


Continue
↓
Accept
↓
Finish


---

## Creating a New Project in PyCharm


PyCharm
   └── File
         └── New Project


Provide:

* Project Name
* Project Location
* Previously Configured Interpreter

Example project structure:

Python/
└── Practice/
    └── hello.py


---

## Advantages of Using an IDE

* Detects errors automatically.
* Underlines syntax mistakes.
* Provides syntax highlighting with different colors.
* Makes coding easier and faster.

---

# Visual Studio Code (VS Code) and Python Integration

## What is Visual Studio Code?

**Visual Studio Code (VS Code)** is a free, lightweight, and powerful source code editor developed by Microsoft. It supports many programming languages, including Python, through extensions.

### Features of VS Code

* Fast and lightweight.
* Free and open source.
* Supports multiple programming languages.
* Built-in terminal.
* Intelligent code completion (IntelliSense).
* Debugging support.
* Git and GitHub integration.
* Large extension marketplace.

---

# Installing Visual Studio Code

1. Visit the official VS Code website.
2. Download the installer for your operating system.
3. Run the installer.
4. Select the following options:

```text
✓ Add to PATH
✓ Register Code as an editor
✓ Create Desktop Icon (Optional)
```

5. Click **Install** and then **Finish**.

---

# Installing the Python Extension

After installing VS Code:

1. Open VS Code.
2. Click on the **Extensions** icon (`Ctrl + Shift + X`).
3. Search for **Python**.
4. Install the **Python** extension published by Microsoft.

This extension provides:

* Syntax highlighting
* IntelliSense (Auto-completion)
* Debugging
* Code formatting
* Linting
* Jupyter Notebook support

---

# Python and VS Code Integration

Once Python and the Python extension are installed:

1. Open VS Code.
2. Create or open a folder for your project.
3. Create a new file with the `.py` extension.

Example:

```text
hello.py
```

VS Code automatically recognizes the file as a Python program.

---

# Selecting the Python Interpreter

Before running Python code, select the correct Python interpreter.

Steps:

```text
Ctrl + Shift + P
        ↓
Python: Select Interpreter
        ↓
Choose the installed Python version
```

Example:

```text
Python 3.13 (64-bit)
```

> **Note:** If Python does not appear, make sure it is installed and added to the system PATH.

---

# Creating Your First Python Program

Create a file named:

```text
hello.py
```

Write the following code:

```python
print("Hello, World!")
```

Save the file.

---

# Running a Python Program

There are multiple ways to run Python code in VS Code.

### Method 1: Run Button

Click the **▶ Run** button in the top-right corner.

---

### Method 2: Integrated Terminal

Open the terminal:

```text
Terminal
   ↓
New Terminal
```

Run the file:

```bash
python hello.py
```

or

```bash
python3 hello.py
```

---

### Method 3: Keyboard Shortcut

Press:

```text
Ctrl + F5
```

Runs the program without debugging.

Press:

```text
F5
```

Runs the program with debugging.

---

# Integrated Terminal

VS Code has a built-in terminal, so there is no need to open Command Prompt separately.

Open it using:

```text
Terminal → New Terminal
```

Common commands:

```bash
python hello.py
```

```bash
python calculator.py
```

```bash
pip install numpy
```

```bash
pip install pandas
```

---

# Installing Python Packages

Python packages are installed using **pip** (Python Package Installer).

Example:

```bash
pip install requests
```

Check installed packages:

```bash
pip list
```

Update pip:

```bash
python -m pip install --upgrade pip
```

---

# Common VS Code Shortcuts

| Shortcut           | Function              |
| ------------------ | --------------------- |
|  Ctrl + S          | Save file             |
|  Ctrl + N          | New file              |
|  Ctrl + Shift + X  | Extensions            |
|  Ctrl + Shift + P  | Command Palette       |
|  Ctrl + /          | Comment or Uncomment  |
|  Ctrl + Shift + `  | Open Terminal         |
|  Ctrl + F5         | Run without Debugging |
|  F5                | Start Debugging       |

---

# Why Use VS Code for Python?

* Easy to learn.
* Lightweight and fast.
* Excellent Python support.
* Supports Git and GitHub.
* Built-in terminal.
* Large collection of extensions.
* Suitable for beginners and professionals.

---

# Summary

* VS Code is a lightweight code editor developed by Microsoft.
* Install the official Python extension for Python development.
* Select the correct Python interpreter before running programs.
* Create Python files using the `.py` extension.
* Use the integrated terminal to run Python programs.
* Install additional libraries using `pip`.
* VS Code provides debugging, IntelliSense, Git integration, and many useful shortcuts.
