# characters defined in 'characters.rpy'

init python:
    import math

    glove_x = 0.45
    glove_y = 0.40

    def play(trans, st, at):
        if st > 0.5:
            trans.xalign = glove_x
            return None
        else:
            trans.xalign = glove_x + 0.2*(abs(st - 0.25) - 0.25)
            return 0

    screen_width = 1280
    screen_height = 720

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

    def snow_update(st):
        for i in snow_sprites:
            i.y += 4.0 + renpy.random.random()
            i.x += 3*renpy.random.random() - 1.5
        return 0.0


# The game starts here.

label start:
    scene beginning
    with fade

    "[rai] Pi"

    jump introduction



label end:
#    scene thend
    scene end
    with fade

    "The end."

    return
