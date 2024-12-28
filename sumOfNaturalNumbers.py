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
        
    def proof(self):
        # Proof by Induction
        proof_title = Text("Proof by Induction:", font_size=32, color=RED).to_edge(UP)
        self.play(Write(proof_title))
        self.wait(0.5)

        # Base Case
        base_case_title = Text("Base Case:", font_size=24, color=GREEN).next_to(proof_title, DOWN).to_edge(LEFT)
        base_case_equation = MathTex(r"S(1) = \frac{1(1+1)}{2}", font_size=24, color=WHITE).next_to(base_case_title, DOWN).shift(RIGHT * 0.5)
        base_case_check = MathTex(r"\text{True for } n = 1", font_size=24, color=BLUE).next_to(base_case_equation, DOWN)
        
        steps = [
            MathTex(r"= \frac{1 \times 2}{2}", font_size=24, color=WHITE).next_to(base_case_equation, RIGHT),
            MathTex(r"= 1", font_size=24, color=BLUE)
        ]
        
        self.play(Write(base_case_title))
        self.wait(0.5)
        self.play(Write(base_case_equation))
        self.wait(0.5)

        for i, step in enumerate(steps):
            if i == 0:
                self.play(Transform(base_case_equation.copy(), step, replace_mobject_with_target_in_scene=True))
            else:
                self.play(Transform(steps[i-1].copy(), step.next_to(steps[i-1], RIGHT), replace_mobject_with_target_in_scene=True))
            self.wait(0.5)
        self.play(Write(base_case_check))
        self.wait(1)

        # Inductive Hypothesis
        to_prove = Text("Inductive Hypothesis:", font_size=24, color=GREEN).next_to(base_case_check, DOWN).to_edge(LEFT)
        inductive_hypothesis = MathTex(r"S(k) = \frac{k(k+1)}{2}", font_size=24, color=WHITE).next_to(to_prove, DOWN).align_to(base_case_equation, LEFT)
        inductive_hypothesis_check = MathTex(r"\text{Assume true for } n = k", font_size=24, color=BLUE).next_to(inductive_hypothesis, DOWN).align_to(base_case_check, LEFT)
        
        self.play(Write(to_prove))
        self.wait(0.5)
        self.play(Write(inductive_hypothesis))
        self.wait(0.5)
        self.play(Write(inductive_hypothesis_check))
        self.wait(1)

        # Proof
        proof_title_1 = Text("Proof:", font_size=24, color=GREEN).next_to(inductive_hypothesis_check, DOWN).align_to(base_case_title, LEFT)
        text = Text("We need to prove that the formula holds for n = k + 1.", font_size=18, color=WHITE, t2c={"n = k + 1": RED}).next_to(proof_title_1, DOWN).align_to(proof_title_1, LEFT).shift(RIGHT * 0.5)
        
        proof_texts = [
            MathTex(r"S(k+1) = \frac{(k+1)(k+1+1)}{2}", font_size=20, color=WHITE),
            MathTex(r"S(k+1) = \frac{(k+1)(k+2)}{2}", font_size=20, color=WHITE),
            MathTex(r"= \frac{k^2 + 3k + 2}{2}", font_size=20, color=WHITE),
            MathTex(r"= \frac{k^2 + 2k + k + 2}{2}", font_size=20, color=WHITE),
            MathTex(r"= \frac{k(k+1)}{2} + k + 1", font_size=20, color=WHITE),
            MathTex(r"= S(k) + k + 1", font_size=20, color=GREEN)
        ]
        
        self.play(Write(proof_title_1))
        self.wait(0.5)
        self.play(Write(text))
        self.wait(0.5)
        
        for i in range(len(proof_texts)):
            if i == 0:
                self.play(Write(proof_texts[i].next_to(text, DOWN).align_to(text, LEFT)))
            elif i > 0 and i < 2:
                self.play(Write(proof_texts[i].next_to(proof_texts[i-1], DOWN).align_to(proof_texts[i-1], LEFT)))
            else:
                self.play(Transform(proof_texts[i-1].copy(), proof_texts[i].next_to(proof_texts[i-1], RIGHT), replace_mobject_with_target_in_scene=True))
            self.wait(0.25)
            
        # Highlight the result
        self.play(Indicate(proof_texts[-1], color=GREEN, scale_factor=2.5))
        self.wait(1)
        

        # Conclusion
        conclusion = Text("Therefore, the formula holds for all Natural Numbers.", font_size=20, color=GREEN, weight=BOLD, t2c={"Natural Numbers": YELLOW}).next_to(proof_texts[-1], DOWN * 2).align_to(proof_title_1, LEFT).shift(RIGHT * 0.5)
        self.play(Write(conclusion))
        self.wait(1)

        # Fade out all objects
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
        self.wait(1)
        self.proof()
        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.play(Write(Text("Thank You!", font_size=36, color=BLUE)))
        self.wait(2)