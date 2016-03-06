from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Choice, Function, Pause)
from lib.format import (
	dashify_text
)

elements = {
	"(A|anchor)": "a",
	"article": "article",
	"aside": "aside",
	"audio": "audio",
	"(B|bold|boldface)": "b",
	"body": "body",
	"(B R|[line] break)": "br",
	"button": "button",
	"canvas": "canvas",
	"caption": "caption",
	"(datalist|data list)": "datalist",
	"(div|D I V|[document] division)": "div",
	"(em|E M|emphasis)": "em",
	"embed": "embed",
	"fieldset": "fieldset",
	"figure": "figure",
	"footer": "footer",
	"form": "form",
	"(H 1|heading 1)": "h1",
	"(H 2|heading 2)": "h2",
	"(H 3|heading 3)": "h3",
	"(H 4|heading 4)": "h4",
	"(H 5|heading 5)": "h5",
	"(H 6|heading 6)": "h6",
	"head": "head",
	"header": "header",
	"(H R|horizontal rule)": "hr",
	"html": "html",
	"(I|italic)": "i",
	"(I|inline) frame": "iframe",
	"(I M G|image)": "img",
	"input": "input",
	"label": "label",
	"legend": "legend",
	"(li|L I|list [item])": "li",
	"link": "link",
	"(meta|meta data)": "meta",
	"(nav|N A V|navigation)": "nav",
	"(noscript|no script)": "noscript",
	"object": "object",
	"(O L|ordered list)": "ol",
	"option": "option",
	"(P|paragraph)": "p",
	"(param|parameter)": "param",
	"(pre|P R E|pre-formatted [text])": "pre",
	"(S|strike through|strikethrough)": "s",
	"script": "script",
	"section": "section",
	"select": "select",
	"small": "small",
	"span": "span",
	"strong": "strong",
	"(sup|S U P|super [script])": "sup",
	"table": "table",
	"(T|table) body": "tbody",
	"(T D|table cell|table data)": "td",
	"template": "template",
	"(textarea|text area)": "textarea",
	"(T|table) foot": "tfoot",
	"(T H|table header) ": "th",
	"(T|table) head": "thead",
	"title": "title",
	"(T R|table row)": "tr",
	"(U|uderline)": "u",
	"(U L|an ordered list)": "ul",
	"video": "video",
}

emmet = {
	"margin": "m",
	"margin bottom": "mb",
	"margin top": "mt",
	"margin left": "ml",
	"margin right": "mr",
	"position": "pos",
	"top": "t",
	"bottom": "b",
	"lend": "l",
	"rice": "r",
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
	"font face": "@f+",
	"align items": 'ai',
	"justify content": 'jc',
}

contextCss = AppContext(title=".css")
contextLess = AppContext(title=".less")
context = contextCss | contextLess

grammar = Grammar("css", context=context)

rules = MappingRule(
	name="css",
	mapping={
		# 'height'
		"<prop>": Text("%(prop)s") + Key("tab"),
		# 'height auto'
		"<prop> <text>": Text("%(prop)s") + Key("tab") + Text('%(text)s') + Pause('70') + Key('s-enter'),
		# 'height 100'
		"<prop> <n>": Text("%(prop)s") + Text("%(n)d") + Key("tab") + Pause('70') + Key('s-enter'),
		# 'height 100 percent'
		"<prop> <n> percent": Text("%(prop)s") + Key("tab") + Text("%(n)d%%") + Pause('70') + Key('s-enter'),
		# '100 pixel'
		"<n> pixel": Text("%(n)dpx"),
		# '100 percent'
		"<n> percent": Text("%(n)d%%"),

		"squeeze <text>": Text(".") + Function(dashify_text) + Text(" {") + Key("enter"),
		"dom <element>": Text("%(element)s"),
	},
	extras=[
		Dictation("text"),
		Choice("prop", emmet),
		Choice("element", elements),
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
