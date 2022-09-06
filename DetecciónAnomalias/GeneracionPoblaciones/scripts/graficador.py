import matplotlib.pyplot as plt

def fpd(valores:list, titulo:str, bins=20):
    n, bins, _=plt.hist(valores,bins=bins)
    plt.xlabel('bins')
    plt.ylabel('count')
    plt.title(titulo)
    plt.grid()
    plt.show()

    return n, bins

def graficar_datos(datos):
    plt.bar([i for i in range(len(datos))], datos)
    plt.xlabel('bins')
    plt.ylabel('count')
    plt.title("INEGI")
    plt.grid()
    plt.show()
