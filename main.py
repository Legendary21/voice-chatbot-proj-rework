from openai import OpenAI as oa
import assemblyai as aai
import sounddevice as sd
from scipy.io.wavfile import write
from dotenv import load_dotenv
import requests,os
from dotenv import load_dotenv

freq = 44100
import sounddevice as sd
from scipy.io.wavfile import write

def record_and_write_audio(filename, duration=7):
    freq = 44100
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    print("Start")
    sd.wait()
    print("Stop")
    
    write(filename, freq, recording)
    print(f"Audio written to {filename}")

if __name__ == "__main__":
    output_filename = "rec.wav"  # Change this to your desired output filename
    record_and_write_audio(output_filename)


aai.settings.api_key = "f91d895f7c874b7883db2a4683c89a43"
transcriber = aai.Transcriber()
#lag here of around 5-10 seconds which is obviously not wanted 
#aneesh pls help :D
transcript = transcriber.transcribe("./rec.wav")
print(transcript.text)
mes = transcript.text

def get(message, apikey, bid, id):
    r = requests.get(
        url=f"http://api.brainshop.ai/get?bid={bid}&key={apikey}&uid={id}&msg={message}"
    )
    return r.json()["cnt"]
print(get(mes,'cU25Ss1SZg7yVZdd',169657,123145))