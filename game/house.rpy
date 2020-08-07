# scene 4 Back at Rai's house in her room with Mia

label house:
      scene deskback
      with fade

      show ruby half neutral:
          xalign 0.5 yalign 0.08

      show mia half chill:
          xalign 0.825 yalign 0.135

      show raspberrypisprite:
          xalign 0.66 yalign 0.5

      show mechanicalhandsprite:
          xalign 0.5 yalign 0.5

      rai "I bet if I hooked this up with my Raspberry Pi I could make it move. But what should it do?"

      show mia half happy:
          xalign 0.825 yalign 0.135

      mia "I can bake a raspberry pie, but how would that make it move?"

      show ruby half whateva:
          xalign 0.5 yalign 0.08

      show mia half chill:
          xalign 0.825 yalign 0.135

      rai "Not that kind of pie! A P-I pi. It's like a little computer."

      show mia half worry:
          xalign 0.825 yalign 0.135

      mia "Oh. Well, since it's a single hand, maybe you can teach it to play solitaire."

      show ruby half happy:
          xalign 0.5 yalign 0.08

      $kiss_flag = False

menu:
    "That's a great ideal! I'm glad I thought of it!":
        jump mia_dejected
    "That's a great ideal! You're a genius, [mia]!":
        jump mia_happy
    "Kiss her.":
        jump mia_surprised

label mia_surprised:

    $kiss_flag = True

    show ruby half annoyed:
        xalign 0.5 yalign 0.08

    show mia half worry:
      xalign 0.825 yalign 0.135


    rai "Wait what? Uh, yeah, no, let's just forget this ever popped in my head."

menu:
    "That's a great ideal! I'm glad I thought of it!":
        jump mia_dejected
    "That's a great ideal! You're a genius, [mia]!":
        jump mia_happy

label mia_dejected:

    show mia half cry1:
          xalign 0.825 yalign 0.135
    rai "That's a great ideal! I'm glad I thought of it!"

    show ruby half happy:
        xalign 0.5 yalign 0.08

    # show mia dejected

    mia "..."

    jump continue

label mia_happy:

    hide mia half worry
    show mia half happy:
          xalign 0.825 yalign 0.135
    rai "That's a great ideal! You're a genius, [mia]!"

    mia "..."

    jump continue

label continue:

      show ruby half neutral:
         xalign 0.5 yalign 0.08

      show mia half chill:
          xalign 0.825 yalign 0.135

      mia "You know the science fair is tomorrow, can you do it by then?"

      "..."

      mia "Can I help?"

      "..."

      show mia half worry:
          xalign 0.825 yalign 0.135

      mia "I'll get some energy drinks, it sounds like it will be a long night."

      jump bedroom
