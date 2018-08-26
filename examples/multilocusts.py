from locust import HttpLocust, TaskSet, task
from locusttasks.commontasks import NormalUserTasks, AdminUserTasks


class NormalUser(HttpLocust):
    min_wait = 1 * 1000
    max_wait = 2 * 1000
    task_set = NormalUserTasks
    weight = 1


class AdminUser(HttpLocust):
    min_wait = 1 * 1000
    max_wait = 2 * 1000
    task_set = AdminUserTasks
    weight = 2
