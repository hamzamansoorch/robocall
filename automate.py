from gtts import gTTS
import os

def text_to_speech(file_path):
    try:
        # Read the contents of the text file
        with open(file_path, 'r') as file:
            text = file.read()
        
        language = 'en'
        speech = gTTS(text=text, lang=language, slow=False)
        
        # Define the save path for the audio file
        save_path = os.path.join(os.path.dirname(file_path), "output.mp3")
        
        speech.save(save_path)
        print("Speech saved successfully at:", save_path)
        
        # Open the audio file
        #os.system("start " + save_path)
        #print("Audio file opened successfully.")
        
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False

# Example usage: Specify the path to your text file
file_path = "C:/Users/hamza.mansoor1/Documents/UiPath/Email_Automation/textToSpeechfile.txt"
text_to_speech(file_path)
