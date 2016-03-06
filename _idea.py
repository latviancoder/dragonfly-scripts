from dragonfly import (Function, Grammar, AppContext, MappingRule, Dictation, IntegerRef, Pause, Mimic,
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
		'gundam': Key('a-f11'),
		'gundam restart': Key('c-f5'),
		'gundam tool': Key('a-4'),

		"dub": Key("a-d"),
		"dub <n>": Key("alt:down/3") + Key("d:%(n)d") + Key("alt:up"),
		"next word": Key("a-g"),
		"next word <n>": Key("alt:down/3") + Key("g:%(n)d") + Key("alt:up"),

		"arch": Key("a-n"),
		"arch file": Key("a-n") + Pause('5') + Key('enter'),
		"arch dir": Key("a-n") + Pause('5') + Key('down, enter'),

		"project bar": Key("a-1"),
		"rename": Key("s-f6"),
		"termi": Key("a-t"),
		"version control": Key("a-f10"),
		"version pull": Key("control:down/3, alt:down/3, rbracket, control:up, alt:up"),

		"[go] to line": Key("c-g"),
		"[go] to line <n>": Key("c-g") + Pause("20") + Text("%(n)d") + Key("enter, end"),
		# move line down/up
		"hamster down": Key("alt:down/3") + Key("s-down") + Key("alt:up"),
		"hamster up": Key("alt:down/3") + Key("s-up") + Key("alt:up"),
		# move statement down/up
		"tiger up": Key("control:down/3") + Key("s-up") + Key("control:up"),
		"tiger down": Key("control:down/3") + Key("s-down") + Key("control:up"),

		"prev file": Key("control:down/3") + Key("tab") + Key("control:up"),
		"prev place": Key("alt:down/3") + Key("s-backspace") + Key("alt:up"),
		"next place": Key("alt:down/3") + Key("s-end") + Key("alt:up"),

		"find in file": Key("a-f"),
		"close file": Key("a-w"),

		# Search everywhere
		"seeker": Key("shift, shift"),
		# Reformat code
		"reformat": Key("control:down/3") + Key("a-l") + Key("control:up"),
		# Go to beginning/end of parent block
		"lap": Key("c-lbracket"),
		"rap": Key("c-rbracket"),
		# Complete current code
		"fin": Key("control:down/3, shift:down/3, enter, shift:up, control:up"),
		# Jump to navigation bar
		"breadcrumb": Key("a-home"),
		# Autocomplete
		"suggest": Key("c-space"),
		# Go to specific tab (using GoToTabs) plugin
		"[go] to tab <n>": Key("control:down/3, alt:down/3") + Key("%(n)d") + Key("control:up, alt:up"),
		# Ace Jump plugin
		"roshan": Key("c-semicolon/20, space"),
		# Surround with live template
		"surround": Key("control:down/3, alt:down/3, j, alt:up, control:up"),
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
