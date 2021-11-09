





def pescamos_titulos_peliculos():
    pescamos_titulos_peliculos = []
    for peli in titulos_peliculos:
        pescamos_peliculos.append(peli.select('a')[0].string)
    
    return pescamos_titulos_peliculos