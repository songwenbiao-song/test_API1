from locust import HttpUser, TaskSet, task
class WebsiteTasks(TaskSet):
    def on_start(self):
        # self.client.post("/login", { "username": "test", "password": "123456" })
        self.client.get("/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456")

    # @task(2)
    def videoCategory(self):
        self.client.get("/videoCategory")

    # @task(1)
    def videoRecommend(self):
        self.client.get("/videoRecommend?id=127398")

    def todayVideo(self):
        self.client.get("/todayVideo")

    def getJoke(self):
        self.client.get("/getJoke?page=1&count=2&type=video")

    def novelSearchApi(self):
        self.client.get("/searchPoetry?name=古风二首%20二")

    tasks = {videoCategory: 2, videoRecommend: 1, todayVideo: 2, getJoke: 3, novelSearchApi: 2}  # 与装饰器效果一致

class WebsiteUser(HttpUser):
    # https://blog.csdn.net/c__chao/article/details/78573737
    # task_set = WebsiteTasks  # Usage of User.task_set is deprecated since version 1.0. Set the tasks attribute instead (tasks = [WebsiteTasks])
    tasks = [WebsiteTasks]
    host = "https://api.apiopen.top"
    min_wait = 1000
    max_wait = 5000