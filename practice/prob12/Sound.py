from winsound import PlaySound, SND_FILENAME
import threading

class Sound:
    
    class SFX():
        WIN = "resource/sounds/win.wav"
        BET = "resource/sounds/chip.wav"
        DEAL = "resource/sounds/cardFlip1.wav"
        AGAIN = "resource/sounds/ding.wav"
        pass

    def PlaySound(self, sfx):
        threading.Thread(target= lambda : PlaySound(str(sfx), SND_FILENAME) ).start()
        


    pass