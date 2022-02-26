
def obtener_texto(ruta:str, obtener_archivo:bool=False)-> str or None:
    """Regresa una cadena de carácteres que se asocian con el contenido del archivo que se encuentra en la ruta dada

    :param ruta: Ubicación del archivo a leer
    :type ruta: str
    :param obtener_archivo: Si es verdadero regresa el archivo de caso contrario regresa el texto, defaults to False
    :type obtener_archivo: bool, optional
    :return: Estrucutra que contiene información del texto
    :rtype: str | io
    """
    archivo= open( ruta )
    if( obtener_archivo ):
        return archivo

    return archivo.read()

def obtener_oraciones( archivo ) -> list:
    """Regresa el contenido del texto leído línea por línea en el texto en una estructura de tipo lista

    :param ruta: Ubicación del archivo a leer
    :type ruta: str
    :return: Lineas del texto identificadas
    :rtype: list
    """
    return [ linea.strip() for linea in archivo ]

def obtener_oraciones_nltk( texto:str )->list:
    """Regresa una lista de oraciones usando nltk

    :param texto: Texto a analizar
    :type texto: str
    :return: Lista de oraciones
    :rtype: list
    """
    # import sys
    # if( not 'nltk' in sys.modules ):        
    import nltk
    return nltk.sent_tokenize(texto)

def obtener_palabras( texto:str, unicas=True )->list:
    """Regresa una lista de palabras únicas encontradas en el texto

    :param texto: Texto a procesar
    :type texto: str
    :return: Lista de palabras únicas
    :rtype: list
    """
    if( unicas ):
        return sorted( set( texto.split() ) )
    return sorted( texto.split() )

def obtener_palabras_filtradas( texto: str | list, remover_simbolos:list= [',','.',':',';','-','?','¿','¡','!','\'','–',chr(8220),chr(8221)], todo_minuscula:bool=True, unicas:bool=True)->list:
    """Procesa un texto retirando cada uno de los símbolos que se indican, además modifica las palabras para que todas esten en minúsculas se puede pedir que solo se obtengan palabras únicas

    :param texto: Texto a analizar, defaults to [',','.',':',';','-','?','¿','¡','!','\'','–',chr(8220),chr(8221)]
    :type texto: _type_, optional
    :param todo_minusculas: Transforma a minúsculas las palabras encontradas, defaults to True
    :type todo_minusculas: bool, optional
    :param unicas: Elimina palabras duplicadas, defaults to True
    :type unicas: bool, optional
    :return: Palabras después de ser procesadas
    :rtype: list
    """
    if( type( texto ) is str):    
        palabras= obtener_palabras( texto )
    palabras= texto.copy()

    if( todo_minuscula ):
        palabras= [ palabra.lower() for palabra in palabras]

    for simbolo in remover_simbolos:
        palabras_sin_simbolos= []
        for palabra in palabras:
            palabras_sin_simbolos.append( remover_simbolo( palabra, simbolo ) )
        palabras= palabras_sin_simbolos.copy()
        

    if( unicas ):
        return sorted( set( palabras ))
    return sorted(palabras)

def obtener_promedio_palabras( oraciones: list )->float:
    """Regresa el número promedio de palabras en una lista de oraciones dadas

    :param oraciones: Lista de oraciones
    :type oraciones: list
    :return: Número promedio de parlabras por oración
    :rtype: float
    """
    promedio= 0
    for oracion in oraciones:
        promedio+= len( oracion )
    
    return promedio/len(oraciones)

def remover_simbolo( palabra:str, simbolo:str ) -> str:
    """Remueve el símbolo de una palabra, si la contiene sino regresa la palabra original

    :param palabra: Palabra a la que se le quiere remover el símbolo
    :type palabra: str
    :param simbolo: Símbolo a retirar
    :type simbolo: str
    :return: Paralbra con el símbolo retirado
    :rtype: str
    """
    return ''.join( [ letra for letra in palabra if not letra.__eq__(simbolo) ] )
    
def obtener_lemas( texto:str | list, es= True, unicos= True )->list:
    """Halla la palabra o lema que represente de forma general a las diferentes flexiones de la palabra y regresa una lista de lemas únicos

    :param texto: Texto a analizar
    :type texto: str | list
    :param es: _description_, defaults to True
    :type es: bool, optional
    :return: _description_
    :rtype: list
    """
    if( type( texto ) is list ):
        texto= " ".join( texto )
    
    # import sys
    # if( not 'spay' in sys.modules ):        
    import spacy

    if( es ):
        nlp = spacy.load('es_core_news_sm')
    else:
        nlp = spacy.load('en_core_web_sm')

    if( unicos ):
        return sorted( set([ token.lemma_.lower() for token in nlp( texto ) ] ) )
    return [ token.lemma_.lower() for token in nlp( texto ) ]

def obtener_etiquetado( texto:str | list, es=True):
    import spacy
    if( es ):
        nlp = spacy.load('es_core_news_sm')
    else:
        nlp = spacy.load('en_core_web_sm')

    if( type( texto ) is list ):
        texto= " ".join( texto )

    doc= nlp( texto )

    return { token.text: token.tag_ for token in doc }

def obtener_frecuencias( palabras: list, ordenado_por_valor=False ) -> dict:
    """Regresa un diccionario de palabras únicas con su valor de aparición en la lista de palabras pasadas a la función. 

    :param palabras: Palabras a analizar
    :type palabras: list
    :param ordenado_por_valor: Si es verdadero ordena las letras por el valor obtenido, de lo contrario las coloca por orden de aparición en las palabras, defaults to False
    :type ordenado_por_valor: bool, optional
    :return: Regresa una lista de palabras
    :rtype: dict
    """
    unicas= sorted(set( palabras ))
    if( ordenado_por_valor ):
        return dict(sorted( {unica: palabras.count( unica ) 
                                    for unica in unicas}.items(),
                            key=lambda item: item[1],
                            reverse=True) )
    return {unica: palabras.count( unica ) for unica in unicas}
