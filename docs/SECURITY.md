# Security and Sanitization

This repository is a public portfolio reconstruction of a controlled academic honeypot project.

## Secret handling

Real API tokens, chat identifiers, passwords, and other credentials must never be committed to this repository.

The Telegram alerting component reads configuration from environment variables. `.env.example` contains placeholders only; a real local `.env` file is ignored by Git.

If a credential is ever exposed publicly, deleting it from a later commit is not sufficient. The credential should be revoked or rotated.

## Data handling

Raw honeypot logs can contain source addresses, usernames, attempted passwords, session identifiers, commands, timestamps, and other potentially sensitive information. Raw logs are therefore excluded from the public repository.

Public log examples should use documentation-only network addresses, fictional credentials, and synthetic session identifiers.

## Screenshots

Original academic screenshots are not published automatically. Before a screenshot is added, it should be reviewed for credentials, identifiers, machine/user names, network addresses, paths, and other information that is unnecessary for demonstrating the project.

## Scope

The project and its documented testing were conducted in a controlled virtual lab. Public materials are provided for defensive cybersecurity portfolio and educational purposes.
