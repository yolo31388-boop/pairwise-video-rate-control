import math


def bits_per_frame(bitrate, fps):
    """每帧比特：平均码率按帧率摊分。"""
    if fps <= 0:
        raise ValueError("fps must be positive")
    return int(round(bitrate / fps))


def vbv_limit(buffer, fps):
    """VBV 上限：以秒计的缓冲量换算成帧数。"""
    if fps <= 0:
        raise ValueError("fps must be positive")
    return int(round(buffer * fps))


def gop_length(cut, default):
    """GOP 长度：场景切换处立即插入 I 帧，否则沿用默认长度。"""
    if cut:
        return 1
    return int(default)


def bframe_depth(buffer, fps):
    """B 帧深度：由解码端缓冲帧数决定，不超过缓冲可容纳的帧数。"""
    if fps <= 0:
        raise ValueError("fps must be positive")
    return max(0, int(round(buffer * fps)))


def lookahead(seconds, fps):
    """lookahead：把秒数换算为帧数。"""
    if fps <= 0:
        raise ValueError("fps must be positive")
    return int(round(seconds * fps))


def qp_effective(crf, offset):
    """QP 偏移：在基础 QP 上叠加编码器偏移并夹到合法范围。"""
    return int(round(min(51, max(0, crf + offset))))


def complexity_weight(motion, texture):
    """复杂度权重：运动与纹理的联合复杂度。"""
    return motion * texture


def deblock_strength(base, blockiness):
    """deblocking 强度：按块效应程度自适应放大基础强度。"""
    return base * (1.0 + blockiness)


def preserve_sei(has_color):
    """保留色彩 SEI：源含色彩信息时转码不得丢弃。"""
    return bool(has_color)


def rate_id(seed, index):
    """码控 id。"""
    return f"{seed}:{index}"


def target_for(complexity, base):
    """目标码率：按复杂度相对基准加权分配。"""
    return complexity * base


def maxrate_cap(bitrate, cap):
    """最大码率：不得超过上限。"""
    return min(bitrate, cap)


def two_pass(first, second):
    """两遍编码：第二遍复用第一遍的复杂度统计。"""
    return second


def scene_weight(delta, threshold):
    """场景权重：帧间差异超过阈值视为场景切换。"""
    return 1.0 if delta > threshold else 0.0


def frame_type(is_cut):
    """帧类型：场景切换处为 I 帧，否则为 P 帧。"""
    return "I" if is_cut else "P"
