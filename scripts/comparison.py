from corneal import *
import matplotlib.pyplot as plt

airfoil = naca_airfoil("2412", 20)   # NACA 2412 airfoil with 20 points per side
airfoil = TransformedBody(airfoil, displacement=(-0.25, 0))
airfoil = TransformedBody(airfoil, angle=10) # rotate by 10 degrees about 1/4 chord
bound = BoundVortices(airfoil)

num_steps = 100
Uinfty = (1,0)
dt = 0.01
Vortices.core_radius = dt

""" Euler Explicit"""
flow_EU = ExplicitEuler(dt, Uinfty, bound)

for i in range(1,num_steps):
    flow_EU.advance()

vort_EU = flow_EU.wake.positions
gam_EU = flow_EU.wake.strengths


""" 2nd Order Runge-Kutta"""
flow_RK2 = RungeKutta2(dt, Uinfty, bound)

for i in range(1,num_steps):
    flow_RK2.advance()

vort_RK2 = flow_RK2.wake.positions
gam_RK2 = flow_RK2.wake.strengths


""" 4th Order Runge Kutta"""
flow_RK4 = RungeKutta4(dt, Uinfty, bound)

for i in range(1,num_steps):
    flow_RK4.advance()

vort_RK4 = flow_RK4.wake.positions
gam_RK4 = flow_RK4.wake.strengths

'''
'''

q = airfoil.get_points()
plt.plot(q[:,0], q[:,1], 'k-')
maxval = 0.01
plt.scatter(vort_EU[:,0], vort_EU[:,1], c=gam_EU,
            cmap='Blues', vmin=-maxval, vmax=maxval, edgecolor='none', label="Euler Explicit")
plt.scatter(vort_RK2[:,0], vort_RK2[:,1], c=gam_RK2,
            cmap='RdYlGn', vmin=-maxval, vmax=maxval, edgecolor='none', label="2nd Order Runge-Kutta")
plt.scatter(vort_RK4[:,0], vort_RK4[:,1], c=gam_RK4,
            cmap='bwr', vmin=-maxval, vmax=maxval, edgecolor='none', label="4th Order Runhge-Kutta")
plt.axis('equal')
plt.xlabel('$X$', fontsize=16)
plt.ylabel('$Y$', fontsize=16)
plt.legend()
plt.title('Comparison of timestepper schemes');
plt.grid(True)
plt.savefig('comparison.pdf')
plt.show()
