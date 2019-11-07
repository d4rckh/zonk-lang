import lexer

def main():

    # Get contents of the file
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()
    print(content)

    # Lexer
    lex = lexer.Lexer(content)
    lex.tokenize()


main()
