# wgit.py

    Beautiful project manager living in your shell. 
    Rewritten in beautiful language.

## Requirements

    python (https://www.python.org)
    pip (https://pip.pypa.io)
    virtualenv (https://virtualenv.pypa.io)

## Setup

    git clone https://github.com/watchgit-com/wgit-py.git ~/.wgit
    cd ~/.wgit
    bash install.sh
    wgit init
    
## Features

### Add current directory to projects
    
    wgit add {alias} {name}
    Example usage: wgit add flask Flask

### Remove current directory from projects

    wgit remove {alias}
    Example usage: wgit remove flask
    
### List all projects and review their current status

    wgit list
    Example output: Flask (flask) master 1 file changed, 4 deletions(-)
    
### Change working directory to the one from project

    cd $(wgit go {alias})
    Example usage: cd $(wgit go flask)
