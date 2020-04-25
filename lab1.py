import pygame
import random

WIDTH = 800
HEIGHT = 700
FPS = 60


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jerry likes cheese")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('jerry1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (YELLOW), (10, 10), 30)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
    

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            playSound2()




all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Ball()
    all_sprites.add(m)
    balls.add(m)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

   
    all_sprites.update()

    
    hits = pygame.sprite.spritecollide(player, balls, True)
    if hits:
        m = Ball()
        all_sprites.add(m)
        balls.add(m)
        

   
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    

pygame.quit()