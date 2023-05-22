import pygame
from gameobject_class import GameObject
from playercharacter_class import PC
from nonplayercharacter_class import NPC

# size of the game screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# RGB color codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# define the clock
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    # Typical rate of 60 , equivalent to FPS
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height, player_image, enemy_image, treasure_image):
        self.title = title
        self.width = width
        self.height = height
        self.player_image = player_image
        self.enemy_image = enemy_image
        self.treasure_image = treasure_image

        # create the game screen
        self.game_screen = pygame.display.set_mode((width, height))

        # set the game screen to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        # 'source_files/project_files/player.png'
        player_character = PC(self.player_image, 375, 700, 50, 50)

        # 'source_files/project_files/enemy.png'
        enemy_0 = NPC(self.enemy_image, 20, 600, 50, 50)
        enemy_0.SPEED *= level_speed

        enemy_1 = NPC(self.enemy_image, self.width - 40, 400, 50, 50)
        enemy_1.SPEED *= level_speed

        enemy_2 = NPC(self.enemy_image, 20, 200, 50, 50)
        enemy_2.SPEED *= level_speed

        # 'source_files/project_files/treasure.png'
        treasure = GameObject(self.treasure_image, 375, 50, 50, 50)

        # Main loop of game - runs until is_game_over == True
        while not is_game_over:

            # checks all events that occur
            for event in pygame.event.get():

                # quit event closes game
                if event.type == pygame.QUIT:
                    is_game_over = True

                # detect when key pressed
                elif event.type == pygame.KEYDOWN:

                    # move forward if key up pressed
                    if event.key ==pygame.K_UP:
                        direction = 1

                    # move back if key up pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1

                # detect when key lifted
                elif event.type == pygame.KEYUP:

                    # stop moving when key lifted
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

                # print(event)

            # Clear screen
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))
            treasure.draw(self.game_screen)
            # Update player position
            player_character.move(direction, self.height)
            # Display player at new position
            player_character.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 2:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)

            if level_speed > 4:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)

            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('YOU LOSE!', True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                clock.tick(1)
                break

            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('YOU WIN!', True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                clock.tick(1)
                break

            # updates all game graphics
            pygame.display.update()
            # tick the clock to update everything in the game
            clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return


# initialise game
pygame.init()


new_game = Game('source_files/project_files/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, 'source_files/project_files/player.png', 'source_files/project_files/enemy.png', 'source_files/project_files/treasure.png')
new_game.run_game_loop(1)
new_game2 = Game('source_files/project_files/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, 'assets/player.png', 'assets/dragon.png', 'assets/treasure.png')
new_game2.run_game_loop(1)


# end game
pygame.quit()
quit()
