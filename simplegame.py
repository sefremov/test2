import pygame
#Hello
# 12345

class Player:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.direction = True

    def update(self, keys):
        if self.direction:
            self.pos[0] += 5
            if self.pos[0] >= SCREEN_WIDTH:
                self.direction = not self.direction
        else:
            self.pos[0] -= 5
            if self.pos[0] <= 0:
                self.direction = not self.direction

        if keys[pygame.K_DOWN]:
            self.pos[1] += 10
        if keys[pygame.K_UP]:
            self.pos[1] -= 10

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.pos, 20)



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, 600))
running = True
player = Player([50, 60])
player2 = Player([200, 30])
direction = True
clock = pygame.time.Clock()

# FPS

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    player.update(keys)
    player2.update(keys)

    screen.fill(WHITE)
    player.draw(screen)
    player2.draw(screen)

    pygame.display.flip()   # Отрисовка содержимого окна
    clock.tick(40)  # FPS

pygame.quit()