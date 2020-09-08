



def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 10
    return damage1, damage2    # 返回多个值，属于元祖的方式，可以省略括号


skill1_damage, skill2_damage = damage(10, 20)


print(skill1_damage, skill2_damage)