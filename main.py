# Estandar
import pygame as pg
import sys
# Complemento
from settings import *          # Constantes
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:

    """Contructor sin Parametros [Init]"""
    def __init__(self):
        # Inicia - pygame
        pg.init()
        # Inicia - Basico
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

        # propiedades
        pg.mouse.set_visible(False)  # Mouse Invisible
        pg.event.set_grab(True)      # Mouse Evita que se salga de la pantalla
        # E-Self
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
    
    """Instancia los import, Ejecuta 1vez """
    def new_game(self):    
        self.map = Map(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
        
        # Draw Constante
        self.object_renderer = ObjectRenderer(self)
        # Update Constante
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)

    """ El bucle Principal Ejecutara >>> Los 3 Funciones Siguientes """
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def update(self):
        # Update - Basica
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

        # Update - Instancia
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        
    def draw(self):
        # Draw - 2D
        # self.screen.fill('black')
        # self.map.draw()
        # self.player.draw()
        # Draw - 3D
        self.object_renderer.draw()
        self.weapon.draw()

    """ Bucle Principal - Se ejecuta Constantemente """
    def run(self):
        while True:
            #Eventos
            self.check_events()
            #Actualiza Data
            self.update()
            #Dibuja
            self.draw()


# El Inicia
if __name__ == '__main__':
    game = Game()
    game.run()
