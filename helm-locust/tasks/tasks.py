from locust import HttpLocust, TaskSet, task


class WebSiteUserTasks(TaskSet):
    @task
    def get_index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    min_wait = 2 * 1000
    max_wait = 5 * 1000
    task_set = WebSiteUserTasks
