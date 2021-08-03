import pygame
from abc import ABC, abstractmethod
Vector2 = pygame.math.Vector2


class Camera:
    def __init__(self, player, resolution: tuple):
        self.player = player
        self.offset = Vector2(0, 0)
        self.offset_float = Vector2(0, 0)
        self.DISPLAY_W, self.DISPLAY_H =  resolution
        self.CONST = Vector2(-self.DISPLAY_W / 2 + self.player.rect.w / 2,
                            -self.player.ground_y + 20)

    def set_method(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()


class CameraScroll(ABC):
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def scroll(self):
        pass


class Follow(CameraScroll):
    def __init__(self, camera, player):
        CameraScroll(self, camera, player)

    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)

        self.camera.offset.x = int(self.camera.offset_float.x)
        self.camera.offset.y = int(self.camera.offset_float.y)


class Border(CameraScroll):
    def __init__(self, camera, player):
        CameraScroll(self, camera, player)

    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)

        self.camera.offset.x = int(self.camera.offset_float.x)
        self.camera.offset.y = int(self.camera.offset_float.y)

        self.camera.offset.x = max(self.player.left_border, self.offset.x)
        self.camera.offset.x = min(self.camera.offset.x, self.player.right_border - self.camera.DISPLAY_W)


class Auto(CameraScroll):
    def __init__(self, camera, player):
        CameraScroll(self, camera, player)

    def scroll(self):
        self.camera.offset.x += 1