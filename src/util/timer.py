import time

class Timer:
    
    def __init__(self, message="Process"):
        self.start = time.process_time()
        self.message = message

    def end(self):
        end = time.process_time() - self.start
        print(self.message, "took:", round(end, 2), "(s)")