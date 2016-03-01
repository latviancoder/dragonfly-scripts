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
        "joke": Text('$('),

        "dub": Key("a-d"),
        "dub <n>": Key("alt:down/3") + Key("d:%(n)d") + Key("alt:up"),
        "next word": Key("a-g"),
        "next word <n>": Key("alt:down/3") + Key("g:%(n)d") + Key("alt:up"),

        "save all": Key("a-s"),
        "arch": Key("a-n"),
        "project bar": Key("a-1"),
        "rename": Key("s-f6"),
        "termi": Key("a-f12"),
        "version control": Key("a-f10"),
        "version pull": Key("a-f10"),

        "[go] to line": Key("c-g"),
        "[go] to line <n>": Key("c-g") + Pause("20") + Text("%(n)d") + Key("enter, end"),

        "hamster down": Key("alt:down/3") + Key("s-down") + Key("alt:up"),
        "hamster up": Key("alt:down/3") + Key("s-up") + Key("alt:up"),

        "prev file": Key("control:down/3") + Key("tab") + Key("control:up"),
        "prev place": Key("alt:down/3") + Key("s-backspace") + Key("alt:up"),
        "next place": Key("alt:down/3") + Key("s-end") + Key("alt:up"),

        "seeker": Key("shift, shift"),
        "find in file": Key("a-f"),
        "close file": Key("a-w"),
        "reformat": Key("control:down/3") + Key("a-l") + Key("control:up"),

        # Go to beginning/end of parent block
        "lap": Key("c-lbracket"),
        "rap": Key("c-rbracket"),

        # Complete current code
        "fin": Key("control:down/3, shift:down/3, enter, shift:up, control:up"),

        # Jump to navigation bar
        "breadcrumb": Key("a-home"),

        "suggest": Key("c-space"),
        "[go] to tab <n>": Key("control:down/3, alt:down/3") + Key("%(n)d") + Key("control:up, alt:up"),
    },
    extras=[
        IntegerRef("n", 1, 10000),
        Dictation("text")
    ])

grammar.add_rule(example_rule)
grammar.load()


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
