'''
토큰: 의미를 가지는 최소 단위
단어: 토큰 규칙과 일치하는 문자열 그 자체

토큰      단어
If       if
While    while
VarName  foo, bar
IntNum   100, 200
'''

class _Tokens:
    def __init__(self):
        self._tokens = {}           # 토큰: 인덱스
        self._token_words = {}      # 단어: 토큰 인덱스

    def __getattr__(self, key):
        ''' self.Token, self['Token'] 형식을 가능하게 한다. '''
        return self._tokens[key]

    def get_kind(self, word):
        ''' 단어와 매칭되는 토큰 종류를 반환한다.
        :param word: 단어
        :return: 단어의 토큰
        '''
        for token_word, token in self._token_words.items():
            if (word == token_word):
                return token

        if word.isdigit(): return self.Integer
        if word.replace('.', '', 1).isdigit(): return self.Float
        if word.isprintable(): return self.Indent
        return self.Others

    def add_tkn(self, name, *words):
        index = len(self._tokens)
        self._tokens[name] = index
        for word in words:
            self._token_words[word] = index


tokens = _Tokens()

tokens.add_tkn('Integer')                  # 데이터 타입 토큰화
tokens.add_tkn('Float')
tokens.add_tkn('String')

tokens.add_tkn('Letter')                   # 단어
tokens.add_tkn('Var', 'var')               # 변수 토큰화
tokens.add_tkn('Global', 'global')
tokens.add_tkn('GlobalVar')
tokens.add_tkn('LocalVar')
tokens.add_tkn('Assign', '=')
tokens.add_tkn('Comma', ',')
tokens.add_tkn('LeftBracket', '[')
tokens.add_tkn('RightBracket', ']')
tokens.add_tkn('DoubleQuarter', '"')

tokens.add_tkn('Func', 'func')             # 함수 토큰화
tokens.add_tkn('LeftBrace', '{')
tokens.add_tkn('RightBrace', '}')
tokens.add_tkn('FCall')
tokens.add_tkn('Return', 'return')

tokens.add_tkn('Print', 'print')           # 내장 함수 토큰화
tokens.add_tkn('Println', 'println')
tokens.add_tkn('ToInt', 'toint')
tokens.add_tkn('ToString', 'tostring')
tokens.add_tkn('Input', 'input')

tokens.add_tkn('If', 'if')                 # 제어문 토큰화
tokens.add_tkn('Elif', 'elif')
tokens.add_tkn('Else', 'else')
tokens.add_tkn('For', 'for')
tokens.add_tkn('To', 'to')
tokens.add_tkn('Step', 'step')
tokens.add_tkn('While', 'while')
tokens.add_tkn('End', 'end')
tokens.add_tkn('Break', 'break')
tokens.add_tkn('Continue', 'continue')
tokens.add_tkn('Exit', 'exit')

tokens.add_tkn('Lparen', '(')              # 식 (expression) 토큰화
tokens.add_tkn('Rparen', ')')
tokens.add_tkn('Plus', '+')
tokens.add_tkn('Minus', '-')
tokens.add_tkn('Multi', '*')
tokens.add_tkn('Divi', '/')
tokens.add_tkn('Mod', '%')
tokens.add_tkn('Less', '<')
tokens.add_tkn('LessEqual', '<=')
tokens.add_tkn('Great', '>')
tokens.add_tkn('GreatEqual', '>=')
tokens.add_tkn('And', '&&')
tokens.add_tkn('Or', '||')
tokens.add_tkn('Not', '!')
tokens.add_tkn('NotEqual', '!=')

tokens.add_tkn('Others')                  # 내부 토큰
tokens.add_tkn('EofProgramme')
tokens.add_tkn('EofLine')
tokens.add_tkn('ErrorToken')

del _Tokens.add_tkn # 메소드는 디스크립터기 때문에 클래스 속성 삭제
