import math as m

pi = m.pi

i = 0
over_x = False
t = 0
E_plun_sita = t * 2 * pi / 400 + pi
S_sita = t * 2 * pi / 365 + pi


while True:
    E_plun_sita = (t * 2 * pi / 400 + pi) % (2*pi)
    S_sita = (t * 2 * pi / 365 + pi) % (2*pi)
    t += 1
    print(((E_plun_sita - S_sita)/pi*180))
