import random
import time

class Device:

    def generate_data(self):

        return {
            "temperature": random.randint(20,40),
            "humidity": random.randint(30,70),
            "timestamp": time.time()
        }