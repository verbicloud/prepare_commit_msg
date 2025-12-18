# Prepare commit message
pre-commit hook to prepare the git commit message

## How to use
Create `.pre-commit-config.yaml` with the following lines:
```
repos:
  - repo: https://github.com/verbicloud/prepare_commit_msg
    rev: v0.0.4
    hooks:
    - id: prepare-commit-msg-hook
```

and simply run `$ pre-commit install --hook-type prepare-commit-msg`

## Development
Modify your .pre-commit-config.yaml to be like this:
```
repos:
  - repo: local
    hooks:
    -   id: prepare-commit-msg
        name: Add commit instructions
        entry: python3 src/prepare_commit_msg/hook.py
        language: python
        stages: [prepare-commit-msg]
        always_run: true
```
