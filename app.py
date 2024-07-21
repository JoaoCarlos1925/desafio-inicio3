def calculate_bmi(weight, height):
    return weight / (height * height)

if __name__ == "__main__":
    weight = float(input("Digite seu peso em kg: "))
    height = float(input("Digite sua altura em metros: "))
    bmi = calculate_bmi(weight, height)
    print(f"Seu IMC é: {bmi:.2f}")
    