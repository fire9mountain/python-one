import turtle  # 导入turtle库，用于图形绘制
import random  # 导入random库，生成随机数
import math  # 导入math库，进行数学计算

# 设置窗口大小和背景颜色
turtle.setup(1.0, 1.0)
turtle.title("烟花绽放动画")
turtle.bgcolor('black')

t = turtle.Turtle()
t.hideturtle()
t.pensize(1)

# 定义烟花的颜色列表
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']


class Firework:
    def __init__(self):
        self.x = random.randint(-400, 400)
        self.y = random.randint(-300, 300)
        self.color = random.choice(colors)
        self.particles = []
        self.exploded = False
        self.lifetime = random.randint(50, 100)
        self.create_particles()

    def create_particles(self):
        for _ in range(random.randint(50, 100)):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 6)
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            self.particles.append([self.x, self.y, dx, dy])

    def update(self):
        if not self.exploded:
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.explode()
        else:
            for particle in self.particles:
                particle[0] += particle[2]
                particle[1] += particle[3]
                particle[3] -= 0.1  # gravity effect

    def explode(self):
        self.exploded = True

    def draw(self):
        if not self.exploded:
            t.penup()
            t.goto(self.x, self.y)
            t.dot(10, self.color)  # 放大烟花点的大小
        else:
            for particle in self.particles:
                t.penup()
                t.goto(particle[0], particle[1])
                t.dot(5, self.color)  # 放大光粒的半径


# 创建一个烟花列表，用来存储烟花实例
fireworks = [Firework() for _ in range(5)]

# 进行无限循环，模拟烟花绽放动画
while True:
    turtle.tracer(0)  # 关闭tracer，提高性能
    t.clear()  # 清除画布内容
    for firework in fireworks:
        firework.update()  # 更新每颗烟花的状态
        firework.draw()  # 重新绘制每颗烟花
    turtle.update()  # 更新屏幕显示内容

    # 创建新的烟花实例以保持持续绽放效果
    if random.random() < 0.1:  # 控制新烟花出现的频率
        fireworks.append(Firework())

    # 移除已经爆炸并消失的烟花实例，防止内存泄漏
    fireworks = [fw for fw in fireworks if not (fw.exploded and all(p[3] <= -1 for p in fw.particles))]

