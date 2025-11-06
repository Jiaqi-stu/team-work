
def mark_task_complete(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


if __name__ == "__main__":
    todo_list = [
        {"id": 1, "title": "Meet tutor", "done": False},
        {"id": 2, "title": "Finish group work", "done": False},
    ]

    print("before:", todo_list)
    marked = mark_task_complete(todo_list, 2)
    print("marked:", marked)
    print("after:", todo_list)

