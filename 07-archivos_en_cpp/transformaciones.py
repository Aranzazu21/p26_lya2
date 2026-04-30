import matplotlib.pyplot as plt
import numpy as np

def traslacion(p, tx, ty):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    return T @ p

def rotacion(p, theta):
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta),  np.cos(theta), 0],
                  [0, 0, 1]])
    return R @ p

def escala(p, sx, sy):
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    return S @ p


punto_seleccionado = None

def onclick(event):
    global punto_seleccionado
    if event.xdata is not None and event.ydata is not None:
        punto_seleccionado = np.array([event.xdata, event.ydata, 1])
        plt.scatter(punto_seleccionado[0], punto_seleccionado[1], c='blue', label='Seleccionado')
        plt.legend()
        plt.draw()
        print("Punto seleccionado:", punto_seleccionado)


fig, ax = plt.subplots()
ax.set_title("Haz clic para seleccionar un punto")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()


if punto_seleccionado is not None:
    p = punto_seleccionado

    print("\nOpciones de transformacion:")
    print("t = TraslaciOn")
    print("r = Rotación")
    print("e = Escala")

    op = input("Elige transformacion: ")

    if op == "t":
        tx = float(input("Traslacion en X: "))
        ty = float(input("Traslacion en Y: "))
        nuevo = traslacion(p, tx, ty)
    elif op == "r":
        ang = float(input("Angulo en grados: "))
        nuevo = rotacion(p, np.radians(ang))
    elif op == "e":
        sx = float(input("Escala en X: "))
        sy = float(input("Escala en Y: "))
        nuevo = escala(p, sx, sy)
    else:
        print("Opción no valida")
        nuevo = p

    
    plt.scatter(p[0], p[1], c='blue', label='Original')
    plt.scatter(nuevo[0], nuevo[1], c='red', label='Transformado')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No se selecciono ningun punto.")
