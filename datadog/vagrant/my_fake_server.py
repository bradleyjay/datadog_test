from ddtrace import tracer
import time
import random

while True:
    #with tracer.trace("web.request", service="my_service") as span:
    #    span.set_tag("my_tag", "my_value")
    span = tracer.trace("My_Interval",service="Fake_Serv")
    time.sleep(random.randint(15,25))
    span.finish()
