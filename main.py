import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_style("darkgrid")

def spacer(ilosc_krokow: int) -> list:
    kroki = []
    pozycja = 0
    for krok in range(ilosc_krokow):
        if random.random() < 0.5:
            pozycja -= 1
            kroki.append(pozycja)
        else:
            pozycja += 1
            kroki.append(pozycja)
    return kroki

def spacer2D(ilosc_krokow: int) -> list:
    kroki = []
    pozycja = [0,0]
    for krok in range(ilosc_krokow):
        mozliwosci = random.choice([[1,0], [0,1], [-1,0], [0,-1]])
        for idx, wybor in enumerate(mozliwosci):
            if wybor != 0:
                pozycja[idx] += wybor
        kroki.append(pozycja.copy())  # Use copy() to append a new object each time
    return kroki
def spacer3D(ilosc_krokow: int) -> list:
    kroki = []
    pozycja = [0,0,0]
    for krok in range(ilosc_krokow):
        mozliwosci = random.choice(
            [
                [1,0,0], [0,1,0], [0,0,1],
                [-1,0,0], [0,-1,0], [0,0,-1],
            ])
        for idx, wybor in enumerate(mozliwosci):
            if wybor != 0:
                pozycja[idx] += wybor
        kroki.append(pozycja.copy())  # Use copy() to append a new object each time
    return kroki



# def spacer_xD(x: int, ilosc_krokow: int) -> list:
#     kroki = []
#     pozycja = [0 for _ in range(x)]
#     for krok in range(ilosc_krokow):


# mozliwosci = []
# for wymiar in range(3):
#     for wybor in range(2*wymiar):
#         for
#         if

def pokaz_kroki(kroki: list) -> None:
    plt.plot(range(1,len(kroki)+1), kroki)
    plt.show()

def wiele_spacerow(ilosc_spacerow: int, ilosc_krokow: int) -> list:
    lista_spacerow = []
    for _ in range(ilosc_spacerow):
        _spacer = spacer(ilosc_krokow)
        lista_spacerow.append(_spacer)
    return lista_spacerow

def wiele_spacerow2D(ilosc_spacerow: int, ilosc_krokow: int) -> list:
    lista_spacerow = []
    for _ in range(ilosc_spacerow):
        _spacer = spacer2D(ilosc_krokow)
        lista_spacerow.append(_spacer)
    return lista_spacerow

def wiele_spacerow3D(ilosc_spacerow: int, ilosc_krokow: int) -> list:
    lista_spacerow = []
    for _ in range(ilosc_spacerow):
        _spacer = spacer3D(ilosc_krokow)
        lista_spacerow.append(_spacer)
    return lista_spacerow

def pokaz_wiele_spacerow(lista_spacerow: list) -> None:
    for spacer in lista_spacerow:
        plt.plot(range(1, len(spacer)+1), spacer)
    plt.show()

def pokaz_wiele_spacerow2D(lista_spacerow: list) -> None:
    for spacer in lista_spacerow:
        x = [step[0] for step in spacer]
        y = [step[1] for step in spacer]
        plt.plot(x, y)
    plt.show()
def pokaz_wiele_spacerow3D(lista_spacerow: list) -> None:
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    lines = []

    # Plot each walk
    for spacer in lista_spacerow:
        x = [step[0] for step in spacer]
        y = [step[1] for step in spacer]
        z = [step[2] for step in spacer]
        line, = ax.plot(x, y, z)
        lines.append(line)

    # Add red dot at the origin [0,0,0]
    origin = ax.scatter(0, 0, 0, color='red', s=100)

    # Add interactivity features
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D Random Walks (Drag to rotate)')

    # Enable rotation with mouse
    def on_key(event):
        if event.key == 'r':  # Press 'r' to reset view
            ax.view_init(elev=30, azim=30)
            fig.canvas.draw_idle()

    # Connect the event handler
    fig.canvas.mpl_connect('key_press_event', on_key)

    # Add rotation animation
    def rotate(angle):
        ax.view_init(elev=30, azim=angle)
        return lines + [origin]

    # Start with an angled view for better 3D perception
    ax.view_init(elev=30, azim=30)

    # Set reasonable axis limits based on data
    all_points = [point for spacer in lista_spacerow for point in spacer]
    if all_points:
        max_range = max([
            max([abs(point[0]) for point in all_points]),
            max([abs(point[1]) for point in all_points]),
            max([abs(point[2]) for point in all_points])
        ])
        ax.set_xlim(-max_range, max_range)
        ax.set_ylim(-max_range, max_range)
        ax.set_zlim(-max_range, max_range)

    plt.tight_layout()
    plt.show()

def wartosc_oczekiwana(lista_spacerow: list) -> float:
    suma = 0
    for spacer in lista_spacerow:
        suma += spacer[-1]
    return suma / len(lista_spacerow)

def prawdopodobienstwo_bycia_w_miejscu(miejsce: int, lista_spacerow: list) -> float:
    miejsca = {}

    for spacer in lista_spacerow:
        if spacer[-1] not in miejsca.keys():
            miejsca[spacer[-1]] = 1
        else:
            miejsca[spacer[-1]] += 1

    if miejsce not in miejsca.keys():
        return 0.
    else:
        return miejsca[miejsce] / len(lista_spacerow)

def histogram_wielu_spacerow(lista_spacerow: list) -> None:

    sns.histplot(lista_spacerow, cumulative=True)

def prawdopodobienstwo_powrotu(lista_spacerow: list) -> float:
    ilosc_powrotow = 0
    for spacer in lista_spacerow:
        if 0 in spacer:
            ilosc_powrotow += 1
    return ilosc_powrotow/len(lista_spacerow)

def prawdopodobienstwo_powrotu2D(lista_spacerow: list) -> float:
    ilosc_powrotow = 0
    for spacer in lista_spacerow:
        if [0,0] in spacer:
            ilosc_powrotow += 1
    return ilosc_powrotow/len(lista_spacerow)
def prawdopodobienstwo_powrotu3D(lista_spacerow: list) -> float:
    ilosc_powrotow = 0
    for spacer in lista_spacerow:
        if [0,0,0] in spacer:
            ilosc_powrotow += 1
    return ilosc_powrotow/len(lista_spacerow)

if __name__ == "__main__":
    # kroki = spacer(500)
    # print(kroki)
    # pokaz_kroki(kroki)

    # pokaz_wiele_spacerow(wiele_spacerow(1000, 100))
    # pokaz_wiele_spacerow2D(wiele_spacerow2D(1000,100))
    pokaz_wiele_spacerow3D(wiele_spacerow3D(10,100))


    # wartosc_oczekiwana(wiele_spacerow(1000, 100))
    # prawdopodobienstwo_bycia_w_miejscu(30, wiele_spacerow(1000,100))
    # histogram_wielu_spacerow(wiele_spacerow(1000,100))

    # prawdopodobienstwo_powrotu(wiele_spacerow(1000, 100))
    # prawdopodobienstwo_powrotu2D(wiele_spacerow2D(1000, 100))
    # prawdopodobienstwo_powrotu3D(wiele_spacerow3D(1000, 100))
