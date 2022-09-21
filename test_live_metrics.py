import time
import random
import dvc.api
from dvclive import Live

params = dvc.api.params_show()

live = Live()

time.sleep(5)

for i in range(params["epochs"]):
    live.log("foo", i + random.random())
    live.log("bar", i + random.random())
    live.next_step()

    time.sleep(5)

time.sleep(5)

live.end()
