root_list = ['C','D','E','F','G','A','B']
notes_order_up = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
notes_order_down = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

notes_order = {
	'#': notes_order_up,
	'b': notes_order_down
}


notes = {
		'C': {
			'b':'0',
			'#':'1',
		},
		'D':{
			'b':'1',
			'#':'1',
		},
		'E':{
			'b':'1',
			'#':'0',
		},
		'F':{
			'b':'0',
			'#':'1',
		},
		'G':{
			'b':'1',
			'#':'1',
		},
		'A':{
			'b':'1',
			'#':'1',
		},
		'B':{
			'b':'1',
			'#':'0',
		},
}


scales = {
	'major': {
		'intervals': [2,2,1,2,2,2,1],
	},
	'minor': {
		'intervals': [2,1,2,2,1,2,2],
	},
	'minor_harm': {
		'intervals': [2,1,2,2,1,3,1],
	},
	'minor_mel': {
		'intervals': [2,1,2,2,2,2,1],
	},
	'ionian': {
		'intervals': [2,2,1,2,2,2,1],
	},
	'dorian': {
		'intervals': [2,1,2,2,2,1,2],
	},
	'phrygian': {
		'intervals': [1,2,2,2,1,2,2],
	},
	'lydian': {
		'intervals': [2,2,2,1,2,2,1],
	},
	'mixolydian': {
		'intervals': [2,2,1,2,2,1,2],
	},
	'aeolian': {
		'intervals': [2,1,2,2,1,2,2],
	},
	'locrian': {
		'intervals': [1,2,2,1,2,2,2],
	},
}


def calculate_scale(direction, root, scale):

	s_list = [root]
	curr_note = root

	n_list = notes_order[direction]
	for interval in scales[scale]['intervals']:
		index = n_list.index(curr_note)
		if index == len(n_list)-1:
			next_note = n_list[interval-1]
		else:
			next_note = n_list[index+interval] if index+interval<len(n_list) else n_list[0]
		s_list.append(next_note)
		curr_note = next_note

	return s_list


def calculate_note_scales(direction,root):

	dict_scales = {}

	for scale in scales.keys():
		dict_scales[scale] = calculate_scale(direction, root, scale)

	return dict_scales



def map_scales(direction):

	s_map = {}

	for note in root_list:
		s_map[note] = calculate_note_scales(direction, note)

	return s_map


def scale_detector():
	
	final_list = []
	print """
#################################
SCALE DETECTOR
#################################
little script for finding a scale given a set of notesdo da un set di note

how it works:
	> insert notes using space as separator
	> insert notes with the English-speaking notation (C D E F etc)
	> insert the alteration symbol (# or b) after the note (i.e. Cb D#)
	> don't mix alteration symbols (no b and # in the same input)

	"""
	try:
		user_notes = raw_input('insert notes:')
		user_notes = user_notes.split(' ')

		if any('#' in note for note in user_notes) and any('b' in note for note in user_notes):
			raise Exception
		else:
			direction = '#' if any('#' in note for note in user_notes) else 'b'

		s_map = map_scales(direction)
		from pprint import pprint
		pprint(s_map)
		for root, scales in s_map.items():
			for scale in scales.keys():
				print '{0} - {1}'.format(set(user_notes),set(scales[scale]))
				if set(user_notes).issubset(set(scales[scale])):
					final_list.append('{0} {1}\n'.format(root, scale))

		print ''.join(final_list)
	except:
		print "\n!!! if you read this you've probably screwed up something."

if __name__ == "__main__":
	scale_detector()
