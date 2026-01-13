import pygame
pygame.init()

import os

clock = pygame.time.Clock()

# window
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 650
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Window")

# colours & tile size
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
TILE_SIZE = 27
font = pygame.font.SysFont("Times New Roman", 18)


# imports
import src.screen as screen
import src.game as game
import src.cards as cards

background = pygame.image.load(cards.DIR_MENU_LOADING)
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
logo = pygame.image.load(cards.DIR_MENU_LOGO)
logo = pygame.transform.scale(logo, (200, 100))

testdisplay = font.render(str(game.player_elixir.elixir_count), True, WHITE)
elixir_regen_interval = pygame.USEREVENT
card_attack_cooldown = pygame.USEREVENT + 1
pygame.time.set_timer(elixir_regen_interval, int(game.player_elixir.elix_interval()) * 1000)
for card in cards.placed_card:
    pygame.time.set_timer(card_attack_cooldown, int(card.attack_cooldown) * 1000)

def loading_screen():
    loading = True
    while loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loading = False
                break
            WINDOW.blit(background, (0, 0))
            WINDOW.blit(logo, (225, 275))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    loading = False
                    break
        

def main():
    running = True
    selected_card = None
    now_attack = False
    while running:
        # dt = seconds passed since last frame
        dt = clock.tick(60) / 1000.0  # 60 FPS cap

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            elif event.type == elixir_regen_interval:
                if game.player_elixir.elixir_count < 10:
                    game.player_elixir.elixir_count += 1
                    print(game.player_elixir.elixir_count)

            elif event.type == card_attack_cooldown:
                print('now attack')
                now_attack = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_state = True
                

                # Check if a card in the deck is clicked
                if screen.rect_1.collidepoint(event.pos):
                    selected_card = cards.deck[0]
                    click_state = False
                if screen.rect_2.collidepoint(event.pos):
                    selected_card = cards.deck[1]
                    click_state = False
                if screen.rect_3.collidepoint(event.pos):
                    selected_card = cards.deck[2]
                    click_state = False
                if screen.rect_4.collidepoint(event.pos):
                    selected_card = cards.deck[3]
                    click_state = False

                if click_state and selected_card:
                    mouse_x, mouse_y = event.pos
                    grid_x = mouse_x // TILE_SIZE
                    grid_y = mouse_y // TILE_SIZE
                    if grid_x >= 18 or grid_y >= 24:
                        click_state = False
                    selected_card.x = grid_x * TILE_SIZE
                    selected_card.y = grid_y * TILE_SIZE

            
                    if game.player_elixir.can_subtract_elixir(selected_card):
                        selected_card.is_friendly = True
                        print(selected_card)
                        cards.placed_card.append(selected_card)
                        game.player_elixir.subtract_elixir(selected_card)
        
                    selected_card = None
                    click_state = False
        
        WINDOW.blit(testdisplay, (500, 500))
        WINDOW.fill(BLACK)
        screen.draw_arena()
        screen.draw_deck()
        screen.draw_elixir()

        for card in cards.placed_card:
            card.pos = pygame.math.Vector2(card.x, card.y)

    
            attacking = card.attack(cards.placed_card, now_attack)

            if attacking:
                print('hello')

            if not attacking:
                if hasattr(card, 'move'):
                    card.x, card.y = card.move(card.x, card.y, 13, 8)
            
            print(card.x // TILE_SIZE, card.y // TILE_SIZE)
      
            screen.draw_cards(card, card.x, card.y)

    

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    loading_screen()
    main()

#towers
#attacking
#game logic
#animations
#card abilities
#enemy ai
#sounds
#attack cooldown

#Fixes
#fix elixir regen bar
#make cards pathfind to towers
#timer
#elixir display
#fix