# wgit.py

Beautiful project manager living in your shell. <br/>
Rewritten in beautiful language.

## Requirements

Requirements for installation

    python (https://www.python.org)
    pip (https://pip.pypa.io)
    virtualenv (https://virtualenv.pypa.io)

## Setup

Installation process

    git clone https://github.com/watchgit-com/wgit-py.git ~/.wgit
    cd ~/.wgit
    bash install.sh
    wgit init
    
## Features

### Add current directory to projects
    
    wgit add {alias} {name}
    Example usage: wgit add flask Flask
    
Each project has it's alias and name. <br/>
Alias is the console shortcut to project name.

### Remove current directory from projects

    wgit remove {alias}
    Example usage: wgit remove flask
    
Keeping project list small and updated is vital. <br/>
Greatly improves the readability and speed of output.
    
### List all projects

    wgit list
    Example output: Flask (flask) master 1 file changed, 4 deletions(-)
    
Iterating through all projects will list their name and alias. <br/>
Current git branch and shortlist of changes.
    
### Go to directory of project

    cd $(wgit go {alias})
    Example usage: cd $(wgit go flask)

Jumping directly to project is what it is all about. <br/>
End user just needs the fast and easy way to navigate.
