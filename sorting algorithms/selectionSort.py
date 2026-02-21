import pygame

#---Variable Global---#
RUNNING,WINDOW,CLOCK,GRID,FONT = None,None,None,None,None
FPS = 0.5
LARGHEZZA = 1000
ALTEZZA = 600
START = False
NUM_CELL = 8
GRIGIO = (0,255,0)
L = 0
#function to excute the selection sort
def selection_sort(list_number):
    for i in range(len(list_number)-1):
        pos_min = i
        for j in range(i+1,len(list_number)):
            if list_number[j] < list_number[pos_min]:
                pos_min = j
        list_number[i], list_number[pos_min] = list_number[pos_min], list_number[i]

def init():
    global WINDOW,CLOCK,GRID,FONT
    pygame.init()
    pygame.font.init()
    WINDOW = pygame.display.set_mode((LARGHEZZA,ALTEZZA))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("SELECTION SORT")

    GRID = [GRIGIO for _ in range(NUM_CELL)]
    FONT = pygame.font.SysFont('arial',50)
    

def event():
    global RUNNING,START
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                RUNNING = False
                return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                START = True
                return

def logic(list_number):
    global RUNNING,L
    if START:
        entry = False
        pos_min = L
        for i in range(L,len(list_number)):
            if list_number[i] < list_number[pos_min]:
                pos_min = i
                entry = True
        list_number[L], list_number[pos_min] = list_number[pos_min], list_number[L]
        L = L+1
        if L == 8:
            RUNNING = False

def render(list_number):
    global WINDOW,GRID
    
    
    WINDOW.fill((100, 255, 150))
    for i in range(NUM_CELL):
        pygame.draw.rect(WINDOW,(255,255,255),(i*150,ALTEZZA//2-50,200,100))
        pygame.draw.line(WINDOW,(0,0,0),(i*125,ALTEZZA//2-50),(i*125,ALTEZZA//2+50),2)
        number = FONT.render(str(list_number[i]),True,(0,0,0))
        WINDOW.blit(number, (i*125+50, ALTEZZA//2-28))
    pygame.draw.line(WINDOW,(0,0,0),(0,ALTEZZA//2-50),(LARGHEZZA,ALTEZZA//2-50),2)
    pygame.draw.line(WINDOW,(0,0,0),(0,ALTEZZA//2+50),(LARGHEZZA,ALTEZZA//2+50),2) 
    pygame.display.flip()

def loop(list_number):
    global RUNNING
    RUNNING = True
    while RUNNING :
        event()
        logic(list_number)
        render(list_number)
        CLOCK.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    list_number = [2,1,4,3,-1,6,-8,5]
    init()
    loop(list_number)




        

