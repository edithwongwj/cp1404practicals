"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""
from programming_language import ProgrammingLanguage

def main():
    """Test the ProgrammingLanguage class."""
    # Create three ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Test the __str__ method by printing one of them
    print(python)
    print() # Just an empty line for neat formatting

    # Put the objects into a list
    languages = [python, ruby, visual_basic]

    # Loop through the list and print only the dynamic ones
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == '__main__':
    main()