import os
import re

welcome_logo = """
███╗   ███╗ █████╗ ██████╗ ██╗     ██╗██████╗ 
████╗ ████║██╔══██╗██╔══██╗██║     ██║██╔══██╗
██╔████╔██║███████║██║  ██║██║     ██║██████╔╝
██║╚██╔╝██║██╔══██║██║  ██║██║     ██║██╔══██╗
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗██║██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚═════╝ 
                                              
"""
welcome_message = """
*************************************
**     Welcome to the MADLIB!      **
**                                 **
**  Mad Libs is a phrasal template **
**   word game which consists of   **
**   one player prompting others   **
**   for a list of words to        **
**   substitute for blanks in a    **
**   story before reading aloud.   **
**                                 **
**  This game will prompt you for  **
**  words (Nouns, verbs, adj &     **
**  adverbs) for our fill-in-the-  **
** blank stories.When you are done **
**  entering all the words MADLIB  **
**   will print out a strange,     **
**  hilarious, and original story  **
**       for you to read!          **
**                                 **
**                                 **
**    Exit game at anytime by      **
**        typing 'QUIT'!           **
*************************************
"""

def read_template(path:str) -> str:
  """[Function takes in a file and returns the contents of that file]

  Args:
      path (str, optional): [the path to the file you want to read]. Defaults to '../assets/madlib.txt'.

  Returns:
      str: [contents of the file]
  """
  if os.path.exists(path):
    with open(path, 'r') as story:
      content = story.read()
      return content
  else:
    raise FileNotFoundError("The limit does not exist")


def parse_template(content:str):
  """[The function takes in the contents of a file and finds all the words between curly braces. It returns the string without those words and a tuple that house all the words found withon the curly braces]

  Args:
      contents (str, optional): [Contents of a file]. Defaults to read_template().

  Returns:
      str: [The content minus words found between {}]
      tuple: [The word found in the {}]
  """
  stripped_words = tuple(re.findall("(?<={).+?(?=})",content))

  content = re.sub("(?<={).+?(?=})", '', content)
    
  return content, stripped_words

def get_user_inputs(stripped_words: tuple) -> tuple:
  """[This function stakes the words stripped out of the content and replaces each word with user input]

  Args:
      stripped_words (tuple): [the words stripped from the content]

  Returns:
      tuple: [words to be replaced in the content]
  """

  user_input_list = []

  for word in stripped_words:
    user_input = input(f'Input {word}: ')

    if user_input.lower() == 'quit':
      return print('You have ended the game! Bye')
    else:
      user_input_list.append(user_input)

  return tuple(user_input_list)

# #I knew os would be what i had to import in order to remove a file but didnt know how to implemt it. Found try/except solution from https://thispointer.com/python-how-to-remove-a-file-if-exists-and-handle-errors-os-remove-os-ulink/

def merge(content:str,tuple_of_words: tuple) -> str:
  """[This function will take in the contents of a file and a tuple of words(i.e Noun, adj, etc.). It returns the content with the new words entered]

  Args:
      contents (str): [conents of file minus madlib words].
      tuple_of_words (tuple): [data structure of mad lib words]. Defaults to read_file().

  Returns:
      str: [The content with newly replaced words from user input]
  """
  for word in tuple_of_words:
    content = re.sub("{(.*?)}", word, content, 1)
      
  return content
  
  
def write_template(content:str) -> str:
  """[This function writes content to a file]

  Args:
      content (str, optional): [takes in the content to write to temp file]. Defaults to merge().

  Returns:
      str: [return the temp file path]
  """
  tmp_file_path = '../assets/final_madlib'
  try:
    os.remove(tmp_file_path)
  except FileNotFoundError:
    pass

  with open('../assets/final_madlib', 'w') as story:
     story.write(content)

  return tmp_file_path


print(welcome_logo)
print(welcome_message)
content,stripped_words = parse_template(read_template('../assets/madlib.txt'))
new_content = merge(content,stripped_words)
write_template(new_content)
print(new_content)