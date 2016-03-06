from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Choice, Function)
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

contextHtml = AppContext(title=".html")
contextJs = AppContext(title=".js")
grammar = Grammar("html", context=contextHtml | contextJs)

rules = MappingRule(
	name="html",
	mapping={
		"<element>": Text("%(element)s"),
		"dom <element>": Text("%(element)s") + Key("tab"),
		"(squeeze) <text>": Text(".") + Function(dashify_text) + Key("tab"),
		"mumbles": Key('a-p'),
		"mumbles <n>": Text('lorem%(n)d') + Key('tab'),
	},
	extras=[
		Dictation("text"),
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
