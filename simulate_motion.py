#DON'T ALTER/READ THIS CELL, JUST RUN IT AND MOVE ON :)
import math
from vpython import *
def simulate_motion(q=0,m=1,vx=1,Ey=0,Bz=0,vy=0,vz=0,total_time=20,fns = []):
    print("White arrows = E field, Yellow arrows = B field, Blue = negative charge and Red = positive charge")
    print("E and B fields are assumed to be uniform all over space.")
    if q!=0:
        scale = math.floor(math.log10(abs((q*vx*Bz+q*Ey)/m)))
        q = q*10**(-scale)
    scene = canvas()
    ######################################################
    #define parameters for the moving point charge
    obj = sphere(radius = 1)
    obj.charge = q
    obj.mass = m
    obj.pos = vector(0,0,0) #initial position vector
    obj.velocity = vector(vx,vy,vz) #initial velocity vector
    obj.color = color.blue
    if obj.charge >0:
        obj.color = color.red
    ######################################################
    #define the uniform E and B fields
    E = vector(0,Ey,0)
    B = vector(0,0,Bz)
    ######################################################
    t = 0 #initial time
    dt = 0.001 #timestep to evolve the system
    trail = curve(color=color.white)
    max_y = 15
    max_x = 50

    #unit vectors

    if E.y != 0:
        mybox = box(pos=vector(0,max_y*E.y/abs(E.y),0), length=max_x, height=0.1, width=50,color=color.blue)
        mybox = box(pos=vector(0,-max_y*E.y/abs(E.y),0), length=max_x, height=0.1, width=50,color=color.red)
        dx = max_x/10
        for x in arange(-max_x/2, max_x/2+dx, 2*dx):
            arrow(pos=vector(x,-max_y*E.y/abs(E.y),0),axis = vector(0,2*max_y*E.y/abs(E.y),0),color=color.white,shaftwidth=0.1)
        scene.range = max_y*2*1.1
        dx = max_x/10
    else:
        max_x = 10
        max_y = 8
        dx = max_x/4
        obj.radius = 0.6
    arrow(pos=vector(0.7*max_x,0,0),axis = vector(5+(5*(E.y != 0)),0,0),color=color.white,shaftwidth=0.1)
    T = text(text='i',align='center', color=color.green,pos=vector(0.7*max_x+2+3*(E.y != 0),-1-2*(E.y != 0),0),height=1+2*(E.y != 0))
    arrow(pos=vector(0.7*max_x,0,0),axis = vector(0,5+(5*(E.y != 0)),0),color=color.white,shaftwidth=0.1)
    T = text(text='j',align='center', color=color.green,pos=vector(0.7*max_x-1-(E.y != 0),1+(E.y != 0),0),height=1+2*(E.y != 0))
    #arrow(pos=vector(0.7*max_x,0,0),axis = vector(0,0,10),color=color.white,shaftwidth=0.1)
    if B.z != 0:
        for x in arange(-max_x/2, max_x/2+dx, 2*dx):
            arrow(pos=vector(x,-max_y/4,-2*max_y*B.z/abs(B.z)*(B.z<0)),axis = vector(0,0,2*max_y*B.z/abs(B.z)),color=color.yellow,shaftwidth=0.1)
            arrow(pos=vector(x,max_y/4,-2*max_y*B.z/abs(B.z)*(B.z<0)),axis = vector(0,0,2*max_y*B.z/abs(B.z)),color=color.yellow,shaftwidth=0.1)

    final_time = total_time
    while t<final_time:

        rate(1000) #slow down the rate of visualization to 600 updates per sec
        F = fns[0](obj.charge,obj.velocity,E,B) #calculate the net force on the charge
        r = fns[2](obj.pos,obj.velocity,obj.mass,F,dt)
        v = fns[1](obj.velocity,obj.mass,F,dt)
        obj.pos = r
        obj.velocity = v
        trail.append(pos=r)
        t = t+dt
        if abs(r.y) >=max_y and E.y!=0:
            break
