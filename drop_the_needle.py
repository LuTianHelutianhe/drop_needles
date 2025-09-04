import numpy as np

def throw_needles(num_throws, L, d):
    
    # 模拟投针法估算圆周率。
    # num_throws: 投掷针的次数
    # L: 针的长度
    # d: 平行线的间距
    # return: 圆周率的估计值

    hits = 0  # 记录与平行线相交的次数

    for _ in range(num_throws):
        # 随机生成针的中心到最近平行线的距离
        y = np.random.uniform(0, d / 2)
        
        # 随机生成针与平行线的夹角（在 0 到 π/2 之间）
        theta = np.random.uniform(0, np.pi / 2)
        
        # 判断针是否与平行线相交
        if y <= (L / 2) * np.sin(theta):
            hits += 1
    
    # 使用投针法公式估计圆周率
    pi_estimate = (2 * L * num_throws) / (hits * d) if hits > 0 else 0
    return pi_estimate

# 参数设定
L = 1.0  # 针的长度
d = 1.0  # 平行线的间距
num_throws = 100000  # 投掷次数

# 估算圆周率
pi_estimation = throw_needles(num_throws, L, d)
print(f"使用投针法估算的圆周率为: {pi_estimation}")

