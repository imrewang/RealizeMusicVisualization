import librosa#Librosa是一个用于音频、音乐分析、处理的python工具包，一些常见的时频处理、特征提取、绘制声音图形等功能应有尽有，功能十分强大。
import numpy as np#NumPy 操作  使用NumPy，开发人员可以执行以下操作：
#数组的算数和逻辑运算。
#傅立叶变换和用于图形操作的例程。
#与线性代数有关的操作。 NumPy 拥有线性代数和随机数生成的内置函数。
import pygame


def clamp(min_value, max_value, value):

    if value < min_value:#如果参数小于范围，该函数将返回最小数值。
        return min_value

    if value > max_value:#如果参数大于范围，该函数将返回最大数值。
        return max_value

    return value#如果参数位于最小数值和最大数值之间的数值范围内，则该函数将返回参数值。


class AudioBar:

    def __init__(self, x, y, freq, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):
        #分贝decibel#freq频率参数
        self.x, self.y, self.freq = x, y, freq

        self.color = color

        self.width, self.min_height, self.max_height = width, min_height, max_height

        self.height = min_height

        self.min_decibel, self.max_decibel = min_decibel, max_decibel

        self.__decibel_height_ratio = (self.max_height - self.min_height)/(self.max_decibel - self.min_decibel)

    def update(self, dt, decibel):

        desired_height = decibel * self.__decibel_height_ratio + self.max_height

        speed = (desired_height - self.height)/0.1

        self.height += speed * dt

        self.height = clamp(self.min_height, self.max_height, self.height)#clamp

    def render(self, screen):
        #render 函数即渲染函数
        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))
        #pygame.draw.rect() 绘制矩形


filename = "Mitsuha.mp3"

time_series, sample_rate = librosa.load(filename)  # 从文件中获取信息###
# time-series音频时间序列  sample_rate采样率
#librosa.load() 如果 sr 缺省，librosa会默认以22050的采样率读取音频文件，高于该采样率的音频文件会被下采样，低于该采样率的文件会被上采样。
#如果希望以原始采样率读取音频文件，sr 应当设为 None。具体做法为 y, sr = librosa(filename, sr=None)。

# 根据频率和时间索引得到一个包含幅度值的矩阵###
# #在librosa中stft，功能是求音频的短时傅里叶变换, librosa.stft 返回是一个矩阵
stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))

spectrogram = librosa.amplitude_to_db(stft, ref=np.max)  # 将矩阵转换为分贝矩阵###，将幅度频谱转换为dB标度频谱。也就是对S取对数。

frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # 获取频率数组###

# 获取时间周期数组
times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048*4)

time_index_ratio = len(times)/times[len(times) - 1]

frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]


def get_decibel(target_time, freq):#spectrogram为频谱图，该频谱图用于短时傅里叶画频谱图。
    return spectrogram[int(freq * frequencies_index_ratio)][int(target_time * time_index_ratio)]


pygame.init()

infoObject = pygame.display.Info()#创建一个视频显示信息对象

screen_w = int(infoObject.current_w/2.5)
screen_h = int(infoObject.current_w/2.5)

# 设置绘图窗口###
screen = pygame.display.set_mode([screen_w, screen_h])


bars = []


frequencies = np.arange(100, 8000, 100)#函数返回一个有终点和起点的固定步长的排列

r = len(frequencies)


width = screen_w/r


x = (screen_w - width*r)/2

for c in frequencies:
    bars.append(AudioBar(x, 300, c, (255, 0, 0), max_height=400, width=width))#AudioBar
    x += width

t = pygame.time.get_ticks()#（以毫秒为单位）获取时间
getTicksLastFrame = t

pygame.mixer.music.load(filename)#加载音乐
pygame.mixer.music.play(0)#pygame.mixer.music.play(重复次数,开始时间)
#开始播放背景音乐。重复次数如果是5，加上原来播放的一次，总共会播放6次。开始时间如果为1.0的话，表示从音乐的第2秒开始播放。

# 运行直到用户要求退出
running = True
while running:

    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    # 用户是否单击了窗口关闭按钮？
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 用白色填充背景
    screen.fill((255, 255, 255))

    for b in bars:
        b.update(deltaTime, get_decibel(pygame.mixer.music.get_pos()/1000.0, b.freq))
        b.render(screen)

    # 翻转显示
    pygame.display.flip()

# 完毕！ 是时候放弃了。
pygame.quit()
