from manim import *

class Proof(Scene):
    def construct(self):
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
        text = Text("We need to prove that the formula holds for n = k + 1", font_size=18, color=WHITE, t2c={"n = k + 1": RED}).next_to(proof_title_1, DOWN).align_to(proof_title_1, LEFT).shift(RIGHT * 0.5)
        
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
        self.play(Indicate(proof_texts[-1], color=GREEN, scale_factor=1.1))
        self.wait(1)
        

        # Conclusion
        conclusion = Text("Therefore, the formula holds for all Natural Numbers.", font_size=20, color=GREEN, weight=BOLD, t2c={"Natural Numbers": YELLOW}).next_to(proof_texts[-1], DOWN * 2).align_to(proof_title_1, LEFT).shift(RIGHT * 0.5)
        self.play(Write(conclusion))
        self.wait(1)

        # Fade out all objects
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
        self.wait(1)