

import pygame



WHITE= (255,255,255)     
BLACK=(0,0,0)
GREY=(211,211,211)
RED=(255,0,0)
YELLOW=(255, 234, 0)
PURPLE =(230,230,250)
ORANGE=(239,64,37)
BLUE=(0,0,210)

     

def get_start(mapx):
    for i in range(len(mapx)):
        for j in range (len(mapx[0])):
            if mapx[i][j].color==YELLOW:
                return i,j
def find_path(maps, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return path
        if start not in maps:
            return None
        
        for node in maps[start]:
            if node not in path:
               
                newpath = find_path(maps, node, end, path)
                if newpath: return newpath
        return None

def get_neighbours(mapx,c):
    neighbours={}
    
    if mapx[c[0]-1][c[1]].color != BLACK and mapx[c[0]-1][c[1]].color != ORANGE  and c[0]-1!=-1 :
        neighbours["up"]= (c[0]-1,c[1] )
    if c[1]+1<len(mapx[0]):
        if mapx[c[0]][c[1]+1].color != BLACK and mapx[c[0]][c[1]+1].color != ORANGE :
            neighbours["right"]= (c[0],c[1]+1)
    if c[0]+1<len(mapx):
        if mapx[c[0]+1][c[1]].color != BLACK and mapx[c[0]+1][c[1]].color != ORANGE  :
            neighbours["down"]= (c[0]+1,c[1] )
    if mapx[c[0]][c[1]-1].color != BLACK and mapx[c[0]][c[1]-1] != ORANGE and c[1]!=0 :
        neighbours["left"]= (c[0],c[1]-1)
    return neighbours

def bfs(st,mapx,length,solution,algorithm="BFS"):
    queue=[]
    lista=[]
    x={}
    start=st
    for j in get_neighbours(mapx,st): lista.append(get_neighbours(mapx,st)[j])

    x[st]=set(lista)
    mapx[st[0]][st[1]].color=ORANGE
    if (mapx[st[0]][st[1]].color==RED):
        return "first"
    for y in get_neighbours(mapx,st):queue.append(get_neighbours(mapx,st)[y])
    while len(queue)!=0:
        lista =[]  
        if algorithm=="BFS":
            current=queue.pop(0)
        else:
            current=queue.pop()
        z=get_neighbours(mapx,current)
        
        if mapx[current[0]][current[1]].color ==RED:
            for p in get_neighbours(mapx,current):lista.append(get_neighbours(mapx,current)[p])
            x[current]=set(lista)
            j=find_path(x,st,current)
            for l in j :

                mapx[l[0]][l[1]].color=BLUE
            mapx[j[0][0]][j[0][1]].color=YELLOW
            mapx[j[len(j)-1][0]] [j[len(j)-1][1]].color=RED
            length.text+=str(len(x))
            solution.text+=str(len(j))
            return j

        for p in z:
            if z[p] not in queue and z[p]  not in x:
                queue.append(get_neighbours(mapx,current)[p])
                lista.append(get_neighbours(mapx,current)[p])
        
        x[current]=set(lista)
        mapx[current[0]][current[1]].color=ORANGE
    mapx[start[0]][start[1]].color=YELLOW    
    length.text+=str(len(x))
    solution.text+="0"
    return "not in list"





