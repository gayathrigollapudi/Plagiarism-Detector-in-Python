class Readfile:
	def __init__(self,file_name):
		self.file_name=file_name
		l=self.file_name.split("\\")
		i=l[-1][:-4]
		self.fname=i
		self.words_list=self.fileread(self.file_name)
	def fileread(self,fi):
		f=open(fi)
		s=f.read()
		s=s.lower()
		s=self.removespecialchar(s)
		self.raw_file=s
		self.char_list=list(s)
		s=list(s.split())
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
		return s1

class Bagwords:
	def __init__(self,l):
		self.files_list=l
		le=len(self.files_list)
		result=[]
		for i in range(le):
			result.append([])
			s=Readfile(l[i])
			for j in range(le):
				s1=Readfile(l[j])
				if i==j:
					result[i].append((s.fname,s1.fname,0))
				else:
					l1=[]
					d=self.frequency(s.words_list)
					d1=self.frequency(s1.words_list)
					k=self.euclidean(d)
					m=self.euclidean(d1)
					h=(math.sqrt(k))*(math.sqrt(m))
					g=self.dotproduct(d,d1)
					r=round((g/h)*100,2)
					r=str(r)+'%'
					result[i].append((s.fname,s1.fname,r))	
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

class Stringmatch:
	def __init__(self,l):
		self.files_list=l
		le=len(self.files_list)
		re=[]
		for i in range(le):
			re.append([])
			s=Readfile(l[i])
			for j in range(le):
				s1=Readfile(l[j])
				if i==j:
					re[i].append((s.fname,s1.fname,0))
				else:
					l1=[]
					lcs=self.substr(s.char_list,s1.char_list)
					match=((lcs*2)/(len(s.raw_file)+len(s1.raw_file)))*100
					r=str(round(match,2))+'%'
					re[i].append((s.fname,s1.fname,r))
		self.result_vect=re
	def substr(self,s,s1):
		le=len(s)
		le1=len(s1)
		lcs=0
		for i in range(le):
			for j in range(le1):
				l=[]
				t=i
				while i<=le-1 and j<=le1-1 and s[i]==s1[j]:
					l.append(s[i])
					i,j=i+1,j+1
				if len(l)!=0:
					l="".join(l)
					l=l.strip()
					le2=len(l)
					if lcs<le2:
						lcs=le2
				i=t
		return lcs
if __name__=='__main__':
	import glob
	import math
	i='G:\project\Plagiarism-Detector-in-Python'
	j=i+'\*.txt'
	l=glob.glob(j)
	a=Bagwords(l)
	print(a.result_vector)
	b=Stringmatch(l)
	print(b.result_vect)