from locust import HttpUser, task
import string,random

import warnings 
warnings.filterwarnings("ignore")
# Utterances length
N=20

words=["What","was", "the", "last", "thing", "you" ,"said"]

class HelloWorldUser(HttpUser):
    @task
    def predict(self):
	 # Random utterance
        utterance=" ".join([random.choice(words) for _ in range(N)])
        id=random.randint(0,10000000)
        self.client.post("/parse",json={"text":utterance,"message_id":str(id)},verify=False)


