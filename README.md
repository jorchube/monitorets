[![Tests](https://github.com/jorchube/monitorets/actions/workflows/CI.yml/badge.svg)](https://github.com/jorchube/monitorets/actions/workflows/CI.yml)

# Monitorets

<p align="center">
    <img src="https://raw.githubusercontent.com/jorchube/monitorets/master/imgs/logo.svg" />
</p>

**Monitorets** is a small utility application offering a simple and quick view at the usage of several of your computer resources. Almost like an applet or a widget for your Linux desktop.

<p align="center">
    <img src="https://raw.githubusercontent.com/jorchube/monitorets/master/imgs/themeable.png" />
</p>

### Flexible:

Select between *horizontal* and *vertical* layout. Or let the application decide based on the window shape.

<p align="center">
    <img src="https://raw.githubusercontent.com/jorchube/monitorets/master/imgs/adaptable.png" />
</p>

### Configurable:

Choose which resources you want to have visible:
* Cpu
* Gpu \[1\]
* Memory
* Network downlink traffic
* Network uplink traffic
* Home folder ( **~** ) space
* Root ( **/** ) space


### Get it now:

You can download the latest version from flathub. Click on the banner below:

<p align="center">
    <a href='https://flathub.org/apps/details/io.github.jorchube.monitorets'>
        <img width='240' alt='Download on Flathub' src='https://flathub.org/assets/badges/flathub-badge-en.png'/>
    </a>
</p>

You can also install it using the command line with the following commands:

```
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install io.github.jorchube.monitorets
```

---

\[1\] GPU monitoring is an experimental feature that may not work at all depending on your GPU vendor and drivers.
