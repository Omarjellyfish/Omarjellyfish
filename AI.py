# #TABLE DRIVEN AGENT
# A='A'
# B='B'
# precepts=[]
# #first build the table
# table={((A,'clean'),):'right',((B,'clean'),):'left',
#        ((A,'dirty'),):'suck',((B,'dirty'),):'suck',
#        ((A,'clean'),(A,'clean')):'right',
#        ((A,'clean'),(A,'dirty')):'suck',
#        ((A,'clean'),(B,'clean')):'left',
#        ((A,'clean'),(B,'dirty')):'suck',
#        ((B,'clean'),(A,'clean')):'right',
#        ((B,'clean'),(A,'dirty')):'suck',
#        ((B,'clean'),(B,'clean')):'left',
#        ((B,'clean'),(B,'dirty')):'suck',
#        ((A,'clean'),(B,'clean'),(A,'dirty')):'suck'}
# def lookup(precepts,table):
#     action=table.get(tuple(precepts))
#     return action
# def table_driven_agent(precept):
#     precepts.append(precept)
#     action=table.get(tuple(precepts))
#     return action
# def run():
#     print('action \tpercepts')
#     print(table_driven_agent((A,'clean'),),'\t',precepts)
#     print(table_driven_agent((B, 'dirty'), ), '\t', precepts)
# run()

#REFLEX AGENT  VACUUM
A='A'
B='B'
enviroment={A:'dirty',B:'dirty','current':A}
def sensor():
    loc=enviroment['current']
    stat=enviroment[loc]
    return (loc,stat)
def reflex_vac_agent(loc,stat):
    if stat=='dirty':
        return 'suck'
    elif loc==A:
        return 'right'
    elif loc==B:
        return 'left'

def acutators(action):
    loc=enviroment['current']
    if action =='suck':
        enviroment[loc]='clean'
    elif action=='right':
        enviroment['current']=B
    elif action=='left':
        enviroment['current']=A

def run(n):
    print('(loc1,status1)\t action\t (loc2,status2)')
    for i in range(n):

        (loc1, stat1) = sensor()
        action = reflex_vac_agent(loc1, stat1)
        acutators(action)
        (loc2, stat2) = sensor()
        print((loc1, stat1),'\t',action,'\t',(loc2, stat2))
run(5)



#simple reflex agent :same as reflex agent vacuum but wtih rules and actions depending on rules
#also use match rule and simple reflex
# A='A'
# B='B'
# enviroment={A:'dirty',B:'dirty','current':A}
# def sensor():
#     loc=enviroment['current']
#     stat=enviroment[loc]
#     return (loc,stat)
#
# action_rule={1:'suck',2:'right',3:"left",4:'noop'}
# rules={(A,'dirty'):1,(B,'dirty'):1,(A,'clean'):2,(B,'clean'):3,(A,B,'clean'):4}
# def match_rule(state,rules):
#     rule=rules.get(state)
#     return rule
#
# def simple_reflex_agent(loc,status):
#     state=(loc,status)
#     rule=match_rule(state,rules)
#     action=action_rule.get(rule)
#     return action
#
# def acutators(action):
#     loc=enviroment['current']
#     if action =='suck':
#         enviroment[loc]='clean'
#     elif action=='right':
#         enviroment['current']=B
#     elif action=='left':
#         enviroment['current']=A
#
# def run(n):
#     print('(loc1,status1)\t action\t (loc2,status2)')
#     for i in range(n):
#         if enviroment[A]=='clean' and enviroment[B]=='clean':
#             rul=rules[(A,B,'clean')]
#             act=action_rule[rul]
#             print('(A,B,clean)','\t',act)
#             break
#         (loc1, stat1) = sensor()
#         action = simple_reflex_agent(loc1, stat1)
#         acutators(action)
#         (loc2, stat2) = sensor()
#         print((loc1, stat1),'\t',action,'\t',(loc2, stat2))
# run(5)


#REFLEX AGENT WITH STATE #depends on precept history
A='A'
B='B'
enviroment={A:'dirty',B:'dirty','current':A}
def sensor():
    loc=enviroment['current']
    stat=enviroment[loc]
    return (loc,stat)

action_rule={1:'suck',2:'right',3:"left",4:'noop'}
rules={(A,'dirty'):1,(B,'dirty'):1,(A,'clean'):2,(B,'clean'):3,(A,B,'clean'):4}

def match_rule(state,rules):
    rule=rules.get(state)
    return rule

state={}
action=None
model={A:None,B:None}
def update(percept):
    (location,status)=percept
    state=percept
    if model[A]==model[B]=='clean':
        state=(A,B,'clean')
    model[location]=status
    return state

def reflex_agent_state(loc,status):
    percept=(loc,status)
    state=update(percept)
    rule=match_rule(state,rules)
    action=action_rule.get(rule)
    return action

def acutators(action):
    loc=enviroment['current']
    if action =='suck':
        enviroment[loc]='clean'
    elif action=='right':
        enviroment['current']=B
    elif action=='left':
        enviroment['current']=A

def run(n):
    print('(loc1,status1)\t action\t (loc2,status2)')
    for i in range(n):

        (loc1, stat1) = sensor()
        action = reflex_agent_state(loc1, stat1)
        acutators(action)
        (loc2, stat2) = sensor()
        print((loc1, stat1),'\t',action,'\t',(loc2, stat2))
run(5)

# GENERAL TREE need to do again
# problem='go to l'
# intial_state= {'go to l':'A'}
# state_space = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'J'], 'E': [], 'F': ['I', 'K'],
#                'G': ['L', 'M'], 'H': [], 'J': [], 'I': [], 'K': [], 'L': [], 'M': []}
#
# goal_test = {"go to l": 'L'}
# class Node:
#     def __init__(self,state , parent=None , depth=0):
#         self.STATE=state
#         self.PARENT_NODE=parent
#         self.DEPTH=depth
#     def path(self):
#         x,result=self,[self]
#         while x.PARENT_NODE:
#             result.append(x.PARENT_NODE)
#             x=x.PARENT_NODE
#         return result
#     def display(self):
#         print(self.STATE,'',self.DEPTH)
#
# def make_node(state):
#     return Node(state)
#
# def insert(node,queue):
#     queue[:0]=[node] #queue alwys insert in front
#     return queue
# def insert_all(list,queue):
#     for node in list:
#         insert(node,queue)
#     return queue
# def removefirst(queue):
#     if len(queue)!=0:
#         first=queue[0]
#         queue[0:1]=[]
#         return first
#     return []
#
# def expand(node):#shows rest of nodes connected
#     successors=[]
#     state_space_node=state_space[node.STATE]
#     for result in state_space_node:
#         s=Node(node)
#         s.STATE=result
#         s.PARENT_NODE=node
#         s.DEPTH=node.DEPTH+1
#         successors=insert(s,successors)#visited
#     return successors
#
# #main funcitoin to check if goal test==state
# def tree_search(problem,fringe):
#     intial=intial_state[problem]
#     nd=make_node(intial)
#     fringe=insert(nd,fringe) #insert A in queue [a]
#     while True:
#         node=removefirst(fringe)
#         if goal_test[problem]==node.STATE:
#             return  node.path()
#         success=expand(node)
#         for i in success:
#             if goal_test[problem]==i.STATE:
#                 return node.path()
#         fringe = insert_all(success,fringe)
#
# def run():
#     print('solution \n state depth')
#     for node in tree_search(problem,[]):
#         node.display()
#
# run()

# BFS
# def bfs(tree,start,dest):
#     queue=list()
#     visited=list()
#     queue.append(start)
#     print('visited',start)
#     result=['not reachable',list()]
#     while queue:
#         node=queue.pop(0)
#         visited.append(node)
#         if node==dest:
#             print('destination node found',node)
#             result[0]='reachable'
#             break
#         print(node,'is not destination node')
#         for child in tree[node]:
#             if child not in visited:
#                 queue.append(child)
#     result[1]=visited
#     return result
#
# tree={'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'J'], 'E': [], 'F': ['I', 'K'],
#                'G': ['L', 'M'], 'H': [], 'J': [], 'I': [], 'K': [], 'L': [], 'M': []}
# result=bfs(tree,'A','H')
# print(result[0])
# print('path to traverse ',result[1])

# DFS
# def dfs(tree,start,dest):
#     stack=list()
#     visited=list()
#     stack.append(start)
#     result=['not reachable',list()]
#     while stack:
#         node=stack.pop()
#         visited.append(node)
#         if node==dest:
#             print('dest node found',node)
#             result[0]='reachable'
#             break
#         print(node,'not destin')
#         for child in tree[node]:
#             if child not in visited:
#                 if child not in visited:
#                     stack.append(child)
#     result[1]=visited
#     return result
#
#
# tree={'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'J'], 'E': [], 'F': ['I', 'K'],
#                'G': ['L', 'M'], 'H': [], 'J': [], 'I': [], 'K': [], 'L': [], 'M': []}
# res=dfs(tree,'A','H')
# print(res)



#DEPTH LIMITED SEARCH
# tree= {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': ['H', 'I'],
#     'E': ['J', 'K'],
#     'F': ['L', 'M'],
#     'G': ['N', 'O'],
#     'H': [],
#     'I': [],
#     'J': [],
#     'K': [],
#     'L': [],
#     'M': [],
#     'N': [],
#     'O': []
# }
# def dls(start,goal, path,level ,maxD):
#     print('current lvevel',level)
#     print(goal,'is the goal')
#     path.append(start)
#     if start==goal:
#         print('goal test succes')
#         return start
#     print('goal node testing failed')
#     if level==maxD:
#         return False
#     print('expanding current node')
#     for child in tree[start]:
#         if dls(child,goal,path,level+1,maxD):
#             return path
#         path.pop()
#     return False
# start="A"
# goal=input('enter ur destination')
# maxD=int(input("enter ur max depth"))
# path=list()
# res=dls(start,goal,path,0,maxD)
# if (res):
#     print('path to goal node availbe')
#     print('path',path)


# BEST FIRST SEARCH NEED REVISE;
# SuccList = {'A': [['B', 3], ['C', 2]], 'B': [['A', 5], ['C', 2], ['D', 2], ['E', 3]],
#             'C': [['A', 5], ['B', 3], ['F', 2], ['G', 4]], 'D': [['H', 1], ['I', 99]], 'F': [['J', 99]],
#             'G': [['K', 99], ['L', 3]]}
# start='A'
# goal='H'
# close=list()
# SUCCESS=True
# Failure=False
# state=Failure
# def goaltest(N):
#     if N==goal:
#         return True
#     return False
#
# def moveGen(N):
#     new_list=list()
#     if N in SuccList.keys():
#         new_list=SuccList[N]
#     return new_list
#
# def Append(L1,L2):
#     new_list=list(L1)+list(L2)
#     return new_list
#
# def Sort(L):
#     L.sort(key=lambda x:x[1])
#     return L
#
# def bestfirstsearch():
#     Open=[[start,5]]
#     Closed=list()
#     global state,close
#     while (len(Open)!=0) and (state!=SUCCESS):
#         print("------------")
#         N = Open[0]
#         print("N=", N)
#         del Open[0]  # delete the node we picked
#         if goaltest(N[0])==True:
#             state=SUCCESS
#             Closed=Append(Closed,[N])
#             print('Closed=',Closed)
#         else:
#             Closed=Append(Closed,[N])
#             print('Closed=',Closed)
#             CHILD=moveGen(N[0])
#             print('child=',CHILD)
#             for val in Open:
#                 if val in CHILD:
#                     CHILD.remove(val)
#             for val in Closed:
#                 if val in CHILD:
#                     CHILD.remove(val)
#             Open=Append(CHILD,Open)
#             print('unsorted open',Open)
#             Sort(Open)
#             print('sorted open=',Open)
#     close=Closed
#     return state
# bestfirstsearch()


#HILL CLIMBING TEQ NEED Revise
# SuccList = {'A': [['B', 3], ['C', 2]], 'B': [['A', 5], ['C', 2], ['D', 2], ['E', 3]],
#             'C': [['A', 5], ['B', 3], ['F', 2], ['G', 4]], 'D': [['H', 1], ['I', 99]], 'F': [['J', 99]],
#             'G': [['K', 99], ['L', 3]]}
# Start='A'
# goal='H'
# closed=list()
#
# def moveGen(N):
#     new_list=list()
#     if N in SuccList.keys():
#         new_list=SuccList[N]
#     return new_list
#
# def Append(L1,L2):
#     new_list=list(L1)+list(L2)
#     return new_list
#
# def Sort(L):
#     L.sort(key=lambda x:x[1])
#     return L
#
# def heu(Node):
#     return Node[1]
#
# def hillclimb(start):
#     global closed
#     N = Start
#     CHILD = moveGen(N)
#     Sort(CHILD)
#     N=[start,5]
#     print('\n start= ',N)
#     print('sorted child list',CHILD)
#     newNode=CHILD[0]
#     Closed=[N]
#     while heu(newNode)<=heu(N):
#         print('\n --------------')
#         N=newNode
#         print('N=',N)
#         Closed=Append(Closed,[N])
#         CHILD=moveGen(N[0])
#         Sort(CHILD)
#         print('sorted child list', CHILD)
#         print('Closed=',Closed)
#         newNode=CHILD[0]
#         closed=Closed
# hillclimb(Start)

# ITERATIVE DEEPING DEPTH FIRST SEARCH
# tree= {
#     'A': ['B', 'C'],
#     'B': ['D','E'],
#     "C": ['G'],
#     'D': [],
#     'E': ['F'],
#     'G': [],
#     'F':[]
# }
#
# path=list()
#
# def dfs(currentNode,destination,tree,maxDepth,curList):
#     print('checking for dest',currentNode)
#     curList.append(currentNode)
#     if currentNode==destination:
#         return True
#     if maxDepth<=0:
#         path.append(curList)
#         return False
#     for node in tree[currentNode]:
#         if dfs(node,destination,tree,maxDepth-1,curList):
#             return True
#         else:
#             curList.pop()
#     return False
#
# def iterDDFS(currentNode,destination,tree,maxDepth):
#     for i in range(maxDepth):
#         curList=list()
#         if dfs(currentNode,destination,tree,i,curList):
#             return True
#     return False
# if not iterDDFS('A','G',tree,4):
#     print('no path')
# else:
#     print('path exists')
#     print(path.pop())
#
# #A STAR
# class Graph:
#     def __init__(self,adja_list):
#         self.adja_list=adja_list
#
#     def getN(self,v):
#         if v in self.adja_list:
#             return self.adja_list[v]
#         return []
#     def h(self,node):
#         H={
#             'A':1,
#             'B':1,
#             'C':1,
#             'D':1
#         }
#         return H[node]
#     def ASTAR(self,start,stop):
#         OPEN_LST=set([start]) #[A]
#         CLOSED_LST=set([])
#         #poo conatians the distance from start to all other vert
#         #defaul val is +inf
#         poo={} #{A:0}
#         poo[start]=0
#         #par contains all adj mapping of all nodes
#         par={} #parent
#         par[start]=start #{'A':'A'}
#         while len(OPEN_LST)>=0:
#             n=None
#             for v in OPEN_LST:
#                 if n==None or poo[v]+self.h(v)<self.h(n)+poo[n]:
#                     n=v
#
#             if n==None:
#                 print('no path')
#                 return None
#             if n==stop:
#                 reconst_path=[]
#
#                 while par[n]!=n:
#                     reconst_path.append(n)
#                     n=par[n]
#                 reconst_path.append(start)
#                 reconst_path.reverse()
#                 print('path found: {}'.format(reconst_path))
#                 return reconst_path
#             #for all neigbours of current node
#             for (m,weight) in self.getN(n):
#                 #if curNode not in open or closed list
#                 #add it ot open list and node n as its parent
#                 if m not in OPEN_LST and m not in CLOSED_LST:
#                     OPEN_LST.add(m)
#                     par[m]=n
#                     poo[m]=poo[n]+weight
#                 #other wise check if its quicker to visit n,then m
#                 #if it is update par and poo data
#                 #and if node was in open list move it to closed list
#                 else:
#                     if poo[m]>poo[n]+weight:
#                         poo[m]=poo[n]+weight
#                         par[m]=n
#                         if m in CLOSED_LST:
#                             CLOSED_LST.remove(m)
#                             OPEN_LST.add(m)
#             #remove n from open list and add it to closed list
#             #because all n's neighbours were visited
#             OPEN_LST.remove(n)
#             CLOSED_LST.add(n)
#         print('path doesnt exist')
#         return None
# adjac_list={
#     'A':[('B',1),('C',3),('D',7)],
#     'B':[('D',5)],
#     'C':[('D',12)]
# }
# graph1=Graph(adjac_list)
# graph1.ASTAR('A','D')
