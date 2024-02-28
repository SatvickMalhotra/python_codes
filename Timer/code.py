from time import sleep
import random
from playsound import playsound

def get_duration():
    hours = int(input("Enter hours (optional, press Enter to skip): ") or 0)
    minutes = int(input("Enter minutes(optional, press Enter to skip): ")or 0)
    seconds = int(input("Enter seconds: "))
    return hours * 3600 + minutes * 60 + seconds

# Choose a sound effect file
sound_file = "your_sound_effect.mp3"  # Replace with your sound file's path

# Get the duration from user
duration = get_duration()

# The current duration
count = 0

# This loop run until the test condition is false
while count < duration:
    print(count, end="\r")
    sleep(1)
    count += 1

# Play the sound when time's up
playsound(sound_file)
print("Your time is up!")
