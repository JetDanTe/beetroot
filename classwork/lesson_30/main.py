



class Diikstra:
    def __init__(self):
        self.__hosts = set()
        self.__edges = dict()

    def add_edge(self, f_host, s_host, dist: int):
        if f_host in self.__hosts and s_host in self.__hosts:
            self.__edges[(f_host, s_host)] = dist
            self.__edges[(s_host, f_host)] = dist


    def add_hosts(self, *hosts):
        for host in hosts:
            self.__hosts.add(host.upper())


    def calc_distance(self, f_host):
        self.__dist = {f_host: 0}
        que = list()
        que.append(f_host)
        while que:
            host = que.pop(0)
            childs = self.neighbours(host)
            for c in childs:
                tmp = self.__dist[host] + self.__edges[(c, host)]
                if not c in self.__dist or self.__dist[c] > tmp:
                    self.__dist[c] = tmp
                    que.append(c)
        print(self.__dist)


    def neighbours(self, host):
        neighbours_set = set ()
        for h_1, h_2 in self.__edges:
            if h_1 == host:
                neighbours_set.add(h_2)
        return neighbours_set




    def __str__(self):
        return f"{self.__hosts}\n"

if __name__ == '__main__':
    d = Diikstra()
    d.add_hosts(*"ABCDEFGH")
    d.add_edge("A", "B", 4)
    d.add_edge("A", "D", 7)
    d.add_edge("A", "C", 6)
    d.add_edge("B", "F", 5)
    d.add_edge("B", "D", 3)
    d.add_edge("B", "G", 15)
    d.add_edge("B", "H", 9)
    d.add_edge("C", "D", 1)
    d.add_edge("C", "G", 13)
    d.add_edge("C", "F", 4)
    d.add_edge("D", "F", 4)
    d.add_edge("D", "G", 12)
    d.add_edge("F", "G", 2)
    d.add_edge("H", "G", 7)
    d.calc_distance("A")
