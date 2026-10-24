# SOP: Batch Job Failure
## Purpose
Resolve failed nightly batch processing jobs and restore data pipeline flow.
## When to Use
An automated monitoring alert triggers, or a user reports missing data/reports for the day.
## Steps
1. Log in to the "DemoPortal" Job Scheduler dashboard.
2. Locate the failed job (e.g., `nightly_sync_job`) and check the error logs.
3. Identify the root cause (e.g., database timeout, file not found, or bad data input).
4. If it is a transient network error, click "Retry Job" in the dashboard.
5. If it fails due to data corruption, isolate the bad records and re-run the job from the last checkpoint.
6. Verify the job completes successfully and check that downstream reports have updated.
7. Update the ticket with the root cause and resolution.
## Escalation
If the job fails twice after a retry, assign the ticket to the L2 team "Data-Engineering" (fake group).
P1 cases (e.g., payroll data failed to process): call on-call lead at ext. 9012 (fake).
## Notes
- Never re-run a job if it partially completed and might cause data duplication. Clean up the target tables first.
- Check for overlapping jobs that might be causing database locks.