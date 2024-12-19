import math
ang = float(input('digite o angulo : '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print('o angulo de {}° tem cos = {:.2f} sen = {:.2f} tangente = {:.2f}'.format(ang, cos, sen, tang))
