import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_special_bullet import CTagSpecialBullet

def system_special_bullet_lockon(world:esper.World) -> int:

    enemy_distance = {}
    components_enemy = world.get_components(CTransform, CTagEnemy)
    bullet = world.get_components(CTransform, CTagSpecialBullet)
    for _, (c_t, _) in bullet:
        for enemy_entity, (c_e_t, _) in components_enemy:
            enemy_distance[enemy_entity] = c_t.pos.distance_to(c_e_t.pos)
    if(len(enemy_distance) > 0):
        enemy = min(enemy_distance, key=enemy_distance.get)
        print("LockOn to enemy: "+str(enemy))
        return enemy
    return None
    
    
    