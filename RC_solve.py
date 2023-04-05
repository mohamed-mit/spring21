# Initial Value Problem:
# Single loop RC circuit using Euler's method and analytical solutions.

# Import libraries

import numpy as np 
import matplotlib.pyplot as plt



def solve_charge_current (R, C, vb, qi, ti, tf, dt,dq_dt, current, charging = True):        
    """For given R,C, emf (vb), initial charge and charging state (True/False) 
    this function integrates the differential equation given by dq_dt using the Euler-Cromer method.
    It returns a tuple of:
    - a list of times between ti and  tf (spaced dt)
    - a list of corresponding q(t) 
    - a list of corresponding I(t)
    """
    
    t = ti
    q = qi 
    I = current(dq_dt(qi,R,C,vb), charging)
   
    if charging == False:
                  vb = 0 
    
    ts = [t]
    qs = [q]
    Is = [I]
   
    while t < tf:
        # Update values

        dqdt = dq_dt(q,R,C,vb)
        q = q + dt * dqdt  # step Euler integration
        t += dt # increment time
        ts.append(t) # append time to list
        qs.append(q) # append charge to list
        
        I = current(dq_dt(q,R,C,vb), charging) # calculate current
        Is.append(I)    # append current to list

    return (ts,qs,Is)    # return tuple of list of times, charges, currents
  
def analytical_sol (R, C, vb, qi, ti, tf, dt, charging  = True):   
   
    """For given R,C, emf (vb), initial charge and charging state (True/False) 
    this function returns the analytical solution to the  differential equation given by dq_dt 
    It returns a tuple of:
    - a list of q(t), for times between ti and  tf (spaced dt) 
    - a list of corresponding I(t)
    """

    t = ti 
    tau = R*C
    q = qi 
    
    if charging == True:
        I = vb*C/tau
    else:    
        I = qi/tau

    qa = [qi]
    Ia = [I]
    
    while t < tf:
        if charging == True:
            q = vb*C * (1- np.exp(-t/tau))
            I = vb*C/tau * np.exp(-t/tau)
        else:    
            q = qi *  np.exp(-t/tau)
            I = qi/tau *  np.exp(-t/tau)
        qa.append(q)
        Ia.append(I)
        t += dt
          
    return (qa, Ia)   
    
    
def plot_Q_I(ts,qs,Is,qa,Ia):
    
    """ Plot all numerical (red) and analytical (scattered blue dots) values!"""
    #plt.scatter(ts,qs,c='r',s=6)
    plt.plot(ts,qs,c='r')
    #plt.plot(ts[::10],qa[::10],c='b')
    plt.scatter(ts[::10],qa[::10],c='b', s=8)
    plt.xlabel('time (s)')
    plt.ylabel('Charge (C)')
    plt.title('Charge on the positive plate of C')
    plt.show()


    plt.plot(ts,Is,c='r')
    plt.scatter(ts[::10],Ia[::10],c='b', s=8)
    plt.xlabel('time (s)')
    plt.ylabel('Current(ampere)')
    plt.title('Current through C')
    plt.show()  
    
    
    
    