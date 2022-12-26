"""
author:leon
project:programmerUpgrade
date:2022/12/26
email:13368447@qq.com
"""


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, aiSettings):
        """初始化统计信息"""
        self.aiSettings = aiSettings
        self.resetStats()
        # 游戏刚启动时处于活动状态
        self.gameActive = True

    def resetStats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.shipsLeft = self.aiSettings.shipLimit
