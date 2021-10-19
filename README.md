# pytest-direnv

A plugin for loading environment variables from a .envrc file when tests are executed.
While running `pytest` from your terminal will likely do this on its own, this plugin is
useful when you are using an external test harness (e.g. the "Testing" panel in Visual
Studio Code).

## External Dependencies
This plugin expects direnv to be installed and configured.  For more information on 
direnv see [direnv.net].

## Usage
simply install this plugin in your pytest-enabled project and you are good to go!
```
pip install pytest-direnv
```
```
poetry add --dev pytest-direnv
```

## Behavior
This plugin hooks into `pytest_load_initial_conftests` so it runs on test startup.  When
loaded, it will use `direnv` in an external shell process to load the `.envrc` file for
your test directory and export any environment variables set in that shell to your test
environment.

Any variables exported by `.envrc` that are already present in your test environment 
will not be overwritten.  Presumably you have set these explicitly in your test runner.
