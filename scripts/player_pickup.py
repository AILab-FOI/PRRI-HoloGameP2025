import bge
import aud
import os

# Build path: from .blend location, go up, into assets/sounds/
blend_path = bge.logic.expandPath("//")
audio_path = os.path.join(blend_path, "..", "sounds", "gear_pickup.mp3")
audio_path = os.path.normpath(audio_path)

device = aud.Device()
gear_sound = aud.Sound(audio_path)

def checkPickup(cont):
    own = cont.owner
    sensor = cont.sensors["Collision"]
    if sensor.positive:
        for obj in sensor.hitObjectList:
            if "Cog" in obj:
                handle = device.play(gear_sound)
                handle.volume = 0.8
                obj.endObject()