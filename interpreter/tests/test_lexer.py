import unittest

from interpreter.lexer import Lexer
from interpreter.token import tokens


class TestLexer(unittest.TestCase):

    def setUp(self):
        filename = './add.sl'
        self.lexer = Lexer(filename)

    def test_assign_statement(self):
        # line2: n = toint(input())
        check_tokens = [tokens.Indent, tokens.Assign, tokens.ToInt, tokens.Input, tokens.EofLine]

        self.assertEqual(len(self.lexer[2]), len(check_tokens))
        for lexer_token, check_token in zip(self.lexer[2], check_tokens):
            self.assertEqual(lexer_token, check_token)

    def test_for_statement(self):
        # line5: for i = 1 to n {
        check_tokens = [tokens.For, tokens.Indent, tokens.Assign, tokens.Integer, tokens.To, tokens.Indent, tokens.LeftBrace, tokens.EofLine]
        self.assertEqual(len(self.lexer[5]), len(check_tokens))
        for lexer_token, check_token in zip(self.lexer[5], check_tokens):
            self.assertEqual(lexer_token, check_token)
