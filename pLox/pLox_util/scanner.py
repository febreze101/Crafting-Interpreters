from typing import List

# local imports
from lox_token import Token
from token_type import TokenType
from lox import Lox


class Scanner:
    # vars
    
    
    def __init__(self, source: str) -> None:
        self.source: str = source
        self.tokens: List[Token] = []
        self.start: int = 0
        self.current: int = 0
        self.line: int = 1
        
    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
            
        self.tokens.append(Token(
                type=TokenType.EOF,
                lexeme="",
                literal=None,
                line=self.line
             ))
        
        return self.tokens
    
    def scan_token(self):
        """scan and add token"""
        c = self.advance()
        match c:
            case '(':
                self.add_token(TokenType.LEFT_PAREN)
            case ')':
                self.add_token(TokenType.LEFT_PAREN)
            case '{':
                self.add_token(TokenType.LEFT_BRACE)
            case '}':
                self.add_token(TokenType.RIGHT_BRACE)
            case ',':
                self.add_token(TokenType.COMMA)
            case '.':
                self.add_token(TokenType.DOT)
            case '-':
                self.add_token(TokenType.MINUS)
            case '+':
                self.add_token(TokenType.PLUS)
            case ';':
                self.add_token(TokenType.SEMICOLON)
            case '*':
                self.add_token(TokenType.STAR)
            case '!':
                self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case '=':
                self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '>':
                self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            # case '/':
                # if self.match('/')
            case _:
                Lox.error(line=self.line, message='Unexpected Character')
                
        
    def advance(self):
        """helper method to advance to the next token"""
        next = self.current + 1
        return self.source[next]
    
    def add_token(self, token: TokenType):
        """calls add_token with None as the literal"""
        self.add_token(token, None)
    
    def add_token(self, literal: object = None):
        """appends a new token to the tokens list"""
        text = self.source[self.start : self.current]
        self.tokens.append(Token(
            type=type,
            lexeme=text,
            literal=literal,
            line=self.line
        ))
        
    def match(self, expected):
        """Match a character to the expected character.
        Used for situations like '!=' where we want to match both characters together in one go."""
        if self.is_at_end() : return False
        
        if self.source[self.current] is not expected : return False
        
        self.current += 1
        return True
    
    def is_at_end(self):
        return self.current >= len(self.source)
        
    