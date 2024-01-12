class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('Идентификатор книги должен быть целым числом')
        self.id = id_

        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должно быть целым числом')
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int) -> int:
        if not isinstance(id_, int):
            raise TypeError('Идентификатор книги должен быть целым числом')
        for i in enumerate(self.books):
            if i[1].id == id_:
                return i[0]
        raise ValueError("Книги с запрашиваемым id не существует")