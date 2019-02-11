import unittest

from interpreter.lexer import Lexer
from interpreter.token import tokens


class TestLexer(unittest.TestCase):

    def setUp(self):
        filename = 'tests/add.sl'
        self.lexer = Lexer(filename)

    def test_assign_statement(self):
        # line2: n = toint(input())
        check_tokens = [tokens.Name, tokens.Assign, tokens.ToInt, tokens.LeftParen, tokens.Input, tokens.LeftParen, tokens.RightParen, tokens.RightParen, tokens.EofLine]

        self.assertEqual(len(self.lexer[2]), len(check_tokens))
        for lexer_token, check_token in zip(self.lexer[2], check_tokens):
            self.assertEqual(lexer_token.kind, check_token)

    def test_for_statement(self):
        # line5: for i = 1 to n {
        check_tokens = [tokens.For, tokens.Name, tokens.Assign, tokens.Integer, tokens.To, tokens.Name, tokens.LeftBrace, tokens.EofLine]

        self.assertEqual(len(self.lexer[5]), len(check_tokens))
        for lexer_token, check_token in zip(self.lexer[5], check_tokens):
            self.assertEqual(lexer_token.kind, check_token)


if __name__ == '__main__':
    unittest.main()
