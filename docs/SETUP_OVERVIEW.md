# Lab Setup Overview

This document summarizes the environment used for the academic project. It is intended as portfolio documentation rather than a production deployment guide.

## Environment

The project used two Kali Linux virtual machines in a controlled lab:

- **Honeypot VM** — hosted the Cowrie SSH/Telnet honeypot and customized deceptive environment.
- **Test VM** — generated controlled interactions used to evaluate logging and alerting behaviour.

## Cowrie Environment

Cowrie provided the emulated SSH/Telnet environment. The default environment was customized with a deceptive filesystem containing fictional files and credentials.

The customized filesystem was prepared for Cowrie using its filesystem tooling. During development, the Cowrie configuration was adjusted so the intended customized filesystem was loaded correctly.

## Logging and Analysis

Cowrie logs were monitored during the experiments. JSON-formatted event data could also be filtered during analysis to inspect specific event types such as command input.

## Alerting

The academic implementation connected log monitoring to a Python notification component. Relevant events could generate Telegram notifications, providing a simple real-time monitoring mechanism.

A systemd service was used so the monitoring component could start automatically with the system.

## Safety

All attack simulations described in this repository refer to controlled experiments conducted in the lab environment. The public repository contains sanitized or synthetic examples and no active credentials.
