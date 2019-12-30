from manimlib.imports import *
import math

class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x^{2}")

        func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)
#         two_pi = TexMobject("x = 2 \\pi")
# label_coord = self.input_to_graph_point(TAU,func_graph)
# two_pi.next_to(label_coord,RIGHT+UP)
        delta_y = TexMobject("\\Delta y")
        label_coord = self.input_to_graph_point(0.5,func_graph)
        delta_y.next_to(label_coord,RIGHT+RIGHT)
        delta_x = TexMobject("\\Delta x")
        label_coord = self.input_to_graph_point(0.5,func_graph)
        delta_x.next_to(label_coord,UP+UP+UP)
        point1 = Dot(self.coords_to_point(1,self.func_to_graph(1)))
        point2 = Dot(self.coords_to_point(0,0))
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point1)
        self.wait(1)
        self.add(point2)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(1)
        self.play(ShowCreation(delta_y))
        self.wait(1)
        self.play(ShowCreation(delta_x))


    def func_to_graph(self, x):
        return (x**2)

    def func_to_graph_2(self, x):
        return(x**3)