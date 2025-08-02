from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class TitleShowUp(Scene) :
    def construct(self) :
        title = Tex(r"Arithmetic is not Math.")
        subtitle = Tex(r"2025届题集 vol.1 \\ $\langle$ 2025年新高考 I 卷 T11 $\rangle$")
        self.add(title)
        self.play(FadeIn(title))
        self.wait()
        self.play(Transform(title, subtitle))

class QuestionShowUp(Scene) :
    def construct(self) :
        question_part1 = Tex(r"已知 $\Delta ABC$ 的面积为 ", font_size = 27)
        question_part2 = Tex(r"$\displaystyle\frac{1}{4}$", color = RED_A, font_size = 27)
        question_part3 = Tex(r"，若 ", font_size = 27)
        question_part4 = Tex(r"$\cos 2A + \cos 2B + 2\sin C = 2$", color = RED_A, font_size = 27)
        question_part5 = Tex(r"$\displaystyle\cos A\cos B\sin C = \frac{1}{4}$", color = RED_A, font_size = 27)
        question_part6 = Tex(r"，则", font_size = 27)
        question_part7 = Tex(r"A.$\sin C = \sin^2 A + \sin^2 B$", font_size = 27)
        question_part8 = Tex(r"B.$AB = \sqrt{2}$", font_size = 27)
        question_part9 = Tex(r"C.$\displaystyle\sin A + \sin B = \frac{\sqrt{6}}{2}$", font_size = 27)
        question_part10 = Tex(r"D.$AC^2 + BC^2 = 3$", font_size = 27)

        question_line1 = VGroup(
            question_part1,
            question_part2,
            question_part3,
            question_part4
        ).arrange(RIGHT, buff = 0.1)

        question_line2 = VGroup(
            question_part5,
            question_part6
        ).arrange(RIGHT, buff = 0.1)

        question_line3 = VGroup(
            question_part7,
            question_part8
        ).arrange(RIGHT, buff = 0.1)

        question_line4 = VGroup(
            question_part9,
            question_part10
        ).arrange(RIGHT, buff = 0.1)

        question = VGroup(
            question_line1,
            question_line2,
            question_line3,
            question_line4,
        ).arrange(DOWN, buff = 0.2)

        question_part7.align_to(question_line1, LEFT)
        question_part9.align_to(question_line1, LEFT)
        question_part10.align_to(question_line1, RIGHT)
        question_part8.align_to(question_part10, LEFT)
        question_line2.align_to(question_line1, LEFT)
        question.to_edge(UL)

        self.add(question)
        self.play(FadeIn(question))
