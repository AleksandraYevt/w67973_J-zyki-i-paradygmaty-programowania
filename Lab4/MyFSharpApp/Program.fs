// For more information see https://aka.ms/fsharp-console-apps
//printfn "Hello from F#"
// let x = 5 // Zmienna o nazwie `x` z wartością 5
// let y = "Hello" // Zmienna `y` z łańcuchem znaków
// printfn "Witaj, świecie!"
// printfn "Wartość zmiennej x: %d" x
// printfn "Pod wartością y mamy: %s" y

// printfn "Podaj swoje imię: "
// let name = System.Console.ReadLine()
// printfn "Witaj, %s!" name // %s - oznacza wstawienie łańcucha znaków
// printfn "Podaj liczbę: "
// let input = System.Console.ReadLine()
// let number = int input // Konwersja tekstu na liczbę całkowitą
// printfn "Wpisałeś liczbę: %d" number

// type Osoba = {
//     Imie: string
//     Wiek: int
// }
// let osoba1 = { Imie = "Anna"; Wiek = 30 }
// let osoba2 = { osoba1 with Wiek = 31 }

// printfn "%A" osoba1
// printfn "%A" osoba2

// type Komunikat =
//     | Powitanie of string
//     | Rozlaczenie
//     | KomunikatBlad of string
// let wyswietlKomunikat komunikat =
//     match komunikat with
//     | Powitanie imie -> printfn "Witaj, %s!" imie
//     | Rozlaczenie -> printfn "Do widzenia!"
//     | KomunikatBlad blad -> printfn "Błąd: %s" blad
// wyswietlKomunikat (Powitanie "Anna") // Witaj, Anna!
// wyswietlKomunikat Rozlaczenie // Do widzenia!
// wyswietlKomunikat (KomunikatBlad "Nieznany błąd") // Błąd: Nieznany błąd
