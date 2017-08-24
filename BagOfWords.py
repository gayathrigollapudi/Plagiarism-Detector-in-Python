class Readfile:
	def __init__(self,file_name):
		self.file_name=file_name
		self.words_list=self.fileread(self.file_name)
	def fileread(self,fi):
		f=open(fi)
		s=f.read()
		self.raw_file=s
		s=s.replace(",",'').replace(".","")
		s=s.lower()
		s=self.removespecialchar(s)
		return s
	def removespecialchar(self,s):
		st=''
		s1=''
		for i in s:
			if (ord(i)<123 and ord(i)>96) or (ord(i)<58 and ord(i)>47) or i=='_':
				st+=i
			elif(i==" "):
				s1+=(st+i)
				st=""
		s1+=st
		return list(s1.split())

class Bagwords:
	def __init__(self,l):
		self.files_list=l
		le=len(self.files_list)
		result=[]
		for i in range(le-1):
			result.append([])
			s=Readfile(l[i])
			for j in range(le):
				if i==j:
					result[i].append((l[i],l[j],0))
				else:
					l1=[]
					s1=Readfile(l[j])
					d=self.frequency(s.words_list)
					d1=self.frequency(s1.words_list)
					k=self.euclidean(d)
					m=self.euclidean(d1)
					h=(math.sqrt(k))*(math.sqrt(m))
					g=self.dotproduct(d,d1)
					r=round((g/h)*100,2)
					r=str(r)+'%'
					result[i].append((l[i],l[j],r))	
		self.result_vector=result
	def frequency(self,s):
		d={}
		for i in s:
			if i not in d:
				d[i]=1
			else:
				d[i]+=1
		return d
	def euclidean(self,d):
		sum=0
		for i in d.values():
			sum+=(i**2)
		return sum
	def dotproduct(self,d,d1):
		sum=0
		for i in d:
			if i in d1:
				sum+=(d[i]*d1[i])
		return sum
import glob
import math
i='G:\project\Plagiarism-Detector-in-Python'
j=i+'\*.txt'
l=glob.glob(j)
a=Bagwords(l)
print(a.result_vector)