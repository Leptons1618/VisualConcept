from manim import *

# Manim Configuration
VIDEO_DIR = "videos/sandbox"
config.video_dir = VIDEO_DIR
config.pixel_height = 1080
config.pixel_width = 1920

class SumOfNaturalNumbers(Scene):
    def create_sum_animation(self, n):
        """
        Creates an animation to demonstrate the sum of the first `n` natural numbers.

        Parameters:
        - n (int): The number up to which the sum is calculated.
        - sum_text (str): The textual representation of the sum.
        - formula_text (str): The formula used for the sum.
        """
        # Display Problem Statement
        prompt = Text(f"Problem: Find the sum of the first {n} natural numbers", font_size=28, color=GREEN)
        prompt.to_edge(UP)
        self.play(Write(prompt))
        self.wait(1)

        # Show Sum Text
        sum_equation = MathTex(str())
        sum_equation.next_to(prompt, DOWN * 2)
        self.play(Write(sum_equation))
        self.wait(1)

        # Step-by-Step Addition
        numbers = [MathTex(str(i), color=RED) for i in range(1, n + 1)]
        for i in range(len(numbers)):
            if i == 0:
                running_sum = numbers[i]
            else:
                running_sum = MathTex(str(sum(range(1, i + 2))), color=BLUE).move_to(sum_equation.get_center())
            numbers_group = VGroup(*numbers[: i + 1])
            numbers_group.arrange(RIGHT, buff=0.5).next_to(prompt, DOWN * 3)
            self.play(FadeIn(numbers_group))
            self.wait(0.5)
            self.play(Transform(sum_equation, running_sum))
            self.wait(0.5)

        # Formula Evaluation Step-by-Step (BODMAS)
        formula_steps = [
            MathTex(rf"{n}({n}+1)", font_size=28, color=YELLOW),
            MathTex(rf"{n * (n + 1)}", font_size=28, color=YELLOW),
            MathTex(rf"{n * (n + 1)} \div 2", font_size=28, color=YELLOW),
            MathTex(rf"{n * (n + 1) // 2}", font_size=28, color=YELLOW),
        ]

        formula_steps[0].to_edge(LEFT)
        self.play(Write(formula_steps[0]))
        self.wait(1)

        for i in range(1, len(formula_steps)):
            formula_steps[i].move_to(formula_steps[i - 1].get_center())
            self.play(Transform(formula_steps[i - 1], formula_steps[i]))
            self.wait(1)

        # Fade Out All Elements
        self.play(FadeOut(prompt), FadeOut(sum_equation), FadeOut(*formula_steps))
        self.wait(1)

    def construct(self):
        # Title
        title = Text("Sum of First N Natural Numbers", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Write the Formula
        equation = MathTex(r'\sum_{i=1}^{n} i = 1 + 2 + 3 + \cdots + n', font_size=28, color=WHITE)
        equal_sign = MathTex(r"=", font_size=28, color=WHITE)
        formula = MathTex(r"\frac{n(n+1)}{2}", font_size=28, color=YELLOW)
        equation.next_to(title, DOWN)
        equal_sign.next_to(equation, RIGHT)
        formula.next_to(equal_sign, RIGHT)
        self.play(Write(equation))
        self.wait(1)
        self.play(Write(equal_sign))
        self.wait(0.5)
        self.play(Write(formula))
        self.wait(2)

        # Explanation
        explanation = Text("Let's understand this with some examples,", font_size=28, color=GREEN)
        self.play(FadeOut(equation), FadeOut(equal_sign), FadeOut(formula))
        self.play(Write(explanation))
        self.wait(1)
        self.play(FadeOut(explanation))
        self.play(FadeOut(title))

        self.create_sum_animation(5)
        self.create_sum_animation(6)
