#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Visualization code credit: https://github.com/tomduck/electrostatics
from new_session import *
start_session()
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# <h1>Field Lines and Equipotentials</h1>
# 
# In this lab, you will 
# 
# <ol>
#     <li> Calculate the electric potential produced by a point charge.</li>
#     <li> Analyze the relation between electric field and potential through visualizations of field lines and equipotentials.</li>
# </ol>
# 
# We provide you with a code that's mostly ready to use. You just need to fill in a few lines and run it.
# 

# <h2>Task 1: Calculating the electric potential due to a point charge</h2>
# 
# Assuming a reference for electric potential energy at infinity, i.e. $U(\infty)=0$, the electric potential produced by a point charge $q$ at a point P in space is given by 
# 
# 
# $$  V = \frac{kq}{|\vec{\mathbf{r}}_P-\vec{\mathbf{r}}_S|} \;\;\; \mbox{(eq. 1)}$$
# 
# 
# where 
# 
# $k=\frac{1}{4\pi\epsilon_0}$ is the Coulomb constant
# 
# $\vec{\mathbf{r}}_S $= source point, or the position of the charge producing potential
# 
# $\vec{\mathbf{r}}_P $= field point, or the position of point P where we want to calculate the potential.
# 
#  If the coordinates of the source point are:
# 
# $$\vec{\mathbf{r}}_S = (x_S, y_S, z_S)$$
# 
# and the coordinates of the field point are:
# 
# $$\vec{\mathbf{r}}_P = (x_P, y_P, z_P)$$
# 
# then
# 
# $$\vec{\mathbf{r}}_P-\vec{\mathbf{r}}_S = (x_P-x_S)\; \hat{\mathbf{i}} + (y_P-y_S)\; \hat{\mathbf{j}} + (z_P-z_S) \;\hat{\mathbf{k}} \;\;\;\; \mbox{(eq. 2)}$$
# 
# We will call the distance between the two points $r_{SP}$ which is defined as 
# 
# $$r_{SP} = |\vec{\mathbf{r}}_P-\vec{\mathbf{r}}_S|  \;\;\; \mbox{(eq. 3)}$$
# 
# The above equations should help you when you fill in the function "Calculate_V( )" in the code below. 
# 
# 
# <b>Please fill in the missing lines in the following code. We provide some test cases so that you can check your work.</b>
# 

# In[3]:


from vpython import *
def calculate_V(q,r_S,r_P):
    #The function takes the following generic inputs:
    #q: value of the point charge in C,
    #r_S: [x_S,y_S,z_S] coordinates of the source point in m,
    #r_P: [x_P,y_P,z_P] coordinates of point P in m    
    # and returns the potential V at point P.
    
    e0 = 8.854187817e-12  
    k = 1.0 / (4 * pi * e0)
    #rSP = FILL IN 
    rSP = sqrt(((r_P[0]-r_S[0])**2) + ((r_P[1]-r_S[1])**2) + ((r_P[2]-r_S[2])**2))
    #Second: Calculate potential
    #V = k*q/rSP
    V = k*q/rSP
    # Review (eq. 1) for the potential. 
    return(V)

#Test cases: They should all return True
print(abs(calculate_V(1e-9,[0,0,0],[0,2,0]) - 4.493775) <= 0.001)
print(abs(calculate_V(-5e-9,[-2,1,0],[0,-3,2]) +9.17288163) <= 0.001)     
print(abs(calculate_V(-2e-9,[-1,3,-2],[-4,-3,-3]) +2.65028443333) <= 0.001)      


# For your reference, we provide below the code we used to calculate the E-field in lab 1. Please comment on the relative difficulty and differences between calculating E and V produced by a point charge.

# In[3]:


def calculate_E(q,r_S,r_P): 
    e0 = 8.854187817e-12  
    k = 1.0 / (4 * pi * e0)
    rSP = sqrt(((r_P[0]-r_S[0])**2) + ((r_P[1]-r_S[1])**2) + ((r_P[2]-r_S[2])**2))
    E_x = k*q *( (r_P[0]-r_S[0]) / rSP**3) 
    E_y = k*q *( (r_P[1]-r_S[1]) / rSP**3) 
    E_z = k*q *( (r_P[2]-r_S[2]) / rSP**3)      
    return([E_x,E_y,E_z])


# <h2>Task 2: Visualizing field lines and equipotentials of a point charge</h2>
# 
# In 2D, equipotential lines are defined to be the lines connecting points of equal potential. They physically represent lines along which charges can move without the electric force exerting any work on them. This is becuase the charge will have the same potential energy at any point on the equipotential. 
# 
# Before running any code, please take a minute to think about the equipotential lines around a point charge and answer the following questions:
# <ol>
# <li> Based on equation 1, what shapes do you expect equipotential lines to look like around a point charge (in 2D)? Hint: for two points to be at the same potential around a point charge, what needs to be the same for both points?</li>
# 
# <li> Make a sketch of some equipotentials around a positive point charge and add field lines too.</li>
# <li> Can you spot any particular relation between the E-field lines on your sketch and equipotentials? Are they paralel, perpendicular or not related?</li>
#  <li> If the source chage isnegative instead of positive, do the equipotential lines change? Justify your answer with a simulation.</li>
# </ol>

# After answering the above questions, please run the cell below to draw field lines and equipotentials around a point charge. You can use the ready function draw_E_and_V(charges,locations) which takes a list of source point charges, and a list of their x-y-z coordinates as arguments.
# 
# 

# In[4]:


from equipotentials import draw_E_and_V
draw_E_and_V([-1e-9],[[0,0,0]])
# E-Field lines are indicated by solid black lines, while equipotentials are the dotted lines  
# Background color inidcates the magnitude of the field.


# Take a screenshot of your output!

# <h2>Task 3: Visualizing field lines and equipotentials of a dipole</h2>
# 
# Now let's revisit the electric dipole consisiting of two charges of equal magnitude $q$ and opposite signs. 
# <ol>
# <li> Based on equation 1, write down the net potential at any point $P$ in space in terms of $k$, $q$, $r_{+}$ and $r_{-}$, where $r_{+}$ and $r_{-}$ are the <b>distances</b> between point $P$ and the positive/negative charge.</li>
# 
# <li> What is the relationship between $r_{+}$ and $r_{-}$ for $V=0$ at a given point in space?</li>
# <li> Based on your answer to 2., what shape would you expect the $V=0$ equipotential to be around the dipole?</li>
# </ol>
# 
# After answering the above questions to the best of your knowledge, modify the code below to draw the field lines and equipotentials of a horizontal dipole of charges $\pm 1 nC$ separated by a distance of 2 m.
# 

# In[7]:


draw_E_and_V([-1e-9,1e-9],[[1,0,0],[-1,0,0]])


# <ol>
# <li>Can you identify the $V=0$ equipotential on the diagram? Please highlight it on a screenshot of the output. </li>
# <li>Discuss whether the equipotentials on the right and left of it will have positive or negative potential.</li>
# <li>Observe the direction of the field lines at all points along the $V=0$ equipotential. Do the field lines at that equipotential point in a special way? Discuss</li>
# 
# <li>By now, you would have observed an ever-existing relationship between the direction of the E-field and the equipotentials at all points in space. Please try to provide a physical argument for why this relationship holds.</li>
# <li> You have done the visualtization of the equipotetential curves in 2D, can you draw by hand the shape of the  equipotential surfaces of the dipole? </li> 
# 
# </ol>
# 
# 

# <h2>Task 4: Pick your own distribution!</h2>
#     
# Finally, decide with your group on a fun configuration to plot! It can consist of 3 or 4 point charges, but keep the magnitudes in the order of $nC$. Choose their signs and place them anywhere you want to observe the resulting fields and potentials everywhere. Modify the code below to draw your configuration. Try to produce a nice looking field :) and attach a screenshot of your results.
# 

# In[11]:


#Example
draw_E_and_V([1e-9,1e-9,-1e-9,-1e-9],[[2,0,0],[-2,0,0],[0,2,0],[0,-2,0]])

