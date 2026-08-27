# STM32F407 V2｜Release

每个正式 release 建独立不可变目录，例如：

```text
REV_A/
REV_B/
```

至少包含或引用：

- release manifest；
- fabrication package；
- assembly package；
- BOM / variant；
- firmware / bitstream；
- test procedure；
- approved open risks。

禁止用“当前目录最新文件”定义生产版本。
