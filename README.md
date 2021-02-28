# AirBnB Clone - The Console
The console is the first part of the AirBnB project.

#### Functionalities of this command interpreter:
* Create a new object
* Read an object
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [Examples of use](#examples-of-use)
* [Authors](#authors)
* [License](#license)

## Environment
This project was created/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/Ramsteven/AirBnB_clone.gitt"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb: `./console` and enter command

## Example
You can start in two Modes:

Interactiva Mode:
you need execute the file console.py, and then you can use the command help and you know the commands.

So if you wnat creat new intance like User, Place, Review, State
`$ ./console.py`

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show

Undocumented commands:
======================
update

(hbnb) help all
Prints all string representation of all
        instances based or not on the class name
(hbnb) help create
Creates a new instance of the class

(hbnb) help destroy
Deletes an instance based on the class name and id

```

====== NOW WE ARE USE THE COMMANDS ======

```

```

None interactive Mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

##



## Bugs
No known bugs at this time. 

## Authors
David Ramirez - [Github](https://github.com/Ramsteven)
Ruben Oliveros - [Github](https://github.com/rubenoliveros)

## License
Public Domain. No copy write protection.
