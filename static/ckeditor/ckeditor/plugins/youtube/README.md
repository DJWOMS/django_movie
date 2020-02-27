Youtube Plugin for CKEditor 4
=============================

Copyright © 2017 Jonnas Fonini <jonnasfonini@gmail.com>.

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the LICENSE file for more details.

This plugin allow you to insert Youtube videos using embed code or just the video URL.

## Installation

### With NPM

 1. npm install ckeditor-youtube-plugin

 2. Add the plugin to CKEditor (config.js):

    ````js
    CKEDITOR.plugins.addExternal('youtube', '../node_modules/ckeditor-youtube-plugin/youtube/');

    config.extraPlugins = 'youtube';
    ````

    You may need to adjust the plugin path. The example is assuming that you have the following directory structure:

    ```
    project
    └───ckeditor
    │   └───config.js
    └───node_modules
        └───ckeditor-youtube-plugin
    ```

### Manual

Follow these steps:

 1. Download the latest version of the plugin from Github.
 2. Extract the downloaded file into the CKEditor's **plugins** folder.
 3. Enable the plugin by changing or adding the extraPlugins line in your configuration (config.js):

    ````js
    config.extraPlugins = 'youtube';
    ````

## Configuration
The default options can be overriden on config.js.

Video width:

```js
config.youtube_width = '640';
```

Video height:

```js
config.youtube_height = '480';
```

Make responsive (ignore width and height, fit to width):

```js
config.youtube_responsive = true;
```

Show related videos:

```js
config.youtube_related = true;
```

Use old embed code:

```js
config.youtube_older = false;
```

Enable privacy-enhanced mode:

```js
config.youtube_privacy = false;
```

Start video automatically:

```js
config.youtube_autoplay = false;
```

Show player controls:

```js
config.youtube_controls = true;
```

Disable the change of settings. The elements on the list will be disabled (but still visible).
See the available element list below.

```js
config.youtube_disabled_fields = ['txtEmbed', 'chkAutoplay'];
```

#### List of UI elements

* txtEmbed
* txtUrl
* txtWidth
* txtHeight
* chkResponsive
* chkNoEmbed
* chkRelated
* chkOlderCode
* chkPrivacy
* chkAutoplay
* txtStartAt
* chkControls


## How to use
If everything is ok, a Youtube icon should appear on the CKEditor toolbar. Click it,
paste your embed code or video URL and the video will be inserted.

## Translators
Thanks to those who helped translate the plugin

 * Eyed Farra (ar)
 * N. Petkov (bg)
 * Lukáš Říha (cs)
 * Sven Jansen (de)
 * Dimitris Kotsakis (el)
 * Victor (pollin14) (es)
 * Kevin Rudissaar (et)
 * Asier Iturralde Sarasola (eu)
 * Jami Pietilä (fi)
 * BiomanRouge (fr)
 * Moshe Simantov (he)
 * Karmacsi Gábor (hu)
 * Francesco Zanoni (it)
 * Yayoshi Nobuhide (ja)
 * MinSoo Kim (ko)
 * Holger Lockertsen (nb, nn)
 * Patrick van Lier (nl)
 * Michał Zalewski, Wirek (pl)
 * Samuel Diogo (pt-br)
 * Alexander Ustimenko (ru)
 * ivanbarlog (sk)
 * Çağdaş Yiğit (tr)
 * Mykola Pukhalskyi (uk)
 * Vu Thao (vi)
 * trowa (zh)


[![Licensed under the WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png "Licensed under the WTFPL")](http://www.wtfpl.net)
