import google.generativeai as genai
import assemblyai as aai

aai.settings.api_key = "99ab830bafe641de92bebb85e9a74ebc"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("C:\\Users\\RAIKAT\\OneDrive\\Documents\\speech-ai\\audio.mp3")

print("Transcripted text : " + transcript.text + "\n\n")

genai.configure(api_key = "AIzaSyDvKzgA-SNGHwI2DjcqcNwCad-C0QjVsmU")

model = genai.GenerativeModel('gemini-1.5-flash')

search = "Make proper notes of the following piece of lecture : " + transcript.text

response = model.generate_content(search)
print("Notes : " + response.text)