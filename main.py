
class Nodo:
    def __init__(self, value=None):
        self.siguientes = {}
        self.value = value

class dictionaryTrie(object):
    def __init__(self):
        self.root = Nodo()
        self.size = 0
        self.keys = []

    def __len__(self):
        return self.size

    def __repr__(self):
        res = "{"
        if len(self)>0:
            i = 0
            while i<len(self.keys)-1:
                res += f"{self.keys[i]} : {self[self.keys[i]]}, "
                i+=1
            res += f"{self.keys[i]} : {self[self.keys[i]]}"

        res +='}'
        return res

    def insert(self,key,value):
        actual = self.root
        for c in key:
            if list(actual.siguientes.keys()).count(c)==0:
                actual.siguientes[c]=Nodo()
            actual= actual.siguientes[c]
        self.keys.append(key)
        actual.value=value
        self.size +=1

    def __getitem__(self, item):
        nd = self.root
        for c in item:
            nd = nd.siguientes[c]
        return nd.value

    def __iter__(self):
        self.it = 0
        return self

    def __next__(self):
        if self.it < len(self.keys):
            aux =self.it
            self.it +=1
            return (self.keys[aux],self[self.keys[aux]])
        else:
            raise StopIteration

    def __contains__(self, item):
        return self.keys.count(item)>0


def main():
    diccTrie = stringMap()
    dicc = {"hola":2,"mundo":3}

    print(diccTrie)

    diccTrie.insert("hola",2)
    diccTrie.insert("mundo",3)
    diccTrie.insert("!",4)

    print(diccTrie)

    for i in diccTrie:
        print(i)


main()