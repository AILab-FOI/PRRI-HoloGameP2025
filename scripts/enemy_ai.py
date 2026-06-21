# enemy_ai.py - Enemy patrol and player detection
# Author: Fran Lesjak

import bge

def init(own):
    if "patrol_dir" not in own:
        own["patrol_dir"] = 1
    if "patrol_timer" not in own:
        own["patrol_timer"] = 0
    if "active" not in own:
        own["active"] = True

def patrol(cont):
    own = cont.owner
    init(own)
    
    if not own["active"]:
        return
    
    speed = 0.04
    own["patrol_timer"] += 1
    
    if own["patrol_timer"] >= 120:
        own["patrol_dir"] *= -1
        own["patrol_timer"] = 0
    
    own.applyMovement([speed * own["patrol_dir"], 0, 0], True)

def detect_player(cont):
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    detection_range = 4.0
    
    for obj in scene.objects:
        if obj.name == "Player.001":
            distance = own.getDistanceTo(obj)
            if distance < detection_range:
                own["active"] = False
                return
    own["active"] = True