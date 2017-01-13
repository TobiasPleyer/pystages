#!/usr/bin/env/python
import sys
import configparser
from subprocess import call, Popen
from colorama import init as init_colorama, deinit as deinit_colorama, Fore
from colorama.ansi import clear_screen
from os import environ, getcwd, remove
from os.path import join
from datetime import datetime
from contextlib import contextmanager


class Runner(object):
    def __init__(self, cfile, vars={}, heading=""):
        self.CLS = clear_screen()
        self.OK = 0
        self.NOK = 1
        self.vars = vars
        self.heading = heading
        self.progress_template = "     {stage:<69}    [{result}]\n"
        self.config = configparser.ConfigParser(allow_no_value=True, interpolation=configparser.ExtendedInterpolation(), defaults=vars)
        self.config.read(cfile)

    def make_yellow(self, text):
        return (Fore.YELLOW + text + Fore.RESET)
        
    def make_red(self, text):
        return (Fore.RED + text + Fore.RESET)
        
    def make_green(self, text):
        return (Fore.GREEN + text + Fore.RESET)
        
    def show_status(self, progress, current, todo, message):
        print(self.CLS)
        status = ""
        if progress:
            status += progress
        if current:
            name = current["short"]
            status += " --> {:<75}\n".format(name)
        for item in todo:
            name = item["short"]
            status += "     {:<75}\n".format(name)
        print(status)
        # If the current stage hasn't completed, this message holds info for the user
        if message:
            print(message)
            
    def query_input(self, current):
        action = input("[(R)un/(d)one/(f)ail/(i)nfo/(s)kip/(c)ancel/(o)pen/(h)elp]? ").upper()
        result = ()
        if action == "":
            action = "RUN"
        if action in ["D", "DONE"]:
            result = (self.OK, self.progress_template.format(stage=current["short"], result=self.make_green('DONE')))
        elif action in ["F", "FAIL"]:
            result = (self.OK, self.progress_template.format(stage=current["short"], result=self.make_red('FAIL')))
        elif action in ["R", "RUN"]:
            success = False
            run = current.get('run', None)
            if run:
                ret = call(run, shell=True, stdout=self.fd_stdout , stderr=self.fd_stderr)
                success = (ret == 0)
                if success:
                    result = (self.OK, self.progress_template.format(stage=current["short"], result=self.make_green('DONE')))
                else:
                    result = (self.OK, self.progress_template.format(stage=current["short"], result=self.make_red('FAIL')))
            else:
                result = (self.NOK, self.make_red("No run command found! Manual work necessary.\n"))
        elif action in ["I", "INFO"]:
            info = current.get('info', "No info available")
            result = (self.NOK, self.make_yellow('\n' + info + '\n'))
        elif action in ["C", "CANCEL"]:
            sys.exit(0)
        elif action in ["S", "SKIP"]:
            result = (self.OK, self.progress_template.format(stage=current["short"], result=self.make_yellow('SKIP')))
        elif action in ["O", "OPEN"]:
            script = current.get('script', None)
            if script:
                Popen(['notepad', script]) # Use Popen to make the call non-blocking
                result = (self.NOK, "")
            else:
                result = (self.NOK, self.make_red("No file associated with this stage!\n"))
        elif action in ["H", "HELP"]:
            result = (self.NOK, self.make_yellow(self.help))
        else:
            result = (self.NOK, self.make_red("Unknown command!\n"))
        return result
        
    @contextmanager    
    def colors(self):
        """
        Very simple context manager.
        Entry: initialize colorama -> wrapped stdout for colored output
        Exit: Revert stdout wrapping -> initial state reinstantiated
        @contextmanager makes sure that deinit_colorama is called even if an exception is raised
        """
        init_colorama()
        yield
        deinit_colorama()

    def run(self):
        with self.colors():
            config = self.config
            try:
                stages = config['STAGES']
            except KeyError:
                print(make_red("No stage definitions found in config file! Aborting!"))
                sys.exit(1)

            # Local status tracking variables
            progress, current, message, todo = self.heading, "", "", []

            for stage in stages.keys():
                if stage in self.vars:
                    break # we have reached the defaults dictionary
                try:
                    stage_data = config[stage]
                except KeyError:
                    stage_data = {}
                if not "short" in stage_data:
                    stage_data["short"] = stage # This will be the one line description displayed
                todo.append(stage_data)
            
            next = True
            while todo:
                if next:
                    current, todo = todo[0], todo[1:]
                self.show_status(progress, current, todo, message)
                (status, result) = self.query_input(current)
                if status == self.OK:
                    progress += result
                    message = ""
                    next = True
                else:
                    message = result
                    next = False
            self.show_status(progress, "", todo, message)
            print(self.make_green("\nFinished all stages.\n"))
        
if __name__ == '__main__':
    r = Runner('C:/Git/HmiUtility/Delivery/Test_freeze.ini', heading="Test\n")
    r.run()