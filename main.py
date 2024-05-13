import pygame
from Checkpoint import checkpoint
from PlayerCar import PlayerCar
from utils import scale_image, blit_rotate_center, blit_text_center


class main:

    pygame.font.init()

    GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
    TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)

    TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
    TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

    FINISH = pygame.image.load("imgs/finish.png")
    FINISH_MASK = pygame.mask.from_surface(FINISH)
    FINISH_POSITION = (130, 250)

    WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racing Game!")

    MAIN_FONT = pygame.font.SysFont("comicsans", 44)

    FPS = 60
    PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551),
            (613, 715), (736, 713),
            (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377),
            (176, 388), (178, 260)]

    CHECKPOINT_COORDINATES = [(90, 30), (19, 285), (199, 515), (281, 463), (381, 333), (506, 525), (530, 407),
                              (435, 250), (278, 237), (438, 172), (531, 125), (336, 33), (186, 240)]
    CHECKPOINT_ANGLES = [90, 0, 45, 0, 90, 90, 0, 90, 0, 90, 0, 90, 0]
    CHECKPOINT_CAR_ANGLES = [90, 180, 225, 0, 270, 270, 0, 90, 0, 270, 0, 90, 180]
    CHECKPOINT_IMAGE = "imgs/checkpoint.png"
    CHECKPOINT_OBJECTS = []

    images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
              (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
    for checkpoint in CHECKPOINT_OBJECTS:
        images.append((checkpoint.rotated, (checkpoint.x, checkpoint.y)))
    player_car = PlayerCar(4, 4)



    def draw(self, win, images, player_car, computer_car, game_info):
        for img, pos in images:
            win.blit(img, pos)

        level_text = self.MAIN_FONT.render(
            f"Level {game_info.level}", 1, (255, 255, 255))
        win.blit(level_text, (10, self.HEIGHT - level_text.get_height() - 70))

        for checkpoint in self.CHECKPOINT_OBJECTS:
            checkpoint.draw_mask(win)

        time_text = self.MAIN_FONT.render(
            f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
        win.blit(time_text, (10, self.HEIGHT - time_text.get_height() - 40))

        # vel_text = MAIN_FONT.render(
        #     f"Vel: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255))
        # win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))

        vel_text = self.MAIN_FONT.render(
            f"Checkpoint: {round(player_car.checkpoint, 1)}", 1, (255, 255, 255))
        win.blit(vel_text, (10, self.HEIGHT - vel_text.get_height() - 100))

        player_car.draw(win)
        computer_car.draw(win)
        pygame.display.update()


    def move_player(self, direction, angle):
        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_a] | angle == -1:
            self.player_car.rotate(left=True)
        if keys[pygame.K_d] | angle == 1:
            self.player_car.rotate(right=True)
        if keys[pygame.K_w] | direction == 1:
            moved = True
            self.player_car.move_forward()
        if keys[pygame.K_s] | direction == 1:
            moved = True
            self.player_car.move_backward()
        if not moved | direction == 0:
            self.player_car.reduce_speed()


    def handle_collision(self):
        next_checkpoint = self.CHECKPOINT_OBJECTS[self.player_car.next_checkpoint()]
        car_mask = pygame.mask.from_surface(self.player_car.img)
        if self.player_car.collide(self.TRACK_BORDER_MASK) is not None:
            previous_checkpoint = (self.player_car.next_checkpoint()-1)%13
            x = self.CHECKPOINT_OBJECTS[previous_checkpoint].centre_x - self.player_car.img.get_rect().width*0.75
            y = self.CHECKPOINT_OBJECTS[previous_checkpoint].centre_y - self.player_car.img.get_rect().height*0.75
            angle = self.CHECKPOINT_OBJECTS[previous_checkpoint].car_angle
            self.player_car.crashes = self.player_car.crashes + 1
            self.player_car.reset_checkpoint(x, y, angle)
        if next_checkpoint.collide(car_mask, self.player_car.x, self.player_car.y) is not None:
            self.player_car.checkpoint = self.player_car.checkpoint+1


    def load_checkpoints(self):
        for i in range(13):
            position = (self.CHECKPOINT_COORDINATES[i][0] * 0.9 * 900 / 610, self.CHECKPOINT_COORDINATES[i][1] * 0.9 * 900 / 610)
            self.CHECKPOINT_OBJECTS.append(checkpoint(position, self.CHECKPOINT_ANGLES[i], self.CHECKPOINT_CAR_ANGLES[i], self.CHECKPOINT_IMAGE, self.WIN))

    def simulate(self, genoma):
        self.load_checkpoints()
        for g in genoma:
            self.move_player(g[0], g[1])
            self.handle_collision()
        check_x = self.CHECKPOINT_OBJECTS[self.player_car.next_checkpoint()].centre_x
        check_y = self.CHECKPOINT_OBJECTS[self.player_car.next_checkpoint()].centre_y
        values = (self.player_car.next_checkpoint(), self.player_car.distance_next_checkpoint(check_x, check_y), self.player_car.crashes)
        return 100 * values[0] + values[1] - 10 * values[2]


#
# run = True
# clock = pygame.time.Clock()
#
#
# while run:
#     clock.tick(FPS)
#
#     draw(WIN, images, player_car, computer_car, game_info)
#
#     while not game_info.started:
#         blit_text_center(
#             WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 break
#
#             if event.type == pygame.KEYDOWN:
#                 game_info.start_level()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             break
#
#     move_player(player_car)
#     computer_car.move()
#
#     handle_collision(player_car, game_info)
#
#     if game_info.game_finished():
#         blit_text_center(WIN, MAIN_FONT, "You won the game!")
#         pygame.time.wait(5000)
#         game_info.reset()
#         player_car.reset()
#         computer_car.reset()
#
# pygame.quit()
