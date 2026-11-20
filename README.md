# pairwise-video-rate-control

同一段素材二次编码后暗部爬满方块，码率控制用 CBR 把预算平均摊到每一帧，复杂镜头直接崩；VBV 缓冲设得过小，I 帧刚吃完额度后面全糊；GOP 长度固定，场景切换落在 P 帧上，切镜后三帧都是残影；B 帧重排深度太大，解码端缓冲不足时丢帧；lookahead 窗口太短，运动复杂度估计滞后；CRF 模式又叠加了最大码率，简单镜头被强行降质；两遍编码第二遍没复用第一遍的复杂度统计，分配几乎和单遍一样；硬件编码器与软件编码器的 QP 偏移不同，同一参数出两种画质；暗部块效应来自 deblocking 强度按全局固定，平坦区域被过度平滑；SEI 里的色彩信息在转码时丢失，HDR 素材被当 SDR 压。media/video_rate_control.py 是核心，tests/test_video_rate_control.py 15个红。要修的是：按复杂度分配码率；VBV 按峰值约束；GOP 随场景切换；B 帧深度按解码缓冲；lookahead 按镜头长度；CRF 与上限解耦；两遍复用统计；硬件编码器 QP 校准；deblocking 按块自适应；转码保留色彩 SEI。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
