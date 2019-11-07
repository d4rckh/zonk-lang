import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        
        tokens = []
        source_code = self.source_code.split()
        source_index = 0 # keep track of the word index.
         
        while source_index < len(source_code):
            word = source_code[source_index]

            if word == "var": tokens.append(["VAR_DECLARATION", word]) # variable declaration
            elif re.match('[a-z]', word) or re.match('[A-Z]', word): tokens.append(['IDENTIFIER', word]) # words
            elif re.match('[0-9]', word): tokens.append(['INTEGER', word]) # integers
            elif word in "=/x=-+": tokens.append(['OPERATOR', word]) # operators

            source_index += 1
        
        return tokens