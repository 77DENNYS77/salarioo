#tarea semana 13
def calcular_salario_semanal(pago_por_hora, horas_trabajadas):
    salario = pago_por_hora * horas_trabajadas
    return salario


if __name__ == "__main__":
    pago_por_hora = 5.50
    horas_trabajadas = 40

    resultado = calcular_salario_semanal(pago_por_hora, horas_trabajadas)

    print("----- Cálculo de salario semanal -----")
    print(f"Pago por hora: ${pago_por_hora}")
    print(f"Horas trabajadas: {horas_trabajadas}")
    print(f"Salario semanal: ${resultado}")
