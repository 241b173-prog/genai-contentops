import random

class IntelligenceAgent:
    def analyze(self, content):
        return {
            "CTR": f"{random.randint(5,15)}%",
            "engagement": random.randint(100, 500)
        }