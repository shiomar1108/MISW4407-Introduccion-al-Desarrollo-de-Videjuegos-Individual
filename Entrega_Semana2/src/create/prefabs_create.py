import esper
import pygame
import random
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.tags.c_tag_bulet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_player import CTagPlayer

def crear_cuadrado(ecs_world:esper.World, size:pygame.Vector2, 
                   pos:pygame.Vector2, vel:pygame.Vector2, 
                   col:pygame.Color) -> int:
    quad_entity = ecs_world.create_entity()
    ecs_world.add_component(quad_entity, CSurface(size=size, color=col) )
    ecs_world.add_component(quad_entity, CTransform(pos=pos) )
    ecs_world.add_component(quad_entity, CVelocity(vel=vel) )

    return quad_entity

def create_enemy_cuadrado(world:esper.World, pos:pygame.Vector2, enemy_info:dict):
    size = pygame.Vector2(enemy_info["size"]["x"], 
                          enemy_info["size"]["y"])
    color = pygame.Color(enemy_info["color"]["r"],
                         enemy_info["color"]["g"],
                         enemy_info["color"]["b"])
    vel_max = enemy_info["velocity_max"]
    vel_min = enemy_info["velocity_min"]
    vel_range_x = vel_min + (random.random() * (vel_max - vel_min))
    vel_range_y = vel_min + (random.random() * (vel_max - vel_min))
    velocity = pygame.Vector2(random.choice([-vel_range_x, vel_range_x]),
                              random.choice([-vel_range_y, vel_range_y]))
    enemy_entity = crear_cuadrado(world, size, pos, velocity, color)
    world.add_component(enemy_entity, CTagEnemy())

def create_enemy_spawner(world:esper.World, level_data:dict):
    spawner_entity = world.create_entity()
    world.add_component(spawner_entity,
                        CEnemySpawner(level_data["enemy_spawn_events"]))
    

def create_player_square (world:esper.World, player_data:dict, player_lvl:dict) -> int:
    size = pygame.Vector2(player_data["size"]["x"], 
                          player_data["size"]["y"])
    color = pygame.Color(player_data["color"]["r"],
                         player_data["color"]["g"],
                         player_data["color"]["b"])
    pos = pygame.Vector2(player_lvl["position"]["x"]- size.x/2,
                         player_lvl["position"]["y"]- size.y/2)
    vel = pygame.Vector2(0,0)
    
    player_entity = crear_cuadrado(world, size, pos, vel, color)
    world.add_component(player_entity, CTagPlayer())

    return player_entity

def create_input_player(world:esper.World):
    input_left = world.create_entity()
    input_right = world.create_entity()
    input_up = world.create_entity()
    input_down = world.create_entity()
    input_bullet = world.create_entity()

    world.add_component(input_left,CInputCommand("PLAYER_LEFT", pygame.K_LEFT))
    world.add_component(input_right,CInputCommand("PLAYER_RIGHT", pygame.K_RIGHT))
    world.add_component(input_up,CInputCommand("PLAYER_UP", pygame.K_UP))
    world.add_component(input_down,CInputCommand("PLAYER_DOWN", pygame.K_DOWN))
    world.add_component(input_bullet,CInputCommand("PLAYER_FIRE", pygame.BUTTON_LEFT))

def create_bullet(world:esper.World, end_destination: pygame.Vector2,
                  start_point: pygame.Vector2, player_size: pygame.Vector2,
                  bullet_data: dict) :
    size = pygame.Vector2(bullet_data["size"]["x"], bullet_data["size"]["y"])
    color = pygame.Color(bullet_data["color"]["r"], bullet_data["color"]["g"],
                           bullet_data["color"]["b"])
    pos = pygame.Vector2(start_point.x + player_size[0] / 2, start_point.y + player_size[1] / 2)

    direccion = (end_destination - start_point)
    direccion = direccion.normalize()
    vel = direccion * bullet_data["velocity"]

    bullet_entity = crear_cuadrado(world, size, pos, vel, color)
    world.add_component(bullet_entity, CTagBullet())