
def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, un palindromo.

    Args:
        sentence: string
    
    Returns:
        bool

    Para testear nos vamos a consola y tecleamos:
        1.- Python3
        2.- Importamos el metodo a testear de nuestro archivo (from docstring import palindromo)
        3.- Introducimos nuestras pruebas:
            - palindromo('Anita lava la tina')
            - palindromo('Otra cadena de prueba')
    Se almacena en __doc__
    Se revisa en help(palindromo)

    Examples:
    >>> palindromo('Anita lava la tina')
    True

    Para probar en terminal tecleamos:
        python3 -m doctest docstring.py -v
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]