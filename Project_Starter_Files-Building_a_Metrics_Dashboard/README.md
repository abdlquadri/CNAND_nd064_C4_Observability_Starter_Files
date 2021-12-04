**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
- Please see _answer-img_ directory.

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
- Please see _answer-img_ directory.

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
- Please see _answer-img_ directory.

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
- The home page should not exceed 5seconds load time for more than 10 times in a month.
- The website should be up and running for above 98% of the time in a month.
- 40x errors should not be more than 1% in a given month.
- 50x should not be more than 0.05% in a given month.
- The CPU should be at more than 90% utilisation in a given month.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
- Login: This should measure the login error and success rates.
- Sign Up: This should measure the sign up error and success rates.
- Home page load: This should measure the uptime of the home page.
- Error rates:  This should measure 40x and 50x error rates.
- Success rates: This should measure API success rates.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
- Please see _answer-img_ directory.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.
- Please see _answer-img_ directory.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
- Please see _answer-img_ directory.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.
- Please see _answer-img_ directory.

TROUBLE TICKET

Name: Abdulquadri Mumuney

Date: 30th, November 2021

Subject: Unexpected Server Errors in Production Application

Affected Area: 

Severity: High

Description: There are noticeable 404 Errors resulting from user action.


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.
- The home page should not exceed 5seconds load time for more than 10 times in a month.
- The website should be up and running for above 99.95% of the time in a month.
- 40x errors should not be more than 0.05% in a given month.
- 50x should not be more than 0.05% in a given month.
- The CPU should be at more than 90% utilisation in a given month.

## Building KPIs for our plan
99% CPU Uptime
99% Latency


## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
- Please see _answer-img_ directory.
