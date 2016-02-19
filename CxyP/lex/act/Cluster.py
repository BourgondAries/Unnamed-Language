def __init__(self, actions, entrytypes, tokentypes):
	self._tokenstack = []
	self._current = []
	self._actions = actions
	self._entrytype = entrytypes
	self._toktype = tokentypes

def pop(self):
	return self._tokenstack.pop(0)

def consume(self, character, action):
	cwl = self._current
	tok = self._tokenstack
	if action == self._actions.N:
		return 0
	if action ==  self._actions.P:
		cwl.append(character)
		return 0
	if action ==  self._actions.E:
		return 1337
	if action ==  self._actions.PTG:
		cwl.append(character)
		tok.append([0, 0, self._entrytype.GROUPING_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		return 1
	if action ==  self._actions.TAPTG:
		tok.append([0, 0, self._entrytype.ALPHA_DIGIT_OR_UNDERSCORE, self._toktype.UNIDENTIFIED, cwl])
		cwl.append(character)
		tok.append([0, 0, self._entrytype.GROUPING_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		return 2
	if action ==  self._actions.TA:
		tok.append([0, 0, self._entrytype.ALPHA_DIGIT_OR_UNDERSCORE, self._toktype.UNIDENTIFIED, cwl])
		return 1
	if action ==  self._actions.TAP:
		tok.append([0, 0, self._entrytype.ALPHA_DIGIT_OR_UNDERSCORE, self._toktype.UNIDENTIFIED, cwl])
		cwl.append(character)
		return 1
	if action ==  self._actions.TRP:
		tok.append([0, 0, self._entrytype.QUOTE_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		cwl.append(character)
		return 1
	if action ==  self._actions.TRPTG:
		tok.append([0, 0, self._entrytype.QUOTE_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		cwl.append(character)
		tok.append([0, 0, self._entrytype.GROUPING_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		return 2
	if action ==  self._actions.TSP:
		tok.append([0, 0, self._entrytype.OTHER_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		cwl.append(character)
		return 1
	if action ==  self._actions.TSPTG:
		tok.append([0, 0, self._entrytype.OTHER_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		cwl.append(character)
		tok.append([0, 0, self._entrytype.GROUPING_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		return 2
	if action ==  self._actions.TS:
		tok.append([0, 0, self._entrytype.OTHER_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		return 1
	if action ==  self._actions.TR:
		tok.append([0, 0, self._entrytype.QUOTE_SYMBOL, self._toktype.UNIDENTIFIED, cwl])
		return 1
	return 0


