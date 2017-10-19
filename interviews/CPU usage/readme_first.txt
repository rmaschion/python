This is a code challenge from a big virtualization company.

Before the interview I was asked to show I could solve this problem.

The goal of the question is to create and test a simple web app that returns the average CPU usage on a machine.
1 Top-Server
Write an application that samples the CPU usage of all processes on the server (similar to `top'). The sampling frequency
should be one second. In addition, the application should act as a web server and listen on port 8845 for HTTP GET requests.
When it gets a request for /cpu usage, it should return usage for each process. The information should be transmitted using
a suitable data structure represented in JSON format. The server-side component should be written in the language of your
choice.
2 Testing
Write unit tests for the functions/methods used in the Top-Server program. Write functional tests that exercise the HTTP
GET work
ow described above. Finally, write tests to calculate and summarize the following performance characteristics of
the Top-Server running on a particular machine.
Given 5 concurrent client requests running for 5 minutes, print a HTML report that shows:
 average number of requests per second
 average time per response
 total number of requests over 5 minutes

---------------SOLUTION----------
*****REQUIREMENTS:
requests
HTML -> python has html library already installed. HTML should installed from the zip attached.
follow the instructions from readme.txt inside the zip file

******MODULES
cpu_main.py
handles the server side. starts listening localhost and the port 8845 and handles the requests

report.py
creates the reports showing
 average number of requests per second
 average time per response
 total number of requests over 5 minutes

test_httpGet.py
functional test to exercise the HTTP GET

Tests.py
Starts unittest and the server

*****to execute the tests
-call python Tests.py to start services
-call python test_httpGet.py to do the GETs and generate the report.html in the current folder


