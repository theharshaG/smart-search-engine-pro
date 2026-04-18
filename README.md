# smart-search-engine-pro

Smart Search Engine Pro (Python Project)
## Overview

This project is an advanced command-line Smart Search Engine implemented in Python. It searches through multiple text files in a folder, supports multiple keywords, highlights matching words, and displays results with file names and line numbers. It uses generators for efficient file processing.

## Features

Search across multiple text files
Support multiple keywords search
Case-insensitive searching
Highlight matched keywords in results
Display file name and line number
Efficient processing using generator

## Technologies Used

Python
File Handling
OS module
Generators (yield)
String manipulation

## Project Structure

smart-search-engine-pro/
│
├── main.py
├── files/
│ ├── file1.txt
│ ├── file2.txt
│ └── ...
└── README.md

## How to Run

install python (VS Code)
Create a folder named "files" and add .txt files
Run the program: smart search engine pro.py

## How It Works

The program scans all .txt files inside the "files" folder

A generator function reads each file line by line
This improves performance for large files

User enters multiple keywords separated by space

For each line:
It checks if any keyword exists (case-insensitive)

If matched:
The line is displayed
Matched words are highlighted using >>> <<<
File name and line number are shown

At the end:
Total number of matches is displayed

## Future Improvements

Add support for more file types (pdf, csv)
Add ranking system for results
Add GUI application
Develop web version using Flask
Add real-time file monitoring
Improve highlighting with colors

# Author
Harsha G
Learning Python | Embedded Systems | IoT
