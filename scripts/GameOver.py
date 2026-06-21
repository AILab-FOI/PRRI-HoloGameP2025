from bge import logic

cont = logic.getCurrentController()
collision = cont.sensors[0]

if collision.positive:
    hit = collision.hitObject

    print("UDARIO SAM:", hit.name)

    if (
        "Locomotive_Cube" in hit.name
        or "RailwayTrack" in hit.name
    ):
        logic.getCurrentScene().replace("GameOver")