import time

import sounddevice as sd
import torch

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000  # 48000
speaker = ['aidar', 'baya', 'kseniya', 'xenia']  # or 'random'
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu или gpu

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)


# воспроизводим
def speak(text: str):
    audio = model.apply_tts(text=text + "..",
                            speaker=speaker[3],
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 0.95)
    time.sleep(len(audio) / sample_rate + 0.5)
    sd.stop()


# speak("движение распознанноо")