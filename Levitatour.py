import pygame
import random
import time
pygame.init()

_screen_width = 600
_screen_height = 600

_game_window = pygame.display.set_mode((_screen_width, _screen_height))
pygame.display.set_caption('Levitatour')

_white = (255, 255, 255)
_black = (0,0,0)
_red = (255, 0, 0)
_purple = (110, 0, 200)
_brown = (67, 27, 5)
_yellow = (255, 255, 150)
_light_blue = (150, 190, 255)
_bg_for_light_blue = (112, 142, 190)
_clock = pygame.time.Clock()
_fps = 60
_platform_list = []
_font = pygame.font.SysFont(None, 40)
_platform_id = 0
_level = 1

def spawn_platform():
    global _platform_id    
    _platform_x = random.randint(60, int(_screen_width-180))
    _platform_y = 0
    _platform_fill = pygame.draw.rect(_game_window, _black, [_platform_x, _platform_y, 120, 8], border_radius=3)
    _platform_id += 1
    _new_platform = []
    _new_platform.append(_platform_id)
    _new_platform.append(_platform_x)
    _new_platform.append(_platform_y)
    _platform_list.append(_new_platform)
    #print('Platform fill =',_platform_fill)#For Debug
    #print('Platform list =',_platform_list)#For Debug

def game_over(_R, _G, _B):
    global _platform_list, _platform_id
    _start_loop = True
    while _start_loop:
        _game_window.fill((_R, _G, _B))
        _game_over_font = pygame.font.SysFont('Gill Sans', 80)
        _gmovr = _game_over_font.render('GAME OVER', 1, _brown)
        _game_window.blit(_gmovr, [_screen_width/2 - _gmovr.get_width()/2, _screen_height/2 - _gmovr.get_height()/2])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    _platform_list = []
                    _platform_id = 0
                    _start_loop = False
                    gameloop()

def game_win():
    global _platform_list, _platform_id, _level
    _start_loop = True
    while _start_loop:
        _game_window.fill(_yellow)
        _game_win_font = pygame.font.SysFont('Harlow Solid', 65)
        _gmwin = _game_win_font.render('Level '+str(_level)+' Completed', 1, _brown)
        _game_window.blit(_gmwin, [_screen_width/2 - _gmwin.get_width()/2, _screen_height/2 - _gmwin.get_height()/2])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    _platform_list = []
                    _platform_id = 0
                    if _level == 1:
                        _level = 2
                        _start_loop = False
                        gameloop()
                    if _level == 2:
                        _level = 3
                        _start_loop = False
                        gameloop()
                    if _level == 3:
                        _start_loop = False
                        end_credits()
                        break

def end_credits():
    _end_game_loop = True
    while _end_game_loop:
        _game_window.fill(_light_blue)

        _l1 = pygame.font.SysFont('Gill Sans', 38).render('THANKS FOR PLAYING THE GAME!', 1, _black)
        _game_window.blit(_l1, [_screen_width/2 - _l1.get_width()/2, 72])

        _l2 = pygame.font.SysFont('Gill Sans', 35).render('END CREDITS', 1, _black)
        _game_window.blit(_l2, [_screen_width/2 - _l2.get_width()/2, _l1.get_height() + 112])

        pygame.draw.rect(_game_window, _bg_for_light_blue, [20, 206, 560, 177])

        _l3 = _font.render('Game Dev: Zaber', 1, _black)
        _game_window.blit(_l3, [_screen_width/2 - _l3.get_width()/2, 215])

        _l4 = _font.render('Module Used: pygame', 1, _black)
        _game_window.blit(_l4, [_screen_width/2 - _l4.get_width()/2, 241])

        _l5 = _font.render('Learned Basics From: CodeWithHarry', 1, _black)
        _game_window.blit(_l5, [_screen_width/2 - _l5.get_width()/2, 268])

        _l6 = _font.render('Learned Advanced From: Tech with Tim', 1, _black)
        _game_window.blit(_l6, [_screen_width/2 - _l6.get_width()/2, 294])

        _l7 = _font.render('Date of Completion: 15/12/2021', 1, _black)
        _game_window.blit(_l7, [_screen_width/2 - _l7.get_width()/2, 320])

        _l8 = _font.render('Made in 15 Days.', 1, _black)
        _game_window.blit(_l8, [_screen_width/2 - _l8.get_width()/2, 346])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    _end_game_loop = False
                    main_menu()

def gameloop():
    global _platform_list, _fps
    
    _end_game = False
    _game_over = False

    _gravity = 10.0
    _no_gravity = False
    _player_x = 450.0
    _player_y = 0.0
    _player_size = 40
    #_velocity_x = 0
    _velocity_y = 0
    _jump = 20
    _motion = 4.5
    _temp_lst = []
    _save_platform_id = 0
    _plat_id = 0
    _platform_x = 0
    _platform_y = 0
    _jumped = False
    _R = 0.0
    _G = 255.0
    _B = 127.5
    _start_time = time.time()
    _time_limit = 60
    _was_on_platform = False
    _time_limit_updated = False
    _time_value_changed = 0
    _record_platform = 0
    _score = 0

    if _level == 1:
        _platform_speed = 0.6
        _decrease_time_limit = 8
    elif _level == 2:
        _platform_speed = 1
        _decrease_time_limit = 8
    else:
        _platform_speed = 1.2
        _decrease_time_limit = 10

    while not _end_game:
        if not _game_over:
            if _R>=0 and _R<=255 and _G>=0 and _G<=255 and _B>=0 and _B<=255:
                _G -= 0.01
                _B += 0.01
        
        _game_window.fill((_R, _G, _B))

        _lvl_font = pygame.font.SysFont('Broadway', 20).render('Level '+str(_level), 1, (0,0,0))
        _game_window.blit( _lvl_font, [0, _screen_height - _lvl_font.get_height()])

        #Timer for playing game.
        _inner_time = time.time()
        _elapsed_time = _inner_time - _start_time
        _time_left = _time_limit - int(_elapsed_time)
        if _time_left < 0:
            _game_over = True
        else:
            _timer = _font.render('Time Left: '+str(_time_left)+'s', 1, _white, _purple)
            _game_window.blit(_timer, [_screen_width - _timer.get_width(), 0])

        #Displaying Score Bar.
        if _score == 50:
            game_win()
            break
        else:
            _score_bar = _font.render('Score: '+str(_score), 1, _white, _purple)
            _game_window.blit(_score_bar, [0,0])

        #Drawing Player.
        pygame.draw.rect(_game_window, _red, [_player_x, _player_y, _player_size, _player_size], 
            border_top_left_radius=18, border_top_right_radius=18, border_bottom_left_radius=10, border_bottom_right_radius=10)

        if _platform_list:
            for id, x, y in _platform_list:
                y += _platform_speed
                pygame.draw.rect(_game_window, _black, [x, y, 120, 8], border_radius=3)
                _temp = []
                _temp.append(id)
                _temp.append(x)
                _temp.append(y)
                _temp_lst.append(_temp)

                #Collision of player with platform.
                if _player_x + ((_player_size/3) * 2) >= x and _player_x + (_player_size/3) <= x + 120:
                    if (_player_y + _player_size) - (y + 8) < 0:
                        if _player_y > y - 45 and _player_y + _player_size < y + 8:
                            _no_gravity = True
                            _gravity = 0
                            _velocity_y = 0
                            _player_y = y - _player_size
                            _was_on_platform = True
                            if x != _record_platform:
                                _time_limit += 2
                                _time_limit_updated = True
                                _time_value_changed = 2
                                _recorded_time = time.time()
                            if id > _save_platform_id:
                                _save_platform_id = id
                                _score += 1
                            _plat_id, _platform_x, _platform_y = id,x,y
                            _record_platform = _platform_x

                if len(_temp_lst) == len(_platform_list):
                    _platform_list = _temp_lst
                    _temp_lst = []
                    if y > 100:spawn_platform()

            for id, x, y in _platform_list:
                if y > _screen_height:
                    if _platform_x == x and _platform_y == y:
                        _platform_x = _platform_y = 0
                    del _platform_list[0]
                #FOR DEBUG PURPOSE
                #if y > 450:
                    #_fps = 2
        else:spawn_platform()

        if _time_limit_updated:
            if _time_value_changed > 0:
                _show_time_changed = _font.render('+2s', 1, _black)
                _game_window.blit(_show_time_changed, [_screen_width - _timer.get_width(), _timer.get_height() + 1])
                if abs(_inner_time - _recorded_time) >= 2:
                    _time_limit_updated = False
            if _time_value_changed < 0:
                _show_time_changed = _font.render('-'+str(_decrease_time_limit)+'s', 1, _black)
                _game_window.blit(_show_time_changed, [_screen_width - _show_time_changed.get_width(), _timer.get_height() + 1])
                if abs(_inner_time - _recorded_time) >= 2:
                    _time_limit_updated = False

        pygame.display.update()
        _clock.tick(_fps)

        #Continous movements: Applying player motions.
        _keys_pressed = pygame.key.get_pressed()
        if _keys_pressed[pygame.K_RIGHT] and _player_x + _motion < _screen_width - 40:
            _player_x += _motion
        if _keys_pressed[pygame.K_LEFT] and _player_x + _motion > 0:
            _player_x += -_motion


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _end_game = True
            if event.type == pygame.KEYDOWN:
                #Single press movements
                if event.key == pygame.K_UP and _velocity_y == 0 and _player_y > 0:
                    if _no_gravity or _player_y > _screen_height - 41:
                        _velocity_y = -_jump
                        _gravity = 0
                        _jumped = True

        
        if _player_x + (_player_size/3) >= _platform_x and (_player_x + _player_size) - (_player_size/3) <= _platform_x + 120:
            if (_player_y + _player_size) - _platform_y < 0:
                if _player_y > _platform_y - 45 and _player_y + _player_size < _platform_y:
                    _no_gravity = True
                    _gravity = 0
                    if not _jumped:
                        _player_y = _platform_y - _player_size
                    else:
                        _no_gravity = False
        else:
            _no_gravity = False

        #Bug fixed: Player was remembering the last platform
        #           on which it was sat, but actully that platform has left the game boundary.
        #Checking current platform in main platform list
        _current_platform_list = []
        _current_platform_list.append(_plat_id)
        _current_platform_list.append(_platform_x)
        _current_platform_list.append(_platform_y)
        if _current_platform_list not in _platform_list:#check if ID is needed to add in _current_platform_list or not
            _platform_x = _platform_y = 0

        #Applying Gravity
        if _player_y < _screen_height - _player_size:
            _player_y += _gravity
        else:#Bug fixed: When jumped, player was moving out of screen height by 5 pixels at bottom.
            if _player_y > _screen_height - _player_size:
                _player_y = _screen_height - _player_size
                if _was_on_platform:
                    _time_limit -= _decrease_time_limit
                    _time_limit_updated = True
                    _time_value_changed = -_decrease_time_limit
                    _recorded_time = time.time()
                    _was_on_platform = False
        if not _no_gravity:
            if _gravity != 10:
                _gravity += 0.5
        
        #Applying Jump
        if _player_y > 0:
            _player_y += _velocity_y
        if _player_y + _velocity_y < 0:
            _player_y = 1
        if _velocity_y > 0:
            _velocity_y -= 1
        if _velocity_y < 0:
            _velocity_y += 1
        if _velocity_y == 0:
            _jumped = False
        
        #Boundary Limiter: Places the player into the game boundary if player trys to move out of the boundary.
        if _player_x - _motion < 0:
            _player_x = 1
        if _player_x + _motion > _screen_width - 40:
            _player_x = _screen_width - 40

        if _game_over:
            game_over(_R, _G, _B)
            break
    #End of while
    pygame.quit()
    quit()
#End of gameloop

def main_menu():
    global _level
    _exit = False
    _level = 1
    while not _exit:
        _game_window.fill(_light_blue)
        
        _wlc = pygame.font.SysFont('Freestyle Script', 110).render('LEVITATOUR', True, _black)
        _game_window.blit(_wlc, [_screen_width/2 - _wlc.get_width()/2, _screen_height/2 - _wlc.get_height()/2])
        
        _prs = pygame.font.SysFont(None, 30).render('Press SPACE or ENTER', True, _purple)
        _game_window.blit(_prs, [_screen_width/2 - _prs.get_width()/2, _screen_height/2 - _prs.get_height()/2 + _wlc.get_height()])
        
        pygame.display.update()
        _clock.tick(_fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    _exit = True
                    gameloop()
    pygame.quit()

#Game Starts here.
main_menu()
