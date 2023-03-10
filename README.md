# RealizeMusicVisualization
编程实现音乐节奏或旋律的可视化

## 一、程序说明

### （一）基本思路

1. 从文件中获取信息
2. 根据频率和时间索引得到一个包含幅度值的矩阵
3. 将矩阵转换为分贝矩阵
4. 获取频率数组
5. 获取时间周期数组
6. 设置绘图窗口
7. 运行直到用户要求退出
8. 用白色填充背景
9. 加载音乐


### （二）说明

filename = "Mitsuha.mp3"

Mitsuha.mp3为所播放音乐名。

运行时，请将Project1.py和Mitsuha.mp3放于同一工作目录下。

### （三）注意

因为选取的是完整钢琴曲，开始运行后，请耐心等待1分钟左右。

## 二、算法原理

**短时傅里叶变换原理**

短时傅里叶变换（STFT，short-time Fourier transform）是和傅里叶变换相关的一种数学变换，用以确定时变信号其局部区域正弦波的频率与相位。
它的思想是：选择一个时频局部化的窗函数，假定分析窗函数g(t)在一个短时间间隔内是平稳（伪平稳）的，移动窗函数，使f(t)g(t)在不同的有限时间宽度内是平稳信号，从而计算出各个不同时刻的功率谱。

短时傅里叶变换使用一个固定的窗函数，窗函数一旦确定了以后，其形状就不再发生改变，短时傅里叶变换的分辨率也就确定了。如果要改变分辨率，则需要重新选择窗函数。
短时傅里叶变换用来分析分段平稳信号或者近似平稳信号犹可，但是对于非平稳信号，当信号变化剧烈时，要求窗函数有较高的时间分辨率；而波形变化比较平缓的时刻，主要是低频 信号，则要求窗函数有较高的频率分辨率。短时傅里叶变换不能兼顾频率与时间分辨率的需求。

短时傅里叶变换窗函数受到W.Heisenberg不确定准则的限制，时频窗的面积不小于2。这也就从另一个侧面说明了短时傅里叶变换窗函数的时间与频率分辨率不能同时达到最优。

## 三、运行截图

![运行截图1](https://github.com/imrewang/RealizeMusicVisualization/blob/main/screenshot/11.png?raw=true)

![运行截图2](https://github.com/imrewang/RealizeMusicVisualization/blob/main/screenshot/12.png?raw=true)

## 四、参考文献

librosa.load：https://librosa.org/doc/latest/generated/librosa.load.html

pygame.display：https://www.pygame.org/docs/ref/display.html

pygame.time：https://www.pygame.org/docs/ref/time.html

pygame.mixer：https://www.pygame.org/docs/ref/mixer.html

pygame.event：https://www.pygame.org/docs/ref/event.html


