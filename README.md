# ChillBoss

[![Downloads](https://static.pepy.tech/personalized-badge/chillboss?period=total&units=international_system&left_color=blue&right_color=green&left_text=Total%20Downloads)](https://pepy.tech/project/chillboss)
[![Downloads](https://static.pepy.tech/personalized-badge/chillboss?period=month&units=international_system&left_color=blue&right_color=green&left_text=Downloads/Month)](https://pepy.tech/project/chillboss)
[![Downloads](https://static.pepy.tech/personalized-badge/chillboss?period=week&units=international_system&left_color=blue&right_color=green&left_text=Downloads/Week)](https://pepy.tech/project/chillboss)

Version: 0.1.0

ChillBoss keeps your mouse moving to keep your status alive.

Installation:

```shell
pip install chillboss
```

![ChillBoss Installation](https://i.imgur.com/EHvbM1H.gif)

Usage:

```shell
python -m chillboss
```

Command line argument accepted:

* --movement: `random` and `square` movements are accepted. Default set to `random`.
* --length: Accepted for `square` type of movement. Default set to `None`.
* --sleeptime: Time to be taken till next movement. Default set to 30 seconds.
* --motiontime: Time consumption of pointer to move from present coordinates to the next coordinates. Default set to 0
  seconds.

![ChillBoss Usage](https://i.imgur.com/Os7cmkk.gif)
