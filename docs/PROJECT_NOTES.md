# Project Notes

This repository is a sanitized reconstruction of a completed Bachelor's cybersecurity project.

## Lab design

The project used a controlled virtual lab with two Kali Linux machines. One hosted Cowrie and the other was used to generate test activity against the honeypot.

## Honeypot customization

The Cowrie environment was customized with a deceptive filesystem containing fictional files and credentials. The filesystem was prepared for Cowrie using its filesystem tooling and configured so the customized environment was loaded by the honeypot.

## Monitoring pipeline

Cowrie activity was written to log files. A shell-based monitoring component watched the log stream for relevant events and passed alert messages to a Python component. The Python component delivered notifications through the Telegram Bot API.

The monitoring workflow covered events such as login attempts, command activity, session closure, and file-download activity.

## Controlled evaluation

The lab evaluation included controlled login attempts, command execution, file retrieval, interaction with deceptive files, log inspection, and verification of real-time notifications.

## Public repository policy

This portfolio version does not contain real API tokens, chat identifiers, personal information, unsanitized logs, or real credentials. Public examples are synthetic or sanitized.
