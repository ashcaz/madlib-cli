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
**    Type in 'YES' to begin!!     **
**                                 **
**    Exit game at anytime by      **
**        typing 'QUIT'!           **
*************************************
"""

print(welcome_logo)
print(welcome_message)

# ready_to_start = input('Are you ready to begin? > ')

# if ready_to_start.lower() is 'yes':
#   pass
# else:

def read_file(path:str='../assets/madlib.txt') -> str:
  """[Function takes in a file and returns the contents of that file]

  Args:
      path (str, optional): [the path to the file you want to read]. Defaults to '../assets/madlib.txt'.

  Returns:
      str: [contents of the file]
  """
  with open(path, 'r') as story:
    contents = story.read()
    return contents

def parse_file(content:str=read_file()) -> str:
  """[The function takes in the contents of a file and finds all the words between curly brackes using re.findall()(regex) which returns all of those words in a list]

  Args:
      contents (str, optional): [Contents of a file]. Defaults to read_file().

  Returns:
      str: [Returns the content with the updated words]
  """
  ask_questions = True

  while ask_questions:

    find_word = re.search("(?<={).+?(?=})",content)
    
    if find_word == None:
      ask_questions = False
    else:
      replace_word = input(f'Input {find_word.group(0)}: ')

      if replace_word.lower() == 'quit':
        return print('You have ended the game! Bye')

      content = re.sub("{(.*?)}", replace_word, content,1)
  
  return content



#I knew os would be what i had to import in order to remove a file but didnt know how to implemt it. Found try/except solution from https://thispointer.com/python-how-to-remove-a-file-if-exists-and-handle-errors-os-remove-os-ulink/
def write_to_new_file(content:str=parse_file()) -> str:
  """[This function will take in the contents you input and write them to a temp file. It returns the PATH of the temp file. If something is already written in the file it will delete the file and create a new one. ]

  Args:
      contents (str, optional): [What you want to write into the temp file]. Defaults to read_file().

  Returns:
      str: [the PATH to the temp file]
  """
  tmp_file_path = '../assets/final_madlib'
  try:
    os.remove(tmp_file_path)
  except FileNotFoundError:
    pass
  
  with open('../assets/madlibs_replced', 'w') as story:
    story.write(content)
  
  return content


print(f'\n\n{write_to_new_file()}')