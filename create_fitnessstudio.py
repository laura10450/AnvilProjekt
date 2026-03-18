import sqlite3

conn = sqlite3.connect("fitnessstudio.db")
cursor = conn.cursor()

cursor.executescript("""
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Zahlung;
DROP TABLE IF EXISTS Anmeldung;
DROP TABLE IF EXISTS Mitgliedschaft;
DROP TABLE IF EXISTS Kurs;
DROP TABLE IF EXISTS Trainer;
DROP TABLE IF EXISTS Mitglied;

CREATE TABLE Mitglied (
    MitgliedID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Geburtsdatum TEXT NOT NULL,
    Email TEXT NOT NULL,
    Telefonnummer TEXT
);

CREATE TABLE Trainer (
    TrainerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Spezialisierung TEXT NOT NULL,
    Email TEXT NOT NULL
);

CREATE TABLE Kurs (
    KursID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titel TEXT NOT NULL,
    TrainerID INTEGER NOT NULL,
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID)
);

CREATE TABLE Mitgliedschaft (
    MitgliedschaftID INTEGER PRIMARY KEY AUTOINCREMENT,
    Datum TEXT NOT NULL,
    Preis REAL NOT NULL,
    MitgliedID INTEGER NOT NULL,
    FOREIGN KEY (MitgliedID) REFERENCES Mitglied(MitgliedID)
);

CREATE TABLE Anmeldung (
    AnmeldungID INTEGER PRIMARY KEY AUTOINCREMENT,
    MitgliedID INTEGER NOT NULL,
    KursID INTEGER NOT NULL,
    Anmeldedatum TEXT NOT NULL,
    FOREIGN KEY (MitgliedID) REFERENCES Mitglied(MitgliedID),
    FOREIGN KEY (KursID) REFERENCES Kurs(KursID)
);

CREATE TABLE Zahlung (
    ZahlungID INTEGER PRIMARY KEY AUTOINCREMENT,
    Betrag REAL NOT NULL,
    Zahlungsmethode TEXT NOT NULL,
    AnmeldungID INTEGER NOT NULL UNIQUE,
    FOREIGN KEY (AnmeldungID) REFERENCES Anmeldung(AnmeldungID)
);

INSERT INTO Mitglied (Name, Geburtsdatum, Email, Telefonnummer) VALUES
('Max Mustermann', '2000-05-12', 'max@example.com', '0664123456'),
('Anna Berger', '1998-11-03', 'anna@example.com', '0664987654');

INSERT INTO Trainer (Name, Spezialisierung, Email) VALUES
('Thomas Huber', 'Krafttraining', 'thomas@fitness.at'),
('Lisa Maier', 'Yoga', 'lisa@fitness.at');

INSERT INTO Kurs (Titel, TrainerID) VALUES
('Bodybuilding Basics', 1),
('Morning Yoga', 2);

INSERT INTO Mitgliedschaft (Datum, Preis, MitgliedID) VALUES
('2025-01-01', 49.99, 1),
('2025-01-01', 39.99, 2);

INSERT INTO Anmeldung (MitgliedID, KursID, Anmeldedatum) VALUES
(1, 1, '2025-02-01'),
(2, 2, '2025-02-02');

INSERT INTO Zahlung (Betrag, Zahlungsmethode, AnmeldungID) VALUES
(19.99, 'Kreditkarte', 1),
(14.99, 'Überweisung', 2);
""")

conn.commit()
conn.close()

print("fitnessstudio.db wurde erstellt.")