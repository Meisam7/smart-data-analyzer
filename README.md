# Smart Data Analyzer

Smart Data Analyzer is a beginner-friendly Python project for analyzing text data.

The project is built step by step while learning Python fundamentals.

## Current Features

- Simple command-line menu
- Direct text input from the user
- Read text from `.txt` files
- Count lines
- Count words
- Count characters
- Basic error handling for missing files
- - Find the most common words
- Clean words by removing punctuation
- - Extract email addresses
- Extract URLs
- Save analysis result as a JSON file
- - Store analysis history in SQLite database
- Show previous analysis history
- Create word-frequency chart

## Concepts Practiced

- Functions
- Variables
- User input
- While loop
- If / elif / else conditions
- String methods
- `len()`
- `split()`
- `splitlines()`
- Return values
- f-strings
- - File reading
- `open()`
- `read()`
- `close()`
- `try / except`
- `FileNotFoundError`
- Function reuse
- - Lists
- Dictionaries
- Tuples
- Sorting
- Lambda function
- For loops
- String cleaning
- - Regular expressions
- `import re`
- `re.findall()`
- Regex patterns
- - JSON
- `import json`
- `json.dump()`
- Writing files
- Result dictionaries
- - SQLite
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

## How to Run

First install dependencies:

```bash
pip install -r requirements.txt
```

Then run the program:

```bash
python main.py
```

### Example File Test

Choose option `2` and enter:

```text
data/sample.txt
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
- Web page text analysis
- Project refactoring into multiple files