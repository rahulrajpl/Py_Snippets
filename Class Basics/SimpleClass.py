class SimpleClass:
	"""This is description about the Simple Class
	Accessed using SimpleClass Object name . __doc__
	"""
	answer_to_life = 233

	def __init__(self): # This will change the value of i
		self.answer_to_life = 42

	def say_hello(self):
		return "Hello World!!"

if __name__ == "__main__":
	obj = SimpleClass()
	print(obj.answer_to_life)
	print(obj.say_hello()) # Insance object is passed as argument by default. SimpleClass.say_hello(obj)
	print(obj.__doc__)
	say = obj.say_hello # Method is given anther reference name.
	print(say())

