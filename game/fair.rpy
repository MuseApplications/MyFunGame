# Scene 6 Science Fair

label fair:
      scene black
      show text "Science Fair" at truecenter
      with fade
      pause 1.5
      with dissolve
      hide text
      with dissolve

      scene fair
      with fade
      play music "audio/scene4.mp3" fadeout 2.0


      yf "I bet no one ever thought of this!"

      yf "As soon as the pressure from the magma is high enough KABLOOEY!"

      "The volcano explodes and gets goop all over [yf] and the judges."

      "..."
 
      rai "Oh no, here are the judges. Okay [rai] time to show them what you're made of."

      rai "I turn on the switch. The mechanical hand whirs into action and everyone stands back amazed as it flips over the cards and moves them around."

      rai "Everyone is applauding! Wow, ok thank god. Still got a few bugs to work out..."

      rai "Hot damn, I even got the blue ribbon!!"

      yf "Hey [rai], congrats on your win."

      rai "Oh, thanks..."

      yf "You know, I think we got off on the wrong foot. I find your scrappy approach admirable."

      yf "I just couldn't admit it because I have a type-A, perfect--did I say perfect? I meant perfectionist--personality."

      yf "Every man in my family for the last four generations has held valedictorian at this high school, and captain of the water polo team, AND decathalon president."

      yf "It's quite a lot of pressure for a young, vigorous man like me, and..."

      "Suddenly [yf]'s volcano erupts again! It looks like Ms. Gupta, our principal, got gooped. [yf] rushes over to apologize."

      mia "I wasn't sure how to rescue you, so I put more baking soda in the volcano."

      rai "A national hero."

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

    rai "Something powdery falls onto my head. A lot of it, actually. Is it snowing?! Oh, nope, [mia] just dumped the remainder of the box of baking soda onto my head."

    jump mia_did_it

label mia_did_it:

      mia "It - it was me, ma'am"

      rk "Okay, no more of this ma'am nonsense. You two should join me as inventors! I can do the mechanical stuff well enough, but all these computers and stuff make my head spin."

      rai "Wow, do you really need us? I thought you were an expert at everything."

      rk "No one is an expert at everything! Now I expect you two to help me on my next project: a robotic vacuum!"

      rai "There's already a robotic vacuum!"

      rk "Yes, but mine also does counters, sinks, windows, and toilets."

      jump end
