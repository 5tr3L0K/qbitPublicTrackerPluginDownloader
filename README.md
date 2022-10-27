# qbitPublicTrackerPluginDownloader
Download all public plugins for QbitTorrent.

## Requirements
- Chocolatey (Windows)
https://chocolatey.org/install
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

## Notes
Use 3.10.8 Python version, not 3.11.
