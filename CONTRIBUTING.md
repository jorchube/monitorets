# Contributing


Hello!

Are you considering contributing to this project? Then thank you very much! :)


## Contributing changes

Before you start working on a new feature or a bug fix it would be a good idea to open an issue explaining what you want to do.

By doing so we start a discussion to flesh out the idea and reach a common ground on the best strategy to follow. In the end this will speed up the process a lot and the change will make its way into a new release faster.


### Setting up the environment

Monitorets is written in *Python* and it uses *Pipenv* to manage its dependencies.

There is a Makefile providing several convenient targets:

* To setup a python virtual environment with all the dependencies:

```
make install-dev-requirements
```

* To enter the new environment:

```
make dev-shell
```

* To run the unit tests:

```
make tests
```

* To check the linting rules:

```
make check-linting
```

* To apply automatically the linting rules:

```
make linting
```


For every PR there are checks ensuring that the unit tests are passing and that the linting is correct, so it is a good idea to ensure the tests are passing and to apply the linting rules before opening a PR.


### Running your changes

The easiest way to build and run Monitorets locally is to use [Gnome Builder](https://wiki.gnome.org/Apps/Builder): You just need to open the project and hit the *run* button.


## Opening issues


### Have you found a bug?

Try to explain as best as you can the nature of the bug.

If the application is behaving in an unexpected manner try to describe the steps necessary to reproduce this behavior and also explain what did you expect to happen instead.

An image (and a video!) is worth a thousand words: Screenshots or screencasts showing the bug are also very helpful!



### Do you have a feature request?

Try to explain your request as clearly as possible. Providing examples (mockups, references to other applications, etc) will make it easier to understand your request.



## Translators

Translations are ***very*** welcome!


If you submit a translation you may consider adding yourself to the [list of translators](https://github.com/jorchube/monitorets/blob/master/src/translators.py). By doing so your name will appear in the credits of the application on *Menu* --> *About* --> *Credits*.
