"""
*===================================================================
* sample code
*===================================================================
"""
from invoke import task


@task
def pylint(c):
    c.run("pylint app tests")


@task
def flake8(c):
    c.run("flake8 app tests")


@task
def tests(c, test_path="tests", verbosity="", pty=True):
    c.run(
        f"PYTHONPATH=$PYTHONPATH:./app pytest {test_path} {verbosity} ", pty=pty)
    # f"PYTHONPATH=$PYTHONPATH:./app pytest {test_path} {verbosity} --cov=app --cov-report=html --cov-report=term --disable-pytest-warnings", pty=pty)
