from locust import HttpUser, task

class SimpleLocustTest(HttpUser):
    @task
    def get(self):
        self.client.get('/')