from pathlib import Path
import time
import pygame

artist = input("Καλλιτέχνης: ")
song = input("Τραγούδι: ")

filename = filename = f"{artist}-{song}.mp3"

music_folder = Path(__file__).parent / "music"
file_path = music_folder / filename

if file_path.exists():
    print("Το αρχείο βρέθηκε!")

    pygame.init()
    pygame.mixer.music.load(str(file_path))
    pygame.mixer.music.play()

    time.sleep(30)

    pygame.mixer.music.stop()
    pygame.quit()
else:
    print("Το αρχείο δεν βρέθηκε.")
