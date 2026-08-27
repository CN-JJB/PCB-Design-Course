# 附录三 KiCad 操作与快捷键速查大全

> 全书操作知识的浓缩索引卡。打印贴墙版。基于 KiCad 10.x，中英对照。

---

## 一、全局与工程

| 操作 | 路径/快捷键 |
|------|------------|
| 新建工程 | File → New Project |
| 打开工程 | 双击 .kicad_pro |
| 切换单位 | Ctrl+U (mm/mil) |
| 保存 | Ctrl+S |
| 撤销/重做 | Ctrl+Z / Ctrl+Y |
| 查找 | Ctrl+F |
| 偏好设置 | Preferences → General |
| 语言切换 | Preferences → Language |

## 二、原理图编辑器

### 放置类

| 功能 | 快捷键 | 助记 |
|------|--------|------|
| 放置符号 | A | Add |
| 放置电源符号 | P | Power |
| 画导线 | W | Wire |
| 放网络标签 | L | Label |
| 放全局标签 | Ctrl+L? Place→Global Label | — |
| 层次标签 | H | Hierarchical |
| 图纸符号(子图) | S? Place→Add Sheet | Sheet |
| 总线 | B | Bus |
| 总线入口 | Place→Bus Entry | — |
| 不连接标记 | Q | — |
| 文本注释 | Place→Text | — |
| 图形框线 | Ctrl+Shift+X? 右键工具条 | — |

### 编辑类

| 功能 | 快捷键 |
|------|--------|
| 移动(断线) | M |
| 拖动(保持连线) | 按住 Alt 拖 或右键 Drag |
| 复制 | C 或 Ctrl+C |
| 旋转 | R |
| 镜像 X/Y | X / Y |
| 属性编辑 | E |
| 删除 | Del |
| 取消/退出 | Esc |

### 检查输出类

| 功能 | 路径 |
|------|------|
| ERC 检查 | Inspect → ERC |
| 标注位号 | Tools → Annotate |
| 分配封装 | Tools → Assign Footprints |
| 导出 BOM | File → Export → BOM |
| 导出 PDF | File → Export → PDF |
| 同步到 PCB | F8(PCB 编辑器内 Update from Schematic) |

## 三、PCB 编辑器

### 视图控制

| 功能 | 快捷键 |
|------|--------|
| 缩放 | Ctrl+滚轮 |
| 平移 | 中键拖动 |
| 单层显示 | 左侧面板 Active Layer Only? 图层列表开关 |
| 高亮网络 | U(可叠加) |
| 清除高亮 | Esc 或再按 U? 点空白 |
| 3D 查看 | 3(Alt+3 刷新) |
| 测量 | Ctrl+Shift+M? 右键 Measure |
| 网格切换 | 右下角网格选择器 + Shift+G? 快速循环 |

### 布局布线核心

| 功能 | 快捷键 | 说明 |
|------|--------|------|
| 布单线 | X | Route→Single Track |
| 布差分对 | 6 | Route→Diff Pair |
| 走线打孔换层 | V(走线中) | ★最高频操作 |
| 切层 | +(小键盘)或点层面板 | 配合 V |
| 推挤模式循环 | Shift+R | Highlight/Shove/Walkaround |
| 拖动(带线) | D | 微调布局神器 |
| 拖动(断线) | G | 与 D 对比体会 |
| 回退上一段 | Backspace(走线中) | — |
| 固定重规划 | Ctrl+点击(走线中) | — |
| 锁定/解锁 | L | 防误碰关键件 |

### 敷铜与过孔工具

| 功能 | 路径/快捷键 |
|------|------------|
| 画 Zone | Ctrl+Shift+Z 或 Place→Zone |
| 重填敷铜 | B |
| 显示敷铜轮廓 | Ctrl+B? 左侧开关 |
| 过孔缝合 | Tools → Via Stitching |
| 添加过孔(独立) | Place→Via? 布线中V为主 |

### 检查与输出

| 功能 | 路径 |
|------|------|
| DRC | Inspect → Design Rules Checker |
| 网络长度报告 | Inspect → Net Inspector ★等长验收 |
| 从原理图更新 | Tools → Update PCB from Schematic(F8) |
| Gerber 输出 | File → Fabrication Outputs → Gerbers |
| 钻孔文件 | Plot 对话框 → Generate Drill Files |
| 贴片坐标 | File → Fabrication Outputs → Component(.pos) |
| 元件反标回原理图 | Tools → Update Schematic from PCB? 反向同步 |

## 四、符号/封装编辑器要点

| 功能 | 路径 |
|------|------|
| 新建库 | File → New Library(选工程级) |
| 新建符号 | 右键库 → New Symbol |
| 放引脚 | P(注意电气类型!) |
| 引脚编号规则 | 必须匹配实物封装 pin 号 |
| 新封装 | Footprint Editor → New Footprint |
| 放焊盘 | 焊盘属性精确输坐标 |
| Courtyard 外扩 | 封装属性自动生成 |

## 五、Board Setup 结构地图

```
File → Board Setup
├── Design Rules
│   ├── Constraints        全局最小值
│   ├── Pre-defined Sizes  线宽/过孔快捷档
│   └── Net Classes        分类规则 ★
├── Custom Rules           .dru 语法细粒度规则
├── Differential Pairs     差分类 w/gap 定义 ★
├── Layers                 层名/颜色
└── Physical Stackup       制造级叠层参数 ★
```

## 六、效率心法十条

1. 手不离键盘：所有高频操作强制快捷键化一周成瘾
2. 网格分级：布局粗网格，布线细网格，丝印中网格
3. U 键是眼睛：任何连通性疑问立刻高亮整网
4. D 键是手：带线拖动比删了重画快十倍
5. B 键纪律：动过线必刷铜
6. Esc 是后悔药：任何卡住的状态先 Esc
7. 快捷键速查面板：忘了按 ?(Shift+/)
8. 设置导出：调好的偏好用 Preferences→Export 存档换机不丢
9. 规则复用：.kicad_dru 文件跨项目携带你的经验
10. 版本快照：每个里程碑压缩 zip 归档，Git 更佳

---

> 本表配合各章节首次出现的详细讲解使用；纯背表无意义，用三天自然内化。


---

## 七、KiCad 10 工程交付增量

### Design Variants

用于同一 PCB 的不同装配配置。Variant / DNP 必须同步 BOM、position 与 assembly output。

### Jobsets

将 ERC/DRC、制造输出等任务固化为可重复 release pipeline。正式项目建议保存 `release.kicad_jobset`。

### kicad-cli

课程 Hardware CI 使用 CLI 执行 ERC/DRC；具体参数随版本核对官方文档。

### 工程输出

除 Gerber / drill 外，理解以下格式在不同制造流程中的作用：

- IPC-D-356
- ODB++
- IPC-2581
- STEP

> 不是每家工厂都要求所有格式；以供应商流程为准。
