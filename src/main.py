import lexer
import parser

def main():

    # Get contents of the file
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()

    # Lexer
    lex = lexer.Lexer(content)
    tokens = lex.tokenize()

    # Parser
    parse = parser.Parser(tokens)
    objs = parse.parse()

main()
