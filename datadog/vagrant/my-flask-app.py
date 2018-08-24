from flask import Flask
import blinker as _                                   # blinker import
from ddtrace import tracer                            # tracer import                      
from ddtrace.contrib.flask import TraceMiddleware     # TraceMiddleWare import
import logging
import sys

# Have flask use stdout as the logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)
c = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c.setFormatter(formatter)
main_logger.addHandler(c)

app = Flask(__name__)

# Create TraceMiddleware object
traced_app = TraceMiddleware(app, tracer, service="my-flask-app", distributed_tracing=False)


@app.route('/')
def api_entry():
    return 'Entrypoint to the Application'

@app.route('/api/apm')
def apm_endpoint():
    return 'Getting APM Started'

@app.route('/api/trace')
def trace_endpoint():
    return 'Posting Traces'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050')
