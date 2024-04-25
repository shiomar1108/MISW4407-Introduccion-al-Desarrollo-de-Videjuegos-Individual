import esper
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_hunter_state import CHunterState, HunterState
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.engine.service_locator import ServiceLocator

def system_hunter_state(world:esper.World, player_entity: int, hunter_data: dict):
    pl_c_t = world.component_for_entity(player_entity, CTransform)

    components = world.get_components(CAnimation, CHunterState, CVelocity, CTransform)
    for _, (c_a,c_h_s,c_v, c_t) in components:
        if c_h_s.state == HunterState.IDLE:
            _do_idle_state(c_a,c_h_s, c_v, c_t, pl_c_t, hunter_data)
        elif c_h_s.state == HunterState.CHASE:
            _do_chase_state(c_a,c_h_s, c_v, c_t, pl_c_t, hunter_data)
        elif c_h_s.state == HunterState.RETURN:
            _do_return_state(c_a,c_h_s, c_v, c_t, pl_c_t, hunter_data)

def _do_idle_state(c_a:CAnimation, c_h_s:CHunterState, c_v:CVelocity, 
                   c_t:CTransform, pl_c_t:CTransform, hunter_data:dict):
    _set_animation(c_a, 1)
    c_v.vel.x = 0
    c_v.vel.y = 0

    dist = c_t.pos.distance_to(pl_c_t.pos)
    if dist < hunter_data["distance_start_chase"]:
        ServiceLocator.sounds_service.play(hunter_data["sound_chase"])
        c_h_s.state = HunterState.CHASE

def _do_chase_state(c_a:CAnimation, c_h_s:CHunterState, c_v:CVelocity,
                    c_t:CTransform, pl_c_t:CTransform, hunter_data:dict):
    _set_animation(c_a, 0)
    c_v.vel = (pl_c_t.pos - c_t.pos).normalize() * hunter_data["velocity_chase"]
    dist = c_h_s.start_pos.distance_to(c_t.pos)
    if dist >= hunter_data["distance_start_return"]:
        c_h_s.state = HunterState.RETURN


def _do_return_state(c_a:CAnimation, c_h_s:CHunterState, c_v:CVelocity,
                     c_t:CTransform, pl_c_t:CTransform, hunter_data:dict):
    _set_animation(c_a, 0)
    c_v.vel = (c_h_s.start_pos - c_t.pos).normalize() * hunter_data["velocity_return"]
    dist = c_h_s.start_pos.distance_to(c_t.pos)
    if dist <= 1:
        c_t.pos.xy = c_h_s.start_pos.xy
        c_h_s.state = HunterState.IDLE

def _set_animation(c_a:CAnimation, num_anim:int):
    if c_a.current_animation != num_anim:
        c_a.current_animation = num_anim
        c_a.current_animation_time = 0
        c_a.curr_frame = c_a.animations_list[c_a.current_animation].start