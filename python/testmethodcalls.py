
class TestMethodCall:

	def __init__(self):
		self.method(1,1)

	def method(self,relay,state):
		print "hello"
		print relay
		print state

x=TestMethodCall()
