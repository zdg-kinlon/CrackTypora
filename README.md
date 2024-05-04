# Crack Typora Project

## Overview

The Crack Typora project is an experimental initiative based on Python 3.12.0, aiming to explore and understand the cracking mechanism of the Typora software (Note: Cracking software may violate software usage agreements and copyright laws. This project is solely for learning and research purposes. Please ensure compliance with relevant laws and regulations).

This project is inspired by an article on the CSDN blog (https://blog.csdn.net/m0_58416529/article/details/136098186), but it does not directly copy its code or methods. Instead, we have written our own code in Python 3.12.0, following the ideas provided in the article, to explore and learn the principles of software cracking for Typora.

## Usage Instructions

### 1. Environment Preparation

Ensure that [Python 3.12.0](https://www.python.org/downloads/) or a later version is installed on your windows computer.

Currently only supports Windows systems.

### 2. Installing Dependencies

This project may rely on third-party libraries, such as PyInstaller, which can be used to compile scripts into executable files and grant read-write permissions to files during runtime. You can install them using the `pip` command.

```bash
pip install pyinstaller
```

### 3. Running the Project

Enter the project directory and run the main program, ensuring you have read-write permissions.

```bash
cd CrackTypora
python crack_typora.py
```

Note: Due to the nature and purpose of this project, running this program may have unpredictable effects on your computer or the Typora software. Please ensure you understand these risks and operate in a safe environment.

### 4. Compiling the Project

```bash
pyinstaller --onefile crack_typora.py
```

After compilation, an executable file will be generated in the `dist` directory.

### 5. Important Notes

- This project is solely for learning and research purposes and should not be used for illegal or unauthorized activities.
- Before using this project, please ensure you understand and comply with relevant laws and regulations, including but not limited to software usage agreements and copyright laws.
- The project authors do not assume any responsibility for any consequences resulting from the use of this project.

Finally, it is emphasized again that this project is solely for learning and research purposes. Please ensure your usage complies with relevant laws, regulations, and ethical standards.
