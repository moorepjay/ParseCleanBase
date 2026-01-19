LogSnips: Human-in-the-Loop Security Parser

Developed as a high-velocity solution during peak operational seasons to bypass the constraints of proprietary C# risk-tooling. By deploying as a Flask-based internal web service, the tool provided a centralized, zero-install interface for an entire team of agents, reducing manual data entry time when volume was at its highest.

LogSnips is a lightweight, extensible Flask framework designed to bridge the gap between raw, unstructured log data and structured security databases. Originally developed as an efficiency tool to reduce manual copy-pasting in operations, it has evolved into a forensic tool for Security Analysts to parse, review, and categorize network indicators.


📋 General Intended Use

The system operates on a three-stage pipeline designed for Accuracy and Auditability:

1) Ingestion (The Blob): Users paste unformatted text—syslogs, firewall outputs, or email headers—directly into a central processing terminal.

2) Extraction (Regex Engine): The backend utilizes specific Regular Expression (Regex) profiles to "snip" high-value data points (IPs, Usernames, Timestamps) from the noise.

3) Human Verification (The Review): Extracted data is presented in a tabular format. An analyst performs a final manual check, adds qualitative comments, and assigns a status (PASS/FAIL/THREAT) before committing to the database.


🛠 Project Architecture

- Flask Web Server: Manages the routing between ingestion and review screens.

- Regex Processing: Decouples text-cleaning logic from the UI, allowing for swappable "Parsing Profiles."

- MongoDB Backend: Stores every parsed entry with a unique UUID, creating a permanent audit trail of forensic decisions.

- Export Utility: Converts verified database entries into CSV/JSON formats for ingestion into Firewalls or SIEM (Security Information and Event Management) tools.


🛡️ NetSec Development Plan (The Roadmap)

The next evolution of LogSnips focuses on converting the general parser into a dedicated Network Security Incident Response tool.

Phase 1: Forensic Indicator Profiles

- Implement CIDR & IPv6 Detection: Expand the regex library to identify complex IP ranges and IPv6 addresses.

- Port & Protocol Mapping: Automatically categorize traffic based on recognized port numbers (e.g., 22 for SSH, 443 for HTTPS).

- User-Agent Analysis: Add patterns to extract browser and device signatures from web server logs.

Phase 2: Threat Intelligence Integration

- IP Reputation Lookups: Automatically query public blacklists (like VirusTotal or AlienVault) during the parsing phase to provide the human reviewer with "Risk Scores."

- Geo-IP Tagging: Map IP addresses to physical locations to identify suspicious geographic origin.

Phase 3: Automated Blocklist Generation

- Firewall Scripting: Create an export function that generates iptables or Cisco ACL commands based on "FAIL" decisions made during the review process.


