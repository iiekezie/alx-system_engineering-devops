# Postmortem Report

## 504 Error While Accessing URL

<p align="center">
<img src="https://raw.githubusercontent.com/MitaliSengupta/holberton-system_engineering-devops/master/0x19-postmortem/image.gif" width="100%" height="100%" />
</p>

### Incident Report: [504 Error / Site Outage](https://github.com/MitaliSengupta/holberton-system_engineering-devops/tree/master/0x17-web_stack_debugging_3)

#### Summary

On September 11th, 2018, at 00:00 PST, the server experienced downtime, causing a 504 error for users attempting to access the website. The server in question runs on a LAMP stack (Linux, Apache, MySQL, PHP).

#### Timeline

- **00:00 PST** - 504 error occurs, blocking access to the website.
- **00:05 PST** - Confirmed that Apache and MySQL services are active.
- **00:10 PST** - Despite services running, the website fails to load properly. Background checks indicate the server and database are functioning as expected.
- **00:12 PST** - Restarting Apache resolves the issue temporarily, returning a 200 status code when the site is accessed via cURL.
- **00:18 PST** - Error logs are reviewed to identify the root cause of the outage.
- **00:25 PST** - Found that the Apache server was being shut down prematurely; however, no PHP error logs were available.
- **00:30 PST** - Discovered that PHP error logging was disabled in `php.ini`. Enabled error logging.
- **00:32 PST** - Restarted Apache and reviewed the PHP error logs.
- **00:36 PST** - Error logs revealed a mistyped file name in the code, causing Apache to crash prematurely.
- **00:38 PST** - Corrected the file name and restarted Apache.
- **00:40 PST** - The server was restored to normal functionality, and the website was accessible again.

#### Root Cause and Resolution

The root cause of the issue was a misspelled file name in the `wp-settings.php` file, which referenced a `.phpp` extension instead of `.php`. This error caused the server to throw a 500 error during cURL requests. Initial log reviews provided little insight due to disabled PHP error logging. After enabling error logging in `php.ini` and restarting the server, the PHP logs revealed the incorrect file extension. Correcting the typo resolved the issue. This was rectified on one server, and the fix was subsequently applied to other servers using Puppet for configuration management. After deploying the corrected code, all servers resumed normal operations.

#### Corrective and Preventive Measures

- Ensure that error logging is always enabled across all servers to streamline troubleshooting during outages.
- Thoroughly test all changes in a local environment before deploying to production servers, especially in a multi-server setup. This reduces the risk of issues occurring in live environments, minimizing downtime.

