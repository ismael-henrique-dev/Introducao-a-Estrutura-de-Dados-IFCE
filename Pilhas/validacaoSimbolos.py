def verifica_simbolos(expressao):
    pilha = []
    for simbolo in expressao:
        if simbolo in '([{':
            pilha.append(simbolo)
        elif simbolo == ')' and (not pilha or pilha.pop() != '('):
            return False
        elif simbolo == ']' and (not pilha or pilha.pop() != '['):
            return False
        elif simbolo == '}' and (not pilha or pilha.pop() != '{'):
            return False
    
    return len(pilha) == 0

print(verifica_simbolos("{[()]}"))  # Saída esperada: True
print(verifica_simbolos("{[(])}"))  # Saída esperada: False
