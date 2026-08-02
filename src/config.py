#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
路径配置
"""
import os
from datetime import datetime

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 时间戳
TIMESTAMP = datetime.now().strftime('%Y%m%d_%H%M%S')

# 输出目录
FIGS_DIR = os.path.join(BASE_DIR, 'figs')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 确保目录存在
os.makedirs(FIGS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
