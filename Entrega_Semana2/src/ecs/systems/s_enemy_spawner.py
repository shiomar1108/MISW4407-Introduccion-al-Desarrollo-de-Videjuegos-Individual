import esper

from src.create.prefabs_create import create_enemy_cuadrado
from src.ecs.components.c_enemy_spawner import CEnemySpawner, SpawnEventData

def system_enemy_spawner(world:esper.World, enemies_data:dict, deltatime:float):
    components = world.get_component(CEnemySpawner)
    c_spw:CEnemySpawner
    for _,  c_spw in components:
        c_spw.actual_time += deltatime
        spw_evt:SpawnEventData
        for spw_evt in c_spw.spawn_event_data:
            if c_spw.actual_time >= spw_evt.time and not spw_evt.procesado:
                spw_evt.procesado = True
                #print('Nuevo Enemigo: ' + spw_evt.enemy_type + ' en el tiempo ' + str(c_spw.actual_time) )
                create_enemy_cuadrado(world,
                              spw_evt.pos,
                              enemies_data[spw_evt.enemy_type])