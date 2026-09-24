import sqlite3

def create_table():
    connection = sqlite3.connect('resume_extractor.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            location TEXT,
            skills TEXT,
            education TEXT,
            work_experience TEXT,
            certifications TEXT
        )
    ''')

    connection.commit()
    connection.close()

def save_candidate(candidate):
    connection = sqlite3.connect('resume_extractor.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO candidates (name, email, phone, location, skills, education, work_experience, certifications)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        candidate["name"],
        candidate["email"],
        candidate["phone"],
        candidate["location"],
        str(candidate["skills"]),
        str(candidate["education"]),    
        str(candidate["work_experience"]),
        str(candidate["certifications"])
    ))

    connection.commit()
    connection.close()

