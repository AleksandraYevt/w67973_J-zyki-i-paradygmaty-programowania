// Zadanie 1. Stwórz aplikację konsolową, która oblicza wskaźnik masy ciała (BMI) użytkownika na
// podstawie wprowadzonych przez niego wagi (kg) i wzrostu (cm). Program powinien komunikować się z
// użytkownikiem, odczytywać dane wejściowe, przeliczać BMI i wyświetlać wynik wraz z kategorią BMI.
// Wymagane funkcje:
// • Komunikacja z użytkownikiem: Odczyt danych za pomocą Console.ReadLine() i wyświetlanie
// wyników za pomocą printfn.
// • Przekształcanie typów: Konwersja danych wejściowych z string na float.
// • Instrukcje warunkowe: Określenie kategorii BMI na podstawie wartości obliczonej.
// • Niezmienne struktury danych: Możesz użyć rekordów do przechowywania danych użytkownika.


type UserData = {
    Weight: float
    Height: float
    BMI: float
}

let categorize_BMI bmi =
    match bmi with
    | value when value >= 40.0 -> "You're Obese"
    | value when value >= 30.0 -> "You're Overweight"
    | value when value >= 18.5 -> "You have Normal weight"
    | _ -> "You're Underweight"

let calculate_BMI weight height = weight / (height * height)

printfn "Program to calculate body mass index (BMI)!"
printfn "Enter your weight (in kilograms): "
let input1 = System.Console.ReadLine()
let weight = float input1
printfn "Enter your height (in metres): "
let input2 = System.Console.ReadLine()
let height = float input2

let user = {
    Weight = weight
    Height = height
    BMI = calculate_BMI weight height
}

printfn "Your's results:\nYour BMI is %F " user.BMI
printfn "%s" (categorize_BMI user.BMI)

