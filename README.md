# Adaptive Honeypot System

**Bachelor's Thesis Project — BSc Cybersecurity and Networks, 2025**

A cybersecurity research project exploring a Cowrie SSH/Telnet honeypot enhanced with human-like deception, attack monitoring, and real-time Telegram alerts.

## Overview

This project was developed as a final-year Bachelor's dissertation. The aim was to investigate whether adding more realistic, human-like behaviour to a honeypot could increase attacker interaction and produce richer security data.

The system was built in a controlled lab environment using two Kali Linux virtual machines. One machine hosted a customized Cowrie honeypot, while the second was used to perform controlled attack simulations.

The honeypot included a deceptive filesystem, fictional credentials and files, simulated activity, automated log monitoring, and real-time administrator notifications.

## Key Features

- Cowrie SSH/Telnet honeypot deployed in a controlled Kali Linux environment
- Customized deceptive filesystem with fictional files and credentials
- Human-like and scripted interactions designed to improve realism
- Monitoring of login attempts, commands, user input, session activity, and download attempts
- Python-based Telegram alert integration
- Bash-based real-time Cowrie log monitoring
- systemd service for automatic monitoring on startup
- JSON log analysis using `jq`
- Controlled testing of brute-force attempts, command execution, and file retrieval

## Architecture

```text
Attacker / Test VM
        |
        | SSH
        v
+-------------------+
|  Cowrie Honeypot  |
|  Deceptive Shell  |
+---------+---------+
          |
          | Cowrie logs
          v
+-------------------+
| Log Monitoring    |
+---------+---------+
          |
          v
+-------------------+
| Python Alerting   |
+---------+---------+
          |
          | Telegram Bot API
          v
+-------------------+
| Real-time Alert   |
+-------------------+
```

## Documentation

- [Project Notes](docs/PROJECT_NOTES.md) — design and implementation summary
- [Lab Setup Overview](docs/SETUP_OVERVIEW.md) — controlled environment and project components
- [Testing and Results](docs/TESTING_AND_RESULTS.md) — evaluation scenarios and evidence produced

## Repository Structure

```text
adaptive-honeypot-system/
├── README.md
├── .gitignore
├── .env.example
├── src/
│   └── send_alerts.py
├── systemd/
│   └── watchlog.service
├── honeypot/
│   └── example_fake_files/
├── samples/
│   └── sanitized_cowrie_event.json
└── docs/
    ├── PROJECT_NOTES.md
    ├── SETUP_OVERVIEW.md
    └── TESTING_AND_RESULTS.md
```

## Academic Context

This repository is a cleaned and sanitized portfolio version of a 2025 Bachelor's dissertation project in Cybersecurity and Networks. The original research investigated the use of more human-like behaviour in honeypot environments and evaluated the resulting interaction through controlled experiments and Cowrie log analysis.

The experiments included simulated brute-force login attempts, command execution, and file retrieval. The project also evaluated a real-time alerting pipeline that connected Cowrie log events to Telegram notifications.

## Security & Privacy

This public repository intentionally excludes real credentials, API tokens, personal identifiers, and unsanitized logs. Example credentials and events included here are fictional or sanitized for demonstration purposes.

## Technologies

Python · Bash · Cowrie · Kali Linux · Linux · systemd · Telegram Bot API · JSON · jq · VirtualBox

## Status

The original academic project was completed in 2025. This repository preserves a sanitized version of the implementation for portfolio and educational purposes.
