# characters defined in 'characters.rpy'

style my_style is text:
    size 40
    color "#ffffff"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]

image sure = Text("Sure!", style="my_style")
image welcome = Text("Welcome", style="my_style")

init python:
    import math

    screen_width = 1280
    screen_height = 720

    x_start = screen_width/2
    y_start = screen_height/2

    # count = 800

    def lava_update(st):
        dv = 0.01
        for i in lava_sprites:
            vx = i.x - x_start
            vy = i.y - y_start
            vl = math.hypot(vx, vy)
            distance = 10.0/vl
            i.x += dv*distance * vx
            i.y += dv*distance * vy
            dv += 1.0/count
        return .01


# The game starts here.

label start:
    play music "audio/rubypi.mp3"
    scene theend
    with fade

    "[rai] Pi"

    jump introduction



label end:
#    scene thend
    scene theend
    with fade

    "The end."

    return
