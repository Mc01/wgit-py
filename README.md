# wgit.py

Beautiful project manager living in your shell. <br/>
Rewritten in beautiful language.

<br/>

![https://github.com/watchgit-com/wgit-py/blob/master/images/wgit.png](images/wgit.png)

<br/>

## Requirements

Requirements for installation

- python (https://www.python.org)
- pip (https://pip.pypa.io)
- virtualenv (https://virtualenv.pypa.io)

<br/>

## Setup

Installation process

    git clone https://github.com/watchgit-com/wgit-py.git ~/.wgit
    cd ~/.wgit
    bash install.sh
    wgit init

<br/>

## Add current directory to projects

Each project has it's alias and name. <br/>
Alias is the console shortcut to project name.
    
    wgit add {alias} {name}

<br/>

> Example usage:

![https://github.com/watchgit-com/wgit-py/blob/master/images/add.png](images/add.png)

<br/>

## Remove current directory from projects

Keeping project list small and updated is vital. <br/>
Greatly improves the readability and speed of output.

    wgit remove {alias}

<br/>

> Example usage:

![https://github.com/watchgit-com/wgit-py/blob/master/images/remove.png](images/remove.png)

<br/>

## List all projects

Iterating through all projects will list their name and alias. <br/>
Current git branch and shortlist of changes.

    wgit list

<br/>

> Example usage: 

![https://github.com/watchgit-com/wgit-py/blob/master/images/list.png](images/list.png)

<br/>

## Go to directory of project

Jumping directly to project is what it is all about. <br/>
End user just needs the fast and easy way to navigate.

    cd $(wgit go {alias})

<br/>

> Example usage:

![https://github.com/watchgit-com/wgit-py/blob/master/images/go.png](images/go.png)

<br/>

## License

MIT
