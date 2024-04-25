import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_tag_special_bullet import CTagSpecialBullet

def system_special_bullet_movement(world:esper.World, lockon_entity: int, special_data:dict):

    if(lockon_entity != None):
        el_c_t = world.component_for_entity(lockon_entity, CTransform)
        components = world.get_components(CVelocity, CTransform, CTagSpecialBullet)
        for _, (c_v, c_t, _) in components:
            c_v.vel = (el_c_t.pos - c_t.pos).normalize() * special_data["velocity"]