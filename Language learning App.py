import tkinter as tk
from tkinter import messagebox
import random
import hashlib
import os

# Vocabulary data for different languages (dictionaries of words and their meanings)
vocabulary = {
    "English": {
        "Hello": "A common greeting",
        "Goodbye": "A farewell",
        "Thank you": "An expression of gratitude",
        "Please": "A polite request",
        "Sorry": "An expression of apology",
        "Friend": "A person whom one knows and with whom one has a bond of mutual affection",
        "Family": "A group consisting of parents and children living together in a household",
        "Home": "The place where one lives permanently",
        "Work": "Activity involving mental or physical effort done to achieve a purpose",
        "Love": "An intense feeling of deep affection",
        "This is a book": "An example sentence",
        "She is my friend": "Another example sentence",
        "I am happy today": "Yet another example sentence",
        "What is your name?": "A question to inquire someone's name",
        "How are you?": "A question asking about one's well-being",
        "Where are you from?": "A question to know someone's place of origin",
        "I like to read books": "A statement expressing a preference",
        "He is a doctor": "A statement about someone's profession",
        "It's raining outside": "A statement about the weather"
    },
    "Spanish": {
        "Hola": "Hello - A common greeting",
        "Adiós": "Goodbye - A farewell",
        "Gracias": "Thank you - An expression of gratitude",
        "Por favor": "Please - A polite request",
        "Lo siento": "Sorry - An expression of apology",
        "Amigo": "Friend - A person whom one knows and with whom one has a bond of mutual affection",
        "Familia": "Family - A group consisting of parents and children living together in a household",
        "Casa": "Home - The place where one lives permanently",
        "Trabajo": "Work - Activity involving mental or physical effort done to achieve a purpose",
        "Amor": "Love - An intense feeling of deep affection",
        "Esto es un libro": "This is a book - An example sentence",
        "Ella es mi amiga": "She is my friend - Another example sentence",
        "Estoy feliz hoy": "I am happy today - Yet another example sentence",
        "¿Cuál es tu nombre?": "What is your name? - A question to inquire someone's name",
        "¿Cómo estás?": "How are you? - A question asking about one's well-being",
        "¿De dónde eres?": "Where are you from? - A question to know someone's place of origin",
        "Me gusta leer libros": "I like to read books - A statement expressing a preference",
        "Él es médico": "He is a doctor - A statement about someone's profession",
        "Está lloviendo afuera": "It's raining outside - A statement about the weather"
    },
    "French": {
        "Bonjour": "Hello - A common greeting",
        "Au revoir": "Goodbye - A farewell",
        "Merci": "Thank you - An expression of gratitude",
        "S'il vous plaît": "Please - A polite request",
        "Désolé": "Sorry - An expression of apology",
        "Ami": "Friend - A person whom one knows and with whom one has a bond of mutual affection",
        "Famille": "Family - A group consisting of parents and children living together in a household",
        "Maison": "Home - The place where one lives permanently",
        "Travail": "Work - Activity involving mental or physical effort done to achieve a purpose",
        "Amour": "Love - An intense feeling of deep affection",
        "C'est un livre": "This is a book - An example sentence",
        "Elle est mon amie": "She is my friend - Another example sentence",
        "Je suis heureux aujourd'hui": "I am happy today - Yet another example sentence",
        "Comment t'appelles-tu ?": "What is your name? - A question to inquire someone's name",
        "Comment ça va ?": "How are you? - A question asking about one's well-being",
        "D'où viens-tu ?": "Where are you from? - A question to know someone's place of origin",
        "J'aime lire des livres": "I like to read books - A statement expressing a preference",
        "Il est médecin": "He is a doctor - A statement about someone's profession",
        "Il pleut dehors": "It's raining outside - A statement about the weather"
    },
    "German": {
        "Hallo": "Hello - A common greeting",
        "Auf Wiedersehen": "Goodbye - A farewell",
        "Danke": "Thank you - An expression of gratitude",
        "Bitte": "Please - A polite request",
        "Entschuldigung": "Sorry - An expression of apology",
        "Freund": "Friend - A person whom one knows and with whom one has a bond of mutual affection",
        "Familie": "Family - A group consisting of parents and children living together in a household",
        "Zuhause": "Home - The place where one lives permanently",
        "Arbeit": "Work - Activity involving mental or physical effort done to achieve a purpose",
        "Liebe": "Love - An intense feeling of deep affection",
        "Das ist ein Buch": "This is a book - An example sentence",
        "Sie ist meine Freundin": "She is my friend - Another example sentence",
        "Ich bin heute glücklich": "I am happy today - Yet another example sentence",
        "Wie heißt du?": "What is your name? - A question to inquire someone's name",
        "Wie geht es dir?": "How are you? - A question asking about one's well-being",
        "Woher kommst du?": "Where are you from? - A question to know someone's place of origin",
        "Ich lese gerne Bücher": "I like to read books - A statement expressing a preference",
        "Er ist Arzt": "He is a doctor - A statement about someone's profession",
        "Es regnet draußen": "It's raining outside - A statement about the weather"
    },
    "Italian": {
        "Ciao": "Hello - A common greeting",
        "Arrivederci": "Goodbye - A farewell",
        "Grazie": "Thank you - An expression of gratitude",
        "Per favore": "Please - A polite request",
        "Mi dispiace": "Sorry - An expression of apology",
        "Amico": "Friend - A person whom one knows and with whom one has a bond of mutual affection",
        "Famiglia": "Family - A group consisting of parents and children living together in a household",
        "Casa": "Home - The place where one lives permanently",
        "Lavoro": "Work - Activity involving mental or physical effort done to achieve a purpose",
        "Amore": "Love - An intense feeling of deep affection",
        "Questo è un libro": "This is a book - An example sentence",
        "Lei è la mia amica": "She is my friend - Another example sentence",
        "Sono felice oggi": "I am happy today - Yet another example sentence",
        "Come ti chiami?": "What is your name? - A question to inquire someone's name",
        "Come stai?": "How are you? - A question asking about one's well-being",
        "Di dove sei?": "Where are you from? - A question to know someone's place of origin",
        "Mi piace leggere libri": "I like to read books - A statement expressing a preference",
        "Lui è un medico": "He is a doctor - A statement about someone's profession",
        "Fuori piove": "It's raining outside - A statement about the weather"
    }
}


USER_DATA_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(',')
                if stored_username == username:
                    return False
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{hash_password(password)}\n")
    return True

def verify_user(username, password):
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
                if stored_username == username and stored_password == hash_password(password):
                    return True
    return False

def register_window():
    def register():
        username = username_entry.get()
        password = password_entry.get()
        if register_user(username, password):
            messagebox.showinfo("Success", "Registration successful! You can now log in.")
            register_win.destroy()
        else:
            messagebox.showerror("Error", "Username already exists. Please choose another.")

    register_win = tk.Toplevel()
    register_win.title("Register")
    register_win.geometry("300x200")
    register_win.configure(bg="#f5deb3")

    tk.Label(register_win, text="Register", font=("Arial", 16, "bold"), bg="#f5deb3").pack(pady=10)
    tk.Label(register_win, text="Username:", bg="#f5deb3").pack()
    username_entry = tk.Entry(register_win)
    username_entry.pack(pady=5)
    tk.Label(register_win, text="Password:", bg="#f5deb3").pack()
    password_entry = tk.Entry(register_win, show='*')
    password_entry.pack(pady=5)
    tk.Button(register_win, text="Register", command=register).pack(pady=10)

def login_window():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if verify_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            login_win.destroy()
            select_language()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("300x200")
    login_win.configure(bg="#f5deb3")

    tk.Label(login_win, text="Login", font=("Arial", 16, "bold"), bg="#f5deb3").pack(pady=10)
    tk.Label(login_win, text="Username:", bg="#f5deb3").pack()
    username_entry = tk.Entry(login_win)
    username_entry.pack(pady=5)
    tk.Label(login_win, text="Password:", bg="#f5deb3").pack()
    password_entry = tk.Entry(login_win, show='*')
    password_entry.pack(pady=5)
    tk.Button(login_win, text="Login", command=login).pack(pady=10)
    tk.Button(login_win, text="Register", command=register_window).pack(pady=10)
    login_win.mainloop()

def display_flashcards(language, num_flashcards):
    language_vocabulary = vocabulary.get(language, {})
    if not language_vocabulary:
        messagebox.showerror("Error", f"No vocabulary available for {language}")
        return
    flashcard_window = tk.Toplevel()
    flashcard_window.title(f"{language} Flashcards")
    flashcard_window.configure(bg="#f5deb3")

    title_label = tk.Label(flashcard_window, text=f"{language} Flashcards", font=("Arial", 18, "bold"), bg="#f5deb3", fg="white")
    title_label.pack(pady=20)

    for _ in range(num_flashcards):
        random_word = random.choice(list(language_vocabulary.keys()))
        meaning = language_vocabulary[random_word]
        flashcard_frame = tk.Frame(flashcard_window, bg="white", padx=20, pady=10)
        flashcard_frame.pack(pady=10)
        word_label = tk.Label(flashcard_frame, text=f"Word: {random_word}", font=("Arial", 14, "bold"), bg="white")
        word_label.pack(anchor="w")
        meaning_label = tk.Label(flashcard_frame, text=f"Meaning: {meaning}", font=("Arial", 12), bg="white")
        meaning_label.pack(anchor="w")

def select_language():
    language_selection_window = tk.Tk()
    language_selection_window.title("Language Learning App")
    language_selection_window.geometry("400x300")
    language_selection_window.configure(bg="#f5deb3")

    title_label = tk.Label(language_selection_window, text="Language Learning App", font=("Arial", 20, "bold"), bg="#f5deb3", fg="grey")
    title_label.pack(pady=20)

    subtitle_label = tk.Label(language_selection_window, text="Select a language to learn:", font=("Arial", 14), bg="#f5deb3", fg="grey")
    subtitle_label.pack(pady=10)

    for language in vocabulary.keys():
        language_button = tk.Button(language_selection_window, text=language, font=("Arial", 12), bg="grey", fg="white", padx=10, pady=5, command=lambda lang=language: display_flashcards(lang, 3))
        language_button.pack(pady=5, fill="x")

    language_selection_window.mainloop()

# Main function
def main():
    login_window()

if __name__ == "__main__":
    main()
