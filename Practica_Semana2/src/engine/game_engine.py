""""Modulo del motor de juego"""

import json
import pygame
import esper
from src.create.prefabs_create import create_enemy_spawner, create_input_player, create_player_square
from src.ecs.systems.s_collision_player_enemy import system_collision_player_enemy
from src.ecs.systems.s_input_player import system_input_player
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner

from src.ecs.components.c_input_command import CInputCommand, CommandPhase
from src.ecs.components.c_velocity import CVelocity

class GameEngine:
    def __init__(self) -> None:

        self._load_json()
        pygame.init()

        pygame.display.set_caption(self.window_data["title"])
        self.screen = pygame.display.set_mode( (self.window_data["size"]["w"], 
                                               self.window_data["size"]["h"]),
                                               pygame.SCALED)
        
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color(self.window_data["bg_color"]["r"],
                                     self.window_data["bg_color"]["g"],
                                     self.window_data["bg_color"]["b"])
        self.is_running = False
        self.framerate = self.window_data["framerate"]
        self.deltatime = 0
        
        self.ecs_world = esper.World()

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        self._player_entity = create_player_square(self.ecs_world, self.player_data, self.level_data["player_spawn"])
        self._player_c_v = self.ecs_world.component_for_entity(self._player_entity, CVelocity)
        create_enemy_spawner(self.ecs_world, self.level_data)
        create_input_player(self.ecs_world)
        

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.deltatime = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            system_input_player(self.ecs_world, event, self._do_action)
            if event.type == pygame.QUIT:
                self.is_running = False
    

    def _update(self):
        system_enemy_spawner(self.ecs_world, self.enemies_data, self.deltatime)
        system_movement(self.ecs_world,self.deltatime)
        system_screen_bounce(self.ecs_world,self.screen)
        system_collision_player_enemy(self.ecs_world, self._player_entity, self.level_data)
        self.ecs_world._clear_dead_entities()

    def _draw(self):
        self.screen.fill(self.bg_color)
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()


    def _clean(self):
        self.ecs_world.clear_database()
        pygame.quit()

    def _load_json(self):
        with open("./assets/cfg/window.json", encoding="utf-8") as window_file:
            self.window_data = json.load(window_file)
        with open("./assets/cfg/enemies.json") as enemies_file:
            self.enemies_data = json.load(enemies_file)
        with open("./assets/cfg/level_01.json") as level_file:
            self.level_data = json.load(level_file)
        with open("./assets/cfg/player.json") as player_file:
            self.player_data = json.load(player_file)
            
    def _do_action(self, c_input:CInputCommand):
        #print(str(c_input.name) + " " + str(c_input.phase) )
        if c_input.name == "PLAYER_LEFT":
            if c_input.phase == CommandPhase.START:
                self._player_c_v.vel.x -= self.player_data["input_velocity"]
            elif c_input.phase == CommandPhase.END:
                self._player_c_v.vel.x += self.player_data["input_velocity"]
        if c_input.name == "PLAYER_RIGHT":
            if c_input.phase == CommandPhase.START:
                self._player_c_v.vel.x += self.player_data["input_velocity"]
            elif c_input.phase == CommandPhase.END:
                self._player_c_v.vel.x -= self.player_data["input_velocity"]
        if c_input.name == "PLAYER_UP":
            if c_input.phase == CommandPhase.START:
                self._player_c_v.vel.y -= self.player_data["input_velocity"]
            elif c_input.phase == CommandPhase.END:
                self._player_c_v.vel.y += self.player_data["input_velocity"]
        if c_input.name == "PLAYER_DOWN":
            if c_input.phase == CommandPhase.START:
                self._player_c_v.vel.y += self.player_data["input_velocity"]
            elif c_input.phase == CommandPhase.END:
                self._player_c_v.vel.y -= self.player_data["input_velocity"]