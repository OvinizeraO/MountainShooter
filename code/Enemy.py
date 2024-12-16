#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = 2  # Velocidade de movimento vertical
        self.direction = 1  # 1 para subir, -1 para descer

    def move(self):
        # MH
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # MV
        self.rect.centery += self.direction * self.vertical_speed

        # Colisão com as bordas
        if self.rect.bottom >= WIN_HEIGHT:  # Bate na borda inferior
            self.direction = -1  # Começa a subir
        elif self.rect.top <= 0:  # Bate na borda superior
            self.direction = 1  # Desce com velocidade dobrada
            self.vertical_speed *= 2  # Dobra a velocidade ao descer
        else:
            self.vertical_speed = 2  # Volta a velocidade normal ao subir
