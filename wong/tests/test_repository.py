from ward import test

from wong.repository import BookRepository


@test('test find by author should return list of book')
def _():
    books = [
        {
            'name': 'Tha gatuk book',
            'author': 'Gatuk'
        },
        {
            'name': 'The Human book',
            'author': 'human'
        }
    ]

    repository = BookRepository(books)
    actual = repository.find_by_author(name='Gatuk')
    assert 1 == len(actual)
    assert 'Gatuk' == actual[0]['author']
