import re

from .utils import fileopen
from .token import tokens, OPERATOR_LETTER, SPECIAL_LETTER

STRING_PATTERN = '[a-zA-Z_]\w*'    # 변수명, 함수명, 문자열 키워드 (Etc. 'func', 'global')
INTEGER_PATTERN = '[0-9]+'
FLOAT_PATTERN = INTEGER_PATTERN + '\.' + INTEGER_PATTERN
OPERATOR_PATTERN = '|'.join(re.escape(operator) for operator in OPERATOR_LETTER)
SPECIAL_PATTERN = '|'.join(re.escape(letter) for letter in SPECIAL_LETTER)
TOKEN_PATTERN = '|'.join((STRING_PATTERN,
                          INTEGER_PATTERN, FLOAT_PATTERN,
                          OPERATOR_PATTERN, SPECIAL_PATTERN))


class Token:
    __slots__ = ('kind', 'text')

    def __init__(self, kind, text=None):
        self.kind = kind
        self.text = text

    def __repr__(self):
        return "Token(%s, %s)" % (self.kind, self.text)


class Lexer:

    def __init__(self, filename):
        self.liens = fileopen(filename)
        self.scan_lines()

    def scan_lines(self):
        ''' 각 line 토큰화re '''
        self._line_tokens = []                       # 각 행의 토큰 목록 초기화
        self._line_tokens.append([tokens.EofLine])   # line 0 패스

        for line in self.liens:
            self._line_tokens.append(list(self.generate_token(line)))

    def generate_token(self, statement):
        ''' 문장 내용 토큰화 '''
        token_words = ''   # 토큰화된 단어들

        for match in re.finditer(TOKEN_PATTERN, statement):
            word = match.group(0)
            token_words += word
            kind = tokens.get_kind(word)
            yield Token(kind, word)

        if len(token_words) != len(statement.replace(' ', '')):
            raise Exception('인터프리터가 식별할 수 없는 문자를 사용했습니다.')
        yield Token(tokens.EofLine)     # 문장 종료

    def __len__(self):
        return len(self._line_tokens)

    def __getitem__(self, index):
        return self._line_tokens[index]
