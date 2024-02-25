# Simple calculator

### python, [FastAPI](https://fastapi.tiangolo.com/)

\
Backend:
- endpoint - get calculator html page,
- endpoint - get solution in response to task,  
- endpoint - get help text,
- endpoint - get user session id,
- session marking middleware.

\
Frontend:
- button clicks handler,
- the solution request,
- the hint text request,
- the session id request,
- saving the state through localStorage.


## Interfaces

- Сalculator http://127.0.0.1:8000
- API documentation http://127.0.0.1:8000/docs

## Launching in Docker

Create and start container:
```bash
$ docker-compose up
```
Stop lifted containers:
```bash
$ docker-compose stop
```
Start stopped containers:
```bash
$ docker-compose start
```
Stop and delete containers and network:
```bash
$ docker-compose down
```
Remove app image:
```bash
$ docker rmi calculator_api
```
