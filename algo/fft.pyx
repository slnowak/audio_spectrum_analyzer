import cmath
import math
import numpy as np

def fourier(sample, nn):
    cdef long n, mmax, m, j, istep, i
    cdef double wtemp, wr, wpr, wpi, wi, theta
    cdef double tempr, tempi
    data = []
    cdef int count = 0
    for i in xrange(2*nn):
        if i % 2 == 0:
            data.append(sample[count])
            count = count + 1
        else:
            data.append(0.0)
    n = nn<<1
    j=1
    for i in xrange(1,n,2):
        if j>i:
            data[j-1], data[i-1] = data[i-1], data[j-1]
            data[j], data[i] = data[i], data[j]
        m = nn
        while m>=2 and j>m:
            j -= m
            m >>= 1
        j += m
 
    mmax=2
    while n>mmax:
        istep = mmax<<1
        theta = -(2*cmath.pi/mmax)
        wtemp = math.sin(0.5*theta)
        wpr = -2.0*wtemp*wtemp
        wpi = math.sin(theta)
        wr = 1.0
        wi = 0.0
        for m in xrange(1,mmax,2):
            for i in xrange(m,n+1,istep):
                j=i+mmax
                tempr = wr*data[j-1] - wi*data[j]
                tempi = wr * data[j] + wi*data[j-1]
 
                data[j-1] = data[i-1] - tempr
                data[j] = data[i] - tempi
                data[i-1] += tempr
                data[i] += tempi
            wtemp=wr
            wr += wr*wpr - wi*wpi
            wi += wi*wpr + wtemp*wpi
        mmax=istep
    samples = []
    for i in xrange(0,2*nn,2):
        samples.append(complex(data[i],data[i+1]))
    return np.array(samples)

