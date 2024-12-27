from manimlib import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        
# Transform square to circle
class SquareToCircle2(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.set_stroke(BLUE_E, width=4)
        circle = Circle()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()

# Transform text
class TextTransform(Scene):
    def construct(self):
        text1 = Text("Hello World")
        text2 = Text("Goodbye World")
        self.play(Write(text1))
        self.wait()
        self.play(Transform(text1, text2))