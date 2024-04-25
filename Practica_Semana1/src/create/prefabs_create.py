import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface

def crear_cuadrado(ecs_world:esper.World, size:pygame.Vector2, 
                   pos:pygame.Vector2, vel:pygame.Vector2, 
                   col:pygame.Color):
    quad_entity = ecs_world.create_entity()
    ecs_world.add_component(quad_entity, CSurface(size=size, color=col) )
    ecs_world.add_component(quad_entity, CTransform(pos=pos) )
    ecs_world.add_component(quad_entity, CVelocity(vel=vel) )