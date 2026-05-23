# score.py - Coin collection and score tracking
# Author: Lovro Đurđević

import bge

def init(own):
    if "score" not in own:
        own["score"] = 0
    if "coins_collected" not in own:
        own["coins_collected"] = 0

def collect_coin(cont):
    own = cont.owner
    init(own)
    scene = bge.logic.getCurrentScene()
    
    for obj in scene.objects:
        if "Coin" in obj.name:
            distance = own.getDistanceTo(obj)
            if distance < 1.2:
                own["score"] += 10
                own["coins_collected"] += 1
                obj.endObject()
                print(f"[SCORE] +10 | Total: {own['score']}")

def get_score(cont):
    own = cont.owner
    return own.get("score", 0)