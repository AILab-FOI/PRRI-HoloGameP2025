import bge

def checkPickup(cont):
    own = cont.owner
    sensor = cont.sensors["Collision"]

    if sensor.positive:
        for obj in sensor.hitObjectList:
            if "Cog" in obj:
                obj.endObject()