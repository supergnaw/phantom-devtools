# phantom-devtools
A collection of files to store locally to develop your Splunk Phantom applications and playbooks in your favorite IDE.

## How To Use

Plase the `phantom` folder inside the working directory for your app or playbook. When creating your tarball package, exclude it from the files:

```powershell
tar --exclude ".\phMy-App\phantom" -czvf ".\phMy-App.tar.gz" ".\phMy-App"
```
