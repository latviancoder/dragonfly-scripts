from dragonfly import (Function, Grammar, AppContext, MappingRule, Dictation, IntegerRef, Pause,
                       Key, Text)
from lib.format import (
    camel_case_text
)

ideaContext1 = AppContext(executable="pycharm", title="Charm")
ideaContext2 = AppContext(executable="webstorm", title="Storm")
ideaContext = ideaContext1 | ideaContext2

grammar = Grammar("idea", context=ideaContext)

example_rule = MappingRule(
    name="example",  # The name of the rule.
    mapping={
        "git": Text("git"),
        "npm": Text("npm"),
        "joke": Text('$('),
        "soft enter": Key('s-enter'),
        "dotmel <text>": Text('.') + Function(camel_case_text),
        "tweet": Key('a-up'),
        "tweet <n>": Key("alt:down/3") + Key("up:%(n)d") + Key("alt:up"),
        "dub": Key("a-d"),
        "dub <n>": Key("alt:down/3") + Key("d:%(n)d") + Key("alt:up"),
        "next word": Key("a-g"),

        "save all": Key("a-s"),
        "arch": Key("a-n"),
        "project bar": Key("a-1"),
        "rename": Key("s-f6"),
        "termi": Key("a-f12"),
        "version control": Key("a-f10"),
        "accept choice": Key("c-enter"),

        "[go] to line": Key("c-g"),
        "[go] to line <n>": Key("c-g") + Pause("20") + Text("%(n)d") + Key("enter, end"),

        "hamster down": Key("alt:down/3") + Key("s-down") + Key("alt:up"),
        "hamster up": Key("alt:down/3") + Key("s-up") + Key("alt:up"),

        "prev file": Key("control:down/3") + Key("tab") + Key("control:up"),
        "prev place": Key("alt:down/3") + Key("s-backspace") + Key("alt:up"),
        "next place": Key("alt:down/3") + Key("s-end") + Key("alt:up"),

        "search file": Key("shift, shift"),
        "find in file": Key("a-f"),
        "close file": Key("a-w"),
        "reformat": Key("control:down/3") + Key("a-l") + Key("control:up"),

        "lamp": Key("a-left"),
        "lamp <n>": Key("alt:down/3") + Key("left:%(n)d") + Key("alt:up"),

        "ramp": Key("a-right"),
        "ramp <n>": Key("alt:down/3") + Key("right:%(n)d") + Key("alt:up"),

        "lace": Key("alt:down/3") + Key("s-left") + Key("alt:up"),
        "lace <n>": Key("alt:down/3") + Key("s-left:%(n)d") + Key("alt:up"),

        "race": Key("alt:down/3") + Key("s-right") + Key("alt:up"),
        "race <n>": Key("alt:down/3") + Key("s-right:%(n)d") + Key("alt:up"),
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text")
    ])

grammar.add_rule(example_rule)
grammar.load()


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
