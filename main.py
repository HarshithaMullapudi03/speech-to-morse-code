import pandas as pd
import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone for input (real-time speech recognition)
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust microphone sensitivity for ambient noise
        print("Please say something...")

        # Capture the audio from the microphone
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use Google Web Speech API for recognition
        text = recognizer.recognize_google(audio)

        text = text.replace(" comma", ",")
        text = text.replace(" period", ".")
        text = text.replace(" question mark", "?")
        text = text.replace(" exclamation mark", "!")
        text = text.replace(" colon", ":")
        text = text.replace(" semicolon", ";")
        text = text.replace(" apostrophe", "'")
        text = text.replace(" quotation mark", '"')
        text = text.replace(" dash", "-")
        text = text.replace(" underscore", "_")
        text = text.replace(" open parenthesis", "(")
        text = text.replace(" close parenthesis", ")")
        text = text.replace(" open bracket", "[")
        text = text.replace(" close bracket", "]")
        text = text.replace(" open brace", "{")
        text = text.replace(" close brace", "}")
        text = text.replace(" slash", "/")
        text = text.replace(" backslash", "\\")
        text = text.replace(" pipe", "|")
        text = text.replace(" tilde", "~")
        text = text.replace(" ampersand", "&")
        text = text.replace(" dollar", "$")
        text = text.replace(" at symbol", "@")
        text = text.replace(" plus", "+")
        text = text.replace(" equals", "=")
        text = text.replace(" less than", "<")
        text = text.replace(" greater than", ">")
        text = text.replace(" tilde", "~")
        text = text.replace(" percent", "%")
        text = text.replace(" caret", "^")
        text = text.replace(" hash", "#")
        text = text.replace(" star", "*")
        text = text.replace(" dot", ".")
        text = text.replace(" space", " ")

        print(text)

        # Ask the user if they want to edit the text
        edit = input("Is there a mistake in the transcription? yes if you want to edit or no to continue (yes/no): ").strip().lower()

        if edit == 'yes':
            # Allow the user to manually edit the transcription
            text = input(f"Edit the text (current: {text}): ").strip()
        
        print(f"Final Transcription: {text}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        text = ""
    except sr.RequestError as e:
        print(f"Error with the request; {e}")
        text = ""

    return text


file_path = "G:\\My Drive\\Interview\\Projects\\speech to morse code\\letters_and_punctuation_to_morse.csv"


df = pd.read_csv(file_path)


def search_letter(word):
    morse_code = ""
    for letter in word: 
        result = df[df['Text'] == letter.upper()] 
        if not result.empty:
            morse_code += (result.iloc[0]['Morse'] + " ")
    if word == "":
        print("error")
    return morse_code

word = speech_to_text()
print(search_letter(word) )


