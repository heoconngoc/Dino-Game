# Import Lib
import pygame 

pygame.init()
clock = pygame.time.Clock()

#Title and Icon
pygame.display.set_caption('Dino game')
icon = pygame.image.load(r'assets/dinosaur.png')

#Game window
screen = pygame.display.set_mode((600,300)) #Length = 600, Width = 300

#Load image
bg = pygame.image.load(r'assets/background.jpg')
tree = pygame.image.load(r'assets/tree.png')
dino = pygame.image.load(r'assets/dinosaur.png')

#Load sound
sound1 = pygame.mixer.Sound(r'sound/tick.wav')
sound2 = pygame.mixer.Sound('sound/te.wav')

#Initialization
score, highscore = 0,0
bg_x,bg_y = 0,0
tree_x,tree_y = 550,230
dino_x,dino_y = 50,230
x_def=5
jump = False
y_def=7
gamePlay = False 

#Check crashing
def check():
    if dino_rectangle.colliderect(tree_rectangle):
        pygame.mixer.Sound.play(sound2)
        return False
    return True

#Print score in game
game_font = pygame.font.Font('04B_19.TTF',25)
def score_view():
    score_txt = game_font.render(f'Score: {int(score)}', True, (255,0,0))
    highscore_txt = game_font.render(f'High Score: {int(highscore)}', True, (255,0,0))
    if not gamePlay:
        start_txt = game_font.render('Click Space To Start', True, (255, 0, 0))
        screen.blit(start_txt, (170, 85))
    else:
        screen.blit(score_txt,(135,50))
        screen.blit(highscore_txt,(315,50))

#Game pocessing loop
running = True
while running:
    #Contrl FPS
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gamePlay:
                if dino_y == 230:
                    pygame.mixer.Sound.play(sound1)
                    jump = True
            if event.key == pygame.K_SPACE and gamePlay == False:
                gamePlay = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gamePlay:
                    gamePlay = True
    if gamePlay:
        #bg
        bg_rectangle = screen.blit(bg,(bg_x,bg_y))
        bg2_rectangle = screen.blit(bg,(bg_x+600,bg_y))
        bg_x -= x_def
        if bg_x == -600: bg_x = 0 
        #tree
        tree_rectangle = screen.blit(tree,(tree_x,tree_y))
        tree_x -= x_def
        if tree_x == -20: tree_x = 620
        #dino
        dino_rectangle = screen.blit(dino,(dino_x,dino_y))

        if dino_y >= 80 and jump:
            dino_y -= y_def
        else:
            jump = False
        if dino_y<230 and jump == False:
            dino_y += y_def
        score += 0.05
        if score % 20 == 0: 
            x_def += 1  

        if highscore<score: highscore = score
        gamePlay = check()
        score_view()
    else:
        #Reset game
        bg_x,bg_y = 0,0
        tree_x,tree_y = 550,230
        dino_x,dino_y = 50,230
        bg_rectangle = screen.blit(bg,(bg_x,bg_y))
        tree_rectangle = screen.blit(tree,(tree_x,tree_y))
        dino_rectangle = screen.blit(dino,(dino_x,dino_y))
        score = 0
        score_view()

    pygame.display.update()
