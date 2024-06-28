# Product API: FastAPI demo

## Instructions for running the app on localhost

1. Install the dependencies. You have two options:

    a. Creating the virtual environment before installing the dependencies

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

    b. Installing directly.

    ```sh
    pip install -r requirements.txt
    ```

2. Run the application.

```sh
fastapi dev src/main.py
```

## TODO

-   [ ] Refactor adding search function
-   [ ] Unit testing
-   [ ] Workflow for pylint + tests
-   [ ] Deployment
-   [ ] User auth
