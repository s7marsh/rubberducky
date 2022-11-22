# rubberducky
Shakes and quacks when you're bored 🦆

## How to use?
1. **Install** [python](https://www.python.org/downloads) and [PyCharm IDE](https://www.jetbrains.com/pycharm/download/) (choose the Free version)
2. **Download** the code then, place (and extract the zip file) into your desired project folder/directory.
![Get code](/img/00_get_code.png)
3. Open the files in PyCharm
![PyCharm open](/img/01_open_project.png)
> **Trust Project** if prompted.
4. **Add a local interpreter.** Go to File > Settings. On the Settings window, go to Project > Python Interpreter. You need to add a local interpreter.
![Settings window](/img/02_settings_window.png)
The Add Python Interpreter window will pop up:
![Add interpreter](/img/03_python_interpreter.png)
5. **Install the necessary packages.** Back to the Settings window, make sure that the interpreter has been updated. Then click on the *plus* icon to add a python package.
![Add pkg_a](/img/04_install_pkg_a.png)
Wait for the package to be installed successfully:
![success pyautogui](/img/04a_install_complete.png)
Do the same for `pynput`.
![success pynput](/img/04b_install_pkg_b.png)
You should have the following packages installed. Click on Apply then OK.
![package list](/img/04c_pkg_list.png)
6. **Test the script.** Open the `main.py` file and try running the script.
![main py test](/img/05_main_py_test.png)
If you see something like this, it means the script is running
![run log](/img/05a_runlog.png)
Let the code run for some time **WITHOUT** moving the mouse or pressing any key. It is expected that the mouse will move on it own. (shake it duckyyy! 🦆)
To stop the script, press the `stop` button **TWICE**
![stop script](/img/05b_stoprun.png)
You should see in the run log window that the code exited to confirm that the script stopped.
![code exit](/img/05c_code_exit.png)

### Some controls
![controls](/img/06_script_controls.png)
* `min_polling_time` and `max_polling_time` are in seconds. These are used in randomizing the polling time. Smaller values will make checking for activity more often which means the duck will move more often.
* `count_to_ctrl_tab` determines how many idle times/count before pressing the 'Ctrl+Tab' (changes the duck's playground)

### How to run the script in background?
On part 6 of **How to use**. When you test the script, the first line shows you the command to execute the python script. Simply copy that line, put it in a notepad and replace `python.exe` with `pythonw.exe`. Then, copy that whole line and open a command prompt (cmd) and paste it there (by right click) and enter. You can close the command prompt and let the duck shake and quack! 🦆
![run in bg](/img/07_run_in_bg.png)
**To stop the duck from running in background**
Open Task Manager (Ctrl+Shift+Esc). Go to Details Tab and type `pythonw`
![stop in bg](/img/07a_stop_in_bg.png)
Right click on the first `pythonw.exe` then End Task, End Process if prompted.
