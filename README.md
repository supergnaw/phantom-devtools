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

## What is `phantom.json`?

The content of this JSON is the output of the following code ran inside a phantom app:

```python
from phantom import vault
from phantom.vault import Vault
import phantom.app as phantom
import phantom.rules as phanrules
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector


def get_attributes(object: Any) -> dict:
    output = {}
    for o in dir(object):
        if f"{o}".startswith("__"):
            continue

        attr = getattr(object, o)

        if callable(attr):
            try:
                output[f"{o}"] = f"function{inspect.signature(attr)}"
            except:
                output[f"{o}"] = "uninspectable callable"
        else:
            output[f"{o}"] = f"({type(attr)}) {attr}"

    return output


def get_phantom_contents() -> dict:
    input = {
        "phantom.app": phantom,
        "phantom.rules": phanrules,
        "phantom.vault": vault,
        "ActionResult": ActionResult,
        "BaseConnector": BaseConnector,
        "Vault": Vault
    }

    output = {
        "phantom.app": {},
        "phantom.rules": {},
        "BaseConnector": {},
        "ActionResult": {},
        "Vault": {}
    }

    for key, item in input.items():
        output[key] = get_attributes(item)

    return output
```
