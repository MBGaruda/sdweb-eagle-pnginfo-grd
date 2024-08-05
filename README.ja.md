# Eagle-pnginfo (Library switch ver.)

[English README](README.md)

- この拡張機能は、[Eagle-pnginfo](https://github.com/bbc-mc/sdweb-eagle-pnginfo)にライブラリをスイッチする機能を付与した物です。

## How to Install

- [Eagle-pnginfo](https://github.com/bbc-mc/sdweb-eagle-pnginfo)を参考にして下さい。

## How to use

- 基本的な設定項目は[Eagle-pnginfo](https://github.com/bbc-mc/sdweb-eagle-pnginfo)を参考にして下さい。

- 設定の"Eagle library path"に、Eagleのライブラリのパスを指定してください。

- 画像を生成すると、ライブラリを切り替えるようにEagleに指示を出します。

- Eagleのライブラリが切り替わったことを確認した後、画像がEagleに送信されます。

- すぐに切り替わらない事があるので、0.2秒毎に1回確認し続けます。10回確認して切り替わりが確認できなかった場合は、今のライブラリに送信します。
