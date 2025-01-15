open System

let countWords (text: string) =
    text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

let countCharactersWithoutSpaces (text: string) =
    text.Replace(" ", "")
        .Replace("\t", "")
        .Replace("\n", "")
        .Replace("\r", "")
        .Length

[<EntryPoint>]
let main argv =
    printf "Podaj tekst: "
    let input = Console.ReadLine()

    let wordCount = countWords input
    let charCountWithoutSpaces = countCharactersWithoutSpaces input

    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCountWithoutSpaces

    0 
