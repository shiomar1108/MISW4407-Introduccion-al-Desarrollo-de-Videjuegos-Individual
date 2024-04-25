import esper
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_surface import CSurface


def system_animation(world:esper.World, deltatime:float):
    components = world.get_components(CSurface, CAnimation)

    c_s:CSurface
    c_s:CSurface
    for _, (c_s, c_a) in components:
        c_a.current_animation_time -= deltatime
        if c_a.current_animation_time <= 0:
            c_a.current_animation_time = c_a.animations_list[c_a.current_animation].framerate
            c_a.curr_frame += 1
            if c_a.curr_frame > c_a.animations_list[c_a.current_animation].end:
                c_a.curr_frame = c_a.animations_list[c_a.current_animation].start
            rect_surf = c_s.surf.get_rect()
            c_s.area.w = rect_surf.w / c_a.frames
            c_s.area.x = c_s.area.w * c_a.curr_frame
