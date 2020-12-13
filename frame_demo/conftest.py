import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="module", autouse=True)
def record_vedio():
    # 使用scrcpy录屏
    command = "scrcpy --record logi.mp4"
    # 使用cmd命令
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    # 结束录制，生成视频
    os.kill(p.pid, signal.CTRL_C_EVENT)
