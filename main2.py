from subjects import Subject
List = []
Class_List = []
print('''Welcome to the subjects manager.
--------------------------------''')
while True:
  choice = input('''Commands:
      1. Add a subject to the list
      2. View a chosen subject from the list
      3. View all subject details from the list
      4. Quit
      Insert your command (number): ''')
  if choice == '1':
    name = input("Subject name: ")
    year = input("Year: ")
    code = input("Class code: ")
    num = input("Number of students: ")
    subject = Subject(name,year,code,num)
    List.append(subject.name)
    Class_List.append(subject)
  elif choice == '2' and List != []:
    for item in List:
      print(item)
    subject = input("View details of which subject? ")
    Class = Class_List[List.index(subject)]
    print(Class.name)
    print(Class.year)
    print(Class.code)
    print(Class.num)
  elif choice == '3' and Class_List != []:
    for item in Class_List:
      Class = item
      print(Class.name)
      print(Class.year)
      print(Class.code)
      print(Class.num)
  elif choice == '4':
    break