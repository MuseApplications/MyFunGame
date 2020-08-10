# Scene 1 Introductions

label introduction:
      scene lockers
      with fade
      play sound "audio/schoolbell.mp3"
      play music "audio/JAG-Aug3.mp3"

      show ruby full happy:
          xalign 0.25 yalign 1.0
      with dissolve

      rai "Hi, I'm [rai]. I'm a normal teenager."

      rai "Well..."

      rai "Well... not so normal. I like electronics and computers."

      rai "All my friends like to hang out with boys."

      show ruby full neutral:
          xalign 0.25 yalign 1.0

      rai "Actually, they're not really my friends."

      show ruby full happy:
          xalign 0.25 yalign 1.0

      show mia full happy:
          xalign 0.75 yalign 1.0 zoom 1.1

      rai "This is my only real friend, [mia]."

      hide mia full happy
      with dissolve

      show ruby full whateva:
          xalign 0.25 yalign 1.0
      rai "Most of my electronic projects don't work."

      scene raspberrypi

      rai "But my mom bought me a Raspberry Pi for my birthday. I'm gonna try and make something really cool with it. Not sure what, though."

      jump bowling
