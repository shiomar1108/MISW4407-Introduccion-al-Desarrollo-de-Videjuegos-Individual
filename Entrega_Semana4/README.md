# Entrega Semana 4

|   Nombre                         |   Correo                      | Codigo    | 
|----------------------------------|-------------------------------|-----------|
| Shiomar Alberto Salazar Castillo | s.salazarc@uniandes.edu.co    | 202213359 |

## Enlace de itch.io

[https://shio1108.itch.io/misw4407-sem4](https://shio1108.itch.io/misw4407-sem4)

[https://shio1108.itch.io/misw4407-sem4-web](https://shio1108.itch.io/misw4407-sem4-web)


## Descripcion
En este repositorio esta el desarrollo de la Entrega 4 de la materia de MISW4407: Introduccion al desarrollo de videojuegos.

Funcionales implementadas:

* Rebote de Asteroides con paredes de Pantallas.
* Limitacion movimiento de jugador en la Pantalla.
* Eliminacion de Balas al salir de la pantalla.
* Colision de Balas con Asteroides.
* Colision de Balas con Hunters.
* Colision de Asteroides con Hunters. (Extra)
* Animacion para Jugador segun movimiento.
* Animacion para Hunters segun movimiento.
* Animacion de Explosiones ante colisiones.
* Sonidos de Disparo.
* Sonidos de Explosion.
* Sonidos de Nuevo Asteroide.
* Sonido de Hunter Chase.
* Se agrega funcionalidad de Pausa.
* Se agrega titulo de Juego.
* Se agrega nueva arma de Homing Missile usando barra espaciadora.

### Commandos de Despliegue del Juego
#### PyInstaller
```
pyinstaller --noconsole --onefile main.py
```

#### Pygbag
```
pygbag main.py
```

### Estructura del proyecto
```
Entrega_Semana4
├─ .gitignore
├─ .pylintrc
├─ .vscode
│  ├─ launch.json
│  └─ settings.json
├─ assets
│  ├─ cfg
│  │  ├─ bullet.json
│  │  ├─ enemies.json
│  │  ├─ explosion.json
│  │  ├─ interface.json
│  │  ├─ level_01.json
│  │  ├─ player.json
│  │  ├─ special.json
│  │  └─ window.json
│  ├─ fnt
│  │  └─ PressStart2P.ttf
│  ├─ img
│  │  ├─ asteroid_01.png
│  │  ├─ asteroid_02.png
│  │  ├─ asteroid_03.png
│  │  ├─ asteroid_04.png
│  │  ├─ bullet.png
│  │  ├─ bullet_especial.png
│  │  ├─ enemy.png
│  │  ├─ explosion.png
│  │  ├─ player.png
│  │  └─ shield.png
│  └─ snd
│     ├─ asteroid.ogg
│     ├─ explosion.ogg
│     ├─ laser.ogg
│     ├─ laser_special.ogg
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
   │  │  ├─ c_animation.py
   │  │  ├─ c_enemy_spawner.py
   │  │  ├─ c_hunter_state.py
   │  │  ├─ c_input_command.py
   │  │  ├─ c_player_state.py
   │  │  ├─ c_special_text.py
   │  │  ├─ c_surface.py
   │  │  ├─ c_transform.py
   │  │  ├─ c_velocity.py
   │  │  ├─ tags
   │  │  │  ├─ c_tag_bulet.py
   │  │  │  ├─ c_tag_enemy.py
   │  │  │  ├─ c_tag_explosition.py
   │  │  │  ├─ c_tag_hunter.py
   │  │  │  ├─ c_tag_player.py
   │  │  │  ├─ c_tag_special_bullet.py
   │  │  │  └─ __init.py
   │  │  └─ __init__.py
   │  ├─ systems
   │  │  ├─ s_animation.py
   │  │  ├─ s_collision_enemy_bullet.py
   │  │  ├─ s_collision_enemy_hunter.py
   │  │  ├─ s_collision_player_enemy.py
   │  │  ├─ s_enemy_spawner.py
   │  │  ├─ s_explosion_animation_end.py
   │  │  ├─ s_hunter_state.py
   │  │  ├─ s_input_player.py
   │  │  ├─ s_movement.py
   │  │  ├─ s_player_state.py
   │  │  ├─ s_rendering.py
   │  │  ├─ s_screen_bounce.py
   │  │  ├─ s_screen_bullet.py
   │  │  ├─ s_screen_player.py
   │  │  ├─ s_special_bullet_charge.py
   │  │  ├─ s_special_bullet_lockon.py
   │  │  ├─ s_special_bullet_movement.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ engine
   │  ├─ game_engine.py
   │  ├─ services
   │  │  ├─ images_service.py
   │  │  ├─ sounds_service.py
   │  │  ├─ texts_service.py
   │  │  └─ __init__.py
   │  ├─ service_locator.py
   │  └─ __init__.py
   └─ __init__.py

```