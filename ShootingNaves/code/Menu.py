#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # Música
        pygame.mixer_music.load('./asset/Menu.flac')
        pygame.mixer_music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        menu_option = 0

        while True:
            # Criação da janela e título
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Shooting", COLOR_ORANGE, ((WIN_WIDTH / 2), 130))
            self.menu_text(50, "Naves", COLOR_ORANGE, ((WIN_WIDTH / 2), 180))

            # Mostra as opções do menu e formata o texto
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 300 + 50 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 300 + 50 * i))

            pygame.display.flip()

            # Verifica eventos - Interação
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fecha o jogo
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # Se uma tecla for pressionada
                    if event.key == pygame.K_DOWN:  # Seta para BAIXO
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # Seta para CIMA
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:  # Tecla ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
