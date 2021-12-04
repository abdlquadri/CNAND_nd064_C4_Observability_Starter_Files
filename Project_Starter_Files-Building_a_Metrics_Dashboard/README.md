**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

![k8s objects](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/k8s-objects.png)

## Setup the Jaeger and Prometheus source
![grafana data sources](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-datasources.png)
![grafana data sources](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-prometheus.png)


## Create a Basic Dashboard
![basic dashboard](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/basic-dashboard.png)

## Describe SLO/SLI

-SLOs
 1. The home page should not exceed 5seconds load time for more than 10 times in a month.
2. The website should be up and running for above 98% of the time in a month.
3. 40x errors should not be more than 1% in a given month.
4. 50x should not be more than 0.05% in a given month.
5. The CPU should be at more than 90% utilisation in a given month.

-SLIs
 1. The website had 95% uptime in the month of November
 2. The home page loads in less than 1s through out the month of November
 3. 40x errors were more than 1% in the month of November
 4. 50x errors where below 0.05% in the month November
 5. The CPU utilization was more than 90% through out the month of Novemeber

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
- Login: This should measure the login error and success rates.
- Sign Up: This should measure the sign up error and success rates.
- Home page load: This should measure the uptime of the home page.
- Error rates:  This should measure 40x and 50x error rates.
- Success rates: This should measure API success rates.

## Create a Dashboard to measure our SLIs
![basic dashboard](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/basic-dashboard.png)

## Tracing our Flask App
![tracing in app](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-span-app-py.png)

## Jaeger in Dashboards
![jaeger dashboard](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-span-dashboard.png)

## Report Error
![jaeger dashboard](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-span-dashboard.png)

TROUBLE TICKET

Name: Abdulquadri Mumuney

Date: 30th, November 2021

Subject: Unexpected Server Errors in Production Application

Affected Area: 

Severity: High

Description: There are noticeable 404 Errors resulting from user action.


## Creating SLIs and SLOs

- SLOs based on Four Golden Signals
1. The latency of the app should not exceed 1ms in any given month.
2. The traffic to each service should not exceed 1000rq/s in any given month.
3. 40x and 50x errors should not be more than 5 in any given month.
4. CPU usage should be above 90% in any given month
 
- SLIs based on Four Golden Signals
1. The latency of the app was below 1ms in the month of November
2. The traffic load to each service was 1000rq/s in the month of November
3. 40x and 50x errors were more than 5 in the month of November
4. Saturation was above 90% in the month of November

## Building KPIs for our plan
1. Increase in monthly revenue based on user signup. 
 - Rationale: If the latency is low and error rates are low, users will be satisfied with the service and keep coming back which directly increase the revenue.

 2. Decrease in infrastructue spending.
  - Rationale: If the CPU per server is well saturated, overalll cost on server spending will go down since redundant servers can be decomissioned.

## Final Dashboard
![final dashboard](https://github.com/abdlquadri/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/kpi-dashboard.png)
