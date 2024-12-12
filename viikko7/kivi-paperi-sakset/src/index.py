from pelifactory import PeliFactory


def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input().strip().lower()

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        try:
            peli = PeliFactory.luo_peli(vastaus)
            peli.pelaa()
        except ValueError as e:
            print(e)
            break


if __name__ == "__main__":
    main()
