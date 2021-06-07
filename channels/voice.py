from channels.channel_interface import Channel
from channels.terminal import Colors

from gtts import gTTS
from pygame import mixer
import os


class Voice(Channel):
    name: str = "Terminale"

    def get_input(self) -> str:
        return input(Colors.OKGREEN + "emiliodallatorre: " + Colors.ENDC)

    def output(self, output: str):
        print(Colors.OKCYAN + "Friday:" + Colors.ENDC, output)
        print()
        gTTS(text=output, lang='it').save("output.mp3")
        mixer.init()
        mixer.music.load("output.mp3")
        mixer.music.play()
        os.remove("output.mp3")
