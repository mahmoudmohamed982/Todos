task_list={}
class Task():
    def __init__ (self,title,desc,date,owner):
        self.title=title
        self.desc=desc
        self.date=date
        self.owner=owner
        self.stutus="new"
    def edit_info(self, **kwargs):
        for key,value in kwargs.items():
            if hasattr(self,key) and value is not None:
                setattr(self,key,value)
class App_functions:
    def __init__(self):
        pass

    def add_new_task(self):
        self.title = input("Title: ")
        self.desc = input("Description: ")
        self.date = input("Date: ")
        self.owner = input("Owner: ")
        task_list[self.title] = Task(self.title, self.desc, self.date, self.owner)
        print("Task added successfully!")
def edit_task(self):
    title_id = input("Enter the title of the task: ").strip()
    task = task_list.get(title_id)
    if task:
        old_title = task.title  # ✅ خزن العنوان الحالي

        new_title = input("New Title: ").strip() or task.title
        new_desc = input("New Description: ").strip() or task.desc
        new_date = input("New Date: ").strip() or task.date
        new_owner = input("New Owner: ").strip() or task.owner
        new_status = input("New Status: ").strip() or task.stutus

        task.edit_info(
            title=new_title,
            desc=new_desc,
            date=new_date,
            owner=new_owner,
            stutus=new_status
        )

        # ✅ حدث العنوان في dict لو اتغير فعلاً
        if new_title != old_title:
            task_list.pop(old_title)
            task_list[new_title] = task
    else:
        print("Task not found.")

        title_id=input("enter the title of the task")
        task=task_list.get(title_id)
        if task:
            new_title = input("New Title: ").strip() or task.title
            new_desc = input("New Description: ").strip() or task.desc
            new_date = input("New Date: ").strip() or task.date
            new_owner = input("New Owner: ").strip() or task.owner
            new_status = input("New Status: ").strip() or task.stutus
            task.edit_info(
                        title=new_title,
                        desc=new_desc,
                        date=new_date,
                        owner=new_owner,
                        stutus=new_status
                    )
        else:
            print("task not found")
        if new_title != task.title:
            task_list.pop(title_id)
            task_list[new_title] = task
    def view_tasks(self):
        for title,task in task_list.items():
           print(f"title is {title}")
           print(f"desc is {task.desc}")
    def user_options(self):
        while True:
            for option_choice in ["1 add new task" , "2 edit task" ,"3 delete task","4 view all" , " 5 exit"]:
                print(option_choice)
            
            try:
                choice_input=int(input("what you need ?"))
                if choice_input == 1:
                    self.add_new_task()
                elif choice_input == 2:
                    self.edit_task()
                elif choice_input == 3:
                    del_task=input("enter title of task to del").strip()
                    delted_task=task_list.get(del_task)
                    if delted_task:
                        task_list.pop(del_task)
                    else:
                        print("task not found")
                elif choice_input == 4:
                    self.view_tasks()
                elif choice_input == 5:
                    print("Exiting program...")
                    break
                else:
                     print("Please choose a correct option (1–5).")
            except ValueError:
                    print("Please enter a valid number.")
user=App_functions()
user.user_options()