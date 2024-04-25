# Entrega Semana 2

|   Nombre                         |   Correo                      | Codigo    | 
|----------------------------------|-------------------------------|-----------|
| Shiomar Alberto Salazar Castillo | s.salazarc@uniandes.edu.co    | 202213359 |


En este repositorio esta el desarrollo de la Entrega 2 de la materia de MISW4407: Introduccion al desarrollo de videojuegos.


### Estructura del proyecto

```
Entrega_Semana2
├─ .gitignore
├─ .pylintrc
├─ .vscode
│  ├─ launch.json
│  └─ settings.json
├─ assets
│  ├─ cfg
│  │  ├─ bullet.json
│  │  ├─ enemies.json
│  │  ├─ level_01.json
│  │  ├─ player.json
│  │  └─ window.json
│  ├─ fnt
│  │  └─ PressStart2P.ttf
│  ├─ img
│  │  ├─ asteroid_01.png
│  │  ├─ asteroid_02.png
│  │  ├─ asteroid_03.png
│  │  ├─ asteroid_04.png
│  │  ├─ bullet.png
│  │  ├─ enemy.png
│  │  ├─ explosion.png
│  │  └─ player.png
│  └─ snd
│     ├─ asteroid.ogg
│     ├─ explosion.ogg
│     ├─ laser.ogg
│     └─ ufo.ogg
├─ esper
│  ├─ py.typed
│  └─ __init__.py
├─ main.py
├─ README.md
├─ requirements.txt
└─ src
   ├─ create
   │  ├─ prefabs_create.py
   │  └─ ___init__.py
   ├─ ecs
   │  ├─ components
   │  │  ├─ c_enemy_spawner.py
   │  │  ├─ c_input_command.py
   │  │  ├─ c_surface.py
   │  │  ├─ c_transform.py
   │  │  ├─ c_velocity.py
   │  │  ├─ tags
   │  │  │  ├─ c_tag_bulet.py
   │  │  │  ├─ c_tag_enemy.py
   │  │  │  ├─ c_tag_player.py
   │  │  │  └─ __init.py
   │  │  └─ __init__.py
   │  ├─ systems
   │  │  ├─ s_collision_enemy_bullet.py
   │  │  ├─ s_collision_player_enemy.py
   │  │  ├─ s_enemy_spawner.py
   │  │  ├─ s_input_player.py
   │  │  ├─ s_movement.py
   │  │  ├─ s_rendering.py
   │  │  ├─ s_screen_bounce.py
   │  │  ├─ s_screen_bullet.py
   │  │  ├─ s_screen_player.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ engine
   │  ├─ game_engine.py
   │  └─ __init__.py
   └─ __init__.py

```