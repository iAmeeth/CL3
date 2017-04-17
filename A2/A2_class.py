import xml.etree.ElementTree as ET
import threading
import unittest
class QuickSort:
	def __init__(self,filename):
		self.filename=filename
		self.inp_list=[]

	def takeInput(self):
		with open(self.filename) as f:
			tree=ET.parse(f)
			root=tree.getroot()
			somedata=root.text.split()
			for val in somedata:
				self.inp_list.append(int(val))
			print "Input array ",self.inp_list

	def partition(self,first,last):
		pivot=self.inp_list[first]
		i=first+1
		j=last
		while(i<=j):
			while(i<=j and pivot>=self.inp_list[i]):
				i+=1
			while(j>=i and pivot<=self.inp_list[j]):
				j-=1
			if(i<j):
				self.inp_list[i],self.inp_list[j]=self.inp_list[j],self.inp_list[i]
		self.inp_list[first],self.inp_list[j]=self.inp_list[j],self.inp_list[first]
		return j

	def QSort(self,low,high):
		if(low<high):
			mid=self.partition(low,high)
			t1=threading.Thread(self.QSort(low,mid-1))
			t2=threading.Thread(self.QSort(mid+1,high))
			t1.start()
			t2.start()
			print "Thread left:",t1.getName()
			t1.join()
			print "Thread right:",t2.getName()
			t2.join()
			

	def printAnswer(self):
		print "Sorted array ",self.inp_list

obj=QuickSort('input.xml')
obj.takeInput()
obj.QSort(0,len(obj.inp_list)-1)
obj.printAnswer()

class MyTest(unittest.TestCase):
	def test_negative(self):
		print "Running Negative test"
		obj.filename='input1.xml'
		self.assertRaises(IOError,obj.takeInput)
	def test_positive(self):
		print "Running Positive test"
		obj.inp_list=[12,4,5,1,100]
		obj.QSort(0,len(obj.inp_list)-1)
		self.assertEquals(obj.inp_list,[1,4,5,12,100])


unittest.main()
