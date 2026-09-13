# Testing and Results

## Controlled Lab Environment

Testing was performed in an isolated virtual lab. The Cowrie honeypot ran on one Kali Linux virtual machine, while a second Kali Linux virtual machine generated controlled test activity.

The tests examined whether the customized environment captured the expected interaction data and whether relevant events could pass through the monitoring and Telegram-alert workflow.

## Documented Test Scenarios

### Authentication activity

Controlled login attempts were generated against the honeypot. The dissertation records both failed and successful authentication events in Cowrie logs and documents a Telegram notification associated with login activity.

### Command activity

After connecting to the emulated environment, commands including `ls`, `cat`, `wget`, and `ps` were used during testing. Cowrie recorded command activity using `cowrie.command.input` events.

### Deceptive file interaction

Fictional files were intentionally placed in the customized Cowrie filesystem. The documented tests included reading deceptive credential-style files and observing the resulting interaction.

### Controlled file retrieval

The experiments included `wget` activity. Cowrie recorded the command and simulated the download within the honeypot environment.

### Real-time notifications

The monitoring implementation connected Cowrie log activity to a Python Telegram notification component. The dissertation documents real-time notifications for relevant events during the controlled experiments.

## Evidence Documented in the Dissertation

The original dissertation includes screenshots or examples showing:

- failed login logging
- successful login logging
- a Telegram login alert
- command-input logging
- a simulated download through `wget`
- access to deceptive credential files
- the Python Telegram alerting script
- the Bash log-monitoring script
- the systemd service configuration
- Telegram notifications produced during command activity

## Interpretation

The research investigated whether human-like and deceptive elements could make the honeypot environment more realistic and encourage useful interaction for analysis. The documented tests verify the technical workflow from interaction, to Cowrie logging, to monitoring, to real-time notification.

The public repository does **not** treat the reconstructed sample events as original experimental measurements and does not claim a quantified improvement in attacker engagement unless supported by the original study data.

Raw experimental logs and private alert data are not published here. Public examples are sanitized or synthetic.
