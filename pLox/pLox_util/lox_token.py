from dataclasses import dataclass

# local imports
from token_type import TokenType

@dataclass(frozen=True)
class Token:
    type: TokenType
    lexeme: str
    literal: object
    line: int
    
    def __str__(self) -> str:
        return f"{self.type} {self.lexeme} {self.literal}"
