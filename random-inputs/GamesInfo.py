from ButtonVariables import *

##################### INPUT LISTS #####################
# Additional inputs to do more actions
HOLD_A = C
GROUNDPOUND = D
CIRCLE = E
gcnInputs = [A, HOLD_A, GROUNDPOUND, B, X, Y, L, R, UP_ARROW, LEFT_ARROW, RIGHT_ARROW, DOWN_ARROW, CIRCLE]
n64Inputs = [A, GROUNDPOUND, HOLD_A, B, L, R, LEFT_ARROW, UP_ARROW, DOWN_ARROW, RIGHT_ARROW, CIRCLE]

# output Function
def output(outButton):
    # If the input is left, right, up or down
    if outButton == LEFT_ARROW or outButton == UP_ARROW or outButton == RIGHT_ARROW or outButton == DOWN_ARROW:
        HoldAndReleaseKey(outButton, 0.7)

    # Button A Held
    elif outButton == HOLD_A:
        HoldAndReleaseKey(A, 1)

    # Makes a Groudpound for Mario Games
    elif outButton == GROUNDPOUND:
        HoldAndReleaseKey(A,0.2)
        time.sleep(0.3)
        HoldAndReleaseKey(A,0.2)

    # Turns in a circle
    elif outButton == CIRCLE:
        MultiKeys(DOWN_ARROW, RIGHT_ARROW, 0.2)
        MultiKeys(DOWN_ARROW, LEFT_ARROW, 0.2)
        MultiKeys(UP_ARROW, LEFT_ARROW, 0.2)
        MultiKeys(UP_ARROW, RIGHT_ARROW, 0.2)

    # If the input is a button (A, B, X, Y, R or L)
    else:
        HoldAndReleaseKey(outButton, 0.2)
##############################################

# Used list of games
gameList = {"GCN": gcnInputs,
            "N64": n64Inputs}
