#assert .- Si la condicion se cumple el programa continua su ejecución, si no se lanza exception

def suma_numeros_positivos(n1: int, n2: int)-> int:
    """Permite sumar dos numeros positivos

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        int: _description_
    """
    assert n1 > 0 and n2 > 0, 'Lo sentimos, solo es posible sumar numeros positivos.'

    return n1 + n2

if __name__ == '__main__':
    resultado = suma_numeros_positivos(-10, 20)
    print(resultado)