The default for StreamHandler is stderr


This from https://lincolnloop.com/blog/django-logging-right-way/    

**Where to Log**

>_Your app should not be concerned with where its logs go. Instead, it should log everything to the console (stdout/stderr) and let the server decide what to do with it from there. Typically this is put in a dedicated (and logrotated) file, captured by the Systemd journal or Docker, sent to a separate service such as ElasticSearch, or some combination of those. Log storage is a deployment concern, not an application concern. The only thing your app does need to concern itself with is the format of the logs. Typically this is just a string with the relevant data, but if your server already adds a timestamp to the log, you probably want to exclude it from your own formatter. Likewise, if your log aggregator can accept JSON, a formatter like python-json-logger may be more appropriate._
