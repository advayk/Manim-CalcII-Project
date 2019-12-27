from manimlib.imports import *

class Equations(Scene):
    def construct(self):
        #Making equations

        first_eq = TextMobject("$$S = \\int_{a}^{b} 2\\pi f(x) \\sqrt{1+[\\frac{dy}{dx}]^2} dx$$")
        second_eq = ["$S$", "=", "$\\int_{a}^{b}$", "$2\\pi f(x)$", "$\\sqrt{1+[f'(x)]^2} dx$",]

        second_mob = TextMobject(*second_eq)

        for i,item in enumerate(second_mob):
            if(i != 0):
                item.next_to(second_mob[i-1],RIGHT)

        eq2 = VGroup(*second_mob)

        des1 = TextMobject("The Surface area of f(x) where $$ a\le x \le b$$ around the x-axis is")
        des2 = TextMobject("Or this...")

        #Coloring equations
        second_mob.set_color_by_gradient("#33ccff","#ff00ff")

        #Positioning equations
        des1.shift(2*UP)
        des2.shift(2*UP)

        #Animating equations
        self.play(Write(des1))
        first_eq.shift(DOWN)
        self.play(Write(first_eq))
        self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
        self.wait(1)

        for i, item in enumerate(eq2):
            if (i<2):
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color="#00FFFF")

        self.add(eq2)
        self.wait(1)
