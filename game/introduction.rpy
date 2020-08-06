# Scene 1 Introductions

label introduction:
      scene lockers
      with fade
      play sound "audio/schoolbell.mp3"

      show rubyspritefullneutral:
          xalign 0.25 yalign 1.0
      with dissolve

      rai "Hi, I'm [rai]. I'm a normal teenager."

      rai "Well..."

      rai "Well... not so normal. I like electronics and computers."

      rai "All my friends like to hang out with boys."

      rai "Actually, they're not really my friends."

      show miaspritefullhappy:
          xalign 0.75 yalign 1.0 zoom 1.1

      rai "This is my only real friend, [mia]."

      hide miaspritefullhappy
      with dissolve

      hide rubyspritefullneutral
      show rubyspritefullannoyed:
          xalign 0.25 yalign 1.0
      rai "Most of my electronic projects don't work."

      scene raspberrypi
      # with fade

      rai "But my mom bought me a Raspberry Pi for my birthday. I'm gonna try and make something really cool with it. Not sure what, though."

      jump bowling
