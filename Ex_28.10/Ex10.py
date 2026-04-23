def agendar_consulta(dia):
    if dia < 1 or dia > 31:
        raise ValueError("Dia inválido para agendamento.")
    else:
        return f"Consulta agendada para o dia {dia}."