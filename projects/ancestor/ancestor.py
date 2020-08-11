class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_ancestors(ancestors, node):
    result = []
    for x in ancestors:
        if x[1] == node:
            result.append(x[0])

    if len(result) > 0:
        return result
    else:
        return None

def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push(starting_node)
    ea = -1
    if get_ancestors(ancestors, starting_node) == None:
        return ea
    while s.size() > 0:
        curr = s.pop()
        parents = get_ancestors(ancestors, curr)

        if parents == None:
            ea = curr
            continue

        for parent in get_ancestors(ancestors, curr):          
            s.push(parent)
    

    return ea



    