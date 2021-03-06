import pyttsx3
import subprocess

engine = pyttsx3.init()
engine.setProperty("voice", "com.apple.speech.synthesis.voice.milena")
# Заранее устанавливаем библиотеку ffmpeg-python в операционную систему.
# ffmpeg -i test.mp3 -c:a libopus test_out.ogg
# ["ffmpeg", '-i', audio_path_wav, '-acodec", 'libopus', audio_path_wav, '-y']
# При входящем  текстовом сообщении, модуль subprocess.run позволяет создавать новые процессы,
# а именно - конвертация из *.mp3 в *.ogg файлы.
def text_to_file(text):
    mp3_file = "data/test,"
    out_file = "data/test_out.ogg"
    engine.save_to_file(text, mp3_file)
    engine.runAndWait()
    subprocess.run(["ffmpeg", "-i", mp3_file, "-acodec", "libopus", out_file, "-y"])
    return out_file

   