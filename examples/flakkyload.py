from locust import HttpLocust, TaskSet, task


class WebsiteUserTasks(TaskSet):
    
    @task(3)
    def get_flakky(self):
        with self.client.get("/flaky", catch_response=True) as response:
            if 'AWESOME!' not in response.content.decode('ascii'):
                response.failure("Got wrong response.")
            else:
                response.success()
            
class WebsiteUser(HttpLocust):
    host = "http://localhost:5000"
    min_wait = 2 * 1000
    max_wait = 5 * 1000
    task_set = WebsiteUserTasks
