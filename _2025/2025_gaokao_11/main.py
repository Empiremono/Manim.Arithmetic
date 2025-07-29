from manim import *

class TitleShowUp(Scene) :
    def construct(self) :
        title = Tex(r"Arithmetic is not Math.")
        subtitle = Tex(r"2025届题集 vol.1 $\langle$ 2025年新高考 I 卷 T11 $\rangle$")
        self.add(title)
        self.play(FadeIn(title))
        self.wait()
        self.play(Transform(title, subtitle))

class QuestionShowUp(Scene) :
    def construct(self) :
        question = Tex(r"已知 $\Delta ABC$ 的面积为 $\displaystyle\frac{1}{4}$，若 $\cos 2A + \cos 2B + 2\sin C = 2$，$\displaystyle\cos A\cos B\sin C = \frac{1}{4}$，则", font_size = 30)
        question.to_edge(UL)
        self.add(question)
        self.play(FadeIn(question))
