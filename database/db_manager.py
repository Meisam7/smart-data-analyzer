import sqlite3
from datetime import datetime


def create_database():
    connection = sqlite3.connect("analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT NOT NULL,
            source_name TEXT NOT NULL,
            line_count INTEGER,
            word_count INTEGER,
            character_count INTEGER,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_analysis_to_database(source_type, source_name, result):
    connection = sqlite3.connect("analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses (
            source_type,
            source_name,
            line_count,
            word_count,
            character_count,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        source_type,
        source_name,
        result["line_count"],
        result["word_count"],
        result["character_count"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_analysis_history():
    connection = sqlite3.connect("analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, source_type, source_name, line_count, word_count, character_count, created_at
        FROM analyses
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows