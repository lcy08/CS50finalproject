from project import get_books, previous_title, get_title, create_data, load_data, get_pages, rewrite_data, Book
import pytest
import os
import pandas as pd
import csv

def input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "the way of king")

def test_get_books_c(monkeypatch):
    input(monkeypatch)
    with pytest.raises(SystemExit) as exit:
        get_books("c")
    assert exit.type == SystemExit
    assert exit.value.code == ("Book already on the list")

def test_get_books_p(monkeypatch):
    input(monkeypatch)
    boo = Book("The Way Of King", 1008)
    boo.reading(10)
    book = get_books("p")
    assert book.title == boo.title
    assert book.total == boo.total
    assert book.read == boo.read

def test_get_books_a():
    assert get_books("a") == False

def input_b(monkeypatch):
    inputs = iter(["the way of kings", 120])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

def test_get_books_c_b(monkeypatch):
    input_b(monkeypatch)
    with pytest.raises(SystemExit) as exit:
        get_books("c")
    assert exit.type == SystemExit
    assert exit.value.code == ("Book has been added to the list, run program again to add progress to the book")

    os.remove("The Way Of Kings.csv")
    tmp = pd.read_csv("books.csv")
    tmp = tmp.drop(tmp.index[-1])
    tmp.to_csv("books.csv", index = False)


def test_get_books_p_b(monkeypatch):
    input_b(monkeypatch)
    with pytest.raises(SystemExit) as exit:
        get_books("p")
    assert exit.type == SystemExit
    assert exit.value.code == ("Book not on the previous list, create the book's data first")

def test_get_books_a_b():
    assert get_books("a") == False


def test_previous_title():
    title = []
    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)
        for book in reader:
            title.append(book['Title'])
    assert previous_title() == title


def test_get_title(monkeypatch):
    inputs = iter(["input", "this is the way", "all i can think"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert get_title() == "Input"
    assert get_title() == "This Is The Way"
    assert get_title() == "All I Can Think"

def test_create_data():
    create_data("Deep Down Under The Sea", 190)
    assert os.path.isfile("Deep Down Under The Sea.csv") == True
    os.remove("Deep Down Under The Sea.csv")

    tmp = pd.read_csv("books.csv")
    assert "Deep Down Under The Sea" in tmp.values[-1:]
    tmp = tmp.drop(tmp.index[-1])
    tmp.to_csv("books.csv", index = False)

def test_load_data():
    out = load_data("The Way Of King")
    print(out[0])
    rows = {"Title": "The Way Of King", "page":"1008", "on page":"0"}
    print(rows)
    assert out[0] == rows


def test_get_pages(monkeypatch):
    book1 = Book("title", 100)
    book1.reading(0)

    inputs = iter(["a", "10", "100", "n", "140", "y"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert get_pages(book1) == 10
    assert get_pages(book1) == 100


def test_rewrite_data():
    title = "Deep Down Under The Sea"
    page = 190
    create_data(title, page)
    assert os.path.isfile(f"{title}.csv") == True

    book2 = Book(title, page)
    book2.reading(0)
    prog = 20
    book2.progress(prog)
    rewrite_data(book2)
    tmp = pd.read_csv(f"{title}.csv")
    assert prog in tmp.values[-1:]
    assert f"{title}" in tmp.values[-1:]

    tmp = pd.read_csv("books.csv")
    assert "Deep Down Under The Sea" in tmp.values[-1:]
    tmp = tmp.drop(tmp.index[-1])
    tmp.to_csv("books.csv", index = False)

    os.remove(f"{title}.csv")

if __name__ == "__main__":
    main()


