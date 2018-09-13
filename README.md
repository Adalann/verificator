# Validator

This script is meant to test the integrity of a GitHub repository. The script generate the sha256 hashes of a local repo and compare them with the GitHub repo. If everything's match, no problem, otherwise the local repo that you got may have been modified in a dangerous way. The goal is to detect malicious code injection.

# Compatibility

This script has been written in Python 3. It has been tested on Linux and MacOS.

# Usage

You can use this verificator just by runnig the script this way :

```shell
python3 verificator.py
```

The script will ask you the url of the GitHub repo (use this format : https://github.com/user/repo-name.git ) and the path to the local repo.

If some modifications are detected, the script will prompt the list of the edited files.

You can specify the url and path directly in arguments :

```shell
python3 verificator.py -u url -p path/to/the/local/repo
```

# Improvements

To improve this code, I may add a feature to specify a commit ID. I also may handle all kind of Git repo (not only GitHub). And finally maybe some multithread to improve perfomance on big repos.

# Licence

This code is delivered under MIT licence.

```
MIT License

Copyright (c) 2018 Théo Martos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


