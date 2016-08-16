# make50

A clang error message parser that accompanies official error messages with "friendlier" interpretations. Meant to help beginning C programmers, especially students in weeks 1 - 3 in [CS50](https://www.edx.org/course/introduction-computer-science-harvardx-cs50x)

Built by Annie Chen and Brian Yu at OS Hacks 2016.

# Usage

###### NOTE: make50 (and the below instructions) were created to be run on CS50 IDE, a specific Cloud9 template. Find more information [HERE](https://cs50.readme.io/)

## For Students

Download the two files you need to run make50 by executing the following commands in your terminal 

```
cd ~/workspace
```
to ensure you're in your workspace directory

```
wget https://raw.githubusercontent.com/annieechen/make50/master/make50?token=APPLIqNTOF_xy077OVj4DbkiE1qjgICwks5Xu5dYwA%3D%3D
```
to download make50

```
wget https://raw.githubusercontent.com/annieechen/make50/master/errors.json?token=APPLIoOk914990ABasIDtqBIDDCfXmcRks5Xu5e1wA%3D%3D
```
to download errors.json
```
./make50 <program>
```
to compile a program in the workspace directory. For instance, if you have 'hello.c' in your workspace directory, you can run 

```
./make50 hello
```
to compile it.

### For Long Term Use

If you're doing more than just playing with make50 (AKA actually using it to compile programs), you can execute the below so that you can run make50 from within any directory.

```
cd ~/workspace
```
to ensure you're within the workspace directory

```
echo "export PATH=$PATH:~/workspace/" >> /home/ubuntu/.bashrc
```
to add the line "export PATH=$PATH:~/workspace/" to your .bashrc file. This permanently sets the PATH environmental variable so that your terminal knows where to look for the make50 file. 

NOTE: don't run the above command more than once, because each time you're adding a line to the end of the .bashrc file. You can open the .bashrc file in cloud9 by running

```
cd
``` 
to switch to /home/ubuntu

```
c9 open .bashrc
```
to open the actual file.

Then, restart your terminal by closing all open terminals (by clicking the x at the right of the tab), and then opening a new one (by clicking the green + at the bottom of the screen)

Afterwards, you can run make50 from within any directory by running
```
make50 <program>
```

For instance, if you're trying to compile hello.c, ensure that hello.c is within your current directory by running

```
ls
``` 
and making sure hello.c is displayed. 

Then, compile hello by running
```
make50 hello
```

