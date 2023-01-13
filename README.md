[![circleci](https://circleci.com/gh/routechoices/routechoices-server.svg?style=shield)](https://circleci.com/gh/routechoices/routechoices-server) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/routechoices/routechoices-server/master.svg)](https://results.pre-commit.ci/latest/github/routechoices/routechoices-server/master)


Routechoices server
===================

Server stack for a live GPS tracking solution for orienteering events.

It includes:

  - A frontend for listing events and displaying live and archived events
  - A dashboard for users to manage their events
  - A public API
  - A TCP server for listening to dedicated trackers
  - A WMS server for serving events maps
  - A SSE server to push data from tracker to clients without delay
  - A full-fledged admin interface for owners

This project rely on the Django and the Tornado Web python frameworks.

Hosted at https://www.routechoices.com
