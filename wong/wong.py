from repository import BookRepository
from loader import load_db
from render import render_table


def main():
    books = load_db("book-db.csv")
    repository = BookRepository(books)
    result = repository.find_by_author('Dan')
    render_table(result)


if __name__ == '__main__':
    main()
