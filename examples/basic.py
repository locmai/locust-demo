from locust import HttpLocust, TaskSet, task


class WebsiteUserTasks(TaskSet):
    @task(3)
    def get_index(self):
        self.client.get("/api", name="GET /api")

    @task(1)
    def post_index(self):
            payload = {'username': 'locmai'}
            self.client.post("/api",data=payload, name="POST /api")


class WebsiteUser(HttpLocust):
    host = "http://localhost:5000"
    min_wait = 2 * 1000
    max_wait = 5 * 1000
    task_set = WebsiteUserTasks

