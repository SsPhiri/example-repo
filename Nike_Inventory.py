Last login: Sun Jun 14 13:42:32 on ttys000
mokgadiphiri@Success-Phiri ~ % pip install tabulate
zsh: command not found: pip
mokgadiphiri@Success-Phiri ~ % python3 -m pip install tabulate
Collecting tabulate
  Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
Installing collected packages: tabulate
Successfully installed tabulate-0.10.0

[notice] A new release of pip is available: 26.0.1 -> 26.1.2
[notice] To update, run: pip3 install --upgrade pip
mokgadiphiri@Success-Phiri ~ % cd mokgadiphiri/ssp-project
cd: no such file or directory: mokgadiphiri/ssp-project
mokgadiphiri@Success-Phiri ~ % ls
Desktop		Github		Library		Pictures	ssp-project
Documents	hello_world.py	Movies		practice.1.py	test.py
Downloads	Level 1		Music		Public
mokgadiphiri@Success-Phiri ~ % ssp-project
zsh: command not found: ssp-project
mokgadiphiri@Success-Phiri ~ % cd ssp-project
mokgadiphiri@Success-Phiri ssp-project % ls
A1		git-task	ifExample	new-projects
file_cd.sh	gitlog.png	ifExample.sh	README.md
mokgadiphiri@Success-Phiri ssp-project % git init
Reinitialized existing Git repository in /Users/mokgadiphiri/ssp-project/.git/
mokgadiphiri@Success-Phiri ssp-project % git add .
warning: adding embedded git repository: git-task
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint: 	git submodule add <url> git-task
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint: 	git rm --cached git-task
hint:
hint: See "git help submodule" for more information.
hint: Disable this message with "git config set advice.addEmbeddedRepo false"
mokgadiphiri@Success-Phiri ssp-project % git rm --cached -r git-task
error: the following file has staged content different from both the
file and the HEAD:
    git-task
(use -f to force removal)
mokgadiphiri@Success-Phiri ssp-project % rm -rf git-task/.git
mokgadiphiri@Success-Phiri ssp-project % git add .
mokgadiphiri@Success-Phiri ssp-project % git commit -m "Fix nested git repo issue and add project files"
[main 60c0706] Fix nested git repo issue and add project files
 7 files changed, 28 insertions(+)
 create mode 100644 .DS_Store
 create mode 100644 A1/.DS_Store
 create mode 100755 file_cd.sh
 create mode 160000 git-task
 create mode 100644 gitlog.png
 create mode 100644 ifExample
 create mode 100755 ifExample.sh
mokgadiphiri@Success-Phiri ssp-project % ls
A1		git-task	ifExample	new-projects
file_cd.sh	gitlog.png	ifExample.sh	README.md
mokgadiphiri@Success-Phiri ssp-project % find . -name "*.py"
./git-task/hello_world.py
mokgadiphiri@Success-Phiri ssp-project % cd ~/ssp-project
mokgadiphiri@Success-Phiri ssp-project % rm -rf git-task
mokgadiphiri@Success-Phiri ssp-project % touch inventory_system.py
mokgadiphiri@Success-Phiri ssp-project % nano inventory_system.py

  UW PICO 5.09               File: inventory_system.py                Modified  

    elif choice == "4":
        re_stock()   
        
    elif choice == "5":
        highest_qty()  
        
    elif choice == "6":
        value_per_item()
        
    elif choice == "7":
        read_shoes_data()
        
    elif choice == "0":
        print("Exiting system... Goodbye!")
        break
        
    else:
        print("Invalid choice. Try again.")
        

^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
