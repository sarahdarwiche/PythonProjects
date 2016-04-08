def questions():
	answer = input('Does it have horns?')
	if (answer == 'yes'):
		answer = input('Does it have hooves?')
		if (answer == 'yes'):
			print('It is a goat.')
		elif (answer == 'no'):
			print('It is a narwhal.')
	elif (answer == 'no'):
		answer = input('Does it have stripes?')
		if (answer == 'yes'):
			answer = input('Does it have hooves?')
			if (answer == 'yes'):
				print('It is a zebra.')
			elif (answer == 'no'):
				answer = input('Does it have a tail?')
				if (answer == 'yes'):
					print('It is a tiger.')
				elif (answer == 'no'):
					print('It is a bee.')
		elif (answer == 'no'):
			answer = input('Does it have hooves?')
			if (answer == 'yes'):
				print('It is a horse.')
			elif (answer == 'no'):
				answer = input('Does it have a tail?')
				if (answer == 'no'):
					print('It is a human.')
				elif (answer == 'yes'):
					answer = input('Does it have more than two legs?')
					if (answer == 'yes'):
						print('It is a lion.')
					elif (answer == 'no'):
						print ('It is a snake.')
questions()
