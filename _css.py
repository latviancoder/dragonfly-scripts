from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Choice, Function)
from lib.format import (
    dashify_text
)

emmet = {
    "margin": "m",
    "margin bottom": "mb",
    "margin top": "mt",
    "margin left": "ml",
    "margin right": "mr",
    "position": "pos",
    "screech top": "t",
    "screech bottom": "b",
    "screech left": "l",
    "screech right": "r",
    "index": "z",
    "float": "fl",
    "clear": "cl",
    "display": "d",
    "overflow": "ov",
    "overflow x": "ovx",
    "overflow y": "ovy",
    "visibility": "v",
    "cursor": "cur",
    "padding": "p",
    "padding bottom": "pb",
    "padding top": "pt",
    "padding left": "pl",
    "padding right": "pr",
    "box sizing": "bxz",
    "box shadow": "bxsh",
    "width": "w",
    "height": "h",
    "max width": "maw",
    "max height": "mah",
    "min width": "miw",
    "min height": "mih",
    "font weight": "fw",
    "font style": "fs",
    "font size": "fz",
    "font family": "ff",
    "vertical align": "va",
    "text align": "ta",
    "text decoration": "td",
    "text transform": "tt",
    "text shadow": "tsh",
    "line height": "lh",
    "letter spacing": "lts",
    "white space": "whs",
    "word break": "wob",
    "word wrap": "wow",
    "background": "bg",
    "background color": "bgc",
    "background image": "bgi",
    "background repeat": "bgr",
    "background position": "bgp",
    "background size": "bgsz",
    "color": "c",
    "opacity": "op",
    "content": "cnt",
    "outline": "ol",
    "table layout": "tl",
    "border": "bd+",
    "border top": "bdt+",
    "border bottom": "bdb+",
    "border left ": "bdl+",
    "border right": "bdr+",
    "border collapse": "bdcl",
    "border radius": "bdrs",
    "list style": "lis",
    "important": "!",
    "font face": "@f+"
}

contextCss = AppContext(title=".css")
contextLess = AppContext(title=".less")
context = contextCss | contextLess

grammar = Grammar("css", context=context)

rules = MappingRule(
    name="css",
    mapping={
        "auto": Text("auto"),

        "<prop>": Text("%(prop)s") + Key("tab"),
        "<prop> <n>": Text("%(prop)s") + Text("%(n)d") + Key("tab"),
        "<n> pixel": Text("%(n)dpx"),
        "<n> percent": Text("%(n)d%"),
        "(class|squeeze) <text>": Text(".") + Function(dashify_text) + Text(" {") + Key("enter"),
    },
    extras=[
        Dictation("text"),
        Choice("prop", emmet),
        Integer("n", 0, 20000),
    ],
    defaults={
        "n": 1
    }
)

grammar.add_rule(rules)

grammar.load()


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
