#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.level import level  # Certifique-se de que essa classe existe no arquivo correspondente.

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Cria uma instância da classe Level
                current_level = level(self.window, 'Level1', menu_return)
                level_return = current_level.run()
                # Você pode decidir o que fazer com level_return, se necessário.
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()

# Código principal para iniciar o jogo
if __name__ == "__main__":
    game = Game()
    game.run()