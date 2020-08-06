# Scene 6 Science Fair

label fair:
    scene black
    show text "Science Fair" at truecenter
    with fade
    pause 1.5
    with dissolve
    hide text
    with dissolve

    scene sfvolcano
    with fade

    show johnspritefull:
        xalign 0.7 yalign 1.0

    yf "I bet no one ever thought of this!"

    yf "As soon as the pressure from the magma is high enough KABLOOEY!"

    python:

        x_start = 9.0*screen_width/20.0
        y_start = 4.0*screen_height/10.0

        count = 600

        lava = SpriteManager(update=lava_update)
        lava_sprites = [ ]
        blob = Image("lava.png")
        for i in range(count):
            lava_sprites.append(lava.create(blob))
        for i in lava_sprites:
            i.x = x_start + 10*renpy.random.random() - 5
            i.y = y_start + 10*renpy.random.random() - 5

        del blob
        del i

    show expression lava as lava

    pause 2.0

    hide lava

    python:
        del lava
        del lava_sprites


    "The volcano explodes and gets goop all over [yf] and the judges."

    scene sfhand

    show raspberrypisprite:
        xalign 0.60 yalign 0.45

    show solitaire:
        xalign 0.25 yalign 0.5

    show mechanicalglovesprite:
        xalign glove_x yalign glove_y

    show rubyspritefull:
        xalign 0.8 yalign 1.0


    ""

    rai "Oh no, here are the judges. Okay [rai] time to show them what you're made of."

    show mechanicalglovesprite:
        xalign glove_x yalign glove_y
        function play
        repeat
    play sound "audio/mechanicalhand.mp3"

    rai "I turn on the switch. The mechanical hand whirs into action and everyone stands back amazed as it flips over the cards and moves them around."

    rai "Everyone is applauding! Wow, ok thank god. Still got a few bugs to work out..."

    show mechanicalglovesprite:
        xalign glove_x yalign glove_y

    play sound "audio/blueribbon.mp3"
    show bleuribbon:
        xalign 0.65 yalign 0.2

    rai "Hot damn, I even got the blue ribbon!!"

    show johnspritefull:
        xalign 0.5 yalign 1.0

    yf "Hey [rai], congrats on your win."

    rai "Oh, thanks..."

    yf "You know, I think we got off on the wrong foot. I find your scrappy approach admirable."

    yf "I just couldn't admit it because I have a type-A, perfect--did I say perfect? I meant perfectionist--personality."

    yf "Every man in my family for the last four generations has held valedictorian at this high school, and captain of the water polo team, AND decathalon president."

    yf "It's quite a lot of pressure for a young, vigorous man like me, and..."

    python:

        x_start = 11.0*screen_width/10.0
        y_start = 4.0*screen_height/10.0

        count = 1200

        lava = SpriteManager(update=lava_update)
        lava_sprites = [ ]
        lava_pos = None
        blob = Image("lava.png")
        for i in range(count):
            lava_sprites.append(lava.create(blob))
        for i in lava_sprites:
            i.x = x_start + 10*renpy.random.random() - 5
            i.y = y_start + 10*renpy.random.random() - 5

        del blob
        del i

    show expression lava as lava

    pause 2.0

    hide lava

    python:
        del lava
        del lava_sprites
        del lava_pos


    "Suddenly [yf]'s volcano erupts again! It looks like Ms. Gupta, our principal, got gooped. [yf] rushes over to apologize."

    hide johnspritefull

    show miaspritefull:
        xalign 0.25 yalign 1.0 zoom 1.2

    mia "I wasn't sure how to rescue you, so I put more baking soda in the volcano."

    rai "A national hero."

    show jackiespritefull:
        xalign 0.5 yalign 1.0 zoom 1.2

    rk "I see you put my mechanical hand to good use."

    rai "Yes, ma'am."

    rk "And the glove? You did that as well?"

    rai "As a matter of fact..."

label try_again:

if (kiss_flag):
    menu:
        "[mia] did it!":
            jump mia_did_it
        "I did it!":
            jump i_did_it
        "KISS HER":
            jump kiss_again
else:

    menu:
        "[mia] did it!":
            jump mia_did_it
        "I did it!":
            jump i_did_it



label kiss_again:

    rai "NO WHAT STOP"

    rai "[mia] finally speaks up, which is good, because I choked on my own spit and had started couging by this point."

    jump mia_did_it

label i_did_it:

    python:
        snow = SpriteManager(update=snow_update)
        snow_sprites = [ ]
        NaHCO3 = Image("NaHCO3.png")
        for i in range(1000):
            snow_sprites.append(snow.create(NaHCO3))
        for i in snow_sprites:
            r = renpy.random.random()**(2.0/3.0)
            theta = 2*math.pi*renpy.random.random()
            i.x = 200*r*math.cos(theta) + 950
            i.y = 500*r*math.sin(theta) - 500

        del NaHCO3
        del i

    show expression snow as snow

    rai "Something powdery falls onto my head. A lot of it, actually. Is it snowing?! Oh, nope, [mia] just dumped the remainder of the box of baking soda onto my head."

    hide snow

    python:
        del snow
        del snow_sprites

    jump mia_did_it

label mia_did_it:

      mia "It - it was me, ma'am"

      rk "Okay, no more of this ma'am nonsense. You two should join me as inventors! I can do the mechanical stuff well enough, but all these computers and stuff make my head spin."

      rai "Wow, do you really need us? I thought you were an expert at everything."

      rk "No one is an expert at everything! Now I expect you two to help me on my next project: a robotic vacuum!"

      rai "There's already a robotic vacuum!"

      rk "Yes, but mine also does counters, sinks, windows, and toilets."

      jump end
