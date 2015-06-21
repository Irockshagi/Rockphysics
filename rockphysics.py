def wylliedens(por,sw,rhoma,rhow,rhohc):
    rho = (1-por)*rhoma + por*(sw*rhow + (1-sw)*rhohc)
    return rho
