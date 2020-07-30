# scene 4 Back at Rai's house in her room with Mia

label house:
      scene house

      play music "audio/scene3.mp3" fadeout 2.0

      rai "I bet if I hooked this up with my Raspberry Pi I could make it move. But what should it do?"

      mia "I can bake a raspberry pie, but how would that make it move?"

      rai "Not that kind of pie! A P-I pi. It's like a little computer."

      mia "Oh. Well, since it's a single hand, maybe you can teach it to play solitaire."

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
    rai "Wait what? Uh, yeah, no, let's just forget this ever popped in my head."
    
menu:
    "That's a great ideal! I'm glad I thought of it!":
        jump mia_dejected
    "That's a great ideal! You're a genius, [mia]!":
        jump mia_happy
  
label mia_dejected:
    # show mia dejected

    jump continue

label mia_happy:
    # show mia happy

    jump continue

label continue:

      mia "You know the science fair is tomorrow, can you do it by then?"

      "..."

      mia "Can I help?"

      "..."

      mia "I'll get some energy drinks, it sounds like it will be a long night."

      jump bedroom
