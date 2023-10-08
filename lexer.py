

import re

# Tokens Classification
keywords = ["main", "void", "static", "dynamic", "null", "malloc", "break", "continue", "return",
               "this", "class", "new", "struct","cout","cin","<<",">>", "endl"]
access_modifiers = ["public", "protected", "private"]
inc_decs = ["++", "--"]
logical_and_operator = '&&'
logical_or_operator = '||'
arithmetic_operators = ["+", "-", "*", "/", "%"]
relational_operators = ["<", ">", ">=", "<=", "!=", "=="]
assignment_operators = ["+=", "-=", "*=", "/=", "%="]
assignment_op="="
conditionals = ["if", "else", "else if", "while", "for", "switch", "case", "do"]
oop_concepts = ["this", "class", "new", "struct"]
string_constant_pattern = r'"([^"\\]*(\\.[^"\\]*)*)"'

punctuators = [";", ":", ",", "(", ")", "[", "]", "{", "}"]
numeric_data_types = ["int", "float", "bool"]
character_data_types = ["char", "string"]
int_constant_pattern = r"\b[0-9]+\b"
float_constant_pattern = r"\b[0-9]*\.[0-9]+\b"
bool_constant_pattern = r"\btrue\b|\bfalse\b"
char_constant_pattern = r"\'[a-zA-Z]\'"
variable_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
dot_op="."

classification_patterns = {
    "string_constant_pattern": string_constant_pattern,
    "keywords": "|".join(keywords),
    "access_modifiers": "|".join(access_modifiers),
    "conditionals": "|".join(conditionals),
    "oop_concepts": "|".join(oop_concepts),
    "inc_decs": "|".join(map(re.escape, inc_decs)),
    "logical_and_operator": re.escape(logical_and_operator),
    "logical_or_operator": re.escape(logical_or_operator),
    "arithmetic_operators": "|".join(map(re.escape, arithmetic_operators)),
    "relational_operators": "|".join(map(re.escape, relational_operators)),
    "assignment_operators": "|".join(map(re.escape, assignment_operators)),
    "assignment_op": assignment_op, 
    "punctuators": "|".join(map(re.escape, punctuators)),
    "numeric_data_types": "|".join(numeric_data_types),
    "character_data_types": "|".join(character_data_types),
    "float_constant_pattern": float_constant_pattern,
    "int_constant_pattern": int_constant_pattern,
    "bool_constant_pattern": bool_constant_pattern,
    "char_constant_pattern": char_constant_pattern,
    "variable_pattern": variable_pattern,
    "dot_op": re.escape(dot_op)
    
}

def tokenize_cpp_code(code):
    tokens = []
    lines = code.split('\n')
    multiline_comment=False

    for line_number, line in enumerate(lines, start=1):

        if multiline_comment==True and '???' not in line:
            continue
        


        #multiline  comments logic
        if '???' in line and multiline_comment is False:

            for i in line.split():
                if '???' in i and '"' not in i:
                    # print(i)
                    split_string = i
                    if split_string in line:
                        parts = line.split(split_string, 1)  # Split the line at the first occurrence of i
                        desired_portion = parts[0]
                        # print(desired_portion)
                        line= desired_portion.strip()
                    else:
                        pass
            multiline_comment=True
        


        if '???' in line and multiline_comment is True:

            for i in line.split():
                if '???' in i and '"' not in i:
                    # print(i)
                    split_string = i
                    if split_string in line:
                        parts = line.split(split_string, 1)  # Split the line at the first occurrence of i
                        desired_portion = parts[1]
                        
                        line= desired_portion.strip()
                        # print(line)
                        
                    else:
                        pass
            multiline_comment=False

                # Skip lines that start with "?"
        if line.strip().startswith('?'):
            continue

        if line.strip().startswith('#include'):
            continue


        # Remove comments after "?" is found.
        
        split_string=''
        if '?' in line:
            
            for i in line.split():
                # print(i)
                if '?' in i and '"' not in i:
                    # print(i)
                    split_string = i
                    
                    if split_string in line:
                        parts = line.split(split_string, 1)  # Split the line at the first occurrence of i
                        desired_portion = parts[0]
                        line= desired_portion.strip()
                    else:
                        pass
        
        # print(line.split())
        





        for classification, pattern in classification_patterns.items():
            for match in re.finditer(pattern, line):
                value = match.group()
                print(value)
                
                if classification == "int_constant_pattern":
                    tokens.append(("int_constant", value, line_number))
                elif classification == "float_constant_pattern":
                    tokens.append(("float_constant", value, line_number))
                elif classification == "bool_constant_pattern":
                    tokens.append(("bool_constant", value, line_number))
                elif '"' in value:
                    #escape character logic '\'
                    escstr=''
                    escape=False
                    for i in value:


                        
                        if "\\" == i and escape==False:
                            escape=True
                            continue

                        if escape==True:
                            escstr+=i
                            escape=False
                            continue
                        escstr+=i
                        
                    
                    escstr=escstr[1:-1]
                    print(escstr)
                        

                    tokens.append(("string_constant", escstr, line_number))

                elif "'" in value:
                    tokens.append(("char_constant", value.strip("'"), line_number))
                elif classification == "dot_op":
                    tokens.append(("dot_operator", value, line_number))
                else:
                    tokens.append((classification, value, line_number))
                
                # Remove the matched token from the line
                line = line.replace(value, '', 1)

        # Print the modified line after removing matched tokens
        # print(line)

    return tokens

input_file_path = "test.cpp"  # Path to the input C++ file

with open(input_file_path, 'r') as cpp_file:
    cpp_code = cpp_file.read()


tokens = tokenize_cpp_code(cpp_code)

with open('tokens.txt','w') as file:
        file.writelines('Classification, Value, Line no.\n')

for token in tokens:
    with open('tokens.txt','a') as file:
        file.writelines(f'{token[0]}, {token[1]}, {token[2]}\n')
        