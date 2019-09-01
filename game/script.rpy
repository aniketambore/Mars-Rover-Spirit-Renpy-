################### Main Script File ###################




########## Define Characters ##########

# Define is a fuction to define a character name.

# The name written in a ("") double quotes eg.Spirit is a full name of character.

# But 's' is the shortcut for the name, like wherever we have to make a character action...
#...we just use the shortcut there.But as we defined the charcter name it gonna display...
#...the fullname of character on the screen.

define s = Character("Spirit")
define a = Character("AnnaNoid")
define d = Character("---")




########## Loading menu screen ##########
# This Runs before the game starts.

# The label statement is use to give a name to a place in the program.

# For eg. which was there on the label splashscreen going to work before the game_main_menu opens.

#scene statement clear all images and display a background image.

# scene black is actually a kind of full black screen based on our Resolution in this case ...
#... it is 1280 X 720

# Sound effect can be played with a play sound statement. *Without Looping.

# queue sound statement plays an audio file after the current file finishes playing.

# show statement display an image as per the respective allignment and transition.

# The 'with' statement takes the name of a transition to use.

# The dissolve transition dissolve from one screen to the next.

# Renpy also supports a hide statement, which hides the given image.

# sound can be stopped with a stop music statement .

# The return statement ends the label splashscreen and run the below label.

label splashscreen :
      scene black
      play sound "Music/loading_sound.mp3"
      queue sound "Music/loading_sound.mp3"
      queue sound "Music/loading_sound.mp3"
      queue sound "Music/loading_sound.mp3"
      show load at truecenter with dissolve
      $ renpy.pause(4.0)
      hide load with fade
      stop sound
      return




########## The game starts here ##########
########## Some Mysterious questios about Mars ##########

# The play music statement takes an audio filename to play...
#...Also Audio filename are interpreted relative to the game directory.

# I've made a Music folder in the game directory where you find all the audios used in the game.

# The 'centered' statement is used to define the text in the center of the screen.
# The '{size=+9} is used to increase the size of text, you can increase or decrease it.
# The {cps=20} is used to give a typo effect to the text.

label start:
     play music "Music/After Dark.mp3"
     play sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}On Earth, where there is water, there is life.{/cps}" with squares
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}But, what if we think about some different Planets ?{/cps}"with squares
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}Is that Planet contains water? \n OR \n Maybe it contains some toxic acids? \n OR \n Maybe there is some other living Species?{/cps}"with squares
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}Many Questions appear in our mind, But the Answer is mysterious.{/cps}"with squares
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}To find the answer of this mystery Nasa has sended Rover Spirit on Mars.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}Spirit Launching Date From Earth was \n June 10, 2003, 1:58:47 p.m. EDT(Eastern Daylight Time.){/cps}" with dissolve
     stop sound
     $ renpy.movie_cutscene("Landing.webm") #It takes a .webm file to support a video.
     play sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}Spirit landed on Mars at \n January 04, 2004, 04:35 UTC(Cordinated Universal Time.){/cps}" with squares#    centered "Spirit landed successfully on Mars in a region called Gusev Crater."
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}Gusev Crater was formed three to four billion years ago. \n It was named after Russian astronomer Matvei Gusev in 1976.{/cps}" with squares
     stop sound
     stop music





########## Story Begins ##########

# Every 'with' statement takes a name of transition . eg- 'fade' , 'easeinleft'.

     scene M1 with fade
     show SR1 with easeinleft :
         xalign -0.01
         yalign 0.8
     play sound "Rover_Sounds/Voice1.mp3"
     s "{size=+5}Hello, My name is Mars Rover Spirit."
     screen hbox_screen: #This displays the text in the horizontal box.
          hbox:
            text "~Sol is refered to the duration of solar day on Mars."
     stop sound
     show screen hbox_screen
     play sound "Rover_Sounds/Voice2.mp3"
     s "{size=+5}And I'm on my 90-sol mission !."
     hide screen hbox_screen
     stop sound


     scene black with dissolve
     play music "Music/After Dark.mp3"
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+9}Spirit started taking the Panoramic images of mars. \n Which gives the information about the geological conditions of Mars to the Scientists on Earth. \n To perform on-site Scientific investigations.{/cps}"
     stop sound

     scene M2 with fade
     show SR2 with easeinleft :
          xalign -0.01
          yalign 0.8
     show Comment with easeintop :
          size(300,250)
          xalign 0.23
          yalign 0.24
     play sound "Music/Keyboard.wav"
     "{cps=20}{size=+5}That image was the first color image taken by the Rover Spirit on Mars.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     "{cps=20}{size=+5}Also that image was the highest Resolution image taken on the surface of another Planet.{/cps}"
     stop sound

#

     scene black with dissolve
     play sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+5}On January 21, 2004 (sol 17).{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+5}Spirit accidentally Stopped communicating with mission control team.{/cps}"
     stop music
     $ renpy.movie_cutscene("ConnectionLoss.webm")

     scene black with dissolve
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     play music "Music/beep.mp3"
     centered "{cps=20}{size=+9}On the next day Spirit sended a beep of 7.8 bit/s , confirming that it had received a transmission from Earth.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+9}But still Spirit Was in a Fault Mode. \n It was described as a very serious issue.{/cps}"
     stop sound


     scene black with fade
     show M7 at truecenter
     play sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+9}Nobody knows, what's happen to Spirit?,What's happening on Mars?{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+9}But in Mars Spirit meet with a different Robot.{/cps}"
     stop sound
     stop music

     scene DM with fade
     show Eye with easeinleft :
               xalign -0.01
               yalign 0.8
     show LRG with easeinright :
               xalign 1.00
               yalign 0.8
     play sound "Rover_Sounds/Voice3.mp3"
     s "{size=+5}Heeeey, Who are you ???"
     stop sound
     play sound "Annanoid_sounds/voice1.mp3"
     d "{size=+5}My Name is AnnaNoid ."
     stop sound
     $NM=None
     play sound "Rover_Sounds/Voice4.mp3"

# The menu statement presents a choice too the player.
# It takes an indented block of lines, each consisting of a string followed by a colon.


     menu :
          s "{size=+5}Do you live on Mars ???"
          "Yes" :
               stop sound
               play audio "Annanoid_sounds/Yes.mp3"
               hide Eye
               show LR2 with dissolve :
                         xalign -0.01
                         yalign 0.8
               play sound "Rover_Sounds/Voice5.mp3"
               s "{size=+5}Well, I'm here to explore Mars."

          "No" :
               play audio "Annanoid_sounds/No.mp3"
               $NM="True"
               play sound "Rover_Sounds/Voice6.mp3"
               s "{size=+5}So, How do you came on Mars???"
               show LRG with dissolve :
                        xalign 1.00
                        yalign 0.8
               stop sound
               play sound "Annanoid_sounds/voice2.mp3"
               a "{size=+5}I was by sended by Aasa from planet Kepler-186f."
               hide LR2
               show SR3 with dissolve :
                        xalign -0.01
                        yalign 0.8
               stop sound
               play sound "Rover_Sounds/Voice7.mp3"
               s "{size=+5}What is Aasa???"
               hide LRG
               show SAYG with dissolve :
                        xalign 1.00
                        yalign 0.8
               show Aasa with easeintop :
                          size(225,225)
                          xalign 1.02
                          yalign 0.14
               stop sound
               play sound "Annanoid_sounds/voice3.mp3"
               a "{size=+5}Aasa was (Aliens Aeronautics and Space Administration)."
               stop sound
               play sound "Rover_Sounds/Voice8.mp3"
               s "{size=+5}What was that about?"
               stop sound
               hide SAYG
               show LRG with dissolve :
                        xalign 1.00
                        yalign 0.8
               play sound "Annanoid_sounds/voice4.mp3"
               a "{size=+5}Aasa was an agency of planet Kepler-186f responsible for all the space programs."
               stop sound
               play sound "Rover_Sounds/Voice9.mp3"
               s "{size=+5}What is your Mission?"
               stop sound
               play sound "Annanoid_sounds/voice5.mp3"
               a "{size=+5}I was here to explore Mars?"
               hide Aasa
               hide SR3

     stop sound
     play sound "Annanoid_sounds/voice6.mp3"
     a "{size=+5}Where do you came from???"
     show LRG with dissolve :
             xalign 1.00
             yalign 0.8
     hide LR2
     hide Eye
     show LR3 with dissolve :
              xalign -0.01
              yalign 0.8
     stop sound
     play sound "Rover_Sounds/Voice10.mp3"
     s "{size=+5}I was sended by Nasa from planet Earth."
     stop sound
     play sound "Annanoid_sounds/voice7.mp3"
     a "{size=+5}What is Nasa???"
     hide LRG
     show LRG with dissolve :
              xalign 1.00
              yalign 0.8
     show Nasa with easeintop :
                size(215,215)
                xalign 0.17
                yalign 0.24
     stop sound
     play sound "Rover_Sounds/Voice11.mp3"
     s "{size=+5}NASA was (National Aeronautics and Space Administration)."
     hide Nasa
     hide LRG
     show HG with dissolve :
              xalign 1.00
              yalign 0.8
     stop sound
     play sound "Annanoid_sounds/voice8.mp3"
     a "{size=+5}What was that about?"
     hide LR3
     show SR3 with dissolve :
              xalign -0.01
              yalign 0.8
     stop sound
     play sound "Rover_Sounds/Voice12.mp3"
     s "{size=+5}NASA is an agency resonsible for the space program on Earth."
     stop sound
     play sound "Annanoid_sounds/voice9.mp3"
     a "{size=+5}What was your mission?"
     stop sound
     play sound "Rover_Sounds/Voice13.mp3"
     s "{size=+5}I was here to explore Mars."
     stop sound
     play sound "Annanoid_sounds/voice10.mp3"
     a "{size=+5}OK."

     hide HG
     show goingG with dissolve :
              xalign 1.00
              yalign 0.8
     stop sound
     play sound "Rover_Sounds/Voice14.mp3"
     s "{size=+5}Where are you going???"
     hide goingG
     show LRG with dissolve :
              xalign 1.00
              yalign 0.8
     stop sound
     play sound "Annanoid_sounds/voice11.mp3"
     a "{size=+5}I'm going to my place now."
     stop sound
     play sound "Rover_Sounds/Voice15.mp3"
     s "{size=+5}where???"
     stop sound
     play sound "Annanoid_sounds/voice12.mp3"
     a "{size=+5}Its Bonneville crater."
     stop sound
     play sound "Rover_Sounds/Voice16.mp3"
     s "{size=+5}What is that?"
     stop sound
     play sound "Annanoid_sounds/voice13.mp3"
     a "{size=+5}Bonneville crater is a location above Gusev Crater."
     stop sound
     play sound "Rover_Sounds/Voice17.mp3"
     s "{size=+5}Ok,Now how we gonna meet ?."
     stop sound
     play sound "Annanoid_sounds/voice14.mp3"
     a "{size=+5}We gonna meet tomorrow near Husband Hill."
     stop sound
     play sound "Rover_Sounds/Voice18.mp3"
     s "{size=+5}Ok, Bye \n Take your care."
     hide LRG
     show goingG with dissolve :
              xalign 1.00
              yalign 0.8
     stop sound
     play sound "Annanoid_sounds/voice15.mp3"
     a "{size=+5}Bye."
#
     scene black
     screen hbox_screen1 :
          hbox:
            text "~Sol is refered to the duration of solar day on Mars."
     show screen hbox_screen1
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=13}It's January, 2005. Sol 341.{/cps}"
     hide screen hbox_screen1
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{size=+9}{cps=20}Spirit has now been on Mars for one Earth year and was driving slowly uphill towards the Husband Hill to meet Annanoid.{/cps}"
     stop sound
     scene HH with fade
     show SR4 with easeinleft :
               xalign -0.01
               yalign 0.8
     show SG1 with easeinright :
               xalign 1.00
               yalign 0.8
     play sound "Rover_Sounds/Voice19.mp3"
     s "{size=+5}Hiiii, AnnaNoid. \n How are You??"
     stop sound
     play sound "Annanoid_sounds/voice16.mp3"
     a "{size=+5}I'm Fine Spirit."
     stop sound
     play sound "Annanoid_sounds/voice17.mp3"
     a "{size=+5}Can I ask you a Question??"
     stop sound
     play sound "Rover_Sounds/Voice20.mp3"
     s "{size=+5}Yes."
     stop sound
     play sound "Annanoid_sounds/voice18.mp3"
     menu :
          a "{size=+5}Do you like to Party."
          "Yes" :
               stop sound
               play sound "Rover_Sounds/Voice21.mp3"
               s "{size=+5}Well Yes."
          "No" :
               stop sound
               play sound "Rover_Sounds/Voice22.mp3"
               s "{size=+5}Well No."
     stop sound
     play sound "Rover_Sounds/Voice23.mp3"
     s "{size=+5}But why are you asking me about party???"
     stop sound
     play sound "Annanoid_sounds/voice19.mp3"
     a "{size=+5}Me and my friends were going to Party today."
     stop sound
     play sound "Rover_Sounds/Voice24.mp3"
     s "{size=+5}Where???"
     stop sound
     play sound "Annanoid_sounds/voice20.mp3"
     a "{size=+5}At Husband Hill DJ club."
     stop sound
     play sound "Annanoid_sounds/voice21.mp3"
     a "{size=+5}Do you wanna come ???"
     stop sound
     play sound "Rover_Sounds/Voice25.mp3"
     s "{size=+5}If you was coming to the party then I'm Gonna come for Sure."

     scene black
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=10}{size=+9}Husband Hill DJ Club.{/cps}"
     stop sound

     scene dis with fade
     show LR2 with easeinleft :
               xalign -0.01
               yalign 0.8
     show LRG with easeinright :
               xalign 1.00
               yalign 0.8

     $music = "None.wav"
     play sound "Annanoid_sounds/voice22.mp3"
     menu choice:
          a "{size=+5}Spirit Which type of Music you like???"
          "Dance Music" :
                #jump ilikeD
                $music = "Dance"
          "Bass House" :
                #jump ilikeB
                $music = "Bass"
          "Electro House" :
                #jump ilikeE
                $music = "Electro"
          "Future House" :
                #jump ilikeF
                $music = "Future"

     #label ilikeD :
     if music == "Dance" :
           play sound "Music/Dance1.mp3"
           scene dis with fade
           show LR3 at bounce1D
           show LRG at bounce1GD
           pause 2.9
           show LR3 at bounce2D
           show LRG at bounce2GD
           pause 3.4
           show LR3 at bounce3D
           show LRG at bounce3GD
           pause 15


     #label ilikeB :
     if music == "Bass" :
          play sound "Music/Bass_House1.mp3"
          scene dis with fade
          show LR3 at bounce1B
          show LRG at bounce1GB
          pause 7.5
          show LR3 at bounce2B
          show LRG at bounce2GB
          pause 5.8
          show LR3 at bounce3B
          show LRG at bounce3GB
          pause 1.2
          show LR3 at bounce4B
          show LRG at bounce4GB
          pause 29


     #Label ilikeE :
     if music == "Electro" :
         play sound "Music/Electro_house1.mp3"
         scene dis with fade
         show LR3 at bounce1E
         show LRG at bounce1GE
         pause 5.7
         show LR3 at bounce2E
         show LRG at bounce2GE
         pause 17.7

     #Label ilikeF
     if music == "Future" :
         play sound "Music/future_house1.mp3"
         scene dis with fade
         show LR3 at bounce1F
         show LRG at bounce1GF
         pause 6
         show LR3 at bounce2F
         show LRG at bounce2GF
         pause 7.5
         show LR3 at bounce3F
         show LRG at bounce3GF
         pause 18
     stop sound

     scene HH with fade
     show SR4 with easeinleft :
               xalign -0.01
               yalign 0.8
     show SG1 with easeinright :
               xalign 1.00
               yalign 0.8
     play sound "Rover_Sounds/Voice26.mp3"
     s "{size=+5}It was Really Great."
     stop sound
     play sound "Annanoid_sounds/voice23.mp3"
     a "{size=+5}Yaaaa."
     stop sound
     play sound "Annanoid_sounds/voice24.mp3"
     menu :
        a "{size=+5}Spirit, Do You Enjoyed it !?."
        "Yesss" :
            stop sound
            play sound "Rover_Sounds/Voice27.mp3"
            s "{size=+5}Yesss, it was Amazing."
            stop sound
            play sound "Rover_Sounds/Voice28.mp3"
            s "{size=+5}That Music was Too good."
            stop sound
            play sound "Annanoid_sounds/voice25.mp3"
            a "{size=+5}Hmmmm."
        "No" :
            stop sound
            play sound "Rover_Sounds/Voice29.mp3"
            s "{size=+5}No."
            stop sound
            play sound "Annanoid_sounds/voice26.mp3"
            a "{size=+5}Why???"
            stop sound
            play sound "Rover_Sounds/Voice30.mp3"
            s "{size=+5}Because the party gets ended at a short time."
            stop sound
            play sound "Annanoid_sounds/voice27.mp3"
            a "{size=+5}ooo."

     stop sound
     play sound "Annanoid_sounds/voice28.mp3"
     a "{size=+5}OK, Now I have to go."
     stop sound
     hide SR4
     show SR5 with dissolve :
               xalign -0.01
               yalign 0.8
     play sound "Rover_Sounds/Voice15.mp3"   #Voice15 contains where
     s "{size=+5}Where ???"
     stop sound
     play sound "Annanoid_sounds/voice29.mp3"
     a "{size=+5}It's was only my one year Mission."
     stop sound
     play sound "Rover_Sounds/Voice31.mp3"
     s "{size=+5}???"
     stop sound
     play sound "Annanoid_sounds/voice30.mp3"
     a "{size=+5}Now, I have to go back on Kepler-186f."
     stop sound
     play sound "Rover_Sounds/Voice32.mp3"
     s "{size=+5}But Why???."
     hide SG1
     show SAYG with dissolve :
               xalign 1.00
               yalign 0.8
     show Battery with easeintop :
                      size(225,225)
                      xalign 1.02
                      yalign 0.14
     stop sound
     play sound "Annanoid_sounds/voice31.mp3"
     a "{size=+5}Because My Battery Just Getting shallow day by day."
     stop sound
     play sound "Rover_Sounds/Voice31.mp3"
     s "{size=+5}Aaaaaaaaaaa."
     stop sound
     play sound "Annanoid_sounds/voice32.mp3"
     a "{size=+5}Ok, Bye."
     hide SAYG
     hide Battery
     show goingG with dissolve :
               xalign 1.00
               yalign 0.8
     stop sound
     play sound "Rover_Sounds/Voice33.mp3"
     s "{size=+5}Listen..."
     hide goingG
     show LRG with dissolve :
               xalign 1.00
               yalign 0.8
     stop sound
     play sound "Annanoid_sounds/Yes.mp3"
     a "{size=+5}Yes."
     stop sound
     play sound "Rover_Sounds/Voice34.mp3"
     s "{size=+5}How we gonna meet now???."
     stop sound
     play sound "Annanoid_sounds/voice33.mp3"
     a "{size=+5}I don't know, they gonna send me back to Mars or Not?. But we going to meet soon in Future."
     stop sound
     play sound "Rover_Sounds/Voice35.mp3"
     s "{size=+5}OK, Take your care ,I'm Gonna miss you."
     hide LRG
     show SAYG with dissolve :
               xalign 1.00
               yalign 0.8
     stop sound
     play music "Music/UFO.mp3"
     show UFO with easeintop :
               xalign 1.20
               yalign 0.1
     stop sound
     play sound "Annanoid_sounds/voice34.mp3"
     a "{size=+5}OK, Now I have to go."
     hide UFO
     show UFO with dissolve :
              xalign 1.20
              yalign 0.1
     hide UFO
     show UFO with dissolve :
              xalign 1.20
              yalign 0.2
     hide SAYG
     show LRG with dissolve :
               xalign 1.00
               yalign 0.8
     stop sound
     play sound "Annanoid_sounds/voice35.mp3"
     a "{size=+5}Bye.{w=0.4}{nw}"
     hide LRG
     show SAYG with dissolve :
               xalign 1.00
               yalign 0.7
     hide SAYG
     show SAYG1 with fade :
               xalign 1.00
               yalign 0.6
     hide SAYG1
     show SAYG2 with fade :
               xalign 1.00
               yalign 0.5
     hide SAYG2
     show SAYG3 with fade :
               xalign 1.00
               yalign 0.4
     hide SAYG3
     show SAYG4 with fade :
               xalign 0.98
               yalign 0.45
     hide SAYG4
     show UFO with vpunch :
              xalign 1.20
              yalign 0.26
     hide UFO
     stop sound
     play sound "Annanoid_sounds/voice36.mp3"
     a "{size=+5}................."
     stop music

     scene black with fade
     play music "Music/After Dark.mp3"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=10}{size=+9}Spirit 419 Mars-sol.{/cps}" with squares
     stop sound
     show BR with fade
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     "{size=+5}{cps=17}The solar panels of Spirit was not doing there work properly. The Dust was getting settled on the panels and the power was decreasing day by day.{/cps}" with squares
     stop sound
     hide BR
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=15}{size=+9}It feels like anytime the battery will gets dead.And the connection of Spirit with us will over.{/cps}" with squares
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=15}{size=+9}But Suddenly one Magic was happened.{/cps}" with squares
     show DD with fade
     "{size=+5}Dust Devil Arrived."
     show AR with fade
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     "{size=+5}{cps=15}A luckily appearance of Dust Devil had cleaned Spirit solar panels successfully.{/cps}"
     stop sound
     hide AR
     play sound "Music/Keyboard.wav"
     "{size=+5}{cps=22}Energy Levels of Spirit was dramatically increased and daily science work was expected to be expanded.{/cps}"
     hide DD
     stop sound
     stop music

     scene HH1 with fade
     show SR3 with dissolve :
               xalign -0.01
               yalign 0.8
     play sound "Rover_Sounds/Voice36.mp3"
     s "{size=+5}Hey, My solar panel get's cleaned successfully."
     stop sound
     play sound "Rover_Sounds/Voice37.mp3"
     s "{size=+5}It seems to be, My energy level has been expanded."
     stop sound
     hide SR3
     scene RN1 with dissolve
     scene RN2 with dissolve
     scene RN3 with dissolve
     "{size=+5}Spirit took a 360 degree panorama in real color,which included the whole Gusev crater." with squares
     play music "Music/CAM.mp3"
     scene RN with dissolve
     "{size=+5}At night Spirit observed the moon phobos and Deimos in order to determine their orbits better." with squares
     "{size=+5}Spirit observed the Mars sky and its atmosphere with it's pancam
     to make a proper science campaign." with squares
     stop music

     scene black with fade
     play music "Music/After Dark.mp3"
     play audio "Music/Keyboard.wav"
     centered "{cps=20}{size=+9}Spirit next stop was planned to be the north face of McCool Hill.{/cps}" with squares
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+9}So as, Because of the Martian Winter scientists decided to tilt Spirit from its side to receive appropriate sunlight.{/cps}" with squares
     stop sound
     scene MCH with fade
     show tilt with dissolve :
               xalign -0.01
               yalign 0.8
     play sound "Rover_Sounds/Voice38.mp3"
     s "{size=+5}woooooooof,The winter was started. \n And i'm just get tilted."
     stop sound
     play sound "Rover_Sounds/Voice39.mp3"
     s "{size=+5}But yes, I'm able to receive sunlight here."

     scene black with fade
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=8}{size=+9}On March 16, 2006.{/cps}" with squares
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=20}{size=+9}Spirit getting troublesome due to certain condition.{/cps}" with squares
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=15}{size=+9}As it's front wheel had stopped working.{/cps}" with squares
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=21}{size=+9}Despite this, spirit was still making progress towards McCool Hill \n Because the control team programmed it to drive towards McCool Hill backwards, by dragging its broken wheel.{/cps}" with squares
     stop sound
     scene MCH with fade
     show SR2 with dissolve :
               xalign -0.01
               yalign 0.8
     "{size=+5}Spirit's power was just decreasing day by day." with squares
     hide SR2
     show tilt1 with dissolve :
               xalign -0.01
               yalign 0.8
     "{size=+5}The main concern was the energy level for Spirit." with squares
     scene black with fade
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=17}{size=+9}To increase the amount of light hitting Spirit was parked on a steep as a slope as possible.{/cps}"
     stop sound
     scene MCH with fade
     show tilt1 with dissolve :
               xalign -0.01
               yalign 0.8
     "{size=+5}Due to the critical condition of Spirit, scientists decided to spend the next 8months of Spirit as a tilted stand alone rover ." with squares
     "{size=+5}No drives were attempted by Spirit Because of the low energy level." with squares
     stop music

     scene black with fade
     play music "Music/After Dark.mp3"
     play sound "Music/Keyboard.wav"
     centered "{cps=10}{size=+9}Spirit 1150 Mars sol."
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=21}{size=+9}Sunlight has been arrived, as it seems to be a Summer Martian season.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=17}{size=+9}Spirit was driving backward with its dead wheel by which it was increasing a borehole for itself.{/cps}"
     stop sound
     scene Silica with fade
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=16}{size=+12}But coincidentally the scientists look at the borehole which contains some whitesh sand.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=22}{size=+12}Spirit had founded a patch of bright-toned soil so rich in Silica.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=22}{size=+12}Scientist propose that the water must have been involved in concentrating it.{/cps}"
     stop sound
     stop music

     scene black with fade
     play music "Music/After Dark.mp3"
     play sound "Music/Keyboard.wav"
     centered "{cps=10}{size=+9}On May 1,2009 (sol 1892).{/cps}"
     stop sound
     scene M6 with fade
     show tilt2 with dissolve :
               xalign -0.01
               yalign 0.8
     "{size=+5}Spirit became stuck in soft sand, the machine resting upon a cache of iron,sulfate hidden under a surface of normal-looking soil." with squares
     show tilt2 with dissolve :
               xalign 0.00
               yalign 0.8
     "{size=+5}Spirit was going through the difficultes from it's wheel to gain traction." with squares
     hide tilt2
     show ME1 with fade
     hide M6
     "{size=+5}Scientists simulated the situation on Earth.By means of a rover mock-up and computer models in an attempt to get Spirit back on a track." with squares
     show ME2 with fade
     "{size=+5}To produce the same soil mechanical conditions on earth as those on mars under low gravity and under weak atmospheric pressure was conducted." with squares
     show ME3 with fade
     "{size=+5}In a special sandbox to attempt to simulate the continuity behavior of poorly combine soils under low graviy." with squares
     stop music

     play music "Music/After Dark.mp3"
     scene black with fade
     play sound "Music/Keyboard.wav"
     centered "{cps=22}{size=+9}The last communication with Spirit was on March 22,2010 (sol 2208).{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     centered "{cps=22}{size=+9}Spirit Battery Energy was lost and the mission clock was stopped.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=15}{size=+9}Scientists continued to attempts to regain contact with Spirit until May 25,2011.{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     centered "{cps=16}{size=+9}Whereas Nasa announced the end of contact efforts and the completion of the mission.{/cps}"
     stop sound

     scene end with fade
     play music "Music/After Dark.mp3"
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     "{b}{size=+5}{cps=17}Spirit was never designed to last this long.Spirit was never designed to go through Martian winter and went through three winters successfully.{/b}{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     "{b}{size=+5}{cps=20}Spirit was never designed to survive rover-killing dust stroms, and yet Spirit survived several significant dust stroms.{/b}{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     "{b}{size=+5}{cps=20}Spirit was climbed the Husband Hill, so did Martian mountaineering, yet another thing it was never designed to do.{/b}{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     queue sound "Music/Keyboard.wav"
     "{b}{size=+5}{cps=20}So out of this rover that had a very limited scope of mission begin with, we are able to do this magnificient adventures.{/b}{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     "{b}{size=+5}{cps=20}And Spirit was very successful on that.{/b}{/cps}"
     stop sound
     play sound "Music/Keyboard.wav"
     "{b}{size=+5}{cps=20}So Spirit solved many mysterious question of mars. And the mission completed.{/b}{/cps}"
     stop music

     scene grids with fade
     pause 5.0

     scene black with fade
     centered "{size=+9}The End.{w=3.0}{nw}"








     return
