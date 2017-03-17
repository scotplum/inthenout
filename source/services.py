Class Quotes(views):
    def __init__(self,urljson):
		self.urljson = urljson
		
	def parse_dict(self, urljson):
		quotes = urljson.get('quotes')
		