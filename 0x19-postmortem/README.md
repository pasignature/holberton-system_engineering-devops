# 0x19. Postmortem

Friday, June 28, 2019
By the DevOps Team

Earlier this week we experienced a network outage in our Consolidatedalliance website. This incident report is provided to give details of the nature of the outage and our responses.

The outage occurred on Friday, June 28, 2019. We know this outage and downtime issue has impacted our valued developers and users, and we apologize to everyone who was affected.
![alt postmortem humor](https://media-exp1.licdn.com/dms/image/C4D12AQGKdbxtCc8qEQ/article-cover_image-shrink_423_752/0?e=1607558400&v=beta&t=FSaqLVXkxjWnRbjbXb_HAx-qXFwWBVEmzH_vtXb29rU)

### Issue Summary
From 6:26 PM to 7:58 PM WAT, requests to most home page of consolidatedalliance.ng resulted in 404 error response messages. Access to other parts of the website were also affected including the login page and booking manager page. The issue affected 80% of traffic to this API infrastructure. Users could continue to access certain parts of the website where you didnt have to go through the home page. The root cause of this outage was an invalid href attribute configuration change in the header file that exposed a bug in the home page. The href attribute specifies the base URL for all relative URLs on a page. It was wrongly set to localhost instead of consolidatedalliance.ng

Timeline (all times West African Time (WAT))
6:19 PM: header file push begins
6:26 PM: Outage begins
6:26 PM: a customer alerted the support team
7:15 PM: Successful header file configuration change rollback
7:19 PM: Server restarts begin
7:58 PM: 100% of traffic back online

### Root Cause
At 6:19 PM WAT, an invalid href attribute in the header file was inadvertently released to the production environment without first being tested. The change specified an invalid url for the home page. This made the page to point to localhost instead of consolidatedalliance.ng As a result, the homepage became inaccessible which also blocked access to other parts of the site and the downtime began.


### Resolution and recovery
At 6:26 PM WAT, the support team informed the DevOps that a customer called in t ocompalin about inability to access the login page to his profile. By 6:40 PM, the develpers identified the problem and set to work immedaitely.
At 7:15 PM, we attempted to rollback the problematic configuration change and it was sucessful since we had previously detected the issue.
At 7:19, We restarted the server. By 7:58, 100% of traffic was recovered and everything went back to normal.


### Corrective and Preventative Measures
We’ve conducted an internal review and analysis of the outage. The following are actions we are taking to address the causes of the issue and to help prevent recurrence and improve response times:
-we will put measures in place to make sure out DevOps get alerted first before the customer discover any bugs in the future.
-we agreed to implement DataDog APIs to alert the team of any issues.
-we put measures in place to always test any little changes to avoid such occurences.

We appreciate your patience while we reviewed and fixed the issue. Again, we apologize for the inconviniences experienced and the impact to you, your users and your business. We thank you for your business with us.

Sincerely,
The DevOps Team

### See complete blog posts on linkedin below  
1. Incident Report <https://www.linkedin.com/pulse/post-mortem-incident-report-andrew-godwin/>  
2. Incident Report with humor <https://www.linkedin.com/pulse/post-mortem-incident-report-andrew-godwin-1f>


![alt postmortem humor](https://media-exp1.licdn.com/dms/image/C4D12AQG0WS_Eb79o0A/article-inline_image-shrink_1500_2232/0?e=1607558400&v=beta&t=oDJLbml-G3vHCH19Y-gSroCt7l4wQorKlDIFoCiBIL0)
