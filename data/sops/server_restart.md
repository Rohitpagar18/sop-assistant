# SOP: Server Restart
## Purpose
Safely restart a production server without causing data loss or interrupting critical services.
## When to Use
Server is unresponsive, experiencing a memory leak, or during scheduled maintenance windows.
## Steps
1. Check the server monitoring dashboard to confirm the server is actually down or degraded.
2. Check for active user sessions or running batch jobs on the server.
3. Send a maintenance broadcast to the #general and #support channels announcing a 5-minute downtime.
4. Gracefully shut down the server via the terminal using the `sudo shutdown -h now` command.
5. Wait 60 seconds, then power the server back on via the cloud provider console.
6. Verify that all critical services (web server, database) start automatically.
7. Test system accessibility and close the maintenance ticket.
## Escalation
If the server fails to boot after two attempts, assign the ticket to the L2 team "Infrastructure" (fake group).
P1 cases: call on-call lead at ext. 4321 (fake).
## Notes
- NEVER perform a hard reboot (pulling the plug) unless absolutely necessary.
- Always verify that the latest database backups completed successfully before restarting a database server.