from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
        
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen
        
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
        
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()
        
class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()
        
# animation of the sum of the first n natural numbers using the formula n(n+1)/2
class SumOfNaturalNumbers(Scene):
    def construct(self):
        n = 10
        formula = MathTex(r"\sum_{i=1}^{n} i = \frac{n(n+1)}{2}")
        formula.to_edge(UP)
        self.play(Write(formula))
        self.wait()

        sum = 0
        for i in range(1, n+1):
            sum += i
            sum_text = MathTex(f"1 + 2 + 3 + ... + {i} = {sum}")
            sum_text.next_to(formula, DOWN)
            self.play(Write(sum_text))
            self.wait()

        self.wait(2)
        self.play(FadeOut(sum_text), FadeOut(formula))
        self.wait(2)

class TextBelowAnother(Scene):
    def construct(self):
        # Create the first text
        main_text = Text("This is the main text.", font_size=36)
        
        # Create the text to appear below
        below_text = Text("This text is below the main text.", font_size=24)
        
        # Position the below_text below the main_text
        below_text.next_to(main_text, DOWN)  # Position below with default spacing
        
        # Optionally adjust spacing between texts
        # below_text.shift(DOWN * 0.5)  # Adjust downward further, if necessary
        
        # Add both texts to the scene
        # self.add(main_text, below_text)
        
        # Animate the texts
        self.play(Write(main_text))
        self.play(Write(below_text))
        self.wait(2)
