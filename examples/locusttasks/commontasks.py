from locust import TaskSet, task


class NormalUserTasks(TaskSet):
    @task
    def get_index(self):
        self.client.get('/api', name="GET /api as Normal User")


class AdminUserTasks(TaskSet):
    @task
    def get_index(self):
        self.client.get('/api', name="GET /api as Admin User")
