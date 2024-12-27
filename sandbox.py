from manim import *

# Manim Configuration
VIDEO_DIR = "videos/sandbox"
config.video_dir = VIDEO_DIR
config.pixel_height = 1080
config.pixel_width = 1920

class SumOfNaturalNumbers(Scene):
    def create_sum_animation(self, n, sum_text, formula_text):
        """
        Creates an animation to demonstrate the sum of the first `n` natural numbers.

        Parameters:
        - n (int): The number up to which the sum is calculated.
        - sum_text (str): The textual representation of the sum.
        - formula_text (str): The formula used for the sum.
        """
        # Display Prompt
        prompt = Text(f"Problem: Find the sum of the first {n} natural numbers", font_size=28, color=GREEN)
        prompt.to_edge(UP)
        self.play(Write(prompt))
        
        # Display numbers
        if n > 5:
            numbers = VGroup(
                MathTex("1", color=RED),
                MathTex("2", color=RED),
                MathTex("3", color=RED),
                MathTex(r"\cdots", color=RED),
                MathTex(str(n), color=RED)
            )
        else:
            numbers = VGroup(*[MathTex(str(i), color=RED) for i in range(1, n + 1)])
        
        numbers.arrange(RIGHT, buff=0.5)
        numbers.next_to(prompt, DOWN * 2)
        self.play(Write(numbers))
        self.wait(1)
        self.play(numbers.animate.next_to(prompt, DOWN))  

        # Highlight the formula
        highlight_formula = MathTex(formula_text, font_size=24, color=PURPLE)
        self.play(Write(highlight_formula))
        self.wait(2)

        # Divider
        divider = Line(UP, DOWN, color=WHITE).scale(2)
        
        # Sum text
        sum_equation = MathTex(sum_text, font_size=24, color=ORANGE)
        self.play(
            highlight_formula.animate.shift(LEFT * 2),
            sum_equation.animate.next_to(divider, RIGHT * 4)
        )

        self.play(GrowFromCenter(divider))
        self.wait(2)

        # Fade out all elements
        self.play(FadeOut(prompt), FadeOut(numbers), FadeOut(highlight_formula), FadeOut(sum_equation), FadeOut(divider))

    def construct(self):
        # Title
        title = Text("Sum of First N Natural Numbers", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Write the formula
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
        
        # Example 1: n = 5
        self.create_sum_animation(5, "1 + 2 + 3 + 4 + 5 = 15", r"\frac{5(5+1)}{2} = 15")
        self.wait(1)
        self.create_sum_animation(6, "1 + 2 + 3 + 4 + 5 + 6 = 21", r"\frac{6(6+1)}{2} = 21")
