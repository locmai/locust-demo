from locust import Locust, TaskSet, task


class UserTaskSet(TaskSet):  # 3
    @task  # 4
    def my_task(self):
        print("executing my_task")


class User(Locust):  # 1
    task_set = UserTaskSet  # 2
    min_wait = 5000
    max_wait = 15000
