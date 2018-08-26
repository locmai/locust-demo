from locust import HttpLocust, TaskSet, task


class WebSiteUserTasks(TaskSet):
    def setup(self):
        print("Setup of TaskSet")

    def on_start(self):
        print("Locust hatched")

    @task(3)
    def get_index(self):
        self.client.get("/api", name="GET /api")
    
    def on_stop(self):
        print("Locust stopped")

    def teardown(self):
            print("Teardown of TaskSet")

class WebsiteUser(HttpLocust):
    host = "http://localhost:5000"
    min_wait = 2 * 1000
    max_wait = 5 * 1000
    task_set = WebSiteUserTasks

    def setup(self):
        print("Setup of Locust")

    def teardown(self):
        print("Teardown of Locust")
