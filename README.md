# notable_health_api

This is the source code for Notable Health's take-home assignment.

## Requirements

The program was written with the assumption of running on Python 3.9. Some features may not work with older or newer Python versions. For example, Uvicorn install fails for Python3.6 or under.

## How to run

1. Virtual Environment Setup

Using virtual environment is recommended. You can set up a virtualenv and activate it by using the following commands. Make sure that the command `python` starts Python 3.9 to avoid any potential error.

```
$ python -m venv venv
$ source venv/bin/activate
```

2. Install packages

Install packages in `requirements.txt` using the following command.

```
$ (venv) pip install -r requirements.txt
```

I used [FastAPI](https://fastapi.tiangolo.com/) as the REST API framework and [Uvicorn](https://www.uvicorn.org/) as the ASGI server.

3. (Optional) Set up CORS Middleware

If you are calling the backend endpoints from a client running on localhost, add the address (e.g. http://localhost:4200) to `origins` in [main.py](./main.py)

4. Run server

Run the backend server using the following command. The default port is `8000`, but if it is already occupied, it will print another port it is using.

```
$ (venv) uvicorn main:app --reload
```

You can access the Swagger UI API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) after running the server.

## Notes

- Initial list of doctors can be found in [data/initial_data.py](./data/initial_data.py)

- All the data is stored in memory. [db/memory_db.py](./db/memory_db.py) is a class to emulate queries.
