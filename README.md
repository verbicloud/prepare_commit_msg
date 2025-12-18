# Prepare commit message
pre-commit hook to prepare the git commit message

## How to use
Create `.pre-commit-config.yaml` with the following lines:
```
repos:
  - repo: https://github.com/verbicloud/prepare_commit_msg
    rev: v0.0.1
    hooks:
    - id: prepare-commit-msg-hook
```

and simply run `$ pre-commit install --hook-type prepare-commit-msg`
