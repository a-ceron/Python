import os
import pygame as pg

def load_image(name, colorkey=None, scale=1):
    image = pg.image.load(name)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    sound = pg.mixer.Sound(name)

    return sound

def load_png(name):
    """ Load image and return image object"""
    try:
        image = pg.image.load(name)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pg.error as message:
        print( 'Cannot load image:', name )
        raise SystemExit, message
    return image, image.get_rect()