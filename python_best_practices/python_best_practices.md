## Creating a New Project
- First commit should consist of all the initial files like:
    - setup.py
    - requirements.txt
    - README.md
    - Dockerfile
    - .gitlab-ci.yml
    - .gitignore
    - .flake8
    - version.py

## Security
- Use only secure libraries in code. This applies for standard as well as third party libraries.  
To find out which libraries are secure, do the below.
    - Read online official documentation about the module.
    - Run python "safety" tool on requirements.txt. This covers third party libraries.
    - Run "bandit" tool on entire code. This covers standard libraries as well as code statements.
- Be cautious while handling sensitive information like credentials.

## Documentation of Technical Decisions
- Document any technical decisions like finalizing a solution/tool and ruling out others on project wiki or at some proper location.

## Imports
- Group imports as standard, third party and project specific, in the same sequence, separated by a line.
- Sort imports within each group in alphabetical order.
- from imports should be at the end of each group.

## Configuration
- Put values that may change in future into configuration file.

## Naming Convention
- Form descriptive names.
- Prefix private function names with "_" which shows that they won't be used directly and are for internal operations only.
- Name only class names in camel case and rest all i.e. methods, variables, modules, packages in small case separated by underscores.

## Docstrings
- Write descriptive docstring title for modules, classes and functions.
- Include description of below in the docstring.
    - function parameters
    - function return value , unless the function returns nothing i.e. None
    - function yield values, in case of a generator
    - default values of function parameters
    - errors raised by function explicitly

## Logging
- Use logging in final code instead of print statements.
- Write descriptive log statements.
- Classify logging statements correctly as debug, info, warning or error.
- Set low logging level low in development but high in production, so that unnecessary low level statements are not logged.

## Error Handling
- Do not write bare except: statements.
- Only catch exceptions that your codes can handle locally.
- Make use of custom exceptions in code to indicate specific types of problems with particular subsystems.
- Descend custom exceptions from a main custom exception.
- Write descriptive error messages.

## Performance (Time and/or Memory)
- Write code that ensures good performance.  
Some important ones are as below.
    - If you are performing many in checks, use sets instead of lists.
    - If you are building strings from collections use the .join() method, instead of a loop.
    - If you are dealing with large data, use generators instead of lists.
- Make sure whatever solution you device is capable of taking the load of production data.  
- Do not do something like response=get() return response, if you do not need the variable, you can directly do return get()

## Reliability
- If function is returning multiple arguments, use namedtuples to ensure accurate usage by caller.
- Do not use sys.argv, instead use argparse or fire or config file instead for named arguments.

## Readability
- Format code with Black and Flake8.
- Don't keep ToDo or FixMe statements in code. Instead, create tickets for pending changes and link them to main ticket.
- Don't write too many explanatory comments in between code lines unnecessarily, if your code is self explanatory.
- Don't keep any commented out lines on your final code.

## Code Style
- open files with context manager(with)
- Use comprehensions instead of loops to build simple collections.
- Try using shorter syntax like filter, map, reduce, lambda, generator expressions
- Care more about readability and reliability than the increased size of code.
- Compose bigger functions from multiple smaller ones.
- Dont write not worth it functions.
- Keep common code at one place and call it wherever needed or use inheritance.
- Use "easier to ask forgiveness than permission" (EAFP) style i.e. do not do too many checks before proceeding with something, rather write normal code and if something is wrong, catch it.
- Keep non functional tasks like say cryptography away from other functional code.
- Do not make classes if they are not needed, rather make standalone functions.
- Raise an exception instead of returning None to tell the caller to handle it differently.
- Dockerize the project.

## Testing
- Write tests that show how the code is expected to be used.
- Write small tests that test only one thing at a time.
- Don't write tests entirely based on mocking.
- Cover maximum code via test cases.
To find code lines not covered by your tests, run coverage command on your code.
- Write negative tests also.
- Write proper asserts. 

## Documentation (README.md)
- Make files like README.md easily followable, so that any person who tries to understand and test your project does not have to reach out to you more often. 
- Use proper markdown in README.md like titles, subtitles, bullets, tables, code blocks.  
- If there are too many setup instructions, they can be put on wiki or in a separate file and linked in the main file.  

## Referring existing code
- If you are referring existing code for your work, its not necessary that all best practices are applied on that, apply them yourself wherever it's missed.

## MR Reviews
- Develop and get code reviewed in smaller chunks.  
Ideally under 400 lines of dev code at a time, excluding tests.
- Make sure to provide details of behavioral changes, testing instructions and technical decisions documentation link in MR description.
- Make sure to resolve merge conflicts quickly, if other MRs get pushed to your master and create conflicts while yours is still in review.  
