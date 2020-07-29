# characters defined in 'characters.rpy'

# The game starts here.

label start:
    scene thend # replace with another file when avaliable
    play music "audio/scene1.mp3" fadeout 2.0
    scene theend

    "Life of [rai]"

    jump introduction



label end:
    scene thend
    play music "audio/scene5.mp3" fadeout 2.0
    scene theend

    "The end."

    return
