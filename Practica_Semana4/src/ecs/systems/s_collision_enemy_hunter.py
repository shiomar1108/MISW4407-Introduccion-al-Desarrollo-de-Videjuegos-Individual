import esper
from src.create.prefabs_create import create_explosion
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_hunter import CTagHunter


def system_collision_enemy_hunter(world:esper.World, explosion_info:dict):
    componenets_hunters = world.get_components(CSurface, CTransform, CTagEnemy, CTagHunter)
    components_enemy = world.get_components(CSurface, CTransform, CTagEnemy)

    c_s:CSurface
    c_t:CTransform
    for hunter_entity, (c_s, c_t, _c_t_e, _c_t_h) in componenets_hunters:
        hunter_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
        for enemy_entity, (c_e_s, c_e_t, _) in components_enemy:
            enemy_rect = CSurface.get_area_relative(c_e_s.area, c_e_t.pos)
            if(world.has_component(enemy_entity, CTagHunter)):
                continue 

            if hunter_rect.colliderect(enemy_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(hunter_entity)
                create_explosion(world,explosion_info,c_t.pos)