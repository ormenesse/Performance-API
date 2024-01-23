/home/ormenesse/anaconda3/bin/locust -f locustfile.py -u 256 -r 1 -t 10m --headless --print-stats --host=http://localhost:8081 -L DEBUG --logfile ./tests/port8081.log --html ./tests/port8081.html
/home/ormenesse/anaconda3/bin/locust -f locustfile.py -u 256 -r 1 -t 10m --headless --print-stats --host=http://localhost:8082 -L DEBUG --logfile ./tests/port8082.log --html ./tests/port8082.html
/home/ormenesse/anaconda3/bin/locust -f locustfile.py -u 256 -r 1 -t 10m --headless --print-stats --host=http://localhost:8083 -L DEBUG --logfile ./tests/port8083.log --html ./tests/port8083.html
/home/ormenesse/anaconda3/bin/locust -f locustfile.py -u 256 -r 1 -t 10m --headless --print-stats --host=http://localhost:8084 -L DEBUG --logfile ./tests/port8084.log --html ./tests/port8084.html
