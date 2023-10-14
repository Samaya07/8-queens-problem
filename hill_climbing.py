import copy
class Make_node:
    def __init__(self,node):
        self.state=node
        self.value,self.queen_pos=self.heuristic()
    def heuristic(self):
        queen_pos=[]
        for i in range(8):
            for j in range(8):
                if self.state[j][i]==1:
                    queen_pos.append([j,i])
        h=0
        for i in range(7):
            x0=queen_pos[i][0]
            y0=queen_pos[i][1]

            for j in range(i+1,8):
                x=queen_pos[j][0]
                y=queen_pos[j][1]
                if x0==x:
                    h=h+1
                if y0==y:
                    h=h+1
                if abs(x0-x)==abs(y0-y):
                    h=h+1
        return h,queen_pos
    
def children(node):
    queen_pos=node.queen_pos
    h_min=float('inf')
    for i in range(8):
        for j in range(8):
            parent_queen_row=queen_pos[i][0]
            child_state=copy.deepcopy(node.state)
            child_state[queen_pos[i][0]][queen_pos[i][1]]=0
            if j!=parent_queen_row:
                child_state[j][i]=1
                child=Make_node(child_state)
                if child.value<h_min:
                    h_min=child.value
                    child_node=child
    return child_node

def hill_climbing(initial_state):
    current=Make_node(initial_state)
    print("The heuristic value of the initial state = ",current.value)
    while(True):
        neighbor=children(current)
        if neighbor.value>=current.value:
            return current
        current=neighbor

if __name__=='__main__':
    initial_state=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],
       [1,0,0,0,1,0,0,0],[0,1,0,0,0,1,0,1],[0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0]]
    print("Initial state --->")
    for ele in initial_state:
        print(ele)
    print()
    result=hill_climbing(initial_state)
    print()
    print("After using the Hill-climbing algorithm, the local minimum generated is --->")
    for ele in result.state:
        print(ele)
    print()
    print("The heuristic value of the resultant state = ",result.value)

