MATEUSZ = "mateusz_"
ZAPU = "zapu"

def daddy(phenny, input):
	phenny.say("%s asks: who's his daddy?" % input.nick) 

	if input.nick == MATEUSZ:
		phenny.say("It's %s obviously!" % ZAPU) 
	else:
		phenny.say("It's %s obviously!" % MATEUSZ) 

daddy.commands = ["daddy"]
daddy.priority = "low"
