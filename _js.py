from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Choice, Function)
from lib.format import (
	camel_case_text
)

contextJs = AppContext(title=".js")
context = contextJs

grammar = Grammar("js", context=context)

rules = MappingRule(
	name="js",
	mapping={
		"fun": Text("f") + Key('tab'),
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
