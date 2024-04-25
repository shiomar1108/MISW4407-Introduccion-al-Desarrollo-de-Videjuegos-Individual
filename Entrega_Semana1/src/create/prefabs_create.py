import esper
import pygame
import random
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner

def crear_cuadrado(ecs_world:esper.World, size:pygame.Vector2, 
                   pos:pygame.Vector2, vel:pygame.Vector2, 
                   col:pygame.Color):
    quad_entity = ecs_world.create_entity()
    ecs_world.add_component(quad_entity, CSurface(size=size, color=col) )
    ecs_world.add_component(quad_entity, CTransform(pos=pos) )
    ecs_world.add_component(quad_entity, CVelocity(vel=vel) )

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
    crear_cuadrado(world, size, pos, velocity, color)

def create_enemy_spawner(world:esper.World, level_data:dict):
    spawner_entity = world.create_entity()
    world.add_component(spawner_entity,
                        CEnemySpawner(level_data["enemy_spawn_events"]))