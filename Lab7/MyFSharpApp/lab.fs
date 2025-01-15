// For more information see https://aka.ms/fsharp-console-apps
printfn "Hello from F#"
type Person(name: string, age: int) =
    //pola przywatne
    let mutable privateAge = age
    //public
    //val mutable public Name: string
    //własciwiości
    member this.Name = Name

    //get set
    member this.Age
        with get() = privateAge
        and set(value) =
            if value > 0 then
                privateAge <-  value
            else
                printfn "Wiek musi być liczbą dodatnią"

    //metoda
    member this.View() =
        printfn "Witaj %s masz %d lat." this.Name this.Age

//klasa pochodna
type Student(name: string, age: int, nrAlbumu: string) =
    inherit Person(name, age)

    //wlasciwosci
    member this.NrAlbumu = nrAlbumu

    override this.View() = 
        printfn "Witaj %s masz %d lat, nr albumu %s" this.Name this.Age this.NrAlbumu

//obiekt klasy
let person = Person("Jan", 23)
person.View()
person.Name <- "Janina"


[<AbstractClass>]
type Shape () =
    abstract member Area : unit -> float
    member this.View() =
        printfn "To jest zwykla metoda z klasy abstracyjnej"

type Circle (radius: float) =
    inherit Shape()

    override this.Area () =
        System.Math.PI * radius * radius

type IShape =
    abstract member Area: float
    abstract member Area1: unit -> float


type Circle1(radius: float) =
    interface IShape with
        //wlasciwosci
        member this.Area = System.Math.PI * radius * radius

        //metoda
        member this.Area1 (): float =
            System.Math.PI * radius * radius




                    

    

