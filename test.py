from manim import *

class SumOfFirstNNumbers(Scene):
    def create_sum_animation(self, n):
        # Display Problem Statement
        prompt = Text(
            f"Problem: Find the sum of the first {n} natural numbers",
            font_size=28,
            color=WHITE,
            t2c={"Problem": RED, str(n): GREEN},
            t2w={"Problem": BOLD, str(n): BOLD}
        )
        prompt.to_edge(UP)
        self.play(Write(prompt))
        self.wait(1)

        # Show Sum Text
        fx = MathTex(r'f(x)', font_size=27, color=RED)
        sum_equation = MathTex(rf'1 + 2 + 3 + \cdots + n', font_size=28, color=WHITE)
        equal_sign_1 = MathTex(r"=", font_size=28, color=WHITE)
        sum_notation = MathTex(rf'\sum_{{i=1}}^{{n}} i', font_size=28, color=WHITE)
        formula = MathTex(r"\frac{n(n+1)}{2}", font_size=28, color=YELLOW)

        self.play(Write(fx.next_to(prompt, DOWN * 2).shift(LEFT * 3)))
        self.wait(0.25)
        self.play(Write(equal_sign_1.next_to(fx, RIGHT)))
        self.wait(0.25)
        self.play(Write(sum_equation.next_to(equal_sign_1, RIGHT)))
        self.wait(0.25)
        equal_sign_2 = equal_sign_1.copy().next_to(sum_equation, RIGHT)
        self.play(Write(equal_sign_2))
        self.wait(0.25)
        self.play(Transform(sum_equation.copy(), sum_notation.next_to(equal_sign_2, RIGHT)))
        self.wait(0.5)
        equal_sign_3 = equal_sign_2.copy().next_to(sum_notation, RIGHT)
        self.play(Write(equal_sign_3))
        self.wait(0.5)
        self.play(Write(formula.next_to(equal_sign_3, RIGHT)))
        self.wait(1)

        # Now change the variable n to the actual number in the sum_equation
        number = [x for x in range(1, n + 1)]
        fx1 = MathTex(rf'(f{n})', font_size=27, color=RED).next_to(fx, DOWN)
        if n <= 6:
            sum_equation_with_n = MathTex(rf'{" + ".join(str(i) for i in number)}', font_size=28, color=WHITE)
        else:
            sum_equation_with_n = MathTex(rf'1 + 2 + 3 + \cdots + {n}', font_size=28, color=WHITE)

        self.play(Transform(fx.copy(), fx1))
        self.wait(0.25)
        equal_sign_4 = equal_sign_3.copy()
        self.play(Write(equal_sign_4.next_to(fx1, RIGHT)))
        self.wait(0.25)
        self.play(Transform(sum_equation.copy(), sum_equation_with_n.next_to(equal_sign_4, RIGHT)))
        self.wait(0.25)

        fx2 = MathTex(rf'(f{n})', font_size=27, color=RED).next_to(fx1, DOWN)
        self.play(Transform(fx1.copy(), fx2))
        self.wait(0.25)
        equal_sign_5 = equal_sign_4.copy().next_to(fx2, RIGHT)
        self.play(Write(equal_sign_5))
        self.wait(0.25)
        sum_result = MathTex(str(sum(number)), font_size=28, color=BLUE)
        self.play(Transform(sum_equation_with_n.copy(), sum_result.next_to(equal_sign_5, RIGHT)))
        self.wait(0.25)
        equal_sign_6 = equal_sign_5.copy().next_to(sum_result, RIGHT)
        self.play(Write(equal_sign_6))
        self.wait(0.5)

        # Highlight the formula
        self.play(Indicate(formula, color=YELLOW))

        # Stepwise Evaluation of the Formula
        formula_steps = [
            MathTex(rf'\frac{{ {n} \times ({n}+1) }}{{2}}', font_size=28, color=BLUE),
            MathTex(rf'\frac{{ {n * (n + 1)} }}{{2}}', font_size=28, color=BLUE),
            MathTex(str(n * (n + 1) // 2), font_size=28, color=BLUE)
        ]

        for i, step in enumerate(formula_steps):
            if i == 0:
                self.play(Transform(formula.copy(), step.next_to(equal_sign_6, RIGHT), replace_mobject_with_target_in_scene=True))
            else:
                self.play(Transform(formula_steps[i-1], step.next_to(equal_sign_6, RIGHT), replace_mobject_with_target_in_scene=True))
            self.wait(0.5)
        
        # Merge the sum_result steps
        self.play(FadeOut(equal_sign_6))
        self.play(Transform(formula_steps[-1], sum_result.set_color(GREEN), replace_mobject_with_target_in_scene=True))
        self.play(Indicate(sum_result, color=GREEN))
        self.wait(0.5)
        # self.play(Write(Text(f'The sum of the first {n} natural numbers is {sum(number)}', font_size=24, color=GREEN, t2c={f"{n}": RED, f"{sum(number)}": YELLOW}, t2w={f"{n}": BOLD, f"{sum(number)}": BOLD}).to_edge(DOWN)))
        result_text = Text(
            f"The sum of the first {n} natural numbers is {sum(number)}",
            font_size=24,
            color=WHITE,
            t2c={str(n): RED, str(sum_result): YELLOW},
            t2w={str(sum_result): BOLD, str(n): BOLD}
        )
        self.play(Write(result_text.to_edge(DOWN)))
        self.wait(1)
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
        self.wait(1)

    def construct(self):
        # Title
        title = Text("Sum of First N Natural Numbers", font_size=42, color=BLUE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Write the Formula
        notation = MathTex(r'\sum_{i=1}^{n} i', font_size=32, color=RED)
        equal_sign = MathTex(r"=", font_size=32, color=WHITE)
        equation = MathTex(r'1 + 2 + 3 + \cdots + n', font_size=32, color=WHITE)
        formula = MathTex(r"\frac{n(n+1)}{2}", font_size=32, color=YELLOW)
        
        self.play(Write(Text("Formula:", font_size=28, color=TEAL).shift(UP).shift(LEFT * 2.5)))
        self.play(Write(notation.shift(LEFT * 2.5)))
        self.wait(0.25)
        self.play(Write(equal_sign.next_to(notation, RIGHT)))
        self.wait(0.25)
        self.play(Write(equation.next_to(equal_sign, RIGHT)))
        self.wait(0.25)
        equal_sign_1 = equal_sign.copy().next_to(equation, RIGHT)
        self.play(Write(equal_sign_1))
        self.wait(0.25)
        self.play(Write(formula.next_to(equal_sign_1, RIGHT)))
        self.wait(1)

        # Explanation
        explanation = Text("Let's understand this with some examples.", font_size=28, color=GREEN)
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
        self.play(Write(explanation.to_edge(UP)))
        self.wait(1)
        self.play(FadeOut(explanation))

        
        self.create_sum_animation(5)
        self.play(Write(Text("Let's take another example...", font_size=28, color=GREEN).to_edge(UP)))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        
        self.create_sum_animation(10)
        self.play(Write(Text("That's it! We have successfully found the sum of the first N natural numbers.", font_size=24, color=GREEN, t2c={"N": BLUE, "sum": RED})))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.play(Write(Text("Thank You!", font_size=36, color=BLUE)))
        self.wait(2)