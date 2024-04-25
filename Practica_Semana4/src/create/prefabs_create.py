import esper
import pygame
import random
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_hunter_state import CHunterState
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.components.c_player_state import CPlayerState
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.tags.c_tag_bulet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_explosition import CTagExplosion
from src.ecs.components.tags.c_tag_hunter import CTagHunter
from src.ecs.components.tags.c_tag_player import CTagPlayer
from src.engine.service_locator import ServiceLocator

def crear_cuadrado(ecs_world:esper.World, size:pygame.Vector2, 
                   pos:pygame.Vector2, vel:pygame.Vector2, 
                   col:pygame.Color) -> int:
    quad_entity = ecs_world.create_entity()
    ecs_world.add_component(quad_entity, CSurface(size=size, color=col) )
    ecs_world.add_component(quad_entity, CTransform(pos=pos) )
    ecs_world.add_component(quad_entity, CVelocity(vel=vel) )

    return quad_entity

def create_sprite(ecs_world:esper.World, pos:pygame.Vector2, 
                   vel:pygame.Vector2, surface:pygame.Surface) -> int:
    sprite_entity = ecs_world.create_entity()
    ecs_world.add_component(sprite_entity, CTransform(pos=pos) )
    ecs_world.add_component(sprite_entity, CVelocity(vel=vel) )
    ecs_world.add_component(sprite_entity, CSurface.from_surface(surface))

    return sprite_entity

def create_enemy_cuadrado(world:esper.World, pos:pygame.Vector2, enemy_info:dict):
    enemy_surf = ServiceLocator.images_service.get(enemy_info["image"])
    vel_max = enemy_info["velocity_max"]
    vel_min = enemy_info["velocity_min"]
    vel_range_x = vel_min + (random.random() * (vel_max - vel_min))
    vel_range_y = vel_min + (random.random() * (vel_max - vel_min))
    velocity = pygame.Vector2(random.choice([-vel_range_x, vel_range_x]),
                              random.choice([-vel_range_y, vel_range_y]))
    enemy_entity = create_sprite(world, pos, velocity, enemy_surf)
    world.add_component(enemy_entity, CTagEnemy())
    ServiceLocator.sounds_service.play(enemy_info["sound"])

def create_enemy_hunter(world:esper.World, pos:pygame.Vector2, hunter_info:dict):
    enemy_surf = ServiceLocator.images_service.get(hunter_info["image"])
    velocity = pygame.Vector2(0, 0)
    enemy_entity = create_sprite(world, pos, velocity, enemy_surf)
    world.add_component(enemy_entity, CAnimation(hunter_info["animations"]))
    world.add_component(enemy_entity, CHunterState(pos))
    world.add_component(enemy_entity, CTagEnemy())
    world.add_component(enemy_entity, CTagHunter())
    #print("Posiciones de Iniciales los Hunters... " + str(pos.x) + " " + str(pos.y) + " con entidad: " + str(enemy_entity))

def create_enemy_spawner(world:esper.World, level_data:dict):
    spawner_entity = world.create_entity()
    world.add_component(spawner_entity,
                        CEnemySpawner(level_data["enemy_spawn_events"]))
    

def create_player_square (world:esper.World, player_data:dict, player_lvl:dict) -> int:
    player_sprite = ServiceLocator.images_service.get(player_data["image"])
    size = player_sprite.get_size()
    size = (size[0] / player_data["animations"]["number_frames"], size[1])
    pos = pygame.Vector2(player_lvl["position"]["x"]- size[0]/2,
                         player_lvl["position"]["y"]- size[1]/2)
    vel = pygame.Vector2(0,0)
    player_entity = create_sprite(world, pos, vel, player_sprite)
    world.add_component(player_entity, CTagPlayer())
    world.add_component(player_entity, CAnimation(player_data["animations"]))
    world.add_component(player_entity, CPlayerState())

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
    
    surface = ServiceLocator.images_service.get(bullet_data["image"])
    bullet_size = surface.get_rect().size
    pos = pygame.Vector2((start_point.x + player_size[0] / 2) - (bullet_size[0]/2), 
                         (start_point.y + player_size[1] / 2) - (bullet_size[1]/2))

    direccion = (end_destination - start_point)
    direccion = direccion.normalize()
    vel = direccion * bullet_data["velocity"]

    bullet_entity = create_sprite(world, pos, vel, surface)
    world.add_component(bullet_entity, CTagBullet())
    ServiceLocator.sounds_service.play(bullet_data["sound"])

def create_explosion(world:esper.World,explosion_data:dict, pos:pygame.Vector2):
    explosion_surf = ServiceLocator.images_service.get(explosion_data["image"])
    vel = pygame.Vector2(0, 0)
    explosion_entity = create_sprite(world, pos, vel, explosion_surf)
    world.add_component(explosion_entity,
                        CAnimation(explosion_data["animations"]))
    world.add_component(explosion_entity, CTagExplosion())
    ServiceLocator.sounds_service.play(explosion_data["sound"])
    return explosion_entity

