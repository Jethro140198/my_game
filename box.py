import pygame

pygame.init()

wy = 500
wx = 500
win = pygame.display.set_mode((wy,wx))

# Importing the character sprites
RunRight = [pygame.image.load(f'Run ({i}).png') for i in range(1,9)]
RunLeft = [pygame.transform.flip(RunRight[i],True, False) for i in range(0,8)]
Dead = [pygame.image.load(f'Dead ({i}).png') for i in range(1,9)]

dino = pygame.image.load('Walk (1).png')

RightSmall = [pygame.transform.rotozoom(RunRight[i],0,0.05) for i in range(0,8)]
LeftSmall = [pygame.transform.rotozoom(RunLeft[i],0,0.05) for i in range(0,8)]
DeadSmall = [pygame.transform.rotozoom(Dead[i],0,0.05) for i in range(0,8)]
dinoSmall = pygame.transform.rotozoom(dino,0,0.05)


clock = pygame.time.Clock()

# Character class
class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 5
        self.isJump = False
        self.jumpCount = 7
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(LeftSmall[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(RightSmall[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                if self.left:
                    win.blit(LeftSmall[self.walkCount // 3], (self.x, self.y))
                else:
                    win.blit(RightSmall[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
            elif self.down:
                if self.left:
                    win.blit(LeftSmall[self.walkCount // 3], (self.x, self.y))
                else:
                    win.blit(RightSmall[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(LeftSmall[0], (self.x,self.y))
            else:
                win.blit(RightSmall[0], (self.x,self.y))

run = True
polly = Character(10,400)

def redrawGameWindow():
    win.fill((0, 0, 0))
    polly.draw(win)
    pygame.display.update()

# Main loop
while run:
    clock.tick(24)

    redrawGameWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() # List of the pressed keys events

    if keys[pygame.K_LEFT]:
        polly.left = True
        polly.right = False
        polly.up = False
        polly.down = False
        polly.standing = False
        if polly.x >= 0:
            polly.x -= polly.vel
        else:
            polly.x = wx

    elif keys[pygame.K_RIGHT]:
        polly.right = True
        polly.left = False
        polly.up = False
        polly.down = False
        polly.standing = False
        if polly.x <= wx:
            polly.x += polly.vel
        else:
            polly.x = 0

    elif keys[pygame.K_DOWN]:
        polly.down = True
        polly.up = False
        polly.standing = False
        if polly.y <= wy:
            polly.y += polly.vel
        else:
            polly.y = 0

    elif keys[pygame.K_UP]:
        polly.up = True
        polly.down = False
        polly.standing = False
        if polly.y >= 0:
            polly.y -= polly.vel
        else:
            polly.y = wy

    else:
        polly.standing = True
        polly.walkCount = 0

    if not polly.isJump:
        if keys[pygame.K_SPACE]:
            polly.isJump = True
            polly.vel = 5
            polly.walkCount = 0
            
    else:
        if polly.jumpCount >= -7:
            neg = 1
            if polly.jumpCount < 0:
                neg = -1
            polly.y -= round((polly.jumpCount**2)*0.5*neg)
            polly.jumpCount -= 1
            if polly.y < 0:
                polly.y = wy
            if polly.y > wy:
                polly.y = 0

        else:
            polly.isJump = False
            polly.jumpCount = 7
            polly.vel = 5

pygame.quit()