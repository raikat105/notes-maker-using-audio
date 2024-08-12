import google.generativeai as genai
import assemblyai as aai

aai.settings.api_key = ASSEMBLY_AI_API_KEY
transcriber = aai.Transcriber()

transcript = transcriber.transcribe(AUDIO_FILE)

print("Transcripted text : " + transcript.text + "\n\n")

genai.configure(api_key = GENAI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

search = "Make proper notes of the following piece of lecture : " + transcript.text

response = model.generate_content(search)
print("Notes : " + response.text)