from manimlib.imports import *

class makeText(Scene):
    def construct(self):
        #######Code#######
        #Making text
        first_line = TextMobject("Why not use the shell theorem?")
        final_line = TextMobject("Reason", color=BLUE)
        color_final_line = TextMobject("Reason")

        #Coloring
        color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text

        #Showing text
        self.wait(1)
        self.play(Write(first_line))
        self.wait(1)
        self.play(FadeOut(first_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)