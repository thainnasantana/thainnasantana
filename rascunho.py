salario = float(input())
reajuste1 = (salario*15) / 100
if salario <= 400.00:
    print("Novo Salário: %0.2f" %salario + reajuste1)