import pygame
import esper
from src.ecs.components.c_special_text import CSpecialText
from src.ecs.components.c_surface import CSurface
from src.engine.service_locator import ServiceLocator

def system_special_bullet_charged(world:esper.World, deltatime:float, interface_data:dict):
    components = world.get_components( CSpecialText, CSurface)
    for _, (c_s_b, c_s) in components:
        if not c_s_b.charged or not c_s_b.next:
            color = pygame.Color(255, 0, 0)
            c_s_b.curr_charge_time += deltatime
            if c_s_b.curr_charge_time > c_s_b.charge_time:
                c_s_b.curr_charge_time = c_s_b.charge_time
                c_s_b.charged = True            
        else:
            color = pygame.Color(0, 255, 0)

        font = ServiceLocator.texts_service.get(interface_data["font"], 
                                                interface_data["special"]["size"])
        text = str(round((c_s_b.curr_charge_time / c_s_b.charge_time)* 100) ) + "%"
        c_s.surf = font.render(text, True, color)
        c_s.area = c_s.surf.get_rect()