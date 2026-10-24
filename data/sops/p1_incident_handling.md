# SOP: P1 Incident Handling
## Purpose
Manage critical system outages to minimize downtime and ensure rapid communication.
## When to Use
When a core system (e.g., DemoPortal, database) is entirely down, or a major feature is unavailable for all users.
## Steps
1. Acknowledge the alert in the monitoring system within 5 minutes.
2. Open a "War Room" bridge call and post the link in the #incidents channel.
3. Notify key stakeholders (Product, Support, Management) that a P1 incident is underway.
4. Assign a "Communications Lead" to provide updates every 15 minutes.
5. Triage the issue: check system health, recent deployments, and error logs.
6. Mitigate the issue (e.g., rollback recent deployment, restart server, failover to backup).
7. Once resolved, provide a final status update and schedule a post-mortem.
## Escalation
If the root cause cannot be found within 15 minutes, call the on-call lead at ext. 56789 (fake).
## Notes
- Communication is more important than immediate root cause analysis. Keep users informed.
- Do not make code changes during a P1 unless it is to roll back a recent breaking change.