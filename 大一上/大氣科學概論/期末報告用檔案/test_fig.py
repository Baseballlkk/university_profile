def testgeof(phi):   
    # import lib
    import numpy as np
    import math as m

    # setting constant
    rho = 1                                               
    omega = 2*(m.pi)/86400                               # period of self rotating
    phi = m.radians(phi)                                  # assume the latitude is 45 degree*
    dt = 10

    # setting array of changing variables
    x = np.zeros(1000000)                                   # array of x-coordinate
    y = np.zeros(1000000)                                   # array of y-coordinate
    vx = np.zeros(1000000)                                  # array of x velocity
    vy = np.zeros(1000000)                                  # array of y velocity
    ax = np.zeros(1000000)                                  # array of x acceleration
    ay = np.zeros(1000000)                                  # array of y acceleration
    t = np.zeros(1000000)                                   # array of time
    theta = np.zeros(1000000)                               # array of degree of wind
    P = np.zeros(100000)                                   # array of pressure    

    # setting initial condition of variables
    x[0] = 0
    y[0] = 0
    vx[0] = 0
    vy[0] = 0                                          # im m/s
    ax[0] = (-1/rho)*(-1/1000)+2*omega*vy[0]*np.sin(phi)
    ay[0] = (-1/rho)*(-1/1000)

    t[0] = 0
    theta[0] = np.radians(90)


    # counting the data
    for i in range(999999):
        if vy[i]>=0:
            t[i+1] = t[i]+dt
            x[i+1] = x[i]+vx[i]*dt
            y[i+1] = y[i]+vy[i]*dt
            vx[i+1] = vx[i]+ax[i]*dt
            vy[i+1] = vy[i]+ay[i]*dt
            dp = -1/1000
            Gy = (-1/rho)*(dp)
            ax[i+1] = 2*omega*vy[i+1]*np.sin(phi)
            ay[i+1] = Gy-2*omega*vx[i+1]*np.sin(phi)
        else :
            break

    # set maximum of position
    xmax = np.max(x)
    ymax = np.max(y)
    vxmax = np.max(vx)
    tmax = np.max(t)
    
    

    return(xmax,ymax,vxmax,tmax)