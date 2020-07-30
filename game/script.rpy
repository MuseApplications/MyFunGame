# characters defined in 'characters.rpy'

# The game starts here.

label start:
#    scene thend # replace with another file when avaliable
    play music "audio/scene1.mp3" fadeout 2.0
    scene theend
    with fade
    
    "[rai] Pi"

    jump introduction



label end:
#    scene thend
    play music "audio/scene5.mp3" fadeout 2.0
    scene theend
    with fade
    
    "The end."

    return
