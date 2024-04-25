import pygame
import esper

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_player import CTagPlayer


def system_screen_player(world: esper.World, screen: pygame.Surface):
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CSurface, CTagPlayer)
    for _, (c_t, c_s, _) in components:
        player_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
        if not screen_rect.contains(player_rect):
            player_rect.clamp_ip(screen_rect)
            c_t.pos.xy = player_rect.topleft
