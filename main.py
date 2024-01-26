import speech_recognition as sr
import tkinter as tk
import sys

trigger_word = "vamos"
trigger_ng = "nuevo juego"
trigger_stop = "salir"
game_length = 11

my_dict = {
    "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
    "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
    "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "veintiuno": 21, "veintidós": 22, "veintitrés": 23, "veinticuatro": 24, "veinticinco": 25,
    "veintiséis": 26, "veintisiete": 27, "veintiocho": 28, "veintinueve": 29, "treinta": 30,
    "treinta y uno": 31, "treinta y dos": 32, "treinta y tres": 33, "treinta y cuatro": 34, "treinta y cinco": 35,
    "treinta y seis": 36, "treinta y siete": 37, "treinta y ocho": 38, "treinta y nueve": 39, "cuarenta": 40,
    "cuarenta y uno": 41, "cuarenta y dos": 42, "cuarenta y tres": 43, "cuarenta y cuatro": 44, "cuarenta y cinco": 45,
    "cuarenta y seis": 46, "cuarenta y siete": 47, "cuarenta y ocho": 48, "cuarenta y nueve": 49, "cincuenta": 50,
}

# Initialize the recognizer
recognizer = sr.Recognizer()

# Declarar la variable scores
scores = {"Player 1": 0, "": 0, "Player 1 Games": 0, "Player 2 Games": 0}

# def check_cond():
#     if scores["Player 1"] > scores["Player 2"]
#         if scores["Player 1"] - scores["Player 2"] >= 2:
             
# Función para verificar las condiciones y comenzar un nuevo juego si es necesario
def check_cond():
    global scores  # Hacer referencia a la variable global

    # Asegurarse de que las claves estén presentes en el diccionario
    if "Player 1" not in scores or "Player 2" not in scores:
        print("Error: Las claves 'Player 1' o 'Player 2' no están presentes en el diccionario.")
        return

    # Definir la longitud del juego y la diferencia mínima requerida
    game_length = 11
    min_difference = 2

    # Verificar si se cumple la condición para comenzar un nuevo juego
    if (
        (scores["Player 1"] >= game_length or scores["Player 2"] >= game_length) and
        abs(scores["Player 1"] - scores["Player 2"]) >= min_difference
    ):
        # Determinar al ganador antes de incrementar los juegos
        current_winner = determine_winner(scores["Player 1"], scores["Player 2"])
        if current_winner is not None:
            # Hay un ganador, incrementar los juegos
            if current_winner == "Player 1":
                scores["Player 1 Games"] += 1
            elif current_winner == "Player 2":
                scores["Player 2 Games"] += 1

            # Reiniciar los marcadores para el nuevo juego
            scores["Player 1"] = 0
            scores["Player 2"] = 0

            # Actualizar la etiqueta del marcador y los juegos
            update_score(scores["Player 1"], scores["Player 2"])
            games_label.config(text=f"Juegos: {scores['Player 1 Games']} - {scores['Player 2 Games']}")
            print("¡Nuevo juego iniciado!")
        
# Function to update the score on the display
def update_score(score_1, score_2):
    score_label.config(text=f"{score_1} - {score_2}")
    scores["Player 1"] = int(score_1)
    scores["Player 2"] = int(score_2)
    check_cond()

# Función para actualizar el marcador con animación
def update_score_with_animation(score_1, score_2):
    score_label.config(text=f"{score_1} - {score_2}")
    scores["Player 1"] = int(score_1)
    scores["Player 2"] = int(score_2)
    check_cond()

    # Realizar la animación cambiando el color del fondo durante un breve periodo
    score_label.config(bg="yellow")  # Color de fondo temporal
    root.after(500, lambda: score_label.config(bg=root.cget("bg")))  # Restaurar el color de fondo original después de 500 milisegundos

# Function to handle voice commands
# def handle_voice_command(phrase):
    # if trigger_word in phrase:
    #     text_array = phrase.split(" ")
    #     text_formatter = []

    #     for word in text_array:
    #         if word.isnumeric():
    #             text_formatter.append(str(word))
    #         elif word in my_dict:
    #             text_formatter.append(str(my_dict[word]))

    #     # Ensure there are at least two elements in text_formatter
    #     if len(text_formatter) >= 2:
    #         update_score(text_formatter[0], text_formatter[1])
    #     else:
    #         print("Incomplete command. Please provide both scores.")
    # # Check if the phrase contains the trigger word to stop the program
    # elif trigger_stop in phrase:
    #     print(">>> CERRANDO EL PROGRAMA <<<")
    #     root.destroy()
    #     sys.exit()

# Función para determinar al ganador o si hay empate
def determine_winner(score_1, score_2):
    if score_1 > score_2:
        return "Player 1"
    elif score_2 > score_1:
        return "Player 2"
    else:
        return None  # Empate

# Function to handle voice commands
def handle_voice_command(phrase):
    global scores  # Hacer referencia a la variable global

    if trigger_word in phrase:
        text_array = phrase.split(" ")
        text_formatter = []

        for word in text_array:
            if word.isnumeric():
                text_formatter.append(str(word))
            elif word in my_dict:
                text_formatter.append(str(my_dict[word]))

        # Asegurarse de que haya al menos dos elementos en text_formatter
        if len(text_formatter) >= 2:
            update_score_with_animation(text_formatter[0], text_formatter[1])
        else:
            print("Comando incompleto. Proporcione ambos puntajes.")
    # Comprobar si la frase contiene la palabra de detención para cerrar el programa
    elif trigger_stop in phrase:
        print(">>> CERRANDO EL PROGRAMA <<<")
        root.destroy()
        sys.exit()
    # Comprobar si la frase contiene el comando para un nuevo juego
    elif trigger_ng in phrase:
        # Verificar si hay un ganador antes de incrementar los juegos
        current_winner = determine_winner(scores["Player 1"], scores["Player 2"])
        if current_winner is not None:
            # Hay un ganador, incrementar los juegos
            if current_winner == "Player 1":
                scores["Player 1 Games"] += 1
            elif current_winner == "Player 2":
                scores["Player 2 Games"] += 1

            # Reiniciar los marcadores para el nuevo juego
            scores["Player 1"] = 0
            scores["Player 2"] = 0

            # Actualizar la etiqueta del marcador y los juegos
            update_score(scores["Player 1"], scores["Player 2"])
            games_label.config(text=f"Juegos: {scores['Player 1 Games']} - {scores['Player 2 Games']}")
        else:
            # En caso de empate, no sumar juegos
            print("Empate. No se suma un nuevo juego.")
    else:
        print("Comando no reconocido. Intente de nuevo.")

# Function to listen for voice commands
def listen_for_voice_command():
    with sr.Microphone() as source:
        try:
            print("Listening for voice command...")
            audio = recognizer.listen(source, timeout=999999)
            print("Processing...")
            phrase = recognizer.recognize_google(audio, language="es-ES").lower()
            print(f"Command: {phrase}")
            handle_voice_command(phrase)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")

    root.after(1000, listen_for_voice_command)

# Create the GUI
root = tk.Tk()
root.title("Ping Pong Score Display")

# Configurar el estilo general
root.geometry("1000x200")  # Tamaño inicial de la ventana
root.configure(bg="#f0f0f0")  # Color de fondo

# Etiqueta de marcador
score_label = tk.Label(root, text="0 - 0", font=("Terminal", 48), bg="#f0f0f0")
score_label.pack(pady=10)

# Etiqueta para mostrar los juegos
games_label = tk.Label(root, text="Juegos: 0 - 0", font=("Terminal", 24), bg="#f0f0f0")
games_label.pack(pady=10)

# Start listening for voice commands
listen_for_voice_command()

# Run the GUI
root.mainloop()