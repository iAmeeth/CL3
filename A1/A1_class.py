import os
import unittest
class BinarySearch:
	def __init__(self,filename):
		self.filename=filename
		self.key=0
		self.inp_list=[]

	def takeInput(self):
		with open(self.filename) as f:
			for entry in f:
				self.inp_list.append(int(entry.strip()))
			print "Entered array is ",self.inp_list

	def sortList(self):
		for i in xrange(len(self.inp_list)-1,0,-1):
			for j in range(i):
				if(self.inp_list[j]>self.inp_list[j+1]):
					self.inp_list[j],self.inp_list[j+1]=self.inp_list[j+1],self.inp_list[j]
		print "Sorted list ",self.inp_list

	def callSearch(self):
		self.key=int(input("Enter the key to be searched"))
		print self.Bsearch(0,len(self.inp_list)-1)

	def Bsearch(self,low,high):
		if(low<=high):
			mid=(low+high)/2
			if(self.key==self.inp_list[mid]):
				return mid

			elif(self.key<self.inp_list[mid]):
				return self.Bsearch(low,mid-1)

			elif(self.key>self.inp_list[mid]):
				return self.Bsearch(mid+1,high)

obj=BinarySearch('input.txt')
obj.takeInput()
obj.sortList()
obj.callSearch()

class MyTest(unittest.TestCase):
	def test_positive(self):
		obj.key=12
		self.assertEquals(obj.Bsearch(0,9),1)
	def test_negative(self):
		obj.key=999999999
		self.assertEquals(obj.Bsearch(0,9),None)

unittest.main()
		
	
