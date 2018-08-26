from locust import HttpLocust, TaskSet, task


def get_index(self):
    self.client.get('/api', name="GET /api")


def post_index(self):
    payload = {"username": "admin", "password": "secret"}
    self.client.post('/api', data=payload, name="POST /api")


class UserTasks(TaskSet):
    tasks = [get_index, post_index]

    @task
    def page404(self):
        self.client.get('/page_not_found')


class WebsiteUser(HttpLocust):
    host = "http://localhost:5000"
    min_wait = 1 * 1000
    max_wait = 2 * 1000
    task_set = UserTasks
