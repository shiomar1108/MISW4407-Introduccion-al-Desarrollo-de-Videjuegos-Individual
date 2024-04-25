# Entreg Semana 1

|   Nombre                         |   Correo                      | Codigo    | 
|----------------------------------|-------------------------------|-----------|
| Shiomar Alberto Salazar Castillo | s.salazarc@uniandes.edu.co    | 202213359 |


En este repositorio esta el desarrollo de la Entrega 1 de la materia de MISW4407: Introduccion al desarrollo de videojuegos.


### Estructura del proyecto

```
Entrega_Semana1
├─ .gitignore
├─ .pylintrc
├─ .vscode
│  ├─ launch.json
│  └─ settings.json
├─ assets
│  ├─ cfg
│  │  ├─ cfg_00
│  │  │  ├─ enemies.json
│  │  │  ├─ level_01.json
│  │  │  └─ window.json
│  │  ├─ cfg_01
│  │  │  ├─ enemies.json
│  │  │  ├─ level_01.json
│  │  │  └─ window.json
│  │  ├─ cfg_02
│  │  │  ├─ enemies.json
│  │  │  ├─ level_01.json
│  │  │  └─ window.json
│  │  ├─ cfg_03
│  │  │  ├─ enemies.json
│  │  │  ├─ level_01.json
│  │  │  └─ window.json
│  │  ├─ enemies.json
│  │  ├─ level_01.json
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
   │  │  ├─ c_surface.py
   │  │  ├─ c_transform.py
   │  │  ├─ c_velocity.py
   │  │  └─ __init__.py
   │  ├─ systems
   │  │  ├─ s_enemy_spawner.py
   │  │  ├─ s_movement.py
   │  │  ├─ s_rendering.py
   │  │  ├─ s_screen_bounce.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ engine
   │  ├─ game_engine.py
   │  └─ __init__.py
   └─ __init__.py

```