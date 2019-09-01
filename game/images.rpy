############## All images used in the game are define in this file ##############

# Image is a kind of function in renpy which defines a image.
# I have used the size() function in the indented block of image so what that size() fuction
# do is it take (width,height) and it change the size of the image as per your requirements.




############## Mars Rover Spirit Pngs #############

# The LR2 is a kind of shortcut to define image it's a python identifer.
image LR2 :
      "images/Rovers_Png/Listening_R2.png"
      size(425,450)

image SR1 :
     "images/Rovers_Png/Simple_R1.png"
     size(400,400)

image SR2 :
     "images/Rovers_Png/Simple_R2.png"
     size(425,450)

image SR3 :
     "images/Rovers_Png/Simple_R3.png"
     size(425,450)

image Eye :
    "images/Rovers_Png/Eyedown_R.png"
    size(425,450)

image LR3 :
    "images/Rovers_Png/img.png"
    size(425,450)

image Nasa = "images/Rovers_Png/Nasa.png"

image SR4 :
     "images/Rovers_Png/Simple_R4.png"
     size(425,450)

image SR5 :
     "images/Rovers_Png/Simple_R5.png"
     size(467,476)

image BR = "images/Rovers_Png/Before.jpg"

image AR = "images/Rovers_Png/After.jpg"

image tilt :
     "images/Rovers_Png/tilt_R.png"
     size(425,450)

image tilt1 :
     "images/Rovers_Png/tilt_R1.png"
     size(425,450)

image tilt2 :
     "images/Rovers_Png/tilt_R2.png"
     size(425,450)




############## AnnaNoid PNGS ##############

image HG :
     "images/GirlRobot_png/Happy_G.png"
     size(425,450)

image LRG :
     "images/GirlRobot_png/Listening_G.png"
     size(400,450)

image SAYG :
      "images/GirlRobot_png/Saying_G.png"
      size(400,450)

image Aasa = "images/GirlRobot_png/Aasa.png"

image goingG :
      "images/GirlRobot_png/going.png"
      size(400,450)

image SG1 :
      "images/GirlRobot_png/Simple_G1.png"
      size(400,450)

image SAYG1 :
      "images/GirlRobot_png/Saying_G.png"
      size(350,400)

image SAYG2 :
      "images/GirlRobot_png/Saying_G.png"
      size(300,350)

image SAYG3 :
      "images/GirlRobot_png/Saying_G.png"
      size(250,300)

image SAYG4 :
      "images/GirlRobot_png/Saying_G.png"
      size(150,250)

image Battery = "images/GirlRobot_png/Battery.png"

image UFO :
     "images/GirlRobot_png/UFO.png"
     size(750,480)




############## This is a short night effect of rover (Spirit) ##############

# Refer line 664 of script.rpy
image RN1 = "images/Rover_N/RN1.jpg"
image RN2 = "images/Rover_N/RN2.jpg"
image RN3 = "images/Rover_N/RN3.jpg"
image RN4 = "images/Rover_N/RN4.jpg"
image RN5 = "images/Rover_N/RN5.jpg"
image RN6 = "images/Rover_N/RN6.jpg"
image RN7 = "images/Rover_N/RN7.jpg"
image RN8 = "images/Rover_N/RN8.jpg"
image RN9 = "images/Rover_N/RN9.jpg"
image RN10 = "images/Rover_N/RN10.jpg"





############## The Background images of Game ##############

# The size of these images are Bydefault 1280 X 720.
# So no need to use the size() there.
# only line 143 image is bigger i.e to use size() function there.

image DM = "images/Mars/Daytime_Mars.jpg"
image M1 = "images/Mars/Mars1.jpg"
image M2 = "images/Mars/Mars2.jpg"
image M6 = "images/Mars/Mars6.jpg"
image Comment = "images/Mars/Comment.png"
image M7 :
     "images/Mars/mars_planet_PNG26.png"
     size(800,800)
image HH = "images/Mars/Husband_Hill.jpg"
image HH1 = "images/Mars/Husband_Hill1.jpg"
image MCH = "images/Mars/MC-Hill.jpg"
image Silica = "images/Mars/silica.jpg"
image ME1 = "images/Mars/ME1.jpg"
image ME2 = "images/Mars/ME2.jpg"
image ME3 = "images/Mars/ME3.jpg"
image end = "images/Mars/End.jpg"
image grids = "images/Grids.jpg"





############## These are the images which was used as a background images....#
#....when the ATL block is executed. ##############

# This is a kind of pin block. Like after every 0.09_secs the following image gonna play
# Refer script.rpy file 375 line
image dis :
     "images/Dis/Dis_1.jpg"
     0.09
     "images/Dis/Dis_2.jpg"
     0.09
     "images/Dis/Dis_3.jpg"
     0.09
     "images/Dis/Dis_4.jpg"
     0.09
     "images/Dis/Dis_5.jpg"
     0.09
     "images/Dis/Dis_6.jpg"
     0.09
     "images/Dis/Dis_7.jpg"
     0.09
     "images/Dis/Dis_8.jpg"
     0.09
     "images/Dis/Dis_9.jpg"
     0.09
     "images/Dis/Dis_10.jpg"
     0.09
     "images/Dis/Dis_11.jpg"
     0.09
     "images/Dis/Dis_12.jpg"
     0.09
     "images/Dis/Dis_13.jpg"
     0.09
     "images/Dis/Dis_14.jpg"
     0.09
     "images/Dis/Dis_15.jpg"
     0.09
     "images/Dis/Dis_16.jpg"
     0.09
     "images/Dis/Dis_17.jpg"
     0.09
     repeat

############## Dust_Devils ##############

# Renpy Doesn't support GIFs i.e we have to use the below define block. To make the image act as GIF.
# 0.65 is just a seconds to run the following image.
# Refer line 638 of script.rpy

image DD :
     "images/Dust_Devils/DD1.jpg"
     0.65
     "images/Dust_Devils/DD2.jpg"
     0.65
     "images/Dust_Devils/DD3.jpg"
     0.65
     "images/Dust_Devils/DD4.jpg"
     0.65
     "images/Dust_Devils/DD5.jpg"
     0.65
     "images/Dust_Devils/DD6.jpg"
     0.65
     "images/Dust_Devils/DD7.jpg"
     0.65
     "images/Dust_Devils/DD8.jpg"
     0.65
     repeat

# 0.55 is just a seconds to run the following image.
# Refer line 669 of script.rpy
image RN :
     "images/Rover_N/RN4.jpg"
     0.55
     "images/Rover_N/RN5.jpg"
     0.55
     "images/Rover_N/RN6.jpg"
     0.55
     "images/Rover_N/RN7.jpg"
     0.55
     "images/Rover_N/RN8.jpg"
     0.55
     "images/Rover_N/RN9.jpg"
     0.55
     "images/Rover_N/RN10.jpg"
     0.55
     repeat


################# LOADING Menu #################
# This is a kind of loading menu which was displayed before the game_main_menu appears.
# Refer line 6 of script.rpy
image load :
     "images/Loading/L1.jpg"
     0.68
     "images/Loading/L2.jpg"
     0.68
     "images/Loading/L3.jpg"
     0.68
     "images/Loading/L4.jpg"
     3.0
     repeat
