from flask import Flask, render_template, request

import logging

from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

metrics = PrometheusMetrics(app)
# static information as metric
metrics.info("app_info", "Application info", version="1.0.3")

logging.getLogger("").handlers = []
logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)



def init_tracer(service):

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
        },
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


tracer = init_tracer("frontend")
flask_tracer = FlaskTracing(tracer, True, app)
@app.route("/")
def homepage():
    with tracer.start_span("request-homepage") as homepage_span:
        logger.info(f"Getting homepage.")
        homepage_span.set_tag("http.status_code", 200)
    return render_template("main.html")

@app.route("/error")
def errorpage():
    with tracer.start_span("request-homepage") as homepage_span:
        logger.info(f"Getting homepage.")
        homepage_span.set_tag("http.status_code", 500)
    return "render_template", 500

if __name__ == "__main__":
    app.run()
