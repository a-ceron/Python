from life import pyLifeGame_v3

def main():
    size=(800, 500)
    g_size= 20

    #vida= pyLifeGame.Vida(size, g_size)

    pyLifeGame_v3.jugar( size )
    
if __name__ == '__main__':
    main()