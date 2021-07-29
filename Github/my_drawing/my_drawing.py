"""
File: my_drawing.py
Name: Zach Hsu
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow

# Global Variables
window = GWindow(1300, 600)                             # creates a window


def main():
    """
    The analogy between minions and objects that Jerry taught brilliantly demonstrates how the class and object work.
    However, Bob seems to still feel confused about who he is!
    """
    body()
    limbs()
    goggles()
    eyes()
    mouth()
    hair()
    suspender()
    leg()
    message()


def body():
    """
    This function illustrates the torso part of the body.
    """
    torso = GOval(250, 400, x=290, y=100)
    torso.filled = True
    torso.fill_color = 'gold'
    torso.color = 'gold'
    window.add(torso)


def limbs():
    """
    This function illustrates four limbs, two gloves, and three fingers on each hand.
    """
    # Right arm
    right_arm = GPolygon()
    right_arm.add_vertex((540, 310))
    right_arm.add_vertex((538, 330))
    right_arm.add_vertex((620, 270))
    right_arm.add_vertex((610, 260))
    right_arm.filled = True
    right_arm.fill_color = 'gold'
    right_arm.color = 'gold'
    window.add(right_arm)

    # Left arm
    left_arm = GPolygon()
    left_arm.add_vertex((290, 310))
    left_arm.add_vertex((292, 330))
    left_arm.add_vertex((210, 270))
    left_arm.add_vertex((220, 260))
    left_arm.filled = True
    left_arm.fill_color = 'gold'
    left_arm.color = 'gold'
    window.add(left_arm)

    # Right glove
    right_glove = GPolygon()
    right_glove.add_vertex((615, 275))
    right_glove.add_vertex((605, 260))
    right_glove.add_vertex((630, 240))
    right_glove.add_vertex((640, 260))
    right_glove.filled = True
    right_glove.fill_color = 'black'
    window.add(right_glove)

    # Right fingers
    right_finger_1 = GOval(20, 20, x=615, y=230)
    right_finger_1.filled = True
    right_finger_1.fill_color = 'black'
    window.add(right_finger_1)

    right_finger_2 = GOval(35, 35, x=630, y=225)
    right_finger_2.filled = True
    right_finger_2.fill_color = 'black'
    window.add(right_finger_2)

    right_finger_3 = GOval(25, 20, x=633, y=250)
    right_finger_3.filled = True
    right_finger_3.fill_color = 'black'
    window.add(right_finger_3)

    # Left glove
    left_glove = GPolygon()
    left_glove.add_vertex((208, 270))
    left_glove.add_vertex((225, 260))
    left_glove.add_vertex((210, 245))
    left_glove.add_vertex((195, 258))
    left_glove.filled = True
    left_glove.fill_color = 'black'
    window.add(left_glove)

    # Left fingers
    left_finger_1 = GOval(25, 20, x=177, y=245)
    left_finger_1.filled = True
    left_finger_1.fill_color = 'black'
    window.add(left_finger_1)

    left_finger_2 = GOval(35, 35, x=175, y=220)
    left_finger_2.filled = True
    left_finger_2.fill_color = 'black'
    window.add(left_finger_2)

    left_finger_3 = GOval(20, 25, x=205, y=230)
    left_finger_3.filled = True
    left_finger_3.fill_color = 'black'
    window.add(left_finger_3)


def goggles():
    """
    This function illustrates two glasses the bondage of goggles.
    """
    # Outer glasses
    right_outer_glasses = GOval(100, 100, x=415, y=180)
    right_outer_glasses.filled = True
    right_outer_glasses.fill_color = 'silver'
    window.add(right_outer_glasses)

    left_outer_glasses = GOval(100, 100, x=315, y=180)
    left_outer_glasses.filled = True
    left_outer_glasses.fill_color = 'silver'
    window.add(left_outer_glasses)

    # Inner glasses
    right_inner_glasses = GOval(60, 60, x=435, y=200)
    right_inner_glasses.filled = True
    right_inner_glasses.fill_color = 'white'
    window.add(right_inner_glasses)

    left_inner_glasses = GOval(60, 60, x=335, y=200)
    left_inner_glasses.filled = True
    left_inner_glasses.fill_color = 'white'
    window.add(left_inner_glasses)

    # Bondage
    right_bondage = GRect(25, 20, x=515, y=220)
    right_bondage.filled = True
    right_bondage.fill_color = 'black'
    window.add(right_bondage)

    left_bondage = GRect(25, 20, x=290, y=220)
    left_bondage.filled = True
    left_bondage.fill_color = 'black'
    window.add(left_bondage)


def eyes():
    """
    This function illustrates two eyes and two pupils.
    """
    # Right eye
    right_eye = GOval(30, 30, x=457, y=205)
    right_eye.filled = True
    right_eye.fill_color = 'coral'
    window.add(right_eye)

    # Left eye
    left_eye = GOval(30, 30, x=355, y=205)
    left_eye.filled = True
    left_eye.fill_color = 'coral'
    window.add(left_eye)

    # Right pupil
    right_pupil = GOval(10, 10, x=470, y=210)
    right_pupil.filled = True
    right_pupil.fill_color = 'black'
    window.add(right_pupil)

    # Left pupil
    left_pupil = GOval(10, 10, x=368, y=210)
    left_pupil.filled = True
    left_pupil.fill_color = 'black'
    window.add(left_pupil)


def mouth():
    """
    This function illustrates the mouth.
    """
    m = GOval(30, 60, x=400, y=300)
    m.filled = True
    m.fill_color = 'red'
    m.color = 'red'
    window.add(m)


def hair():
    """
    This function illustrates three pieces of hair.
    """
    hair_1 = GLine(400, 100, 360, 50)
    window.add(hair_1)

    hair_2 = GLine(415, 100, 415, 30)
    window.add(hair_2)

    hair_3 = GLine(430, 100, 470, 50)
    window.add(hair_3)


def suspender():
    """
    This function illustrates different parts of the suspender, including braces, buttons, and pockets.
    """
    # Upper part of the suspender
    upper = GRect(140, 50, x=350, y=380)
    upper.filled = True
    upper.fill_color = 'steelblue'
    upper.color = 'steelblue'
    window.add(upper)

    # Braces
    right_brace = GPolygon()
    right_brace.add_vertex((540, 310))
    right_brace.add_vertex((540, 280))
    right_brace.add_vertex((475, 400))
    right_brace.add_vertex((490, 400))
    right_brace.filled = True
    right_brace.fill_color = 'steelblue'
    right_brace.color = 'steelblue'
    window.add(right_brace)

    left_brace = GPolygon()
    left_brace.add_vertex((290, 310))
    left_brace.add_vertex((290, 280))
    left_brace.add_vertex((365, 400))
    left_brace.add_vertex((350, 400))
    left_brace.filled = True
    left_brace.fill_color = 'steelblue'
    left_brace.color = 'steelblue'
    window.add(left_brace)

    # Buttons
    right_button = GOval(12, 12, x=481, y=385)
    right_button.filled = True
    right_button.fill_color = 'black'
    window.add(right_button)

    left_button = GOval(12, 12, x=347, y=385)
    left_button.filled = True
    left_button.fill_color = 'black'
    window.add(left_button)

    # Bottom part of the suspender
    bottom_1 = GPolygon()
    bottom_1.add_vertex((300, 420))
    bottom_1.add_vertex((530, 420))
    bottom_1.add_vertex((500, 475))
    bottom_1.add_vertex((330, 475))
    bottom_1.filled = True
    bottom_1.fill_color = 'steelblue'
    bottom_1.color = 'steelblue'
    window.add(bottom_1)

    bottom_2 = GOval(170, 55, x=330, y=445)
    bottom_2.filled = True
    bottom_2.fill_color = 'steelblue'
    bottom_2.color = 'steelblue'
    window.add(bottom_2)

    # Pockets
    pocket_1 = GRect(75, 50, x=380, y=410)
    pocket_1.filled = True
    pocket_1.fill_color = 'cornflowerblue'
    pocket_1.color = 'darkblue'
    window.add(pocket_1)

    pocket_2 = GOval(75, 20, x=380, y=400)
    pocket_2.filled = True
    pocket_2.fill_color = 'steelblue'
    pocket_2.color = 'darkblue'
    window.add(pocket_2)

    pocket_3 = GRect(75, 20, x=380, y=390)
    pocket_3.filled = True
    pocket_3.fill_color = 'steelblue'
    pocket_3.color = 'steelblue'
    window.add(pocket_3)

    # Pocket icons
    icon_1 = GOval(35, 35, x=399, y=423)
    icon_1.filled = True
    icon_1.fill_color = 'black'
    window.add(icon_1)

    icon_2 = GPolygon()
    icon_2.add_vertex((417, 423))
    icon_2.add_vertex((434, 440))
    icon_2.add_vertex((417, 458))
    icon_2.add_vertex((400, 440))
    icon_2.filled = True
    icon_2.fill_color = 'steelblue'
    icon_2.color = 'steelblue'
    window.add(icon_2)

    icon_3 = GLabel('C')
    icon_3.font = 'Times-20'
    window.add(icon_3, x=408, y=456)


def leg():
    """
    This function illustrates two legs and shoes.
    """
    # Right leg
    right_leg = GPolygon()
    right_leg.add_vertex((440, 500))
    right_leg.add_vertex((490, 480))
    right_leg.add_vertex((480, 520))
    right_leg.add_vertex((460, 520))
    right_leg.filled = True
    right_leg.fill_color = 'steelblue'
    right_leg.color = 'steelblue'
    window.add(right_leg)

    # Left leg
    left_leg = GPolygon()
    left_leg.add_vertex((340, 480))
    left_leg.add_vertex((400, 495))
    left_leg.add_vertex((380, 520))
    left_leg.add_vertex((360, 520))
    left_leg.filled = True
    left_leg.fill_color = 'steelblue'
    left_leg.color = 'steelblue'
    window.add(left_leg)

    # Right shoe
    right_shoe = GOval(60, 30, x=450, y=510)
    right_shoe.filled = True
    right_shoe.fill_color = 'black'
    window.add(right_shoe)

    # Left shoe
    left_shoe = GOval(60, 30, x=330, y=510)
    left_shoe.filled = True
    left_shoe.fill_color = 'black'
    window.add(left_shoe)


def message():
    """
    This function illustrates two pieces of message and imaginary bubbles.
    """
    # Sentences
    sentence_1 = GLabel('Hey, Kevin! Are we OBJECTS!??\n I thought we are BANANAS!')
    sentence_1.font = 'Courier-25'
    window.add(sentence_1, x=690, y=160)

    sentence_2 = GLabel('      Shush! Bob!!\n  You are not helping!!\n   Just get ready at\nconstructor department!')
    sentence_2.font = 'Courier-25'
    window.add(sentence_2, x=680, y=500)

    # Create lines that emphasize speeches
    line_1 = GLine(600, 100, 720, 20)
    window.add(line_1)

    line_2 = GLine(600, 120, 800, 10)
    window.add(line_2)

    line_3 = GLine(600, 190, 720, 210)
    window.add(line_3)

    line_4 = GLine(600, 170, 800, 200)
    window.add(line_4)

    line_5 = GLine(1250, 500, 1220, 400)
    window.add(line_5)

    line_6 = GLine(1240, 520, 1180, 350)
    window.add(line_6)

    line_7 = GLine(1240, 560, 1040, 540)
    window.add(line_7)

    line_8 = GLine(1230, 580, 1100, 570)
    window.add(line_8)


if __name__ == '__main__':
    main()
