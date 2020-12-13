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

def read_file(path:str) -> str:

  with open(path, 'r') as story:
    contents = story.read()
    return contents

