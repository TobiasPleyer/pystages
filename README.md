Stages
======

Overview
--------
*Stages* is a very basic tool to run independent stages (i.e. scripts and commands) sequentially. Each stage represents some task to be carried out. The stages and the order in which they should be run is managed in a config file. The syntax of that config file is that of Windows .ini files. The ConfigParser standard library module is used internally to parse these files.

For whom?
---------
*Stages* is a very basic and simplistic version of a pipeline process. It is intended for people that need to run a bunch of sequential steps, but for whom other more sophisticated tools like [Jenkins](https://jenkins.io/index.html "Jenkin's Homepage") would be overkill.
A nice feature of *stages* is the fact that each stage doesn't necessarily have to be associated with a runnable command or alike, instead it can serve just as a placeholder for a manual step. In this way it is a very nice first starting point if your current process is a wild mix of automated and manual tasks. *Stages* interprets its configuration as a todo list, visiting all todo items in the order they have been defined. The user can decide what to do at each stage (e.g. choosing to skip it or mark it as done if it is a manual step).

Usage
-----
```python
>>> from stages import Runner
>>> runner = Runner("config_file", heading="Hello world example")
>>> runner.run()

```

Example configuration
---------------------
```
[env]
greeting: Hello world.
goodbye: See you!

[STAGES]
greet
goodbye

[greet]
info: Simply print a greeting phrase to stdout
run: echo ${env:greeting}

[goodbye]
info: Prints the goodbye phrase to stdout
run: echo ${env:goodbye}
```

Description
-----------
The above example already shows the two key points about *stages*
### The *STAGES* section
This is the key component of every *stages* configuration file. Every line specifies the name of one stage to be executed. The order of the stages will be the line order. We don't assign a value to the stages, each line is just a reference to a stage that can be defined somewhere else in the document.

### The *env* section
This section holds global data that can be used everywhere else in the document. If we want to reference the value **v** of the global variable with the name **n**, then we can do so using the following syntax: ${**env**:**n**}. The value of this expression will be substituted before further interpretation of the command.

These two sections are the basis of every *stages* script. The *stages* program will run through each defined stage and query the user what to do. In order to give the user more options, the stages need to have items connected to them. The follwoing is the list of all supported items
* **run**: This item defines the command that has to be executed. The given string will be executed in a shell
* **short**: This text will be displayed in the todo list
* **info**: Everything written here will be printed to the screen when the user requests further help.
* **script**: This item allows to associate a file with this stage, most likly the one that will be execued with the *run* item. This allows the user to quick open the file and edit it before execution, or just have a look at what it's doing.
