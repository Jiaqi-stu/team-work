import datetime
from collections import defaultdict

def get_valid_date(prompt):
    """获取有效的日期"""
    while True:
        date_str = input(prompt)
        try:
            for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%m-%d-%Y', '%m/%d/%Y']:
                try:
                    return datetime.datetime.strptime(date_str, fmt).date()
                except ValueError:
                    continue
            raise ValueError("This is not a correct date.")
        except ValueError as e:
            print(f"Error: {e}, please enter in the format of YYYY-MM-DD or MM/DD/YYYY.")

def get_valid_deadline(task_date):
    """获取当天的截止时间（几点几分）"""
    while True:
        time_str = input("Please enter the deadline time (in HH:MM format): ")
        try:
            time_obj = datetime.datetime.strptime(time_str, '%H:%M').time()
            deadline = datetime.datetime.combine(task_date, time_obj)
            if deadline.date() != task_date:
                print("Deadline must be within the task date (00:00-23:59)")
                continue
            return deadline
        except ValueError:
            print("Invalid time format. Please use HH:MM")

def input_task():
    """输入任务信息"""
    print("enter new task")
    
    task_date = get_valid_date("Please enter the task date: ")
    
    deadline = get_valid_deadline(task_date)
    
    task_content = input("Please enter the task content: ").strip()
    while not task_content:
        print("Task content cannot be empty. Please try again.")
        task_content = input("Please enter the task content: ").strip()
    
    return {
        'date': task_date,
        'content': task_content,
        'deadline': deadline
    }

def display_tasks(tasks):
    """按日期分组，同日期内按截止时间排序"""
    if not tasks:
        print("Don't find tasks.")
        return
    
    grouped_tasks = defaultdict(list)
    for task in tasks:
        grouped_tasks[task['date']].append(task)
    
    sorted_dates = sorted(grouped_tasks.keys())
    
    print("Task list")
    for date in sorted_dates:
        print(f"\n【{date.strftime('%B %d, %Y')}】")
        sorted_tasks = sorted(grouped_tasks[date], key=lambda x: x['deadline'])
        for i, task in enumerate(sorted_tasks, 1):
            print(f"  {i}. Deadline: {task['deadline'].strftime('%H:%M')}")
            print(f"     Content: {task['content']}")

def main():
    tasks = []
    print("Wekcome to use.")
    
    while True:
        print("1. Add new tasks")
        print("2. View all tasks")
        print("3. Exit program")
        
        choice = input("Please select an option (1/2/3): ").strip()
        
        if choice == '1':
            task = input_task()
            tasks.append(task)
            print("Task added successfully!")
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Please select the correct option.")

if __name__ == "__main__":
    main()