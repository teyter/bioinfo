def adj(lst):
    for i in range(len(lst)-1):
        element = lst[i]
        index_next = i+1
        current_left = lst[i][0]
        next_left = lst[i+1][0]
        next_right = lst[i+1][1]
        indices = []
        
        if current_left == next_left:
            element.append(next_right)
            next_left = "x"
            indices.append(index_next)
    return lst

def test():
    data = "".join(open('sample.txt')).split()
    k = int(data[0])
    text = data[1]
    comp = composition_k(text,3)
    dic = dict.fromkeys(comp,[])
    dic["AAG"].append("teitur")
    print(dic)

def main():
    data = "".join(open('sample.txt')).split()
    k = int(data[0])
    text = data[1]
    comp = composition_k(text,3)
    tpl = lst2tpl(comp)
    tpl.sort()
    tpl = dict(tpl)
    #result = adj(tpl)
    printdict(tpl)
