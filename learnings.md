* The default for StreamHandler is stderr


* This from https://lincolnloop.com/blog/django-logging-right-way/    

**Where to Log**

>_Your app should not be concerned with where its logs go. Instead, it should log everything to the console (stdout/stderr) and let the server decide what to do with it from there. Typically this is put in a dedicated (and logrotated) file, captured by the Systemd journal or Docker, sent to a separate service such as ElasticSearch, or some combination of those. Log storage is a deployment concern, not an application concern. The only thing your app does need to concern itself with is the format of the logs. Typically this is just a string with the relevant data, but if your server already adds a timestamp to the log, you probably want to exclude it from your own formatter. Likewise, if your log aggregator can accept JSON, a formatter like python-json-logger may be more appropriate._

* The above works for a mature API-like module which is called from other extension applications. But my use case is mainly to do with an _Application-level_ logger that is still under active development and also calls other smaller modules along the way -all with least amount of additional code.

* Why don't I just log everything to stderr and write to a log file at the end? This prevents the need to pass a logger object, pre-configured to write to a file. 1) While in development it is easy to forget writing to stderr. 2) Seems like there is no easy command to write stderr to file? (from within IDE like Jupyter)

* Why not have a fixed logging configuration that is imported each time? Well, This config is stored in a central location and not customizable from within the project code, at least not easily. On the flip side, it carries the same issues as passing a logger object around. Only in this case, you are importing it from a central location instead of configuring it on the go.

* bash script.sh | tee -a temp.log
