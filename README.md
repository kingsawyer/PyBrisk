# PyBrisk
This is a simple wrapper over the Brisk API written in Python. Some constants and protocols may have changed. It was written for Python 2.7 but if you want to update it for Python 3.x go for it :-) Pull requests accepted!

The meat.py file contains a sample bot that doesn't play very well. It simply fortifies a random territory and doesn't attack.

The basic idea for your bot is to do something like this

```
loop
  wait for our turn
  if the game is over
    break
  make our moves
  end turn
```
