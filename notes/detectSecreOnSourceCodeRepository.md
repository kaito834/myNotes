This documents are noting how to detect secrets like API key on source code repositories.

# Helpful tools
- [gitrob](https://github.com/michenriksen/gitrob)
- [git-secrets](https://github.com/awslabs/git-secrets)
- [truffleHog](https://github.com/dxa4481/truffleHog)
- [repo-supervisor](https://github.com/auth0/repo-supervisor)

## Related Links
- https://www.digitalocean.com/community/tutorials/an-introduction-to-managing-secrets-safely-with-version-control-systems
- https://auth0.engineering/detecting-secrets-in-source-code-bd63b0fe4921
  * "*2017年6月。repo-supervisor. 文字列のエントロピーをもとにsecretのような文字列を検出する。CLIモードだとディレクトリ内を再帰的にスキャンできる。*"
  * Via https://twitter.com/kaito834/status/1016854601188818944

# Notes for Usage
## gitrob
### What type of secrets gitrob can detect
- Files which are secrets by themselves
- Files which may include secrets in usual
  * You can find signatures at [core/signatures.go](https://github.com/michenriksen/gitrob/blob/master/core/signatures.go#L163)

## truffleHog
### Environments
- Windows 10
- Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
- git version 2.10.1.windows.1

### Install
Refer to https://github.com/dxa4481/truffleHog#install
```
pip install truffleHog
```

### Run
Scanning high signal regex checks and entropy checks against my [myNotes](https://github.com/kaito834/myNotes) repo is as following:
```
$ truffleHog --regex --entropy=True https://github.com/kaito834/myNotes.git
~~~~~~~~~~~~~~~~~~~~~
[92mReason: High Entropy[0m
[92mDate: 2018-02-17 22:11:43[0m
[92mHash: 64e493a92713b74da8e58e311628567595ccfc7e[0m
[92mFilepath: snippets/python/copyStrToClipboardByTk.py[0m
[92mBranch: origin/master[0m
[92mCommit: Appended a comment about pyperclip module into this snippet.
[0m
@@ -4,9 +4,6 @@
 # Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

 # This was based on https://gist.github.[93mcom/danielrasmusonsnippet/89fd62037febf465b52b[0m
-#
-# Found useful python module, pyperclip: https://github.com/asweigart/pyperclip
-# According to the github repository, "Python module for cross-platform clipboard functions."
 def copyStrToClipboard():
 #def main():
     from tkinter import Tk

~~~~~~~~~~~~~~~~~~~~~
(snip)
~~~~~~~~~~~~~~~~~~~~~
[92mReason: High Entropy[0m
[92mDate: 2015-07-25 18:51:10[0m
[92mHash: d2d988e69c6c203bce2ffeeffd129615396544a8[0m
[92mFilepath: snippets/python/copyStrToClipboardByTk.py[0m
[92mBranch: origin/master[0m
[92mCommit: Added a snippet to copy string to clipboard on Windows.
[0m
@@ -1,37 +0,0 @@
-#!/usr/bin/env python
-# I tested by Python 3.4.3 on Windows 8.1
-# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
-
-# This was based on https://gist.github.[93mcom/danielrasmusonsnippet/89fd62037febf465b52b[0m
-def copyStrToClipboard():
-#def main():
-    from tkinter import Tk
-
-    r = Tk()
-    r.withdraw()
-    r.clipboard_clear()
-
-    '''
-    According Python issue 23760, I cannot copy to clipboard correctly
-    when r.destory() is called after r.clipboard_append() by Python 3.4.3 on Windows 8.
-    The issue happened to me, so this snippet call input() after r.clipboard_append().
-
-    http://bugs.python.org/issue23760
-    http://stackoverflow.com/questions/26321333/
-    '''
-    str = input("Please input string that be copied to clipboard:\n> ")
-    r.clipboard_append(str)
-    print('[!] Copied "{0}" to clipboard.'.format(str))
-    input('Please enter if you confirmed > ')
-
-    r.destroy()
-
-def main():
-    copyStrToClipboard()
-
-    while input("\nWould you like to retry? (Y/N) > ").upper() == 'Y':
-        print('')
-        copyStrToClipboard()
-
-if __name__ == '__main__':
-    main()

~~~~~~~~~~~~~~~~~~~~~
```

NOTE: truffleHog needs `git` Windows executable file to run. An error was happened if I run truffleHog on Windows command prompt which was not set `git` path.
```
$> truffleHog --regex --entropy=True https://github.com/kaito834/myNotes.git
Traceback (most recent call last):
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\git\cmd.py", line 598, in execute
    **subprocess_kwargs
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\subprocess.py", line 997, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] 指定されたファイルが見つかりません。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Users\kaito\AppData\Local\Programs\Python\Python36-32\Scripts\trufflehog.exe\__main__.py", line 9, in <module>
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\truffleHog\truffleHog.py", line 53, in main
    output = find_strings(args.git_url, args.since_commit, args.max_depth, args.output_json, args.do_regex, do_entropy, surpress_output=False, branch=args.branch)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\truffleHog\truffleHog.py", line 247, in find_strings
    project_path = clone_git_repo(git_url)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\truffleHog\truffleHog.py", line 122, in clone_git_repo
    Repo.clone_from(git_url, project_path)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\git\repo\base.py", line 925, in clone_from
    return cls._clone(git, url, to_path, GitCmdObjectDB, progress, **kwargs)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\git\repo\base.py", line 874, in _clone
    v=True, **add_progress(kwargs, git, progress))
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\git\cmd.py", line 424, in <lambda>
    return lambda *args, **kwargs: self._call_process(name, *args, **kwargs)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\git\cmd.py", line 873, in _call_process
    return self.execute(call, **_kwargs)
  File "c:\users\kaito\appdata\local\programs\python\python36-32\lib\site-packages\git\cmd.py", line 601, in execute
    raise GitCommandNotFound(command, err)
git.exc.GitCommandNotFound: Cmd('git') not found due to: FileNotFoundError('[WinError 2] 指定されたファイルが見つかりません。')
  cmdline: git clone -v https://github.com/kaito834/myNotes.git C:\Users\kaito\AppData\Local\Temp\tmpkcymh80n
```

### What type of secrets truffleHog can detect
- BASE64/Hex strings which entropies are high in commit logs
- Strings which are matched regular expressions defined at [regexes.json on truffleHogRegexes](https://github.com/dxa4481/truffleHogRegexes/blob/master/truffleHogRegexes/regexes.json)

### How truffleHog detects secrets
Refer to https://github.com/dxa4481/truffleHog#how-it-works

Also, I looked through the source code and summarized steps as below:
- `main()`: Parse command line arguments and call `find_strings()` ([Link on the code](https://github.com/dxa4481/truffleHog/blob/master/truffleHog/truffleHog.py#L53))
- `find_strings()`: Clone the target repo into local, and retrieve each commits on each branches
- `find_strings()`: Call `diff_worker()` to search secrets at diff between 2 commits ([Link to the code](https://github.com/dxa4481/truffleHog/blob/master/truffleHog/truffleHog.py#L280-L287))
- `diff_worker()`: Check whether the target diff is text format, and not binary format ([Link on the code](https://github.com/dxa4481/truffleHog/blob/master/truffleHog/truffleHog.py#L219-L221))
- `diff_worker()`: Call `find_entropy()` and/or `regex_check()` based on command line arguments ([Link on the code](https://github.com/dxa4481/truffleHog/blob/master/truffleHog/truffleHog.py#L224-L230))
- `find_entropy()`: Split strings on the target diff by `\n` and white space(s), and generate strings set based on BASE64 encoding and hex ([Link on the code](https://github.com/dxa4481/truffleHog/blob/master/truffleHog/truffleHog.py#L163-L167))
  * Refer to https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split
- `find_entropy()`: Calculate entropy for the 2 strings set by `shannon_entropy()`
- `find_entropy()`: Determine the 2 strings set may be secret(s) if the entropy is bigger than pre-defined value ([Link on the code](https://github.com/dxa4481/truffleHog/blob/master/truffleHog/truffleHog.py#L168-L177))
- `regex_check()`: Find matched strings based on regular expression patterns ([Link on the code](https://github.com/dxa4481/truffleHog/blob/master/truffleHog/truffleHog.py#L198-L202))
- `regex_check()`: Determine the matched strings may be secrets
