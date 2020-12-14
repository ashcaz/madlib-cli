import pytest
from madlib_cli import __version__
from  madlib_cli.madlib import read_template, parse_template,merge

def test_version():
    assert __version__ == '0.1.0'

# def test_read_file_test_output():
#   actual = read_file('../assets/test_text.txt')
#   expected = 'I the {Adjective} and {Adjective} {A First Name}'
#   assert actual == expected 

# def test_write_to_new_file_test_output():
#   actual = write_to_new_file(read_file('../assets/test_text.txt'))
#   expected = '../assets/final_madlib'
#   assert actual == expected 

# def test_parse_file():
#   actual = parse_file(read_file('../assets/test_text.txt'))
#   expected = 'I the funny and slow Ashley'
#   assert actual == expected 

def test_read_template_returns_stripped_string():
    actual = read_template("../assets/dark_and_stormy_night.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)