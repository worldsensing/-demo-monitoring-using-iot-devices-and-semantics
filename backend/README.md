# demo-monitoring-using-iot-devices-and-semantics

## Setup

To have the FastAPI backend running, a database has to be created in the PostgreSQL container, 
to do so:

Open `localhost:5050`. The user and password are the ones that are shown in the `docker-compose.
yml`.

To connect to the postgres database. Click in `Add New Server` and add the following information
in the `Connection` tab:

```bash
Host name/address: postgresdb
Port: 5432
Maintenance database: postgres
Username: postgres
Password: postgres
Role:
Service: