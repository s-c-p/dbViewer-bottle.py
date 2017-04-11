# Simple MVC with SQLite3, TPL and bottle.py

> this is in continuation to the fs-date-forensics project

All I wanted to do was to look at my SQLite database in nice form and not in terminal so I started writing entire ecosystem in pure python and soon realised the need of, felt the thirst for, a protocol and a server and then finally began appreciating HTTP and WebServer. Thanks to bottle.py and its inbuilt templating system, otherwise I'd have continued writing `detectChanges.py`, `updateHTMfile.py`, etc.

Next I will try to implement this in Flask, then in web.py, then Django

And no javascript used, yay :D

## Usage

```bash
$ py dbReader.py # runs tests in CLI sans server
$ py controller.py # the web-app
```

## Questions

1. is this really MVC?
2. does this qualify as a single-page web-app?

## Todo:

- robust error handling in url as in CLI mode
- the errors.tpl is intentionally left in an immature state, look at `files` portion of code to learn and complete the `errors` part
- use CSS to make tables beautiful
- populate errors table in the database
