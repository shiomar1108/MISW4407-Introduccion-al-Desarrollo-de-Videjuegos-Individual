""""Modulo del motor de juego"""

import asyncio
import json
import pygame
import esper
from src.create.prefabs_create import create_bullet, create_enemy_spawner, create_input_player, create_special_bullet_interface, create_special_bullets, create_text_interface, create_player_square
from src.ecs.components.c_special_text import CSpecialText
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bulet import CTagBullet
from src.ecs.systems.s_animation import system_animation
from src.ecs.systems.s_collision_enemy_bullet import system_collision_enemy_bullet
from src.ecs.systems.s_collision_enemy_hunter import system_collision_enemy_hunter
from src.ecs.systems.s_collision_player_enemy import system_collision_player_enemy
from src.ecs.systems.s_explosion_animation_end import system_explosion_animation_end
from src.ecs.systems.s_hunter_state import system_hunter_state
from src.ecs.systems.s_input_player import system_input_player
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_player_state import system_player_state
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner

from src.ecs.components.c_input_command import CInputCommand, CommandPhase
from src.ecs.components.c_velocity import CVelocity
from src.ecs.systems.s_screen_bullet import system_screen_bullet
from src.ecs.systems.s_screen_player import system_screen_player
from src.ecs.systems.s_special_bullet_charge import system_special_bullet_charged
from src.ecs.systems.s_special_bullet_lockon import system_special_bullet_lockon
from src.ecs.systems.s_special_bullet_movement import system_special_bullet_movement

class GameEngine:
    def __init__(self) -> None:

        self._load_json()
        pygame.init()

        pygame.display.set_caption(self.window_data["title"])
        self.screen = pygame.display.set_mode( (self.window_data["size"]["w"], 
                                               self.window_data["size"]["h"]))
        
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color(self.window_data["bg_color"]["r"],
                                     self.window_data["bg_color"]["g"],
                                     self.window_data["bg_color"]["b"])
        self.is_running = False
        self.is_paused = False
        self.framerate = self.window_data["framerate"]
        self.deltatime = 0
        self.special_look_on = None
        self.ecs_world = esper.World()
        self.bullets_count = 0

    async def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            if not self.is_paused:
                self._update()
            self._draw()
            await asyncio.sleep(0)
        self._clean()

    def _create(self):
        self._player_entity = create_player_square(self.ecs_world, self.player_data, self.level_data["player_spawn"])
        self._player_c_v = self.ecs_world.component_for_entity(self._player_entity, CVelocity)
        self._player_c_t = self.ecs_world.component_for_entity(self._player_entity, CTransform)
        self._player_c_s = self.ecs_world.component_for_entity(self._player_entity, CSurface)
        create_enemy_spawner(self.ecs_world, self.level_data)
        create_input_player(self.ecs_world)
        create_text_interface(self.ecs_world, self.interface_data, "title")
        create_text_interface(self.ecs_world, self.interface_data, "controles")
        charge_text_entity = create_special_bullet_interface(self.ecs_world, self.interface_data, self.special_data)
        self._special_bullet_text = self.ecs_world.component_for_entity(charge_text_entity, CSpecialText)
        

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
        self.special_look_on = system_special_bullet_lockon(self.ecs_world)
        if(self.special_look_on != None):
            system_special_bullet_movement(self.ecs_world, self.special_look_on,self.special_data)

        system_player_state(self.ecs_world)
        system_hunter_state(self.ecs_world, self._player_entity, self.enemies_data["Hunter"])
        system_special_bullet_charged(self.ecs_world,self.deltatime,self.interface_data)


        system_screen_bounce(self.ecs_world,self.screen)
        system_screen_player(self.ecs_world,self.screen)
        system_screen_bullet(self.ecs_world, self.screen)

        if(system_collision_enemy_bullet(self.ecs_world, self.explosion_data)):
            self.special_look_on = None
            self._special_bullet_text.next = True
        system_collision_enemy_hunter(self.ecs_world, self.explosion_data)
        system_collision_player_enemy(self.ecs_world, self._player_entity, self.level_data, self.explosion_data)
        system_explosion_animation_end(self.ecs_world)

        system_animation(self.ecs_world,self.deltatime)
        self.ecs_world._clear_dead_entities()
        self.bullets_count = len(self.ecs_world.get_component(CTagBullet))
        #print(self.bullets_count)

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
        with open("./assets/cfg/bullet.json") as bullet_file:
            self.bullet_data = json.load(bullet_file)
        with open("./assets/cfg/explosion.json") as explosion_file:
            self.explosion_data = json.load(explosion_file)
        with open("./assets/cfg/interface.json") as interface_file:
            self.interface_data = json.load(interface_file)
        with open("./assets/cfg/special.json") as special_file:
            self.special_data = json.load(special_file)
            
    def _do_action(self, c_input:CInputCommand):
        #print(str(c_input.name) + " " + str(c_input.phase) )
        if c_input.name == "PAUSE_GAME" and c_input.phase == CommandPhase.START:
            self.is_paused = not self.is_paused
            if self.is_paused:
                self.pause_text_entity = create_text_interface(self.ecs_world, self.interface_data, "pause")
                return
            else:
                self.ecs_world.delete_entity(self.pause_text_entity)

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
        if ( c_input.name == "PLAYER_FIRE" and 
            self.bullets_count < self.level_data["player_spawn"]["max_bullets"] and 
            c_input.phase == CommandPhase.START):
            create_bullet(self.ecs_world, c_input.mouse_pos, self._player_c_t.pos,
                          self._player_c_s.area.size, self.bullet_data)
        if c_input.name == "SPECIAL" and c_input.phase == CommandPhase.START and self._special_bullet_text.charged and self._special_bullet_text.next:
            self._special_bullet_text.charged = False
            self._special_bullet_text.next = False
            self._special_bullet_text.curr_charge_time = 0
            create_special_bullets(self.ecs_world, self._player_c_t.pos, self._player_c_s.area.size ,self.special_data)