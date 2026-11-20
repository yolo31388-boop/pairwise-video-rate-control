import math

def bits_per_frame(bitrate, fps):
    """每帧比特。"""
    raise NotImplementedError("TODO: bits_per_frame")

def vbv_limit(buffer, fps):
    """VBV 上限。"""
    raise NotImplementedError("TODO: vbv_limit")

def gop_length(cut, default):
    """GOP 长度。"""
    raise NotImplementedError("TODO: gop_length")

def bframe_depth(buffer, fps):
    """B 帧深度。"""
    raise NotImplementedError("TODO: bframe_depth")

def lookahead(seconds, fps):
    """lookahead。"""
    raise NotImplementedError("TODO: lookahead")

def qp_effective(crf, offset):
    """QP 偏移。"""
    raise NotImplementedError("TODO: qp_effective")

def complexity_weight(motion, texture):
    """复杂度权重。"""
    raise NotImplementedError("TODO: complexity_weight")

def deblock_strength(base, blockiness):
    """deblocking 强度。"""
    raise NotImplementedError("TODO: deblock_strength")

def preserve_sei(has_color):
    """保留色彩 SEI。"""
    raise NotImplementedError("TODO: preserve_sei")

def rate_id(seed, index):
    """码控 id。"""
    raise NotImplementedError("TODO: rate_id")

def target_for(complexity, base):
    """目标码率。"""
    raise NotImplementedError("TODO: target_for")

def maxrate_cap(bitrate, cap):
    """最大码率。"""
    raise NotImplementedError("TODO: maxrate_cap")

def two_pass(first, second):
    """两遍编码。"""
    raise NotImplementedError("TODO: two_pass")

def scene_weight(delta, threshold):
    """场景权重。"""
    raise NotImplementedError("TODO: scene_weight")

def frame_type(is_cut):
    """帧类型。"""
    raise NotImplementedError("TODO: frame_type")
