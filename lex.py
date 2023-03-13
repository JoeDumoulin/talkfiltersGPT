# lex.py - common lexer for talkfilters

import re
import random

#keys
pattern = "pattern"
replaceWith = "replaceWith"

def make_regex(instr):
    return r"\b" + re.escape(instr) + r"\b"

def pick(lst, instr):
    return lst[random.randrange(len(lst))]
    
# add a pattern to the lexer
def add(lexer, patternVal, replaceWithVal):
    print("{} => {}".format(patternVal, replaceWithVal))
    lexer.append({pattern:re.compile(patternVal), 
        replaceWith:replaceWithVal})

# checkReplace - check the input string,
#  for each pattern, 
#    check the text for each pattern
#    replace the pattern with the replaceWith
#    
def checkReplace(lex_patterns, instr):
    outstr = instr
    for pat in lex_patterns:
        outstr = pat[pattern].sub(pat[replaceWith], outstr)
    return outstr



