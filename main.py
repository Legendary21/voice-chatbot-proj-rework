from openai import OpenAI as oa
import assemblyai as aai
import sounddevice as sd
from scipy.io.wavfile import write
import threading

freq = 44100
def record_audio():
    freq = 44100
    duration = 7
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    print("Start")
    sd.wait()
    print("Stop")
    return recording

def write_audio(recording, filename):
    write(filename, freq, recording)
    print(f"Audio written to {filename}")

if __name__ == "__main__":
    recording = record_audio()
    filename = "rec.wav"
    write_thread = threading.Thread(target=write_audio, args=(recording, filename))
    write_thread.start()
    write_thread.join()

aai.settings.api_key = "f91d895f7c874b7883db2a4683c89a43"
transcriber = aai.Transcriber()
#lag here of around 5-10 seconds which is obviously not wanted 
#aneesh pls help :D
transcript = transcriber.transcribe("./rec.wav")
print(transcript.text)
f = open("rec.txt", "w")
f.write(transcript.text)