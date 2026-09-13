# Testing and Results

## Controlled Lab Environment

Testing was performed in an isolated virtual lab. The Cowrie honeypot ran on one Kali Linux virtual machine, while a second Kali Linux machine was used to generate controlled test activity.

The purpose of the tests was to verify that the customized honeypot could record interaction with the deceptive environment and that relevant activity could be surfaced through the monitoring and alerting workflow.

## Test Scenarios

### Login attempts

Controlled authentication attempts were generated against the honeypot. Cowrie recorded failed and successful login events, allowing authentication activity to be reviewed in the logs.

### Command activity

Commands were entered through the emulated SSH environment to verify that command input was captured by Cowrie and could be identified by the monitoring workflow.

### Deceptive file interaction

The customized filesystem contained fictional files and credentials intended to make the environment more realistic. Tests included accessing these files and verifying that the resulting activity appeared in the honeypot logs.

### File retrieval activity

Controlled download activity was generated to verify that file-retrieval events could be recorded and detected by the monitoring workflow.

### Real-time notifications

The alerting pipeline was tested by monitoring Cowrie activity and sending relevant event information through a Python component using the Telegram Bot API.

## Evidence Produced During the Project

The dissertation documented evidence including:

- failed login events
- successful login events
- Telegram notifications for login activity
- captured command execution
- file-download activity
- access to deceptive credential files
- the Python alerting component
- the shell log-monitoring component
- the systemd monitoring service
- Telegram notifications triggered by command activity

## Interpretation

The project explored whether adding human-like and deceptive elements could encourage additional interaction with a honeypot and provide richer telemetry for analysis. The controlled tests demonstrated the complete workflow from honeypot interaction to event logging and real-time notification.

This repository does not publish raw experimental logs or private alert data. Public examples are sanitized or synthetic.
