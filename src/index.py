from varasto import Varasto

def main():
    x = 3
    print(x)
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)

    huono = Varasto(-100.0)
    print(huono)
    huono = Varasto(100.0, -50.7)
    print(huono)

    olutta.lisaa_varastoon(1000.0)

    mehua.lisaa_varastoon(-666.0)

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
