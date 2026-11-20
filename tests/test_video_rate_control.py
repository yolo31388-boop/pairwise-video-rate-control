import pytest
import math
from media import video_rate_control as mod

CASES = [
    ("bpf", 'm.bits_per_frame(1000000, 25) == 40000'),
    ("vbv", 'm.vbv_limit(1, 25) == 25'),
    ("gop", 'm.gop_length(True, 250) == 1'),
    ("b", 'm.bframe_depth(0.4, 25) == 10'),
    ("look", 'm.lookahead(2, 25) == 50'),
    ("qp", 'm.qp_effective(23, -2) == 21'),
    ("cw", 'm.complexity_weight(2, 3) == 6'),
    ("deblock", 'm.deblock_strength(2, 0.5) == approx(3.0)'),
    ("sei", 'm.preserve_sei(True) is True'),
    ("id", 'm.rate_id(3, 2) == "3:2"'),
    ("target", 'm.target_for(2, 500) == 1000'),
    ("cap", 'm.maxrate_cap(1200, 1000) == 1000'),
    ("pass", 'm.two_pass(1, 2) == 2'),
    ("scene", 'm.scene_weight(0.5, 0.3) == approx(1.0)'),
    ("type", 'm.frame_type(True) == "I"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
