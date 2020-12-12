# Lab - Class 03: Errors, Files, and Packaging

### Author: Ashley Casimir

- [Pull Request URL](https://github.com/ashcaz/madlib-cli/pull/3) 

### Set it up

Use the following commands to set up the project:

```
$ poetry new madlib-cli
$ cd madlib-cli
$ poetry add --dev black --allow-prereleases
$ touch madlib_cli/madlib_cli.py
$ mv README.rst README.md
$ git init
$ git add .
$ git commit -m "first commit"
```
Now you are ready to rock and roll!

To start your enviornment use:
- ```$ poetry shell```

To run the program and see the output run:
- `$ python madlib-cli.py` or `$ python3 madlib-cli.py` depending on your seystem

### Assignment

- Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:
  - Print a welcome message to the user, explaining the Madlib process and command line interactions
  - Read a template Madlib file (Example), and parse that file into usable parts.
    - You need to decide what components of this file are useful, and how to break those useful pieces apart
  - Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
  - With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
  - After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
  - Write the completed text (Example)to a new file on your file system (in the repo).
- **Note**: A smaller example file is included as well which can be handy when developing/testing.