
from vpython import *

def calculate_E(q,r_S,r_P):
    e0 = 8.854187817e-12  
    k = 1.0 / (4 * pi * e0)
    rSP = sqrt(((r_P[0]-r_S[0])**2) + ((r_P[1]-r_S[1])**2) + ((r_P[2]-r_S[2])**2))
    E_x = k*q *( (r_P[0]-r_S[0]) / rSP**3) 
    E_y = k*q *( (r_P[1]-r_S[1]) / rSP**3) 
    E_z = k*q *( (r_P[2]-r_S[2]) / rSP**3)      
    return([E_x,E_y,E_z])


def draw_configuration(charges,loc,points,draw_contributions = True, mode = None):
    
    if mode !=None:
        draw_contributions = False
    for point in points:
        Es = [calculate_E(charges[index],loc[index],point) for index in range(len(charges))]
        E_tot = [sum(E) for E in zip(*Es)]
        colors = [color.blue if charge<0 else color.red for charge in charges]
        radii = [0.5e9*abs(charge) for charge in charges]
        if mode==None:
            for index in range(len(charges)):
                sphere(pos=vector(loc[index][0],loc[index][1],loc[index][2]), radius=radii[index], color=colors[index])
        Emagn = mag(vector(E_tot[0], E_tot[1],E_tot[2]))
        scale = 1
        if  Emagn >0:
            if mode !=None:
                scale = 1. / Emagn 
            E_tot = [e*scale for e in E_tot]
            if mode !=None and charges[0]<0:
                Earrow_tot=arrow(pos=vector(-E_tot[0]+point[0],-E_tot[1]+point[1],-E_tot[2]+point[2]), axis=vector(E_tot[0], E_tot[1],E_tot[2]), shaftwidth=0.05,color=color.green)
            else:
                Earrow_tot=arrow(pos=vector(point[0],point[1],point[2]), axis=vector(E_tot[0], E_tot[1],E_tot[2]), shaftwidth=0.05,color=color.green)
        if draw_contributions:
            for index in range(len(Es)):
                E = [e*scale for e in Es[index]]
                arrow(pos=vector(point[0],point[1],point[2]), axis=vector(E[0], E[1],E[2]),  shaftwidth=0.03,color=colors[index])

def canvas_with_instructions():
    scene = canvas() 
    s = "Rotate the camera by dragging with the right mouse button,\n"
    s += "To zoom, drag with the left+right mouse buttons or use the mouse pad.\n"
    s += "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
    scene.caption = s
    return scene
                
def draw_charged_sphere(charge=1e-9,radius=1,distance=2):
    scene = canvas_with_instructions() 
    col = color.blue 
    if charge>0:
        col = color.red 
    sphere(pos=vector(0,0,0), radius=radius, color=col,opacity = 0.5)
    if distance < radius:
        charge = charge*(distance**3)/(radius**3)
        
    d = distance/(sqrt(2))
    points = [[0,0,distance],[0,distance,0],[distance,0,0]]
    points+= [[0,0,-distance],[0,-distance,0],[-distance,0,0]]
    points+= [[0,d,d],[d,d,0],[d,0,d],[0,-d,-d],[-d,-d,0],[-d,0,-d]]
    points+= [[0,-d,d],[-d,d,0],[-d,0,d],[0,d,-d],[d,-d,0],[d,0,-d]]
    
    draw_configuration([charge],[[0,0,0]],points,draw_contributions = False, mode = "sphere")

def draw_charged_cylinder(lambda0=1e-9,length=10,radius=1,distance=2):
    scene = canvas_with_instructions() 
    
    col = color.blue 
    if lambda0>0:
        col = color.red 
    cylinder(pos=vector(-length/2,0,0),axis=vector(length,0,0), radius=radius, color=col,opacity = 0.5)
    if distance <radius:
        lambda0 = lambda0*(distance**2)/(radius**2)
    dx = length/1000
    charges = []
    locs = []
    for x in arange(-length/2, length/2, dx):
        charges.append(lambda0*dx)
        locs.append([x,0,0])
    d = distance/(sqrt(2))
    points = []
    dx = length/10
    for x in arange(-length/2, length/2,dx):
        points += [[x,0,distance],[x,distance,0]]

        points+= [[x,0,-distance],[x,-distance,0]]
        points+= [[x,d,d],[x,-d,-d]]
        points+= [[x,-d,d],[x,d,-d]]
    #points+= [[-length/1.98,0,0],[0.05+length/1.98,0,0],[-length/1.6,0,0],[0.05+length/1.6,0,0]]
    draw_configuration(charges,locs,points,draw_contributions = False, mode = "cylinder")

def draw_charged_slab(rho=1e-9,length=10,height=10,width=1,distance=2):
    scene = canvas_with_instructions() 
    col = color.blue 
    if rho>0:
        col = color.red 
        
    box(pos=vector(0,0,0),length=length,height=height,width=width, color=col,opacity = 0.5)
    if distance <width/2:
        rho = 2*rho*(distance)/(width)
    dx = length/50
    dy = height/50
    charges = []
    locs = []
    for x in arange(-length/2, length/2, dx):
        for y in arange(-height/2,height/2,dy):
            charges.append(rho*distance*dx*dy)
            locs.append([x,y,0])
    d = distance/(sqrt(2))
    points = []
    dx = length/8
    dy = height/8
    for x in arange(-length/2, length/2,dx):
        for y in arange(-height/2, height/2,dy):
            points += [[x,y,distance],[x,y,-distance]]
    for y in arange(-int(height/2), int(height/2)):
        points+= [[-length/1.98,y,0],[0.05+length/1.98,y,0]]
    draw_configuration(charges,locs,points,draw_contributions = False, mode = "plane")

    
def draw_Gaussian_surface(mode,radius=1,base_centers=[[0,0,0],[10,0,0]]):
    if mode =="sphere":
        sphere(pos=vector(0,0,0),radius=radius,color=color.white,opacity = 0.2)
    if mode =="cylinder":
        base = base_centers[0]
        diff = [base_centers[1][i]-base[i] for i in range(3)]
        cylinder(pos=vector(base[0],base[1],base[2]),axis=vector(diff[0],diff[1],diff[2]), radius=radius, color=color.white,opacity = 0.2)
