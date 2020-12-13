import os

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

def write_to_new_file(contents:str=read_file()) -> str:
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
    story.write(contents)
  
  return tmp_file_path