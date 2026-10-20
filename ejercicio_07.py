"""Pila dinámica enlazada y evaluación de expresiones posfijas."""


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class PilaDinamica:
    def __init__(self):
        self.tope = None
        self.cantidad = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        self.tope = Nodo(dato, self.tope)
        self.cantidad += 1

    def peek(self):
        if self.esta_vacia():
            raise ValueError("Pila vacía")
        return self.tope.dato

    def pop(self):
        dato = self.peek()
        self.tope = self.tope.siguiente
        self.cantidad -= 1
        return dato


def evaluar(expresion):
    pila = PilaDinamica()
    for token in expresion.split():
        if token in ("+", "-", "*", "/", "^"):
            if pila.cantidad < 2:
                raise ValueError("Faltan operandos")
            b = pila.pop()  # Primero sale el operando derecho.
            a = pila.pop()
            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                if b == 0:
                    raise ValueError("División entre cero")
                resultado = a / b
            else:
                resultado = a ** b
            pila.push(resultado)
        else:
            try:
                pila.push(float(token))
            except ValueError:
                raise ValueError("Token inválido: " + token)
    if pila.cantidad != 1:
        raise ValueError("Expresión vacía o sobran operandos")
    return pila.peek()


def mostrar(numero, expresion):
    print(f"Ejercicio {numero}")
    print(f"Expresión posfija: {expresion}")
    try:
        print(f"Resultado: {evaluar(expresion):g}")
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    mostrar(7, "15 5 + 7 3 - /")
