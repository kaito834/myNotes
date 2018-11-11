### My tutorial for GitHub repository
1. [Set up Git](https://help.github.com/articles/set-up-git/)
  - Install "Git for Windows"
  - git config --global user.name "YOUR NAME"
  - git config --global user.email "YOUR EMAIL ADDRESS"
    * `git config --global` modify git global configuration for each users; `~/.gitconfig` or `~/.config/git/config`
      + Refer to https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration
    * You can use different github accounts for each GitHub repositories: `--system`, `--global` or `--local`
      + Refer to https://qiita.com/0084ken/items/f4a8b0fbff135a987fea (in Japanese)
  - Authenticating with GitHub from Git; ssh case is following
2. [Authenticate with GitHub via ssh](https://help.github.com/articles/generating-ssh-keys/)
  - Generate SSH key pair
  - ssh-agent -s; ssh-add ~/.ssh/id_rsa
  - Add SSH public key on GitHub
3. [Create a Repository on GitHub](https://help.github.com/articles/create-a-repo/)
  - Click "_New Repository_"
  - Set repository name and description
  - Select _public_ or _private_; paid accounts can only seletect _private_
  - (Optional) Initialize this repository with a README
  - (Optional) Add .gitignore
  - (Optional) Add a license
4. [Clone a repository to local computer](https://help.github.com/articles/cloning-a-repository/)
  - (ssh) git clone git@github.com:USERNAME/OTHERREPOSITORY.git
  - (https) git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
  - You'd like to understand how git store authentication credentials, see https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage
5. Create or Modify files in repository on local computer
  - Add files or wildcard to [.git/info/exclude](https://help.github.com/articles/ignoring-files/#explicit-repository-excludes) if you would like to ignore those on only local repository.
6. [Add the files to the repository on GitHub](https://help.github.com/articles/adding-a-file-to-a-repository-from-the-command-line/)
  - git add .
  - git commit -m 'First commit'
  - git push origin master
7. Pull commits from GitHub to local if I edit something on GitHub
  - git pull origin master

### GitHub Tips
#### GitHub Personal Access Token
Refer to https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/

#### How to download files under a specific directory on GitHub repository
Run `svn export` against GitHub repository
- Refer to https://qiita.com/raucha/items/1219327df8a9ded494df (in Japanese)

## References
- [BootCamp, GitHub Help](https://help.github.com/categories/bootcamp/)
- [Keeping your email address private, GitHub Help](https://help.github.com/articles/keeping-your-email-address-private/)
- [Adding an existing project to GitHub using the command line, GitHub Help](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
- [Git Cheat Sheets, GitHub Training](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf) ([Japanese](https://training.github.com/kit/downloads/ja/github-git-cheat-sheet.pdf))
- [Good Resources for Learning Git and GitHub, GitHub Help](https://help.github.com/articles/good-resources-for-learning-git-and-github/)
- [入門git](https://www.amazon.co.jp/dp/427406767X), Japanese translation of "[Pragmatic Version Control Using Git](https://pragprog.com/book/tsgit/pragmatic-version-control-using-git)"
