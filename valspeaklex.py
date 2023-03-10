# valspeaklex.py - regex transformations for valspeak

import re
import random

#keys
pattern = "pattern"
replaceWith = "replaceWith"

def make_regex(instr):
    return r"\b" + re.escape(instr) + r"\b"

is_lst = [" like, ya know,", 
          " like wow!", 
          " ya know, like,"
        ]

maybe_lst = ["if you're a Pisces",
            "if the moon is full",
            "if the vibes are right",
            "when you get the feeling",
            ]

comma_lst = [", like",
             ", fer shure",
             ", like, wow",
             ", oh, baby",
             ", man",
             ", mostly",
            ]

bang_lst = ["!  Gag me with a SPOOOOON!",
            "!  Gag me with a pitchfork!",
            "!  Oh, wow!",
        ]

def pick(lst, instr):
    return lst[random.randrange(len(lst))]
    

lex_patterns = [
    {pattern:re.compile(r"\b[Bb]ad\b"), replaceWith:'mean'},
    {pattern:re.compile(r"\b[Bb]ig\b"), replaceWith:"bitchin'est"},
    {pattern:re.compile(r"\b[Bb]ody\b"), replaceWith:"bod"},
    {pattern:re.compile(r"\b[Bb]ore\b"), replaceWith:"drag"},
    {pattern:re.compile(r"\b([Cc]ar|[Aa]utomobile)\b"), replaceWith:"rod"},
    {pattern:re.compile(r"\b[Dd]irty\b"), replaceWith:"grodie"},
    {pattern:re.compile(r"\b[Ff]ilthy\b"), replaceWith:"grodie to thuh max"},
    {pattern:re.compile(r"\b[Ff]ood\b"), replaceWith:"munchies"},
    {pattern:re.compile(r"\b[Gg]irl\b"), replaceWith:"chick"},
    {pattern:re.compile(r"\b[Gg]ood\b"), replaceWith:"bitchin'"},
    {pattern:re.compile(r"\b[Gg]reat\b"), replaceWith:"awesum"},
    {pattern:re.compile(r"\b[Gg]ross\b"), replaceWith:"grodie"},
    {pattern:re.compile(r"\b[Gg]uy\b"), replaceWith:"dude"},
    {pattern:re.compile(r"\bher\b"), replaceWith:"that chick"},
    {pattern:re.compile(r"\bhim\b"), replaceWith:"that dude"},
    {pattern:re.compile(r"\bis\b"), replaceWith:lambda x: pick(is_lst, x.group())},
    {pattern:re.compile(r"\b[Hh]ouse\b"), replaceWith:"pad"},
    {pattern:re.compile(r"\b[Ii]nteresting\b"), replaceWith:"cool"},
    {pattern:re.compile(r"\b[Ll]arge\b"), replaceWith:"awesum"},
    {pattern:re.compile(r"\b[Ll]eave\b"), replaceWith:"blow"},
    {pattern:re.compile(r"\b[Mm]an\b"), replaceWith:"nerd"},
    {pattern:re.compile(r"\b[Mm]aybe\b"), replaceWith:lambda x: pick(maybe_lst, x.group())},
    {pattern:re.compile(r"\b[Mm]eeting\b"), replaceWith:"party"},
    {pattern:re.compile(r"\b[Mm]ovie\b"), replaceWith:"flick"},
    {pattern:re.compile(r"\b[Mm]usic\b"), replaceWith:"tunes"},
    {pattern:re.compile(r"\b[Nn]eat\b"), replaceWith:"keen"},
    {pattern:re.compile(r"\b[Nn]ice\b"), replaceWith:"class"},
    {pattern:re.compile(r"\b[Nn]o\b"), replaceWith:"just no way"},
    {pattern:re.compile(r"\b[Pp]eople\b"), replaceWith:"guys"},
    {pattern:re.compile(r"\b[Rr]eally\b"), replaceWith:"totally"},
    {pattern:re.compile(r"\b[Ss]trange\b"), replaceWith:"freaky"},
    {pattern:re.compile(r"\b[Tt]he\b"), replaceWith:"thuh"},
    {pattern:re.compile(r"\b[Vv]ery\b"), replaceWith:"super"},
    {pattern:re.compile(r"\b[Ww]ant\b"), replaceWith:"wanna"},
    {pattern:re.compile(r"\b[Ww]eird\b"), replaceWith:"far out"},
    {pattern:re.compile(r"\b[Yy]es\b"), replaceWith:"fer shure"},
    {pattern:re.compile(r"\bBut\b"), replaceWith:"Man,"},
    {pattern:re.compile(r"\b[Hh]e\b"), replaceWith:"that dude"},
    {pattern:re.compile(r"\bI{WB}like\b"), replaceWith:"I can dig"},
    {pattern:re.compile(r"\bNo,\b"), replaceWith:"Like, no way,"},
    {pattern:re.compile(r"\b[Ss]ir\b"), replaceWith:"Man"},
    {pattern:re.compile(r"\b[Ss]he\b"), replaceWith:"That fox"},
    {pattern:re.compile(r"\b[Tt]his\b"), replaceWith:"Like, ya know, this"},
    {pattern:re.compile(r"\b[Tt]here\b"), replaceWith:"Like, there"},
    {pattern:re.compile(r"\b[Ww]e\b"), replaceWith:"Us guys"},
    {pattern:re.compile(r"\bYes,\b"), replaceWith:"Like,"},
    {pattern:re.compile(r","), replaceWith:lambda x: pick(comma_lst, x.group())},
    {pattern:re.compile(r"!"), replaceWith:lambda x: pick(bang_lst, x.group())},
]


# checkReplace - check the input string,
#  for each pattern, 
#    check the text for each pattern
#    replace the pattern with the replaceWith
#    
def checkReplace(instr):
    outstr = instr
    for pat in lex_patterns:
        outstr = pat[pattern].sub(pat[replaceWith], outstr)
        #print(outstr)
    return outstr


