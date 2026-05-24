# Smart Data Analyzer

Smart Data Analyzer is a beginner-friendly Python project for analyzing text data.

The project was built step by step while practicing Python fundamentals from basic programming concepts to file handling, regular expressions, web scraping, SQLite databases, data visualization, and project structure.

## Current Features

- Simple command-line menu
- Direct text input from the user
- Read text from `.txt` files
- Count lines
- Count words
- Count characters
- Find the most common words
- Clean words by removing punctuation
- Extract email addresses
- Extract URLs
- Save analysis results as a JSON file
- Store analysis history in a SQLite database
- Show previous analysis history
- Create word-frequency charts
- Analyze text from web pages
- Organized code into multiple modules
- Basic error handling for missing files and network errors

## Concepts Practiced

- Functions
- Variables
- User input
- While loops
- If / elif / else conditions
- String methods
- `len()`
- `split()`
- `splitlines()`
- Return values
- f-strings
- File reading
- `open()`
- `read()`
- `close()`
- `try / except`
- `FileNotFoundError`
- Function reuse
- Lists
- Dictionaries
- Tuples
- Sorting
- Lambda functions
- For loops
- String cleaning
- Regular expressions
- `import re`
- `re.findall()`
- Regex patterns
- JSON
- `import json`
- `json.dump()`
- Writing files
- Result dictionaries
- SQLite
- `import sqlite3`
- Database connection
- SQL `CREATE TABLE`
- SQL `INSERT`
- SQL `SELECT`
- `fetchall()`
- Date and time with `datetime`
- Data visualization
- `matplotlib`
- Bar charts
- Saving figures
- HTTP requests
- `requests`
- Web scraping
- HTML parsing
- `BeautifulSoup`
- Network error handling
- Python modules
- Packages
- Imports
- Code organization
- Project structure

## Project Structure

```text
smart-data-analyzer/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── sample.txt
│
├── reports/
│
├── analyzers/
│   ├── __init__.py
│   ├── text_analyzer.py
│   ├── file_handler.py
│   ├── web_analyzer.py
│   └── visualizer.py
│
└── database/
    ├── __init__.py
    └── db_manager.py
```

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the program:

```bash
python main.py
```

After running the program, you will see a menu like this:

```text
==============================
Smart Data Analyzer
==============================
1. Analyze direct text
2. Analyze text file
3. Analyze web page
4. Show analysis history
5. Exit
```

## Example File Test

Choose option `2` and enter:

```text
data/sample.txt
```

The program will analyze the file and show:

- Number of lines
- Number of words
- Number of characters
- Most common words
- Emails found
- URLs found

## Example JSON Export

After analysis, the program asks:

```text
Do you want to save the result as JSON? (y/n):
```

Enter:

```text
y
```

Then enter an output path, for example:

```text
data/result.json
```

## Example Chart Export

After analysis, the program asks:

```text
Do you want to create a word-frequency chart? (y/n):
```

Enter:

```text
y
```

Then enter an output path, for example:

```text
reports/word_frequency.png
```

## Project Roadmap

- Basic menu and direct text input ✅
- Basic text analysis: lines, words, and characters ✅
- Text file analysis ✅
- Most common word analysis ✅
- Email and URL extraction with regular expressions ✅
- JSON export for analysis results ✅
- SQLite database history ✅
- Data visualization with charts ✅
- Web page text analysis ✅
- Project refactoring into multiple files ✅

## Notes

Generated output files such as JSON results, SQLite database files, and chart images are ignored by Git using `.gitignore`.

The project is designed as a learning project, so the code is intentionally simple and readable.