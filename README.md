# phantom-devtools
A collection of files to store locally to develop your Splunk Phantom applications and playbooks in your favorite IDE. This enables fun quality-of-life features like linting, tool tips, type casting, and documentation, all within your IDE.

## How To Use

Plase the `phantom` folder inside the working directory for your app or playbook. When creating your tarball package, exclude it from the files:

```powershell
tar --exclude ".\phMy-App\phantom" -czvf ".\phMy-App.tar.gz" ".\phMy-App"
```

## What's Inside

- **action_results.py**: Contains the `ActionResult` class
- **app.py**: Contains the API functions available to phantom apps
- **base_connector.py**: Contains the `BaseConnector` class
- **rules.py**: Contains the API functions available to phantom playbooks
- **vault.py**: Contains the vault API functions and the `Vault` class
