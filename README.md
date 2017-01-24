An experiment with Django-channels
==================================

Simple worker-with-feedback.

tl;dr version: provide an interface to control backend workers, where
the entire work is counting up to specified number of seconds, sending
back updates on current second and time as feedback.

One non-standard requirement is that I wanted the worker to use a
separate Redis instance just for its request and response queues.
This is not necessary, and in fact `runserver` will run everything
with a single in-memory backend.

To start execute one of:

- `make runserver` -- will start everything in a single process, using
  in-memory backend,
- `make start` -- run as multiple processes (**requires redis and honcho**)


Minimal functionality
---------------------

Provide a single web page that exposes a form:

- input: seconds
- submit button

When submitted, the form sends a task to perform the work.  All
connected browsers receive updates about the state of current task.


Potential upgrades
------------------

- Tie tasks to http sessions (show updates only to the one who sent
  the request)
- Tests
- IDs

  Let the user specify additional ID as part of URL.  Instead of one
  task per entire session, the user can run one task per each
  combination of (session, ID).

- Fall back to long polling
