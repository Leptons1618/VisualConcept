from manim import *
VIDEO_DIR = "videos/sumOfNaturalNumbers"
config.video_dir = VIDEO_DIR
config.pixel_height = 1080
config.pixel_width = 1920

class SumOfNaturalNumbers(Scene):
    def construct(self):
        self.display_title()
        self.display_formula()
        self.visualize_sum()
        self.show_examples()

    def display_title(self):
        title = Text("Sum of First N Natural Numbers", font_size=36, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.title = title

    def display_formula(self):
        formula = MathTex(r"1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}", font_size=28, color=YELLOW)
        self.play(Write(formula))
        self.wait(2)
        self.play(formula.animate.next_to(self.title, DOWN))
        self.formula = formula

    def visualize_sum(self):
        explanation = Text("Let's visualize the sum of the first 5 natural numbers", font_size=28, color=GREEN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))

        numbers = VGroup(*[MathTex(str(i), color=RED) for i in range(1, 6)])
        numbers.arrange(RIGHT, buff=0.5)
        self.play(Write(numbers))
        self.wait(1)
        self.play(FadeOut(self.title))
        self.play(numbers.animate.to_edge(UP))

        highlight_formula = MathTex(r"\frac{5(5+1)}{2} = 15", font_size=24, color=PURPLE)
        self.play(Transform(self.formula, highlight_formula))
        self.wait(2)

        divider = Line(UP, DOWN, color=WHITE).scale(2)
        sum_text = MathTex("1 + 2 + 3 + 4 + 5 = 15", font_size=24, color=ORANGE)

        self.play(
            self.formula.animate.shift(LEFT * 2),
            sum_text.animate.next_to(divider, RIGHT)
        )
        self.play(GrowFromCenter(divider))
        self.wait(2)

        ending_text = Text("The sum of the first 5 natural numbers is 15!", font_size=24, color=TEAL)
        ending_text.next_to(divider, DOWN)
        self.play(Write(ending_text))
        self.wait(2)

        self.play(FadeOut(ending_text), FadeOut(self.formula), FadeOut(sum_text), FadeOut(divider), FadeOut(numbers))

    def show_examples(self):
        examples = [
            (6, "1 + 2 + 3 + 4 + 5 + 6 = 21", r"\frac{6(6+1)}{2} = 21"),
            (15, "1 + 2 + 3 + \cdots + 15 = 120", r"\frac{15(15+1)}{2} = 120"),
            (100, "1 + 2 + 3 + \cdots + 100 = 5050", r"\frac{100(100+1)}{2} = 5050")
        ]

        for n, sum_text, formula_text in examples:
            numbers = VGroup(
                MathTex("1", color=RED),
                MathTex("2", color=RED),
                MathTex("3", color=RED),
                MathTex(r"\cdots", color=RED),
                MathTex(str(n), color=RED)
            ) if n > 5 else VGroup(*[MathTex(str(i), color=RED) for i in range(1, n + 1)])
            numbers.arrange(RIGHT, buff=0.5)

            self.play(Write(numbers))
            self.wait(1)
            self.play(numbers.animate.to_edge(UP))

            highlight_formula = MathTex(formula_text, font_size=24, color=PURPLE)
            self.play(Write(highlight_formula))
            self.wait(2)

            divider = Line(UP, DOWN, color=WHITE).scale(2)
            sum_text = MathTex(sum_text, font_size=24, color=ORANGE)

            self.play(
                highlight_formula.animate.shift(LEFT * 2),
                sum_text.animate.next_to(divider, RIGHT)
            )
            self.play(GrowFromCenter(divider))
            self.wait(2)

            self.play(FadeOut(numbers), FadeOut(highlight_formula), FadeOut(sum_text), FadeOut(divider))