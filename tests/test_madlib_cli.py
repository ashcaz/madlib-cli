from madlib_cli import __version__
from  madlib_cli.madlib_cli import *

def test_version():
    assert __version__ == '0.1.0'

def test_read_file_test_output():
  actual = read_file('../assets/test_text.txt')
  expected = 'I the {Adjective} and {Adjective} {A First Name}'
  assert actual == expected 

def test_write_to_new_file_test_output():
  actual = write_to_new_file(read_file('../assets/test_text.txt'))
  expected = True
  assert actual == expected 