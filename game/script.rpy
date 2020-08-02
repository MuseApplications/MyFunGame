# characters defined in 'characters.rpy'


style my_style is text:
    size 40
    color "#ffffff"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]

image sure = Text("Sure!", style="my_style")
image welcome = Text("Welcome", style="my_style")

# The game starts here.

label start:
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
