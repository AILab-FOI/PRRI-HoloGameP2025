import bge

MOVE_SPEED = 8.5
JUMP_FORCE = 7.0

def main():
    cont = bge.logic.getCurrentController()
    own = cont.owner
    keyboard = bge.logic.keyboard
    keys = keyboard.events

    left  = keys[bge.events.AKEY]     == bge.logic.KX_INPUT_ACTIVE
    right = keys[bge.events.DKEY]     == bge.logic.KX_INPUT_ACTIVE
    jump  = keys[bge.events.WKEY]     == bge.logic.KX_INPUT_JUST_ACTIVATED

    vel = own.getLinearVelocity(False)

    if left:
        vel.x = -MOVE_SPEED
    elif right:
        vel.x = MOVE_SPEED
    else:
        vel.x = 0.0

    if jump and abs(vel.z) < 0.1:
        vel.z = JUMP_FORCE

    own.setLinearVelocity(vel, False)

main()