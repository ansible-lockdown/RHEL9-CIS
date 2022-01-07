# Changes to rhel9CIS

## Initial

- based on RHEL8 currently as RH or CIS not GA
- Changes to systctl, auditd, aide cron changes to utilise templates - see issue #1
- Collection statement added to meta/main.yml using only community-general
- aide crontab moved to template due to module change
