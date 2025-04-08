from constantes import *
from math import pi
Tv=0
Tr=0
T = [Tv, Tr]
def Q1(T):
    Tv=T[0]
    Tr=T[1]
    RcondVf = e / (2*kvidro)*2*pi*(r + 0.75*e)*altura
    RconvV = 1 / (h*2*pi*(r+e)*altura)
    Q1 = (Tamb - T)/(RcondVf + RconvV)
    return Q1

def Q2(T):
    Tv=T[0]
    Tr=T[1]
    Rcondvb = e / (2*kvidro*2*pi*(r+0.25*e)*altura)
    Q2 = (Tv - Tr) / Rcondvb
    return Q2

def Q3(T, t):
    Tv=T[0]
    Tr=T[1]

