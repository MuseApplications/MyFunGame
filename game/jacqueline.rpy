# Scene 3 Jacqueline's house

label jacqueline:
      scene jaqueline

      show text "After school" at truecenter
      with dissolve
      pause 1
      hide text
      with dissolve
      play music "audio/scene2.mp3" fadeout 2.0

      rai "I better check the mail before mom starts nagging..."

      rai "Oh, there's a letter for my neighbor [rk] in here."

      rai "I'm a little nervous going up to her door. When we were growing up, the neigborhood boys swore she was a witch."

      rai "I don't know if she even has a job. I've seen her leave the house maybe two or three times, ever."

      rai "But I don't believe in witches. That's just what you call old ladies who don't act normal. When I grow up, everyone will probably think I'm a witch."

      rai "Next to the door is a gloved hand attached to the wall. I reached for it."

      rai "It grabbed my hand!!! Oh, it's shaking it. That's...okay."

      show text "Welcome" at truecenter
      pause 1.5
      hide text
      with dissolve

      "Off in the distance, a gong sounded."

      rk "Curse that mailman, he's always giving my mail to everyone but me! Next time I'm going to sic my mechanical dog on him."



#      rai "You,"
#
#      rai "You, you,"
#
#      rai "You, you, you have a mechanical dog?"
#

$menu_bitmap = 3

label do_menu:

if menu_bitmap == 0:
     jump choice1_A

if menu_bitmap == 1:
    menu:
         "You have a mechanical dog?":
              jump all_done
         "Are you a witch?":
              jump choice1_B

if menu_bitmap == 2:
    menu:
        "You have a mechanical dog?":
             jump all_done
        "Wut":
             jump choice1_C

if menu_bitmap == 3:
    menu:
         "You... you have a mechanical dog?":
              jump all_done
          
         "Are you a witch?":
              jump choice1_B
          
         "...Wut.":
              jump choice1_C

label choice1_A:
    rai "You have a mechanical dog?"

    jump all_done

label choice1_B:

    $menu_bitmap -= 1
    
    rk "Excuse me? I'll have you know that my myriad accomplishments in locomotion and automation have nothing to do with simple witchcraft, but are in fact the result of my prodigious technological know-how!"

    rai "She seems flustered but doesn't slam the door in my face. Yikes. I'm not sure why I'd ask anyway. Did I think she'd tell me yes?"

    jump do_menu

label choice1_C:

      $menu_bitmap -= 2

      rk "Young lady, did you just say \"what\" but spelled w-u-t?"

      rai "...Yeah..."

      jump do_menu

label all_done:

      rk "Doesn't everyone? Would you like to meet her?"

      rk "Erector! Erector come down and meet this young lady."

      rai "I'm [rai], by the way. And her name is Erector?"

      rk "Yes, I built her when I was your age with an Erector set I stole from my brother. Of course, I didn't add the motorized stuff until I was in college."

      rai "I liked your doorbell, did you create that?"

      rk "Yes, my specialty is mechanical hands, would you like one? It doesn't actually do anything."

      show text "Sure!" at truecenter
      with dissolve
      pause 1
      hide text
      with dissolve

      jump house
