from src.calculator import Calculator

calc = Calculator()
result = []

result.append([
    "Add",
    "1, 1",
    2,
    calc.add(1, 1),
    "Pass" if calc.add(1, 1) == 2 else "Fail"
])

result.append([
    "Subtract",
    "5, 1",
    4,
    calc.subtract(5, 1),
    "Pass" if calc.subtract(5, 1) == 4 else "Fail"
])

result.append([
    "Multiply",
    "2, 4",
    8,
    calc.multiply(2, 4),
    "Pass" if calc.multiply(2, 4) == 8 else "Fail"
])

result.append([
    "Divide",
    "6, 2",
    3,
    calc.divide(6, 2),
    "Pass" if calc.divide(6, 2) == 3 else "Fail"
])

result.append([
    "Power",
    "2, 2",
    4,
    calc.power(2, 2),
    "Pass" if calc.power(2, 2) == 4 else "Fail"
])

result.append([
    "Sqrt",
    "16",
    4,
    calc.sqrt(16),
    "Pass" if calc.sqrt(16) == 4 else "Fail"
])

result.append([
    "Modulo",
    "10, 6",
    4,
    calc.modulo(10, 6),
    "Pass" if calc.modulo(10, 6) == 4 else "Fail"
])

print(f"{'Metod':<12} | {'Input':<10} | {'Förväntat':<12} | {'Faktiskt':<12} | {'Pass/Fail'}")
print("-" * 80)
for row in result:
    print(f"{row[0]:<12} | {row[1]:<10} | {row[2]:<12} | {row[3]:<12} | {row[4]}")

if calc.add(1, 1) == 2:
    print("Add = Korrekt")
else:
    print("Add = Wrong")

if calc.subtract(5, 1) == 4:
    print("Sub = Korrekt")
else:
    print("Sub = Wrong")

if calc.multiply(2, 4) == 8:
    print("Mul = Korrekt")
else:
    print("Mul = Wrong")

if calc.divide(6, 3) == 2:
    print("Div = Korrekt")
else:
    print("Div = Wrong")

if calc.power(2, 2) == 4:
    print("Power = Korrekt")
else:
    print("Power = Wrong")

if calc.sqrt(16) == 4:
    print("Sqrt = Korrekt")
else:
    print("Sqrt = Wrong")

if calc.modulo(10, 6) == 4:
    print("Mod = Korrekt")
else:
    print("Mod = Wrong")
