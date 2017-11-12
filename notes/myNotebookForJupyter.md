This is my notes for [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/index.html).

# Install Jupyter Notebook with venv
## Installed Environment
- Windows 10 Pro
- Python 3.6.3

## Installation Procedures
Update pip to the latest version
```
C:\Users\kaito>pip3 install --upgrade pip
Requirement already up-to-date: pip in c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages
```

Create python virtual environment for Jupyter Notebook by [venv](https://docs.python.org/3/library/venv.html)
```
C:\Users\kaito>python -m venv jupyter-venv
C:\Users\kaito>cd jupyter-venv
C:\Users\kaito\jupyter-venv>.\Scripts\activate.bat
(jupyter-venv) C:\Users\kaito\jupyter-venv>
```

Install Jupyter Notebook in the python virtual environment
```
(jupyter-venv) C:\Users\kaito\jupyter-venv>pip3 install jupyter
Collecting jupyter
  Using cached jupyter-1.0.0-py2.py3-none-any.whl
Collecting notebook (from jupyter)
  Using cached notebook-5.2.1-py2.py3-none-any.whl
Collecting jupyter-console (from jupyter)
  Using cached jupyter_console-5.2.0-py2.py3-none-any.whl
Collecting qtconsole (from jupyter)
  Using cached qtconsole-4.3.1-py2.py3-none-any.whl
Collecting nbconvert (from jupyter)
  Using cached nbconvert-5.3.1-py2.py3-none-any.whl
Collecting ipykernel (from jupyter)
  Using cached ipykernel-4.6.1-py3-none-any.whl
Collecting ipywidgets (from jupyter)
  Using cached ipywidgets-7.0.4-py2.py3-none-any.whl
Collecting traitlets>=4.2.1 (from notebook->jupyter)
  Using cached traitlets-4.3.2-py2.py3-none-any.whl
Collecting ipython-genutils (from notebook->jupyter)
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl
Collecting jinja2 (from notebook->jupyter)
  Using cached Jinja2-2.10-py2.py3-none-any.whl
Collecting jupyter-core (from notebook->jupyter)
  Using cached jupyter_core-4.4.0-py2.py3-none-any.whl
Collecting tornado>=4 (from notebook->jupyter)
  Using cached tornado-4.5.2-cp36-cp36m-win32.whl
Collecting nbformat (from notebook->jupyter)
  Using cached nbformat-4.4.0-py2.py3-none-any.whl
Collecting jupyter-client (from notebook->jupyter)
  Using cached jupyter_client-5.1.0-py2.py3-none-any.whl
Collecting pygments (from jupyter-console->jupyter)
  Using cached Pygments-2.2.0-py2.py3-none-any.whl
Collecting ipython (from jupyter-console->jupyter)
  Using cached ipython-6.2.1-py3-none-any.whl
Collecting prompt-toolkit<2.0.0,>=1.0.0 (from jupyter-console->jupyter)
  Using cached prompt_toolkit-1.0.15-py3-none-any.whl
Collecting bleach (from nbconvert->jupyter)
  Using cached bleach-2.1.1-py2.py3-none-any.whl
Collecting entrypoints>=0.2.2 (from nbconvert->jupyter)
  Using cached entrypoints-0.2.3-py2.py3-none-any.whl
Collecting mistune>=0.7.4 (from nbconvert->jupyter)
  Using cached mistune-0.8.1-py2.py3-none-any.whl
Collecting testpath (from nbconvert->jupyter)
  Using cached testpath-0.3.1-py2.py3-none-any.whl
Collecting pandocfilters>=1.4.1 (from nbconvert->jupyter)
  Using cached pandocfilters-1.4.2.tar.gz
Collecting widgetsnbextension~=3.0.0 (from ipywidgets->jupyter)
  Using cached widgetsnbextension-3.0.7-py2.py3-none-any.whl
Collecting decorator (from traitlets>=4.2.1->notebook->jupyter)
  Using cached decorator-4.1.2-py2.py3-none-any.whl
Collecting six (from traitlets>=4.2.1->notebook->jupyter)
  Using cached six-1.11.0-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from jinja2->notebook->jupyter)
  Using cached MarkupSafe-1.0.tar.gz
Collecting jsonschema!=2.5.0,>=2.4 (from nbformat->notebook->jupyter)
  Using cached jsonschema-2.6.0-py2.py3-none-any.whl
Collecting python-dateutil>=2.1 (from jupyter-client->notebook->jupyter)
  Using cached python_dateutil-2.6.1-py2.py3-none-any.whl
Collecting pyzmq>=13 (from jupyter-client->notebook->jupyter)
  Using cached pyzmq-16.0.3-cp36-cp36m-win32.whl
Collecting simplegeneric>0.8 (from ipython->jupyter-console->jupyter)
  Using cached simplegeneric-0.8.1.zip
Collecting jedi>=0.10 (from ipython->jupyter-console->jupyter)
  Using cached jedi-0.11.0-py2.py3-none-any.whl
Collecting pickleshare (from ipython->jupyter-console->jupyter)
  Using cached pickleshare-0.7.4-py2.py3-none-any.whl
Collecting colorama; sys_platform == "win32" (from ipython->jupyter-console->jupyter)
  Using cached colorama-0.3.9-py2.py3-none-any.whl
Requirement already satisfied: setuptools>=18.5 in c:\users\kaito\jupyter-venv\lib\site-packages (from ipython->jupyter-console->jupyter)
Collecting wcwidth (from prompt-toolkit<2.0.0,>=1.0.0->jupyter-console->jupyter)
  Using cached wcwidth-0.1.7-py2.py3-none-any.whl
Collecting html5lib!=1.0b1,!=1.0b2,!=1.0b3,!=1.0b4,!=1.0b5,!=1.0b6,!=1.0b7,!=1.0b8,>=0.99999999pre (from bleach->nbconvert->jupyter)
  Using cached html5lib-1.0b10-py2.py3-none-any.whl
Collecting parso==0.1.0 (from jedi>=0.10->ipython->jupyter-console->jupyter)
  Using cached parso-0.1.0-py2.py3-none-any.whl
Collecting webencodings (from html5lib!=1.0b1,!=1.0b2,!=1.0b3,!=1.0b4,!=1.0b5,!=1.0b6,!=1.0b7,!=1.0b8,>=0.99999999pre->bleach->nbconvert->jupyter)
  Using cached webencodings-0.5.1-py2.py3-none-any.whl
Installing collected packages: decorator, ipython-genutils, six, traitlets, MarkupSafe, jinja2, jupyter-core, webencodings, html5lib, bleach, pygments, entrypoints, mistune, testpath, pandocfilters, jsonschema, nbformat, nbconvert, tornado, python-dateutil, pyzmq, jupyter-client, simplegeneric, parso, jedi, pickleshare, colorama, wcwidth, prompt-toolkit, ipython, ipykernel, notebook, jupyter-console, qtconsole, widgetsnbextension, ipywidgets, jupyter
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for pandocfilters ... done
  Running setup.py install for simplegeneric ... done
Successfully installed MarkupSafe-1.0 bleach-2.1.1 colorama-0.3.9 decorator-4.1.2 entrypoints-0.2.3 html5lib-1.0b10 ipykernel-4.6.1 ipython-6.2.1 ipython-genutils-0.2.0 ipywidgets-7.0.4 jedi-0.11.0 jinja2-2.10 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.1.0 jupyter-console-5.2.0 jupyter-core-4.4.0 mistune-0.8.1 nbconvert-5.3.1 nbformat-4.4.0 notebook-5.2.1 pandocfilters-1.4.2 parso-0.1.0 pickleshare-0.7.4 prompt-toolkit-1.0.15 pygments-2.2.0 python-dateutil-2.6.1 pyzmq-16.0.3 qtconsole-4.3.1 simplegeneric-0.8.1 six-1.11.0 testpath-0.3.1 tornado-4.5.2 traitlets-4.3.2 wcwidth-0.1.7 webencodings-0.5.1 widgetsnbextension-3.0.7
```

Run Jupyter Notebook
```
(jupyter-venv) C:\Users\kaito\jupyter-venv>jupyter notebook
[I 00:37:05.094 NotebookApp] Serving notebooks from local directory: C:\Users\kaito\jupyter-venv
[I 00:37:05.094 NotebookApp] 0 active kernels
[I 00:37:05.094 NotebookApp] The Jupyter Notebook is running at:
[I 00:37:05.094 NotebookApp] http://localhost:8888/?token=78c877***
[I 00:37:05.110 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 00:37:05.110 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=78c877***
[I 00:37:05.586 NotebookApp] Accepting one-time-token-authenticated connection from ::1
[W 00:37:06.445 NotebookApp] 404 GET /static/components/moment/locale/ja.js?v=20171113003702 (::1) 16.00ms referer=http://localhost:8888/tree
```

## Related Links
- https://jupyter.readthedocs.io/en/latest/install.html
- https://qiita.com/icoxfog417/items/175f69d06f4e590face9 (in Japanese)
- http://ymotongpoo.hatenablog.com/entry/2017/01/29/002039 (in Japanese)
