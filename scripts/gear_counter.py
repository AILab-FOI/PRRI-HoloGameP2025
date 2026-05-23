# gear_counter.py - Updates gear pickup counter on HUD
# Author: Jakov Zoricic

import bge
from bge import logic


def update(cont):
    own = cont.owner
    sensor = cont.sensors["Collision"]

    if not sensor.positive:
        return

    # Count gear pickups this frame (objects with the "Cog" game property)
    picked_up = 0
    for obj in sensor.hitObjectList:
        if "Cog" in obj:
            picked_up += 1

    if picked_up == 0:
        return

    # Initialize counter on player if not present
    if "gear_count" not in own:
        own["gear_count"] = 0

    own["gear_count"] += picked_up

    # Update all 4 HUD text objects (one per pyramid side)
    scene = bge.logic.getCurrentScene()
    new_value = str(own["gear_count"])

    for side in ("N", "S", "E", "W"):
        hud_text = scene.objects.get(f"HUDgearCount{side}")
        if hud_text is not None:
            hud_text["Text"] = new_value
       
    #When player reaches 11 gears, game ends and scene is set to winning scene / implemented by ktuksa22        
    if own["gear_count"] >= 11:
        print("GAME WON TRIGGERED")
        logic.getCurrentScene().replace("GameWon")