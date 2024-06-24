import pygame
"""
You are dead, dead dead
You are dead, dead dead
Thought you were hot, guess what you're not
You are dead, dead dead
Brought your whole adventure to a screeching hault
You are dead, dead dead

Your heart has stopped and your brain is cold, you are so so dead
And now your body is starting to mold, you are so so dead
This dimension, cuts like a knife

You are dead, dead dead
What a pitiful waste of a human life
You are dead, dead dead

Your heart has stopped and your brain is cold, you are so so dead
And now your body is starting to mold, you are so so dead

Aww, such a sad sad story
You're gone empty head in the red, game over
You're through, gone
How does it feel to be dead? (You are dead)
Bye bye, you're history, you're through! You're dust (You are dead, dead dead)
I hope you improve your lousy score (You are dead, dead dead)
Adios, see you later, bye bye (You are dead, dead dead)
Try Again

You are dead, dead dead
You are dead, dead dead
You are dead, dead dead
You are dead, dead dead
You are dead, dead dead
You are dead, dead dead
You are dead, dead dead
You are dead, dead dead
You are dead, dead dead
...
You are dead, dead dead
You are dead, dead dead
"""

def you_are_dead():
    pygame.init()
    pygame.mixer.music.load("sfx/total_distortion_you_are_dead.mp3")
    pygame.mixer.music.set_volume(1)
    # sound created by Bobby Richards on youtube music
    pygame.mixer.music.play()

you_are_dead()