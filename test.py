B=[ 0,  1,  2,  3,  4,  5,  6,  7,  8, 
  9, 10, 11, 12, 13, 14, 15, 16, 17, 
 18, 19, 20, 21, 22, 23, 24, 25, 26, 
 27, 28, 29, 30, 31, 32, 33, 34, 35, 
 36, 37, 38, 39, 40, 41, 42, 43, 44, 
 45, 46, 47, 48, 49, 50, 51, 52, 53,  
 54, 55, 56, 57, 58, 59, 60, 61, 62,  
 63, 64, 65, 66, 67, 68, 69, 70, 71,  
 72, 73, 74, 75, 76, 77, 78, 79, 80, -1]
l=[ 1, 1, 1, 1, 1, 1, 2, 0, 1, 
    1, 1, 1, 1, 1, 2, 2, 0, 0, 
    1, 1, 1, 2, 1, 2, 2, 1, 2, 
    1, 2, 2, 2, 1, 2, 2, 1, 2, 
    1, 1, 1, 1, 1, 1, 2, 1, 2, 
    2, 2, 0, 2, 0, 1, 2, 1, 2,  
    1, 1, 1, 2, 0, 0, 2, 1, 2,  
    1, 1, 1, 2, 0, 1, 2, 1, 2,  
    1, 1, 1, 2, 0, 0, 2, 1, 2, 1]
from time import time
def _isOnBoard(x,y):
        return x >= 0 and x < 9 and y >= 0 and y < 9


def flatten(coord) :
    return 9 * coord[0] + coord[1]


def voisin(i) :
    d = divmod(i, 9)
    neighbors = ((d[0]+1, d[1]), (d[0]-1, d[1]), (d[0], d[1]+1), (d[0], d[1]-1))
    v=[]
    for c in neighbors :
        if _isOnBoard(c[0], c[1]) :
            v.append(flatten(c))
    return(v)


def getGroup(l,i,color,done,v):
    v.append(i)
    neighbors=voisin(i)
    neighbors=list(set(neighbors) - set(done))
    for c in neighbors :
        done = list(dict.fromkeys(done))
        if l[c]==color  :
            done.append(c)
            getGroup(l,c,color,done,v)
        else : 
            done.append(c)
    v = list(dict.fromkeys(v))
    return (v)


def getGroups(l,color_self,color_oppo):
    g_self=[]
    g_oppo=[]
    for i in range(81) :
        if l[i]==color_self :
            fait=False
            for h in g_self :
                if i in h :
                    fait=True
                    break
            if fait==False :
                v=getGroup(l,i,color_self,[i],[])
                g_self.append(v)
        elif l[i]==color_oppo :
            fait=False
            for h in g_oppo :
                if i in h :
                    fait=True
                    break
            if fait==False :
                v=getGroup(l,i,color_oppo,[i],[])
                g_oppo.append(v)
    return(g_self,g_oppo)

def libertiesOfGroup (l,g,oppo) :
    k=[]
    for i in g :
        v=voisin(i)
        v=list(set(v) - set(g))
        k=k+v
    k = list(dict.fromkeys(k))
    liberties=0
    for i in k :
      B=[ 0,  1,  2,  3,  4,  5,  6,  7,  8, 
  9, 10, 11, 12, 13, 14, 15, 16, 17, 
 18, 19, 20, 21, 22, 23, 24, 25, 26, 
 27, 28, 29, 30, 31, 32, 33, 34, 35, 
 36, 37, 38, 39, 40, 41, 42, 43, 44, 
 45, 46, 47, 48, 49, 50, 51, 52, 53,  
 54, 55, 56, 57, 58, 59, 60, 61, 62,  
 63, 64, 65, 66, 67, 68, 69, 70, 71,  
 72, 73, 74, 75, 76, 77, 78, 79, 80, -1]
l=[ 1, 1, 1, 1, 1, 1, 2, 0, 1, 
    1, 1, 1, 1, 1, 2, 2, 0, 0, 
    1, 1, 1, 2, 1, 2, 2, 1, 2, 
    1, 2, 2, 2, 1, 2, 2, 1, 2, 
    1, 1, 1, 1, 1, 1, 2, 1, 2, 
    2, 2, 0, 2, 0, 1, 2, 1, 2,  
    1, 1, 1, 2, 0, 0, 2, 1, 2,  
    1, 1, 1, 2, 0, 1, 2, 1, 2,  
    1, 1, 1, 2, 0, 0, 2, 1, 2, 1]
from time import time
def _isOnBoard(x,y):
        return x >= 0 and x < 9 and y >= 0 and y < 9


def flatten(coord) :
    return 9 * coord[0] + coord[1]


def voisin(i) :
    d = divmod(i, 9)
    neighbors = ((d[0]+1, d[1]), (d[0]-1, d[1]), (d[0], d[1]+1), (d[0], d[1]-1))
    v=[]
    for c in neighbors :
        if _isOnBoard(c[0], c[1]) :
            v.append(flatten(c))
    return(v)


def getGroup(l,i,color,done,v):
    v.append(i)
    neighbors=voisin(i)
    neighbors=list(set(neighbors) - set(done))
    for c in neighbors :
        done = list(dict.fromkeys(done))
        if l[c]==color  :
            done.append(c)
            getGroup(l,c,color,done,v)
        else : 
            done.append(c)
    v = list(dict.fromkeys(v))
    return (v)


def getGroups(l,color_self,color_oppo):
    g_self=[]
    g_oppo=[]
    for i in range(81) :
        if l[i]==color_self :
            fait=False
            for h in g_self :
                if i in h :
                    fait=True
                    break
            if fait==False :
                v=getGroup(l,i,color_self,[i],[])
                g_self.append(v)
        elif l[i]==color_oppo :
            fait=False
            for h in g_oppo :
                if i in h :
                    fait=True
                    break
            if fait==False :
                v=getGroup(l,i,color_oppo,[i],[])
                g_oppo.append(v)
    return(g_self,g_oppo)

def libertiesOfGroup (l,g,oppo) :
    k=[]
    for i in g :
        v=voisin(i)
        v=list(set(v) - set(g))
        k=k+v
    k = list(dict.fromkeys(k))
    liberties=0
    for i in k :
        if l[i]==oppo :
            liberties+=1
    return liberties
def libertiesOfGroups(l,groups,oppo) :
    v=[]
    for group in groups :
        v.append(libertiesOfGroup(l,group,oppo))
    return v
startTime =time()
print(getGroups(l,1,2))
print(libertiesOfGroups(l,getGroups(l,1,2)[0],2))
print(time() - startTime)