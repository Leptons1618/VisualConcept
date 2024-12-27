from manim import *

class test(Scene):
    def construct(self):
        # Display Problem Statement
        n = 5
        prompt = Text(f"Problem: Find the sum of the first {n} natural numbers", font_size=28, color=GREEN)
        prompt.to_edge(UP)
        self.play(Write(prompt))
        self.wait(1)

        # Show Sum Text
        sum_notation = MathTex(r'\sum_{i=1}^{n} i', font_size=28, color=WHITE)
        equal_sign = MathTex(r"=", font_size=28, color=WHITE)
        sum_equation = MathTex(r'1 + 2 + 3 + \cdots + n', font_size=28, color=WHITE)
        sum_notation.next_to(prompt, DOWN * 2)
        equal_sign.next_to(sum_notation, RIGHT)
        sum_equation.next_to(equal_sign, RIGHT)
        self.play(Write(sum_notation))
        self.wait(0.5)
        self.play(Write(equal_sign))
        self.wait(0.5)
        self.play(Transform(sum_notation, sum_equation))
        self.wait(1)

        # # Now change the variable n to the actual number in the sum_equation
        # sum_equation_with_n = MathTex(rf'\sum_{{i=1}}^{{{n}}} i = 1 + 2 + 3 + \cdots + {n}', font_size=28, color=WHITE)
        # sum_equation_with_n.move_to(sum_equation.get_center())
        # self.play(Transform(sum_equation, sum_equation_with_n))
        # self.wait(2)
        
        # # Step-by-Step Addition
        # # show the numbers 1 to n below the sum text
        # numbers = [MathTex(str(i), color=RED) for i in range(1, n + 1)]
        # numbers_group = VGroup(*numbers)
        # numbers_group.arrange(RIGHT, buff=0.5).next_to(sum_equation_with_n, DOWN * 3)
        # self.play(Transform(sum_equation_with_n, numbers_group))
        # self.wait(1)
        