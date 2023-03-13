# valspeaklex.py - regex transformations for valspeak
import re

import lex


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

lex_values = [
    (r"\b[Bb]ad\b", 'mean'),
    (r"\b[Bb]ig\b", "bitchin\'est"),
    (r"\b[Bb]ody\b", "bod"),
    (r"\b[Bb]ore\b", "drag"),
    (r"\b([Cc]ar|[Aa]utomobile)\b", "rod"),
    (r"\b[Dd]irty\b", "grodie"),
    (r"\b[Ff]ilthy\b", "grodie to thuh max"),
    (r"\b[Ff]ood\b", "munchies"),
    (r"\b[Gg]irl\b", "chick"),
    (r"\b[Gg]ood\b", "bitchin\'"),
    (r"\b[Gg]reat\b", "awesum"),
    (r"\b[Gg]ross\b", "grodie"),
    (r"\b[Gg]uy\b", "dude"),
    (r"\bher\b", "that chick"),
    (r"\bhim\b", "that dude"),
    (r"\bis\b", lambda x: lex.pick(is_lst, x.group())),
    (r"\b[Hh]ouse\b", "pad"),
    (r"\b[Ii]nteresting\b", "cool"),
    (r"\b[Ll]arge\b", "awesum"),
    (r"\b[Ll]eave\b", "blow"),
    (r"\b[Mm]an\b", "nerd"),
    (r"\b[Mm]aybe\b", lambda x: lex.pick(maybe_lst, x.group())),
    (r"\b[Mm]eeting\b", "party"),
    (r"\b[Mm]ovie\b", "flick"),
    (r"\b[Mm]usic\b", "tunes"),
    (r"\b[Nn]eat\b", "keen"),
    (r"\b[Nn]ice\b", "class"),
    (r"\b[Nn]o\b", "just no way"),
    (r"\b[Pp]eople\b", "guys"),
    (r"\b[Rr]eally\b", "totally"),
    (r"\b[Ss]trange\b", "freaky"),
    (r"\b[Tt]he\b", "thuh"),
    (r"\b[Vv]ery\b", "super"),
    (r"\b[Ww]ant\b", "wanna"),
    (r"\b[Ww]eird\b", "far out"),
    (r"\b[Yy]es\b", "fer shure"),
    (r"\bBut\b", "Man,"),
    (r"\b[Hh]e\b", "that dude"),
    (r"\bI{WB}like\b", "I can dig"),
    (r"\bNo,\b", "Like, no way,"),
    (r"\b[Ss]ir\b", "Man"),
    (r"\b[Ss]he\b", "That fox"),
    (r"\b[Tt]his\b", "Like, ya know, this"),
    (r"\b[Tt]here\b", "Like, there"),
    (r"\b[Ww]e\b", "Us guys"),
    (r"\bYes,\b", "Like,"),
    (r",", lambda x: lex.pick(comma_lst, x.group())),
    (r"!", lambda x: lex.pick(bang_lst, x.group())),
]

lex_patterns = []

for item in lex_values:
    lex.add(lex_patterns, item[0], item[1])

