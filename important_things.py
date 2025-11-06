import datetime
import time
from dataclasses import dataclass, field
from typing import List


@dataclass
class ImportantTask:
    title:str
    deadline:datetime.datetime
    remind_advance:int = 60
    create_time: datetime.datetime = field(default_factory=datetime.datetime.now)

    def get_remind_time(self) -> datetime.datetime:
        return self.deadline - datetime.timedelta(minutes=self.remind_advance)

    def is_remind_time(self) -> bool:
        now = datetime.datetime.now()
        return self.get_remind_time() <= now <= self.deadline

    def __str__(self) -> str:
        return (
            f"[mission] {self.title}\n"
            f"createtime {self.create_time.strftime('%Y-%m-%d %H:%H:%S')}\n"
            f"deadlinetime {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"noticetime {self.get_remind_time().strftime('&Y-%m-%d %H:%M:%S')}\n"
        )

class ImportantNoticeManager:
    def __init__(self):
        self.tasks: List[ImportantTask] = []

    def add_task(self):

    print("\n==== add important mission ====")
    title = input("please enter the title name:")

    while True:
        deadline_str = input("please print the deadlinetime(format: YYYY-MM-DD HH:MM): ")
        try:
            deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            if deadline <= datetime.datetime.now():
                print("deadlinetime can not earlier than right now time, please enter the right time! ")
                continue
            break
        except ValueError:
            print("")
