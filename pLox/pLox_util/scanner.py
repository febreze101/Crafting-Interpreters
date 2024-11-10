from typing import List

# local imports
from lox_token import Token
from token_type import TokenType
from lox import Lox

KEYWORDS = {
    "and": TokenType.AND,
    "class": TokenType.CLASS,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "for": TokenType.FOR,
    "fun": TokenType.FUN,
    "if": TokenType.IF,
    "null": TokenType.NULL,
    "or": TokenType.OR,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "var": TokenType.VAR,
    "while": TokenType.WHILE
}

class Scanner: 
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
            case '/':
                if self.match('/'):
                    # comment will go til the end of the line
                    while self.peek() != '\n' and not self.is_at_end: 
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n':
                self.line += 1
            case '"':
                self.string()
            case _:
                if self.is_digit(c):
                    self.number()
                elif self.is_alpha(c):
                    self.identifier()
                else:
                    Lox.error(line=self.line, message='Unexpected Character')
                
        
    def advance(self) -> str:
        """helper method to advance to the next token"""
        next = self.current + 1
        return self.source[next]
    
    def add_token(self, token: TokenType):
        """calls add_token with None as the literal"""
        self.add_token(token=token, literal=None)
    
    def add_token(self, token:TokenType, literal: object = None):
        """appends a new token to the tokens list"""
        text = self.source[self.start : self.current]
        self.tokens.append(Token(
            type=type,
            lexeme=text,
            literal=literal,
            line=self.line
        ))
        
    def peek(self) -> str:
        """Looks at the next character without advancing"""
        if self.is_at_end():
            return '\0'
        return self.source[self.current]
    
    def peek_next(self) -> str:
        if not self.source[self.current + 1] >= len(self.source):
            return self.source[self.current + 1]
        
    def match(self, expected: str) -> bool:
        """Match a character to the expected character.
        Used for situations like '!=' where we want to match both characters together in one go."""
        if self.is_at_end() : return False
        
        if self.source[self.current] is not expected : return False
        
        self.current += 1
        return True
    
    def is_digit(self, c: str) -> bool:
        """check if the character is a digit"""
        return c.isdigit()
    
    def is_alpha(self, c: str) -> bool:
        """check if the character is an alphabetical character"""
        return True if c.isalpha() or c == '_' else False
    
    def is_alpha_numeric(self, c: str) -> bool:
        """Check if the character is alpha-numeric"""
        return c.isalnum()
        
    def string(self):
        """If we encounter a single quote, we will read until we reach another single quote."""
        """If we reach the a return character, go to the next line."""
        while self.peek() is not '"' and not self.is_at_end():
            if self.peek() is '\n':
                self.line += 1
            self.advance()
            
        if self.is_at_end():
            Lox.error(
                line=self.line,
                message='Unterminated string.'
            )
            return     
        
        # closing ".
        self.advance()
        
        # Trim surrounding quotes
        string_value = self.source[self.start + 1: self.current - 1]
        self.add_token(TokenType.STRING, string_value)
        
    def number(self):
        """look for more digits including fractional parts and add the token"""
        while self.is_digit(self.peek()):
            self.advance()
            
        # look for fractional parts
        if '.' in self.peek() and self.is_digit(self.peekNext()):
            # consume the '.'
            self.advance()
            
            while self.is_digit(self.peek()):
                self.advance()
            
        # add the token 
        self.add_token(token=TokenType.NUMBER, literal=float(self.source[self.start:self.current])) 
        
    def identifier(self):
        """checks if if our identifier string is a reserved keyword or not"""
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        
        text = self.source[self.start:self.current]
        token_type = KEYWORDS.get(text, TokenType.IDENTIFIER)

        self.add_token(token=token_type)
        
        
    def is_at_end(self) -> bool:
        """Check if we are at the end the source we are reading from """
        return self.current >= len(self.source)
        
    