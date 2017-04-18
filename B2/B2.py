import os
from flask import Flask
from flask import render_template
from flask import request 
app=Flask(__name__)
class PlagiarismChecker:
	def __init__(self,filename):
		self.filename=filename
		self.lineScore=0
		self.wordScore=0
		self.data_lines=[]
		self.data_words=set()
		self.inp_lines=[]
		self.inp_words=set()
		
	def loadData(self):
		temp=[]
		with open(self.filename) as f:
			for lines in f:
				for line in lines.split('.'):
					line=line.replace(",","")
					line=line.replace(".\n","")
					line=line.replace("\n","")
					line=line.replace(":","")
					line=line.replace("'","")
					line=line.lower()
					self.data_lines.append(line)
					temp=line.split()
					for val in temp:
						self.data_words.add(val)
	def loadInput(self,inp_string):
		temp=[]
		for line in inp_string.split('.'):
			line=line.replace(",","")
			line=line.replace(".\n","")
			line=line.replace("\n","")
			line=line.replace(":","")
			line=line.replace("'","")
			line=line.lower()
			self.inp_lines.append(line)
			temp=line.split()
			for val in temp:
				self.inp_words.add(val)
			

	def scoreByWords(self):
		for dword in self.data_words:
			for iword in self.inp_words:
				if(dword==iword):
					self.wordScore+=1
		print self.wordScore
		self.wordScore=float(self.wordScore)/float(len(self.data_words))*100
	
	def scoreByLines(self):
		for dline in self.data_lines:
			for iline in self.inp_lines:
				if(dline==iline and ((dline or iline) !='')):
					self.lineScore+=1
		print self.lineScore
		self.lineScore=float(self.lineScore)/float(len(self.data_lines))*100

	def CheckPlagiarism(self):
		self.scoreByWords()
		self.scoreByLines()	
		print "Score by word matching = ",self.wordScore
		print "Score by line matching = ",self.lineScore
		print "Average Score =",float((self.wordScore+self.lineScore)/2)
		return "Score :="+str(float((self.wordScore+self.lineScore)/2))	

@app.route('/')
def init():	
	return render_template('index.html')	
	

@app.route('/',methods=["POST"])
def calculate():
	obj=PlagiarismChecker('data.txt')
	obj.loadData()
	str_inp=request.form["val"]
	obj.loadInput(str_inp)	
	someVal=obj.CheckPlagiarism()
	return someVal

if __name__=="__main__":
	app.run("localhost",debug=True)
