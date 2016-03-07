from dragonfly import (Function, Grammar, AppContext, MappingRule, Dictation, IntegerRef, Pause, Mimic,
                       Key, Text)
from lib.format import (
	camel_case_text
)

ideaContext1 = AppContext(executable='pycharm', title='Charm')
ideaContext2 = AppContext(executable='webstorm', title='Storm')
ideaContext = ideaContext1 | ideaContext2

grammar = Grammar('idea', context=ideaContext)

example_rule = MappingRule(
	name='idea',
	mapping={
		# Start new line
		'softy': Key('s-enter'),
		# Extend selection
		'tweet': Key('c-w'),
		'tweet <n>': Key('control:down/3') + Key('w:%(n)d') + Key('control:up'),
		# Show gulp tasks
		'gundam': Key('a-f11'),
		# Restart running gulp task
		'gundam restart': Key('c-f5'),
		# Duplicate line or block
		'dub': Key('c-d'),
		'dub <n>': Key('control:down/3') + Key('d:%(n)d') + Key('control:up'),
		# Select next occurrence
		'next word': Key('a-j'),
		'next word <n>': Key('alt:down/3') + Key('j:%(n)d') + Key('alt:up'),
		# Creating files and directories
		'arch': Key('a-n'),
		'arch file': Key('a-n') + Pause('5') + Key('enter'),
		'arch dir': Key('a-n') + Pause('5') + Key('down, enter'),
		# Go to project bar
		'project bar': Key('a-1'),
		# Rename file/directory/variable
		'rename': Key('s-f6'),
		# Open terminal
		'termi': Key('a-f12'),
		# VCS operations popup (custom shortcut)
		'version control': Key('a-f10'),
		# VCS pull (custom shortcut)
		'version pull': Key('control:down/3, alt:down/3, rbracket, control:up, alt:up'),
		# Go to line
		'[go] to line': Key('c-g'),
		'[go] to line <n>': Key('c-g') + Pause('5') + Text('%(n)d') + Key('enter, end'),
		# Move line down/up
		'hamster down': Key('alt:down/3') + Key('s-down') + Key('alt:up'),
		'hamster up': Key('alt:down/3') + Key('s-up') + Key('alt:up'),
		# Move statement down/up
		'tiger up': Key('control:down/3') + Key('s-up') + Key('control:up'),
		'tiger down': Key('control:down/3') + Key('s-down') + Key('control:up'),
		# Jumping back/forth in code
		'prev file': Key('control:down/3') + Key('tab') + Key('control:up'),
		'prev place': Key('alt:down/3') + Key('s-backspace') + Key('alt:up'),
		'next place': Key('alt:down/3') + Key('s-end') + Key('alt:up'),
		# Find
		'find in file': Key('c-f'),
		# Close tab
		'close file': Key('c-f4'),
		# Search everywhere
		'seeker': Key('shift, shift'),
		# Reformat code
		'reformat': Key('control:down/3') + Key('a-l') + Key('control:up'),
		# Go to beginning/end of parent block
		'lap': Key('c-lbracket'),
		'rap': Key('c-rbracket'),
		# Complete current code
		'fin': Key('control:down/3, shift:down/3, enter, shift:up, control:up'),
		# Jump to navigation bar
		'breadcrumb': Key('a-home'),
		# Autocomplete
		'suggest': Key('c-space'),
		# Go to specific tab (using GoToTabs plugin)
		'[go] to tab <n>': Key('control:down/3, alt:down/3') + Key('%(n)d') + Key('control:up, alt:up'),
		# Ace Jump plugin (somewhat buggy)
		'roshan': Key('c-semicolon/20, space'),
		# Surround with live template
		'surround': Key('control:down/3, alt:down/3, j, alt:up, control:up'),
	},
	extras=[
		IntegerRef('n', 1, 10000),
		Dictation('text')
	])

grammar.add_rule(example_rule)
grammar.load()


def unload():
	global grammar
	if grammar: grammar.unload()
	grammar = None
