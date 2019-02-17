"""
@file
@brief Helpers with grammar for mokadi.
"""
from .mokadi_parser import get_tree_string, parse_mokadi, run_parse
from .mokadi_exceptions import MokadiException
from .grammars import MokadiGrammar_frParser, MokadiGrammar_frLexer, MokadiGrammar_frListener


def interpret(sentance, MokadiGrammarParser=None, MokadiGrammarLexer=None,
              MokadiGrammarListener=None):
    """
    Interprets a sentance and returns a list of words.

    @param      MokadiGrammarParser     parser for a specific language
    @param      MokadiGrammarLexer      lexer for a specific language
    @param      MokadiGrammarListener   listener for a specific language
    @param      sentance                any string
    @return                             list of tuple (word, kind)
    """
    if MokadiGrammarParser is None:
        MokadiGrammarParser = MokadiGrammar_frParser
    if MokadiGrammarLexer is None:
        MokadiGrammarLexer = MokadiGrammar_frLexer
    if MokadiGrammarListener is None:
        MokadiGrammarListener = MokadiGrammar_frListener
    parser = parse_mokadi(sentance, MokadiGrammarParser, MokadiGrammarLexer)
    stdout, stderr, tree = run_parse(parser)
    if stderr and len(stderr) > 0:
        raise MokadiException(
            "Unable to parse '{0}'\nOUT\n{1}\nERR\n{2}".format(sentance, stdout, stderr))
    _, simple = get_tree_string(
        MokadiGrammarListener, tree, parser, sentance)
    return simple
