open System


let isPalindrome (text: string) =
    let cleanedText = 
        text.ToLower()
        |> Seq.filter Char.IsLetterOrDigit
        |> Seq.toArray
    cleanedText = Array.rev cleanedText

printfn "Podaj ciąg znaków: "
let userInput = Console.ReadLine()

if isPalindrome userInput then
    printfn "Podany ciąg jest palindromem."
else
    printfn "Podany ciąg nie jest palindromem."