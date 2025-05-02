class Subject:
    List = []
    Class_List = []
    def __init__(self, name, year, code, num):
        global List
        global Class_List
        self.name = name
        self.year = year
        self.code = code
        self.num = num
        List.append(name)
        Class_List.append(self)
    def Subjects():
      global List
      for item in List:
        print(item)