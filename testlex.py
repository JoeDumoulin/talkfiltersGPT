# tests.py - test the lexer and other things
import valspeaklex as lex

def make_regex_does_the_thing():
    expected=r"\bfoo\b"
    inputstr = 'foo'
    assert(lex.make_regex(inputstr)==expected)

def lexer_understands_words():
    instr = 'Big badaboom'
    expected = "bitchin'est badaboom"
    assert(lex.checkReplace(instr)==expected)

def lexer_sees_words_at_the_end():
    instr = "don't be bad"
    expected = "don't be mean"
    #print(lex.checkReplace(instr))
    assert(lex.checkReplace(instr)==expected)
    
def lexer_sees_words_at_the_beginning():
    instr = "Bad luck"
    expected = "mean luck"
    assert(lex.checkReplace(instr)==expected)

def lexer_processes_multiple_words():
    instr = "Big bad Girl needs some Food and a car."
    expected = "bitchin'est mean chick needs some munchies and a rod."
    #print(lex.checkReplace(instr))
    assert(lex.checkReplace(instr)==expected)

def lexer_gets_sub_lambda():
    instr = "Cake is good food."
    actual = lex.checkReplace(instr)
    assert(actual.startswith("Cake"))

def run():
    make_regex_does_the_thing()
    lexer_understands_words()
    lexer_sees_words_at_the_end()
    lexer_sees_words_at_the_beginning()
    lexer_processes_multiple_words()
    lexer_gets_sub_lambda()

if __name__ == '__main__':
    run()


