# this is a repo that practices on how to use poetry to build and publish python packages with poetry

## pyproject.toml

pyproject.toml file serves as the configuration file for a Poetry project, containing information about the project and its dependencies. The file has three tables by default:

- tool.poetry

    1. `name, version, description, and authors` being required while others are optional.
    2. Poetry assumes that a package with the same name as the tool.poetry.name specified in the pyproject.toml file is located at the root of the project. But if the package location is different, the packages and their locations can be specified in the `tool.poetry.packages` key.

- tool.poetry.dependencies

    1. declare the Python version for which the package is compatible.

- build-system

    1. `requires` is a list of dependencies required to build the package,
    2. `build-backend` is the Python object used to perform the build process.

## create a virtual env

To create a virtual environment for your library, navigate to your project directory and run the env use command:

```bash
poetry env use /full/path/to/python
```

The /full/path/to/python specifies the full path to the Python executable.

## Configure Project Dependencies

add for project dependencies

```bash
poetry add [name] 
```

add for project test dependencies

```bash
poetry add [name] --group test
```

Once you have installed the requests library, the poetry.lock file will be updated, and to create a requirements.txt file from the poetry.lock file, you can use the following command:

```bash
poetry export --output requirements.txt
```

## tests with pytest

in this example, `pytest.fixture` and `mock_requests` to create a test for validator, after this, we can do

```bash
poetry run pytest -v
```

to test perform the test
