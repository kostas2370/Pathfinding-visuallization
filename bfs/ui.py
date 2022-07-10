import pygame
from button import Button
from bfs import bfs,get_start

#We check if there is any of the wanted colour in our map 
def check_for_color(lista,color):
    
    for x in range(15):
        for j in range(20):
          if lista[x][j].color==color:
            return (x,j)  
    return False
#A function that draws the buttons 
def draw(lista):
    for x in range(15):
        for j in range(20):
            lista[x][j].draw(win,(0,0,0))  

   
    finale_mode.draw(win,(0,0,0))        
    trap_mode.draw(win,(0,0,0))
    start_mode.draw(win,(0,0,0))
    run_button.draw(win,(0,0,0))
    reset_button.draw(win,(0,0,0))
    clear_solution_button.draw(win,(0,0,0))
    dfs_selection_button.draw(win,(0,0,0))
    bfs_selection_button.draw(win,(0,0,0))
    but.draw(win,(0,0,0))
    nodes_visited.draw(win,(0,0,0))
    solution_lenght.draw(win,(0,0,0))
#A funtion to clear our solution
def clear_solution():
    for x in range(15):
        for j in range(20):
            if koumpia[x][j].color == ORANGE or koumpia[x][j].color == BLUE:
                koumpia[x][j].color=GREY
    nodes_visited.text="Nodes visited : "
    solution_lenght.text="Solution lenght : "
#A function to reset our map
def reset():
    nodes_visited.text,solution_lenght.text="Nodes visited : ","Solution lenght : "
            
    for x in range(15):
        for j in range(20):
            koumpia[x][j].color=GREY
            koumpia[0][0].color=YELLOW
            koumpia[14][19].color=RED

pygame.init()
#COLORS:
BACKGROUND= (225,179,120)     
BLACK=(0,0,0)
GREY=(211,211,211)
RED=(255,0,0)
YELLOW=(255, 234, 0)
PURPLE =(230,230,250)
ORANGE=(239,64,37)
BLUE=(0,0,210)
PINK=(255, 192, 203)
GREEN=(0,255,0)
HEAVY_PINK=(255,153,153)

#MAKING THE WINDOW
win=pygame.display.set_mode((1000,800))
win.fill(BACKGROUND)
#START THE DISPLAY
pygame.display.set_caption("Path Finding")
pygame.display.flip()
mode=YELLOW
algorithm="BFS"
koumpia=[]
x,y=50,60
Run=True

#Making our map :
for i in range (15):
    lista=[]
    for j in range(20):

        buton=Button(GREY,x,y,40,40)
        x+=42
        lista.append(buton)
    koumpia.append(lista)
    y+=42
    x=50

#Creatingour buttons
start_mode=Button(YELLOW,20,10,40,40)
trap_mode=Button(BLACK,70,10,40,40)
finale_mode= Button(RED,120,10,40,40)
run_button=Button(PURPLE,175,10,140,40,"Run")
reset_button=Button(HEAVY_PINK,335,10,140,40,"Reset")
clear_solution_button=Button((GREEN),490,10,140,40,"Reset Sol.")
but=Button(mode,20,700,40,40)
bfs_selection_button=Button(RED,660,10,90,40,"BFS")
dfs_selection_button=Button(PINK,780,10,90,40,"DFS")
nodes_visited=Button(BACKGROUND,150,700,300,40,"Nodes visited : ")
solution_lenght=Button(BACKGROUND,480,700,300,40,"Solution_lenght : ")
koumpia[0][0].color=YELLOW
koumpia[14][19].color=RED



while Run:
    
    
    pygame.display.update()
    draw(koumpia)
    but.color=mode
    for event in pygame.event.get(): 
        pos=pygame.mouse.get_pos()
        if event.type == pygame.QUIT: 
              Run = False
        for x in range(15):
            for j in range(20):
                
                if koumpia[x][j].hover(pos)==True: 
                    if event.type==pygame.MOUSEBUTTONDOWN :
                        if koumpia[x][j].color==GREY:
                            if mode==RED:
                                lt=check_for_color(koumpia,RED)
                                if lt != False:
                                    koumpia[lt[0]][lt[1]].color=GREY
                            if mode==YELLOW:
                                lt=check_for_color(koumpia,YELLOW)
                                if lt != False:
                                    koumpia[lt[0]][lt[1]].color=GREY
                            koumpia[x][j].color=mode


                        else:
                            koumpia[x][j].color=GREY

                             
                   
        if finale_mode.hover(pos)and event.type==pygame.MOUSEBUTTONDOWN:   
            mode=RED
            
        if trap_mode.hover(pos) and event.type==pygame.MOUSEBUTTONDOWN:
            mode=BLACK 

        if start_mode.hover(pos) and event.type==pygame.MOUSEBUTTONDOWN:
            mode=YELLOW 

        if run_button.hover(pos) and event.type==pygame.MOUSEBUTTONDOWN:
            

            
            clear_solution()
            bfs(get_start(koumpia),koumpia,nodes_visited,solution_lenght,algorithm)
        
        if reset_button.hover(pos):
            reset_button.color=GREY
        else:
            reset_button.color=(255,153,153)


        if run_button.hover(pos):
            run_button.color=GREY
        else:
            run_button.color=PURPLE
        

        if reset_button.hover(pos) and event.type==pygame.MOUSEBUTTONDOWN:
            reset()

        if clear_solution_button.hover(pos) and event.type==pygame.MOUSEBUTTONDOWN:
            
            
            clear_solution()
 
        if clear_solution_button.hover(pos):
            clear_solution_button.color=GREY
        else:
            clear_solution_button.color=(0,255,0)

        if dfs_selection_button.hover(pos) and event.type==pygame.MOUSEBUTTONDOWN:
            algorithm="DFS"
            dfs_selection_button.color,bfs_selection_button.color=RED,PINK
            clear_solution()
        if bfs_selection_button.hover(pos) and event.type==pygame.MOUSEBUTTONDOWN:
            algorithm="BFS"
            dfs_selection_button.color,bfs_selection_button.color=PINK,RED
            
            clear_solution()