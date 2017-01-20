An experiment with Django-channels
==================================

Simple worker-with-feedback.

tl;dr version: provide an interface to control backend workers, where
the entire work is counting up to specified number of seconds, sending
back updates on current second and time as feedback.

Minimal functionality
---------------------

Provide a single web page that exposes a form:

- input: seconds
- submit button

When submitted, the form sends a task to perform the work.  That task
is tied to this particular session; if a task is already pending or
active the page displays task state instead of the form.

Also, the page shows the final update from all tasks executed in
context of its session.


Upgrades
--------

- Handle multi-server setups
- Handle lost tasks

  Introduce a way to "drop" a task.
  Handle dropped tasks by re-sending a task from the frontend.

- IDs

  Let the user specify additional ID as part of URL.  Instead of one
  task per entire session, the user can run one task per each
  combination of (session, ID).

- WebSocket polyfill (SockJS?)
