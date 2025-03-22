from .sensor import (
    CONFIG_SCHEMA,
    to_code,
    DEPENDENCIES,
    AUTO_LOAD,
    CONFLICTS_WITH,
)

# 可选：定义组件元数据（如依赖项、冲突组件等）
DEPENDENCIES = ["gpio"]  # 依赖 GPIO 组件
AUTO_LOAD = []
CONFLICTS_WITH = []
