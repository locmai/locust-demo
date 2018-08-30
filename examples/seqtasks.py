class NormalUser(TaskSequence):
    @seq_task(1)
    def login_first(self):
        pass

    @seq_task(2)
    @task(25) # You can also set the weight in order to execute the task for `weight` times one after another.
    def then_read_thread(self):
        pass

    @seq_task(3)
    def then_logout(self):
        pass

        