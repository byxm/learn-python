
# 计算一颗一级石头需要消耗的金子
def computeOneLevelStonePrice():
    return 0.75 + 8 * 0.05

# 计算从一级石到二级石需要花费的金子


def composeOneLevelStoneToThreeLevelStone():
    oneLevelTotalPrice = 12 * computeOneLevelStonePrice()
    return 10 + 0.39 + oneLevelTotalPrice


def composeThreeLevelStoneToFourLevelStone():
    pass


def composeFourLevelStoneToSixLevelStone():
    oneLevelTotalPrice = 12 * computeOneLevelStonePrice()
    return 10 + 19.75 + oneLevelTotalPrice
