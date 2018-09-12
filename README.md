# Validator

This script is meant to test the integrity of a GitHub repository. The script generate the sha256 hashes of a local repo and compare them with the GitHub repo. If everything's match no problem, otherwise the local repo that you got may have been modified in a dangerous way. The goal is to detect malicious code injection.



# Compatibility

This script has been written in Python 3. It has been tested on Linux and MacOS.



# Usage

You can use this verificator just by runnig the script this way :

```shell
python3 verificator.py
```

The script will ask you the url of the GitHub repo (use this format : https://github.com/user/repo-name.git ) and the path to the local repo.

If some modification are detected, the script will prompt the list of the edited files.

You can specify the url and path directly in arguments :

```shell
python3 verificator.py -u url -p path/to/the/local/repo
```



# Improvements

To improve this code, I may add a feature to specify a commit ID. I also may handle all kind of Git repo (not only GitHub). And finally maybe some multithread to improve perfomance on big repos.



# Licence

This code is delivered under [MIT licence](LICENCE).
