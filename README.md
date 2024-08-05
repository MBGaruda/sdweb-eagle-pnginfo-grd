# Eagle-pnginfo (Library switch ver.)

[English README](README.md)

- This extension adds the functionality to switch libraries in [Eagle-pnginfo](https://github.com/bbc-mc/sdweb-eagle-pnginfo).

## How to Install

- Please refer to [Eagle-pnginfo](https://github.com/bbc-mc/sdweb-eagle-pnginfo)

## How to use

- Please refer to [Eagle-pnginfo](https://github.com/bbc-mc/sdweb-eagle-pnginfo) for the basic configuration settings.

- Please specify the path of Eagle's library in the "Eagle library path" in the settings.

- When generating an image, it instructs Eagle to switch the library.

- After confirming that Eagle has switched the library, the image is sent to Eagle.

- Since it may not switch immediately, it will check every 0.2 seconds. If it fails to switch after 10 attempts, it will send the image to the current library.

