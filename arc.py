from manimlib.imports import *

class Equations(Scene):
    def construct(self):
        #Making equations
        first_eq = TextMobject("$$ \\sqrt{{\\Delta x}^2 + {\\Delta y}^2}$$")
        sec_eq = TextMobject("$$ \\sqrt{({\\Delta x}^2) *(1+\\frac{({\\Delta y}^2)}{({\\Delta x}^2)})}$$")
        second_eq = ["=", "$\\sqrt{(1+{f'(x)}^2})$",]
        second_mob = TextMobject(*second_eq)

        for i,item in enumerate(second_mob):
            if(i != 0):
                item.next_to(second_mob[i-1],RIGHT)

        eq2 = VGroup(*second_mob)

        des1 = TextMobject("To find a single length of a slice with the pythagorean theorem: ")
        des2 = TextMobject("Or this...")

        #Coloring equations
        second_mob.set_color_by_gradient("#33ccff","#ff00ff")

        #Positioning equations
        des1.shift(2*UP)
        des2.shift(2*UP)

        #Animating equations
        self.play(Write(des1))
        first_eq.shift(UP)
        self.play(Write(first_eq))
        self.wait(3)
        sec_eq.shift(DOWN)
        self.play(Write(sec_eq))
        self.play(FadeOut(sec_eq))
        
        self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
        self.wait(1)

        for i, item in enumerate(eq2):
            if (i<2):
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color="#00FFFF")

        self.add(eq2)
        self.wait(1)
