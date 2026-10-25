# satat-sandbox

Throwaway repo for testing Satat. Run the tests with `python -m unittest`.

## Satat commands

`.satat/commands.yaml` tells Satat's agent how to work here: `setup` installs the git hooks
(`pre-commit` must be installed) and `test` is the fast test loop. The pre-push hook, configured
in `.pre-commit-config.yaml`, runs `python -m unittest` before every push.
