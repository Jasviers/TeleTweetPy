class loginSrBot:
	
	def __init__(self, du, contr):
		self.dueno = du
		self.contra = contr

	def comprobarLogin(self,du, contr):
		return self.dueno == du and self.contra == contr
