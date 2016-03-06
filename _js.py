from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Choice, Function)
from lib.format import (
	camel_case_text,
	dashify_text
)

contextJs = AppContext(title=".js")
context = contextJs

grammar = Grammar("js", context=context)

rules = MappingRule(
	name="js",
	mapping={
		"fun": Text("f") + Key('tab'),
		'dom div': Text('<div></') + Key('left/1:6'),
		"selector <text>": Text('$(\'.') + Function(dashify_text),
		"protected <text>": Text("_") + Function(camel_case_text),
	},
	extras=[
		Dictation("text"),
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
