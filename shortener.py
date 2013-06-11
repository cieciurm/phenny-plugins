import requests

SHORTENER_ENGINE_URL = "http://ujeb.se/a/add?u="

def shortener(phenny, input):
	"""Shortens given URL using ujeb.se"""
	url = input.group(2)

	if not url:
		return phenny.say("%s, gimme something to shorten!" % input.nick)

	r = requests.get(SHORTENER_ENGINE_URL + url)
	shortened = r.text

	phenny.say("%s told me to shorten a link, result: %s" % (input.nick, shortened))

shortener.commands = ["sh", "shorten"]
shortener.example = ".sh http://wanna.shorten.it"
shortener.priority = "medium"
