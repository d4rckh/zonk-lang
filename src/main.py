import lexer

def main():

    # Get contents of the file
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()

    # Lexer
    lex = lexer.Lexer(content)
    print(lex.tokenize())


main()
