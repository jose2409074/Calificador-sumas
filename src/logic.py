def validar_operacion(entrada):
    partes = entrada.split("=")
    operacion = partes[0].strip()
    resultado_alumno = int(partes[1].strip())

    resultado_real = eval(operacion)

    return resultado_real == resultado_alumno
