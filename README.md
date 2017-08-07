# Bandaudit

Overview
---
This program monitors the bandwidth over the current network and displays 
a graph over the [local host](0.0.0.0:8080) server and port. A PNG of the 
graph is also exported to the project directory. 

This programs runs on MacOS and Linux.

Dependencies
---
* [sivel](https://github.com/sivel/speedtest-cli) `speedtest-cli`
* python `matplotlib`
* python `pandas`

Usage
---
0. `pip install -r requirement.txt`
0. `python log.py`
0. _wait an hour..._
0. `python server.py`

Note
---
There is a cron job running to ensure that the log.py is continually
updated; however, if there are any errors, output is logged. Errors
will likely occur due to a disconnection since the data packets 
are continuously being sent out to the server. The crontab 
sequence used in this project:
`* * * * * cd ~/path/to/this/dir/ && python log.py`

To log error outputs that may occur, append this to the line above:
`>> ~/path/to/dir/errors.txt 2>&1`

This sequence runs `log.py` every minute and outputs the data to
`speeds.log` which is parsed by `plot.py` via a `server.py` run.

To see the progress of `log.py`, you can type `cat speeds.log` 
which will display the data columns. If for some reason, you 
get an error in the program, check `speeds.log` and move to 
the top level directory to see if there are any erroneous 
values from the `log.py` output.

There is an available `hour.log` file which you can use by changing 
the name to `speeds.log`; however, this will be overwritten by the 
program if and once run correctly.

You may ignore `test_server.py`: travis-ci's integration test-script.

TODO
---
* graph display data in real-time and update with crontab
* better fail-safe provisions so `speeds.log` is clean
* graph available to view in cli format
* disconnect server after pytest run

Version
---
1.0.0 | (08/08/17)

License
---
Licensed under the WTFPL - see [LICENSE](./LICENSE) for explicit details.
