from subjects import Subject
print('''Welcome to the subjects manager.
--------------------------------''')
while True:
  choice = input('''Commands:
      1. Add a subject to the list
      2. View a chosen subject from the list
      3. View all subject details from the list
      Insert your command (number): ''')
  if choice == '1':
    subject = Subject()