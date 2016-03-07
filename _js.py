from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Choice, Function)
from lib.format import (
	camel_case_text,
	dashify_text
)

contextJs = AppContext(title='.js')
context = contextJs

grammar = Grammar('js', context=context)

rules = MappingRule(
	name='js',
	mapping={
		# jQuery selectors
		'joke': Text('$('),
		'selector <text>': Text('$(\'.') + Function(dashify_text),
		# Arrow function
		'fun': Text('f') + Key('tab'),
		# Creating div elements inside of strings
		'dom div': Text('<div></') + Key('left/1:6'),
		# _myProtectedMethod
		'protected <text>': Text('_') + Function(camel_case_text),
		# __myPrivateMethod
		'private <text>': Text('__') + Function(camel_case_text),
	},
	extras=[
		Dictation('text'),
		Integer('n', 0, 20000),
	],
	defaults={
		'n': 1
	}
)

grammar.add_rule(rules)

grammar.load()


def unload():
	global grammar
	if grammar: grammar.unload()
	grammar = None
