import esper
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.tags.c_tag_explosition import CTagExplosion


def system_explosion_animation_end(world: esper.World):
    components = world.get_components(CTagExplosion, CAnimation)
    for entity, (_c_t_e, c_a) in components:
        if c_a.curr_frame == c_a.animations_list[c_a.current_animation].end:
            world.delete_entity(entity)