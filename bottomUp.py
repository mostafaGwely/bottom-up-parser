from pygraphviz import * 
from PIL import Image

class Stack:
	def __init__(self):
		self.s = [] 
	def pop(self):
		return self.s.pop()
	def push(self, item):
		self.s.append(item)
	def sizeOfStack(self):
		return len(self.s)
	def peak(self):
		return self.s[len(self.s)-1]
	def printStack(self):
		for i in range(len(self.s)):
			print(self.s[i])

class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return self.q == []

    def enqueue(self, item):
        self.q.insert(0,item)
    def enqueueAppend(self,item):
    	self.q.append(item)
    def dequeue(self):
        return self.q.pop()

    def sizeOfQueue(self):
        return len(self.q)
    def printQueue(self):
    	for i in range(len(self.q)):
    		print(self.q[i])

	
def foo(string ):
	global  index , inpIndex,inp,s,nodeNum,flage

	try:
		#print(string)
		index = int(string)
	except:
		if string[0] == 'r': # do reducing 
			temp = RulesTable[int(string[1:])]
			temp = temp.split("->")
			g = temp[1].split(" ")
			for i in range( len(g)*2 ):
				label = s.pop()
			num  = s.peak()
			s.push(temp[0])
			s.push(LR1Table[num][goto[temp[0]]])
			index = LR1Table[num][goto[temp[0]]]
			####################################
			# print the tree 
			# ####################################

			try:

				if len(g) == 1:
					q.enqueue((str(temp[0]),str(label)))
					# print((str(temp[0]),str(label)))
					if inp[inpIndex] in "+*/-":
						q.enqueue((str(inp[inpIndex])))
						# print(str(inp[inpIndex]))

				else:
					newq = Queue()
					for i in range(len(g)):
						n = q.dequeue()
						try:
							n = int(n)
							newq.enqueue(n)
						except:
							if len(n) == 2 :
								A.add_node(nodeNum,label=n[0]) #parent
								A.add_node(nodeNum+1,label=n[1]) #parent
								A.add_edge(nodeNum,nodeNum+1)
								newq.enqueue(nodeNum)
								nodeNum+=2
							elif len(n) == 1:
									A.add_node(nodeNum,label=n) #parent
									newq.enqueue(nodeNum)
									nodeNum+=1
					A.add_node(nodeNum,label=str(temp[0])) #parent
					for i in range(len(g)):
						A.add_edge(nodeNum,newq.dequeue())
					
					q.enqueueAppend(str(nodeNum))
					nodeNum+=1
					#########################
					# end of the tree ptinting 
					#########################
			except:
				print("error in tree becouse of ()")
		else: # do shifting 

			s.push(inp[inpIndex])
			s.push(int(string[1:]))
			inpIndex+=1
			index = s.peak()


A = AGraph(directed=True)
A.node_attr['shape']='circle'
A.node_attr['color']='plum'
A.node_attr['style']='filled'
A.node_attr['float']='right'
A.node_attr['labelfloat']='false'

index = 0
inpIndex = 0  # input pointer 
nodeNum = 0  # number of node for graphviz 
flage =1

s = Stack()
q = Queue()


inp = input(" enter taken ")
inp += " $"
inp = inp.split(' ')

terminals = ['+','ID']
nonterminals = ['S\'','S']

action  = {'+':0 ,'ID':1, '$':2}
goto ={'S\'':3 , 'S':4}

#rl(1) table 
LR1Table = []
LR1Table.append(['','s2','','',1])
LR1Table.append(['s3','','acc','',''])
LR1Table.append(['r2','','r2','',''])
LR1Table.append(['','s2','','',4])
LR1Table.append(['s3','','r1','',''])

#rules table
RulesTable = [] 
RulesTable.append("S'->S")
RulesTable.append("S->S + S")
RulesTable.append("S->ID")


s.push(0)
temp  = LR1Table[index][action[inp[inpIndex]]]

while(temp != "acc"):
	if temp == '':
		print("error")
		break
	foo(temp)
	temp  = LR1Table[index][action[inp[inpIndex]]]


#graphviz
A.layout()  # layout with default (neato)
A.draw('simple.png',prog='dot',args="-Grankdir=TB") # draw png
img = Image.open('simple.png')
img.show()




