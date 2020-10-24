import csv

from DownKlass import DownKlass
from GifCreator import GifCreator
from PNGCreator import PNGCreator
from UpKlass import UpKlass

w, h = 60, 60
quadEdge = 12
temQuad = 200
upTemp = 100
quality = 1

def research(q, iters):
    with open('results.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['№', 'Точность', 'UP', 'DOWN', 'Отношение UP/DOWN'])
        for i in range(iters):
            UP = UpKlass(w, h, temQuad, upTemp, quadEdge, 1.5)
            DOWN = DownKlass(w, h, temQuad, upTemp, quadEdge, 1.5)
            upc = UP.find(q)
            downc = DOWN.find(q)
            q /= 10
            filewriter.writerow([i, str(q).replace('.', ','), upc, downc, str(upc / downc).replace('.', ',')])


def compare(q, iters):
    with open('results.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['№', 'Точность', 'Обычно', 'Со множителем в 1.5', 'Обычно / множитель'])
        for i in range(iters):
            UP_C = UpKlass(w, h, temQuad, upTemp, quadEdge)
            DOWN_C = DownKlass(w, h, temQuad, upTemp, quadEdge)
            upc_C = UP_C.find(q)
            downc_C = DOWN_C.find(q)

            comp_C = upc_C / downc_C

            UP_S = UpKlass(w, h, temQuad, upTemp, quadEdge, 1.5)
            DOWN_S = DownKlass(w, h, temQuad, upTemp, quadEdge, 1.5)
            upc_S = UP_S.find(q)
            downc_S = DOWN_S.find(q)

            comp_S = upc_S / downc_S

            q /= 10
            filewriter.writerow([i, str(q).replace('.', ','), str(comp_C).replace('.', ','), str(comp_S).replace('.', ','), str(comp_C / comp_S).replace('.', ',')])


compare(quality, 15)
# research(quality, 30)
# UP = UpKlass(w, h, temQuad, upTemp, quadEdge)
# iters = UP.find(.0001)
# PNGCreator(UP.matrix).draw()
# GifCreator('Common.gif', [f"images/{i}.png" for i in range(iters)]).save()
