//bank
open System

type Book (title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    //metoda
    member this.GetInfo() =
        sprintf "Tytuł: %s, Autor: %s, Liczba stron: %d" this.Title this.Author this.Pages

//user
type User (name: string) =

    //lista kszizek
    let borrowBooks = System.Collections.Generic.List<Book> ()

    member this.Name = name

    member this.BorrowBooks (book: Book) =
        borrowBooks.Add(book)
        printfn "%s wyporzyczył ksziążkę: \"%s\"" this.Name book.Title

    member this.Return_Book(book: Book) =
        if borrowBooks.Contains(book) then
            borrowBooks.Remove(book)
            printfn "%s zwrocił ksiazke \"%s\"" this.Name book.Title
        else
            printfn "%s nie ma ksiazke \"%s\" do zwrócenia" this.Name book.Title


    //metoda do wyswetlania ksiazek wypozyczonych

    member this.ListBorrowBooks() =
        if Borrowed_Books.Count > 0 then
                Borrowed_Books
                |> Aeq.map(fun book -> book.GetInfo())
                |> String.concat "\n"
                |> printfn "Książki wypożyczone prez $%s: \n %s " this.Name

        else
            printfn "%s nie ma wypozyczonych ksiazek" this.Name

type Library() =
    let mutable books = System.Collections.Generic.List<Book> ()
    member this.AddBook(book) =
        books.Add(book)
        printfn "Książka \"%s\" została dodana" book.Title

    member this.RemoveBook(book) = 
        if books.Contains(book) then
            books.Remove(book)
                printfn "Ksiazke \"%s\" zostala usunieta" this.Name book.Title
            else
                printfn "%s nie ma ksiazke \"%s\" do zwrócenia" this.Name book.Title
