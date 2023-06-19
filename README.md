__Iris AI Installation Procedure__
***

This document is meant to define all instructions required to help you set up Iris AI on your desktop.
Please follow all instructions carefully for a seamless experience.

`Note: Highly Recommended to set up a new python virtual environment. Please keep all environment related files in the root directory of the project`


Installing Dependencies :
- Run the following command to install all python dependencies. Make sure pip is installed.
```
pip install -r requirements.txt
```
Installing PyAudio on Windows can be quite challenging and often leads to various complications. However, by following the steps provided below, you can effortlessly bypass all of these potential issues using pipwin.

pipwin is a tool by Christoph Gohlke for pip, that helps you install unofficial python package binaries for windows directly from http://www.lfd.uci.edu/~gohlke/pythonlibs/.

To achieve the installation, all you have to do is use these two steps on your terminal while in the activated virtual environment.
```
pip install pipwin
pipwin install pyaudio
```

Go to path *OpenAI_integration/secrets.py* and add your own API key.

If this method doesn't work please refer https://stevemats.medium.com/solved-fix-pyaudio-pip-installation-errors-on-a-win-32-64-bit-operating-system-1efe6cd90c8d
