# arkham-bag-simulator
A web-based simulation tool for simulating success probabilties for Arkham Horror: The Card Game.

## Backend
A FastAPI web backend running the simulation in Python.
TODO: Add celery queuing for queries with 5+ "draw_again" tokens.
## Frontend
A Vue (vue-cli) SPA using Highcharts for visualization.

## Database
PostgreSQL database for storing cached runs, and eventually storing users/queues.

## Local Development
`docker-compose -f docker-compose-dev.yml up -d`

## Deployment
`docker-compose up -d`