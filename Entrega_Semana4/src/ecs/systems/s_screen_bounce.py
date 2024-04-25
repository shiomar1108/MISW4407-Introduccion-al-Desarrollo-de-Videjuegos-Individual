import pygame
import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_hunter import CTagHunter

def system_screen_bounce(world:esper.World, screen: pygame.Surface):
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CSurface, CVelocity, CTagEnemy)

    c_t: CTransform
    c_s: CSurface
    c_v: CVelocity
    for entity, (c_t, c_s, c_v, c_e) in components:

        if(world.has_component(entity, CTagHunter)):
                continue 
    
        quad_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
        if quad_rect.left < 0 or quad_rect.right > screen_rect.width:
            c_v.vel.x *= -1
            quad_rect.clamp_ip(screen_rect)
            c_t.pos.x = quad_rect.x
        if quad_rect.top < 0 or quad_rect.bottom > screen_rect.height:
            c_v.vel.y *= -1
            quad_rect.clamp_ip(screen_rect)
            c_t.pos.y = quad_rect.y
        