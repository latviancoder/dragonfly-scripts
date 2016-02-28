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

}

context = AppContext(title=".css")
grammar = Grammar("css", context=context)

rules = MappingRule(
    name="css",
    mapping={
        "auto": Text("auto"),

        "<prop>": Text("%(prop)s") + Key("tab"),
        "<prop> <n>": Text("%(prop)s") + Text("%(n)d") + Key("tab"),
        "<n> pixel": Text("%(n)dpx"),
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
