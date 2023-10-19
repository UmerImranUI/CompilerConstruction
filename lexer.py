import re

KeyWord = {
    "DataType": ["int","float","char","string","bool","double","short"],
    "if": "if",
    "while": "while",
    "else": "else",
    "do": "do",
    "for": "for",
    "const": "const",
    "Jump statements": ["break","continue"],
    "return": "return",
    "void": "void",
    "Access Modifier": ["public","private","protected"],
    "class": "class",
    "enum": "enum",
    "static": "static",
    "virtual": "virtual",
    "friend": "friend",
    "abstract": "abstract",
    "cin": "cin",
    "cout": "cout",
    "new": "new",
    "true": "true",
    "false": "false",
    "main": "main"
}

Operator = {
    "inc/dec": ["++","--"],
    "!": "!",
    "PM": ["+","-"],
    "MDM": ["*","/","%"],
    "RO": ["<>","<=",">=","!=","==","<",">"],
    "LO": ["&&","||"],
    "=": "=",
    #"*": "*",
    "PMMDM": ["+=","-=","*=","/=","%="]
}

Punctuator = {
    ",": ",",
    ";": ";",
    ":": ":",
    "[": "[",
    "{": "{",
    "(": "(",
    "]": "]",
    "}": "}",
    ")": ")",
    "::": "::",
    "~": "~",
    ".": "."
}

def isKeyWord(ui):
    for item in KeyWord:
        if (item == "DataType"):
            for j in range (7):
                #print(KeyWord[item][j])
                if (ui == KeyWord[item][j]):
                    #isExist = True
                    #print("Yes it exist")
                    #print(ui,"  ",item)
                    return item
        elif(item == "Jump statements"):
            for k in range (2):
                if (ui == KeyWord[item][k]):
                    #print("Yes it exist")
                    #print(ui,"  ",item)
                    return item
        elif(item == "Access Modifier"):
            for l in range (3):
                if(ui == KeyWord[item][l]):
                    #print(ui,"  ",item)
                    return item
        elif(ui == item):
            return item

    return None


def isOperator(ui):
    for item in Operator:
        if (item == "inc/dec"):
            for j in range (2):
                #print(KeyWord[item][j])
                if (ui == Operator[item][j]):
                    return item
        elif(item == "PM"):
            for k in range (2):
                if (ui == Operator[item][k]):
                    #print("Yes it exist")
                    #print(ui,"  ",item)
                    return item
        elif(item == "MDM"):
            for l in range (3):
                if(ui == Operator[item][l]):
                    #print(ui,"  ",item)
                    return item
        elif(item == "LO"):
            for j in range (2):
                if(ui == Operator[item][j]):
                    #print(ui,"  ",item)
                    return item
        elif(item == "RO"):
            for k in range (7):
                if(ui == Operator[item][k]):
                    #print(ui,"  ",item)
                    return item
        elif(item == "PMMDM"):
            for l in range (5):
                if(ui == Operator[item][l]):
                    #print(ui,"  ",item)
                    return item
        elif(ui == item):
            #isExist = True
            #print("Yes it exist")
            #print(item)
            return item
    #print("Sorry not exist")
    return None


def isPunctuator(ui):
    for item in Punctuator:
        if (ui == item):
            #print(item)
            return item
    #print("Sorry not found")
    return None
    


def isIdentifier(ui):
    pattern = re.compile(r'^[_a-zA-Z][a-zA-Z0-9_]*$')
    if(pattern.match(ui)):
        return True
    else:
        return False

def isIntConstant(ui):
    pattern = re.compile(r'^\d+$')
    if(pattern.match(ui)):
        return True
    else:
        return False

def isFloatConstant(ui):
    pattern = re.compile(r'^(\+|-)*\d*\.\d+$')
    if(pattern.match(ui)):
        return True
    else:
        return False

def isStringConstant(ui):
    pattern = re.compile(r'^\"(\D*|\d*)\"$')
    if(pattern.match(ui)):
        return True
    else:
        return False

def isCharConstant(ui):
    pattern = re.compile(r'^\'([^\'\"\\]|\\(\'|\"|\\)|\\(n|t|r|f|b|v|a))\'$')
    if(pattern.match(ui)):
        return True
    else:
        return False


    
Tokens = []

class Token:
    def __init__(self):
        self.className = "",
        self.value = "",
        self.lineNumber = 0

def token():
    file = open("cpp.txt","r")
    input = file.read()
    #lines = input.strip()
    #lines = input.split("\n")
    #res = data.replace('_', ' ').replace(', ', ' ').split()
    lines = input.replace('\t','').split("\n")
    #lines.remove('')
    t = 0
    #lines = lines.split("\t")
    #print(lines)
    #length_of_line = len(lines)
    #print(len(lines))
    #return lines[i]
    #print("umer")
    #for t in range(len(lines)):
    while(t < len(lines)):
        #print(t)
        line = lines[t]
        sp = []
        temp = ''
        i = 0
        #for i in range (len(line)):
        while (i < len(line)):
            #print(i)
            #print(line[i])
            if line[i]==' ':
                #sp.append(temp)
                #temp = ''
                if(temp==''):
                    #sp.append(temp)
                    temp=''
                else:
                    if '\"' in temp:
                        temp+=line[i]
                    else:
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '.'):
                j = i - 1
                if((line[j] >= '0' and line[j] <= '9') or
                   line[j] == '' or temp == ''):
                    #print(len(line),"   ",i)
                    temp += line[i]
                    i = i + 1
                    #print(i)
                    while(line[i] != '.' and i != len(line)-1):
                        #print("Qasim")
                        temp += line[i]
                        i = i + 1
                        #print(i)
                    if(i == len(line)-1):
                        #print("umer")
                        sp.append(temp)
                        temp = ''
                        temp+=line[i]
                    #temp += line[i]
                    sp.append(temp)
                    temp = ''
                    if(line[i] == '.'):
                        sp.append(line[i])
                        temp = ''
                else:
                    #print("QASIM")
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''
            elif (line[i]=='~'):
                if(temp == ''):
                    sp.append(line[i])
                else:
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''
            #elif (line[i] == '\"'):
                #i = i + 1
                #while (line[i] != '\"'):
                #    temp+=line[i]
                #    i = i + 1
                #sp.append(temp)
                #temp = ''
            elif (line[i]=='+' or line[i]=='-'):
                j = i + 1
                if (temp==''):
                    if (line[j] >= '0' and line[j] <= '9'):
                        #print("umer")
                        temp += line[i]
                    #sp.append(temp)
                    elif (line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        sp.append(line[i])
                        temp = ''
                elif '\"' in temp:
                    temp+=line[i]
                else:
                    sp.append(temp)
                    #sp.append(i)
                    temp = ''
                    #print(line[i])
                    if (line[j] == line[i]):
                        #print("umer")
                        temp += line[i]
                        temp += line[j]
                        i=i + 1
                        sp.append(temp)
                        temp = ''
                    elif (line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '='):
                if (temp == ''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    j = i + 1
                    if(line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '*' or line[i] == '%'):
                if (temp == ''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    j = i + 1
                    if(line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '/'):
                j = i + 1
                if (temp == ''):
                    if(line[j] == 'm'):
                        #t = t + 1
                        #while (lines[t][i] != '/'):
                            #print(lines[t][i])
                        #    i = i + 1
                        #i = i + 1
                        #break
                        i = i + 2
                        while (lines[t][i] != '/' or lines[t][i+1] != 'm'):
                            #print("umer")
                            if(i == len(lines[t])-2):
                                #print(len(lines[t]) - 1)
                                t = t + 1
                                i = 0
                            else:
                                i = i + 1
                            #print(i)
                        #print(line,"    ",i)
                        #print(lines[t])
                        t = t + 1
                        line = lines[t]
                        i = -1
                        #print(line,"    ",i)
                    elif(line[j] == 'c'):
                        i = i+1
                        while (line[i] != '/' ):
                            #print(line[i])
                            #j = i
                            i = i+1
                        i = i + 1  
                    
                    else:
                        sp.append(line[i])
                        temp = ''
                #if '\"' in temp:
                #    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    
                    if(line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                        #print(line[i])
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '\''):
                j = i + 1
                if(temp == ''):
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\''):
                        if(i == len(line)-1):
                            break
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
                else:
                    sp.append(temp)
                    temp = ''
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\''):
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
            elif (line[i] == '\"'):
                j = i + 1
                if(temp == ''):
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\"'):
                        if(i == len(line)-1):
                            break
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
                else:
                    sp.append(temp)
                    temp = ''
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\"'):
                        if(i == len(line)-1):
                            break
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
            elif (line[i] == '!' or line[i] == '<' or line[i] == '>'):
                #print("umer")
                if (temp == ''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    j = i + 1
                    if(line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    elif(line[j] == '<' or line[j] == '>'):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        #print("umer")
                        #sp.append(line[i])
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i]==';' or line[i]=='(' or line[i]==')' or line[i]=='{' or line[i]=='}' or line[i]=='[' or line[i]==']'):
                if (temp==''):
                    #sp.append(temp)
                    #print("umer")
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    #print("umer")
                    temp+=line[i]
                else:
                    #print(temp)
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''
            elif (line[i]==','):
                if (temp==''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp+=line[i]
                else:
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''
            
            elif (line[i] == ':'):
                j = i + 1
                if (temp==''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp+=line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    if(i == len(line) - 1):
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                    else:
                        if(line[j] == line[i]):
                            temp += line[i]
                            temp += line[j]
                            i = i + 1
                            sp.append(temp)
                            temp = ''
                        else:
                            sp.append(line[i])
                            temp = ''
            elif (line[i] == '&' or line[i] == '|'):
                j = i + 1
                if(temp==''):
                    if(line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        sp.append(temp)
                        sp.append()
                elif '\"' in temp:
                    temp+=line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    if(line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        sp.append(temp)
                        sp.append()
            #elif i=='\'':
            #    i+=1
            #    while (i=='\''):
            #        temp += i
            #        i+=1
            else:
                temp+=line[i]

            i+=1

        #if (temp==';' or temp=='(' or temp==')' or temp=='{' or temp=='}'):
        #    sp.append(temp)
        #    temp = ''
        if temp:
            #print("QASIM")
            sp.append(temp)
            temp = ''

        #sp.remove('')
        
        for j in sp:
            #print(" j : ",j[0])
            Tobj = Token()
            if(j[0] == '_'):
                if(isIdentifier(j)):
                    #Tobj = Token("ID",j,t)
                    Tobj.className = "ID"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    #Tobj = Token("Invalid Lexeme",j,t)
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
            elif((j[0] >= 'a' and j[0] <= 'z') or (j[0] >= 'A' and j[0] <= 'Z')):
                if(isIdentifier(j)):
                    CP = isKeyWord(j)
                    if(CP == None):
                        Tobj.className = "ID"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        #Tobj = Token(CP,j,t)
                        if (CP != j):
                            Tobj.className = CP
                            Tobj.value = j
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                        else:
                            Tobj.className = CP
                            Tobj.value = ""
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                else:
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
            elif(j[0] >= '0' and j[0] <= '9'):
                if(isIntConstant(j)):
                    #(j[0] == '+' and j[1] >= '0' and j[1] <= '9')
                    Tobj.className = "Int Const"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                elif(isFloatConstant(j)):
                    Tobj.className = "Float Const"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    #print("umer")
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
            elif ((j[0] == '+' and len(j) > 1) or (j[0] == '-' and len(j) > 1)):
                #print("umer")
                if(j[1] >= '0' and j[1] <= '9'):
                    if(isIntConstant(j)):
                        #(j[0] == '+' and j[1] >= '0' and j[1] <= '9')
                        Tobj.className = "Int Const"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    elif(isFloatConstant(j)):
                        Tobj.className = "Float Const"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        #print("umer")
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                else:
                    CP = isOperator(j)
                    if(CP == None):
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = CP
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            elif (j[0] == '.'):
                if(j == '.'):
                    Tobj.className = "."
                    Tobj.value = ""
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    if(isFloatConstant(j)):
                        Tobj.className = "Float Const"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            elif (j[0] == '\"'):
                if(isStringConstant(j)):
                    Tobj.className = "String Constant"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    if(j[-1] == '\"'):
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:-1]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            elif (j[0] == '\''):
                if(isCharConstant(j)):
                    Tobj.className = "Char Const"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    if(j[-1] == '\''):
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:-1]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            else:
                CP = isOperator(j)
                if(CP == None):
                    CJ = isPunctuator(j)
                    if (CJ == None):
                        #print("umer")
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        if(CJ == j):
                            Tobj.className = CJ
                            Tobj.value = ""
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                        else:
                            Tobj.className = CJ
                            Tobj.value = j
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                else:
                    if (CP == j):
                        Tobj.className = CP
                        Tobj.value = ""
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = CP
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
        t+=1

    return Tokens



def write_in_file(tk,umer_file):
    with open(umer_file, 'w') as file:
        for token in tk:

            file.write(f"{token.className}, {token.value}, Line: {token.lineNumber}\n")
        file.write(f"$, , Line: {token.lineNumber + 1}")




    
if __name__ == '__main__':
    umer_file = 'tokens.txt'
    tk = token()
    write_in_file(tk,umer_file)
    print("file parsed.")
