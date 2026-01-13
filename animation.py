import os
import pyganim
import pygame


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANI_DIR_CARDKNIGHT = os.path.join(BASE_DIR, "cardknight")
ANI_DIR_CARDGOLEM = os.path.join(BASE_DIR, "cardgolem")
ANI_DIR_KNI_E = os.path.join(ANI_DIR_CARDKNIGHT, "knight_walk_E")
ANI_DIR_KNI_N = os.path.join(ANI_DIR_CARDKNIGHT, "knight_walk_N")
ANI_DIR_KNI_S = os.path.join(ANI_DIR_CARDKNIGHT, "knight_walk_S")
ANI_DIR_GOL_E = os.path.join(ANI_DIR_CARDGOLEM, "golem_walk_E")
ANI_DIR_GOL_N = os.path.join(ANI_DIR_CARDGOLEM, "golem_walk_N")
ANI_DIR_GOL_S = os.path.join(ANI_DIR_CARDGOLEM, "golem_walk_S")



def load_animation(dir_path, speed=100):
    frames = []
    for file_name in sorted(os.listdir(dir_path)):
        file_path = os.path.join(dir_path, file_name)
        image = pygame.image.load(file_path).convert_alpha()
        scaled_image = pygame.transform.scale(image, (50, 50))
        frames.append((scaled_image, speed))

    anim = pyganim.PygAnimation(frames)
    anim.play()
    
    return anim


knight_walk_E = load_animation(ANI_DIR_KNI_E)
knight_walk_N = load_animation(ANI_DIR_KNI_N)
knight_walk_S = load_animation(ANI_DIR_KNI_S)
golem_walk_E = load_animation(ANI_DIR_GOL_E)
golem_walk_N = load_animation(ANI_DIR_GOL_N)
golem_walk_S = load_animation(ANI_DIR_GOL_S)


#knight_walk_W = pygame.transform.flip(knight_walk_E[1], True, False)


    
