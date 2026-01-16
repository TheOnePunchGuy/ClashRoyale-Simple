import pygame
pygame.init()

import os

clock = pygame.time.Clock()

# window setup
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

# loading screen assets
background = pygame.image.load(cards.DIR_MENU_LOADING)
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
logo = pygame.image.load(cards.DIR_MENU_LOGO)
logo = pygame.transform.scale(logo, (200, 100))

testdisplay = font.render(str(game.player_elixir.elixir_count), True, WHITE)

# timers
elixir_regen_interval = pygame.USEREVENT
card_attack_cooldown = pygame.USEREVENT + 1
enemy_spawn_interval = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_spawn_interval, 5000) #spawn enemy every 5 seconds
pygame.time.set_timer(elixir_regen_interval, int(game.player_elixir.elix_interval()) * 1000)
for card in cards.placed_card:
    pygame.time.set_timer(card_attack_cooldown, int(card.attack_cooldown) * 1000)
        
# main game loop
def main():
    loading = True
    while loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loading = False
                break
            WINDOW.blit(background, (0, 0))
            WINDOW.blit(logo, (225, 275))
            pygame.display.update()
            if event.type == pygame.KEYDOWN: #press any key to continue
                loading = False
                break
    running = True
    selected_card = None
    now_attack = False
    while running:
        # dt = seconds passed since last frame
        dt = clock.tick(60) / 1000.0  # 60 FPS cap

        # quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            elif event.type == elixir_regen_interval: # player elixir regen
                if game.player_elixir.elixir_count < 10:
                    game.player_elixir.elixir_count += 1

            elif event.type == card_attack_cooldown:
                print('now attack')
                now_attack = True

            if event.type == pygame.MOUSEBUTTONDOWN: # mouse click
                click_state = True
                # Check if a card in the deck is clicked
                if screen.rect_1.collidepoint(event.pos):
                    selected_card = cards.deck[0]
                    click_state = False
                elif screen.rect_2.collidepoint(event.pos):

                    selected_card = cards.deck[1]
                    click_state = False
                elif screen.rect_3.collidepoint(event.pos):
                    selected_card = cards.deck[2]
                    click_state = False
                elif screen.rect_4.collidepoint(event.pos):
                    selected_card = cards.deck[3]
                    click_state = False

                # card placement on arena
                if click_state and selected_card:
                    print(f'Placing card: {selected_card}')
                    mouse_x, mouse_y = event.pos
                    grid_x = mouse_x // TILE_SIZE
                    grid_y = mouse_y // TILE_SIZE
                    if grid_x <= 18 and grid_y <= 24: # inside arena
                        # new card instance
                        new_card = selected_card(
                            x=grid_x * TILE_SIZE,
                            y=grid_y * TILE_SIZE,
                            is_friendly=True)
                        
                        # valid elixir check
                        if game.player_elixir.can_subtract_elixir(new_card):
                            game.player_elixir.subtract_elixir(new_card)
                            
                            # card placement
                            print(f'new_card.x: {new_card.x}, new_card.y: {new_card.y}')
                            cards.placed_card.append(new_card)
                    selected_card = None
                    click_state = False

                # spawn enemy troop
                if event.type == enemy_spawn_interval:
                    enemy = cards.Enemy()
                    enemy.enemy_spawn(game.enemy_elixir, cards.enemy_deck)
        
        # screen update
        WINDOW.blit(testdisplay, (500, 500))
        WINDOW.fill(BLACK)
        screen.draw_arena()
        screen.draw_deck()
        screen.draw_elixir()

        # card attacking
        for card in cards.placed_card:
            print(f'card: {card}')
            card.pos = pygame.math.Vector2(card.x, card.y)

            attacking = card.attack(cards.placed_card, now_attack)
            towers_down = game.Gamelogic().tower_down(pygame.time.get_ticks() // 1000)

            if attacking:
                print('hello')

            if not attacking:
                if hasattr(card, 'move'):
                    towers_down = True #temp for testing
                    card.x, card.y = card.move(card.x, card.y, 8, 1)   
                    print(card.x, card.y)
                    #if card.x >= 8:
                        #card.x, card.y = card.move(card.x, card.y, 8, 1)                        
                        #card.x, card.y = card.move(card.x, card.y, 2, 5)
                    #elif card.x < 8:
                        #card.x, card.y = card.move(card.x, card.y, 9, 1)    
                        #card.x, card.y = card.move(card.x, card.y, 15, 5)
            print(f'x: {card.x // TILE_SIZE}, y: {card.y // TILE_SIZE}')
      
            screen.draw_cards(card, card.x, card.y)

        # update display
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
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