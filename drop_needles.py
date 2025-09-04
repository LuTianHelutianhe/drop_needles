from manim import *
import numpy as np

# 配置动画的全局参数
config.pixel_height = 800
config.pixel_width = 1200
config.frame_height = 8.0
config.frame_width = 14.0

class BuffonNeedleFast(Scene):
    def construct(self):
        # 创建平行线
        line_spacing = 2.0
        num_lines = 7
        lines = VGroup()
        for i in range(num_lines):
            y_position = (i - num_lines // 2) * line_spacing
            line = Line(start=[-7, y_position, 0], end=[7, y_position, 0], color=BLUE)
            lines.add(line)
        self.play(Create(lines))
        
        # 投掷针的模拟
        needle_length = 1.5
        num_needles = 500  # 增加投针次数
        intersection_count = 0
        
        for _ in range(num_needles):
            # 随机生成针的中心位置和角度
            x_center = np.random.uniform(-6, 6)
            y_center = np.random.uniform(-3, 3)
            angle = np.random.uniform(0, np.pi)
            
            # 计算针的两个端点
            x_offset = (needle_length / 2) * np.cos(angle)
            y_offset = (needle_length / 2) * np.sin(angle)
            
            start_point = np.array([x_center - x_offset, y_center - y_offset, 0])
            end_point = np.array([x_center + x_offset, y_center + y_offset, 0])
            
            needle = Line(start=start_point, end=end_point, color=YELLOW)
            
            # 检查针是否与平行线相交
            intersects = False
            for line in lines:
                if line_spacing / 2 >= np.abs(line.get_y() - y_center) <= needle_length / 2 * np.sin(angle):
                    intersects = True
                    break
            
            if intersects:
                needle.set_color(RED)
                intersection_count += 1
            else:
                needle.set_color(GREEN)
            
            # 显示针，调整 run_time 加快速度
            self.play(Create(needle), run_time=0.05)  # 投针速度设置为 0.1s
            
        # 输出统计信息
        pi_estimation = (2 * needle_length * num_needles) / (intersection_count * line_spacing)
        result_text = Text(f"Estimated Pi: {pi_estimation:.5f}", font_size=36)
        self.play(Write(result_text))
        self.wait(2)

