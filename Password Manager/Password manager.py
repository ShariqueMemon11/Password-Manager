

def view():
   pass

def add():
   name=input("Enter your user name:\n")
   pwd=input("Enter your password:\n")
   with open('password.txt','a') as p:
      p.write(name + "|" + pwd)

while(True):
   mode=input("Do you want to see existing paswords or add a new password (view, add)? or press q to quit\n").lower()
  
   if mode == 'q':
        quit()

   if mode == 'view':
      view()
   
   if mode =='add':
      add()
   
   else:
      print('invalid mode')
      continue