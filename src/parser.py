from Objects.varObject import VariableObject

class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0
        self.transpiled_code = ""

    def parse(self):

        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])

            # TODO: let, const

            self.token_index += 1

        print(self.transpiled_code)

    def parse_variable_declaration(self, token_stream):

        tokens_checked = 0

        name = ""
        operator = ""
        value = ""

        for token in range(0, len(token_stream)):
            
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            # if the statement end is found, break the for loop.
            if token_type == "STATEMENT_END": break

            if token == 0:
                pass
                #print('Variable type: ' + token_value)
            elif token == 1 and token_type == "IDENTIFIER":
                name = token_value
            elif token == 1 and token_type != "IDENTIFIER":
                print("ERROR: invalid variable name '" + token_value + "'")
                quit()
            elif token == 2 and token_type == "OPERATOR":
                operator = token_value
            elif token == 2 and token_type != "OPERATOR":
                print("ERROR: invalid asignament operator is missing or invalid, it should be '='")
                quit()
            elif token == 3 and token_type in ["STRING","INTEGER", "IDENTIFIER"]:
                value = token_value
            elif token == 3 and token_type not in ["STRING","INTEGER", "IDENTIFIER"]:
                print('ERROR: invalid variable name')
                quit()

            tokens_checked += 1
        
        varObj = VariableObject()
        self.transpiled_code += varObj.transpile(name, operator, value)

        self.token_index += tokens_checked