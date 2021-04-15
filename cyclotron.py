from vpython import *


def Lorentz_F(q,v,E,B):
    # calculates and returns the Lorentz force given:
    # q= charge of object, v= velocity vector, E= Electric field vector and B= Magnetic field vector
    # In vpython, cross(A,B) returns the cross product A x B
    F = q*(E+cross(v,B))
    return F
def update_v(vi,m,F,dt):
    # calculates and returns the final velocity vector after a short time-step, i.e. v(t+dt) given:
    # vi = initial velocity v(t), m = mass, F = net force on the object and dt = time step
    vf = vi + F*dt/m
    return vf
def update_position(ri,vi,m,F,dt):
    # calculates and returns the final position vector after a short time-step, i.e. r(t+dt) given:
    # ri = initial position v(t), vi = initial velocity v(t), m = mass, F = net force on the object and dt = time step
    rf = ri + update_v(vi,m,F,dt)*dt
    return rf


def cyclotron(B=0,E=0):
    Emag = E
    Bmag = B
    scene = canvas()
    trail = curve(color=color.yellow)
    myell = ellipsoid(pos=vector(0,0,0),length=1, height=1, width=0.1,color=color.white,opacity = 0.3)
    box(pos=vector(0,0,0), length=0.2, height=1, width=0.1,color=color.black,opacity = 0.8)
    scene.lights = []
    distant_light(direction=vec( 1.1,  0.44,  0.88), color=color.gray(0.8))
    obj = sphere(radius = 0.06)
    obj.charge = 1
    obj.mass = 1
    obj.pos = vector(-0.09,0,0) #initial position vector
    obj.velocity = vector(0,0,0) #initial velocity vector
    obj.color = color.blue
    if obj.charge >0:
        obj.color = color.red


    ######################################################
    t = 0 #initial time
    dt = 0.001 #timestep to evolve the system
    in_B = False
    n = 1
    while obj.pos.mag <0.5:

        rate(600) #slow down the rate of visualization to 600 updates per sec
        if abs(obj.pos.x) >=0.1:
            E = vector(0,0,0)
            B = vector(0,0,Bmag)
            in_B = True
        else:
            if in_B:
                in_B = False
                n = -n
            E = vector(Emag*n,0,0)
            B = vector(0,0,0)

        F = Lorentz_F(obj.charge,obj.velocity,E,B) #calculate the net force on the charge
        r = update_position(obj.pos,obj.velocity,obj.mass,F,dt)
        v = update_v(obj.velocity,obj.mass,F,dt)
        obj.pos = r
        obj.velocity = v
        trail.append(pos=r)
        t = t+dt

