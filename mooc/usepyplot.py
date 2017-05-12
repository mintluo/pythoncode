import numpy as np
from matplotlib.pyplot import *

X = np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S = np.cos(X*X),np.sin(X)
plot(X,C,"ro",label="$sin(x)$")
plot(X,S,"gx",label="$cos(x^2)$")
xlabel("xlabel")
ylabel("ylabel")
legend()
title("this is title")
show()