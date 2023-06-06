from siege import game
from siege.log import Log


def registrationFinished():
    for content in game.content.getContents():
        if hasattr(content.data().entity, 'item'):
            if hasattr(content.data().entity.item, 'stack'):
                content.data().entity.item.stack = 99999


def register():
    game.onUnregistration.listen(systemUnregistration)
    game.events["registration_finished"].listen(registrationFinished)


def systemUnregistration():
    game.onUnregistration.remove(systemUnregistration)
    game.events["registration_finished"].remove(registrationFinished)
