
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_bulet import CTagBullet


def system_collision_enemy_bullet(world: esper.World):
    components_enemy = world.get_components(CSurface, CTransform, CTagEnemy)
    components_bullet = world.get_components(CSurface, CTransform, CTagBullet)

    c_s:CSurface
    c_t:CTransform
    for enemy_entity, (c_s, c_t, _) in components_enemy:
        ene_rect = c_s.surf.get_rect(topleft=c_t.pos)
        for bullet_entity, (c_b_s, c_b_t, _) in components_bullet:
            bullet_rect = c_b_s.surf.get_rect(topleft=c_b_t.pos)
            if ene_rect.colliderect(bullet_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(bullet_entity)
