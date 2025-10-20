from manim import *



class DopplerEquation(Scene):
    def construct(self):
        title = Text("Doppler Effect", font_size=60)
        equation = MathTex(
            r"f_{o}=f_{s}\left(\frac{v\pm v_{o}}{v\mp v_{s}}\right)",
            font_size=72,
        )


        equation[0][0].set_color(RED)

        equation[0][3].set_color(RED)

        equation[0][6].set_color(BLUE)
        equation[0][8].set_color(GREEN)
        equation[0][9].set_color(GREEN)
        equation[0][11].set_color(BLUE)
        equation[0][13].set_color(ORANGE)
        equation[0][14].set_color(ORANGE)


        

        title.to_edge(UP)
        equation.next_to(title, DOWN, buff=2)

        self.play(Write(title))
        self.play(Write(equation))


        numerator_term = VGroup(*[equation[0][i] for i in range(6, 10)])
        denominator_term = VGroup(*[equation[0][i] for i in range(11, 15)])

        numerator_brace = Brace(numerator_term, direction=UP)
        numerator_text = Text("Observer motion", font_size=32)
        numerator_text.next_to(numerator_brace, UP)

        denominator_brace = Brace(denominator_term, direction=DOWN)
        denominator_text = Text("Source motion", font_size=32)
        denominator_text.next_to(denominator_brace, DOWN)

        self.play(GrowFromCenter(numerator_brace), FadeIn(numerator_text))
        self.play(GrowFromCenter(denominator_brace), FadeIn(denominator_text))

        self.play(ShrinkToCenter(numerator_brace), FadeOut(numerator_text), ShrinkToCenter(denominator_brace), FadeOut(denominator_text))



        light_title = Text('Doppler Effect (For Light)', font_size=60)

        light_title.to_edge(UP)
        equation.next_to(light_title, DOWN, buff=2)

        self.play(ReplacementTransform(title,light_title))



        light_equation = MathTex(r"\lambda_{o}=\lambda_{s}\sqrt{\frac{1+\frac{v}{c}}{1-\frac{v}{c}}}",font_size=72)
        light_equation[0][0].set_color(RED)

        light_equation[0][3].set_color(RED)

        light_equation[0][9].set_color(BLUE)
        light_equation[0][15].set_color(BLUE)
        light_equation[0][11].set_color(ORANGE)
        light_equation[0][17].set_color(ORANGE)

        self.play(ReplacementTransform(equation,light_equation))
        self.play(light_equation.animate.to_edge(LEFT))


        observer_text = Text("Velosity of the sourse")
        sol_explain = Text("Speed of light")

        observer_text.shift(UP*0.5)
        sol_explain.shift(DOWN*0.5)
        observer_text.shift(RIGHT*3)
        sol_explain.shift(RIGHT*3)
        observer_arrow = Arrow(start=observer_text[0].get_center(), end=light_equation[0][9].get_center())
        sol_arrow = Arrow(start=sol_explain[0].get_center(), end=light_equation[0][17].get_center())
        self.play(FadeIn(observer_text),FadeIn(sol_explain),Create(observer_arrow),Create(sol_arrow))

        self.play(FadeOut(light_equation),FadeOut(light_title),FadeOut(observer_arrow),FadeOut(observer_text),FadeOut(sol_arrow),FadeOut(sol_explain))
        
class WindSpeedExample(Scene):
    def construct(self):
        title = Text("Measuring Wind Speed with Doppler", font_size=48)
        title.to_edge(UP)

        ground = Line(LEFT * 6 + DOWN * 2, RIGHT * 6 + DOWN * 2, color=GRAY)

        radar_label = Text("Radar", font_size=30)
        radar_base = Rectangle(height=0.4, width=1.0, color=BLUE, fill_opacity=0.6)
        radar_dish = Triangle(color=BLUE, fill_opacity=0.6).scale(0.5)
        radar_dish.rotate(-PI / 2)
        radar_dish.next_to(radar_base, UP, buff=0)
        radar_label.next_to(radar_dish, UP)
        radar = VGroup(radar_base, radar_dish, radar_label).shift(LEFT * 4 + DOWN * 1.4)

        cloud = Ellipse(width=2.6, height=1.4, color=GRAY_B)
        cloud.set_fill(GRAY_D, opacity=0.8)
        cloud.move_to(RIGHT * 3 + DOWN * 1.1)
        cloud_label = Text("Moving air parcel", font_size=30)
        cloud_label.next_to(cloud, UP)

        wind_arrow = Arrow(
            start=cloud.get_center() + RIGHT * 2.2,
            end=cloud.get_center() + RIGHT * 0.3,
            buff=0.1,
            color=GREEN_B,
        )
        wind_label = Text("Wind toward radar", font_size=28, color=GREEN_B)
        wind_label.next_to(wind_arrow, UP, buff=0.2)

        freq_info = VGroup(
            MathTex(r"f_{\text{sent}} = 193.0~\text{THz}", font_size=44),
            MathTex(r"f_{\text{return}} = 193.000004~\text{THz}", font_size=44),
        )
        freq_info.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        freq_info.to_edge(RIGHT).shift(UP * 0.5)

        doppler_eq = MathTex(
            r"f_{o}=f_{s}\sqrt{\frac{1+\frac{v_{\text{wind}}}{c}}{1-\frac{v_{\text{wind}}}{c}}}",
            font_size=56,
        )

        doppler_eq[0][0].set_color(RED)
        doppler_eq[0][1].set_color(RED)
        doppler_eq[0][3].set_color(BLUE)
        doppler_eq[0][4].set_color(BLUE)
        for i in range(9,14):
            doppler_eq[0][i].set_color(ORANGE)
        for i in range(19,24):
            doppler_eq[0][i].set_color(ORANGE)
        doppler_eq[0][15].set_color(GREEN)
        doppler_eq[0][25].set_color(GREEN)

        doppler_eq.to_edge(LEFT).shift(UP * 0.5)

        ratio_eq = MathTex(
            r"\left(\frac{f_{o}}{f_{s}}\right)^{2} = \frac{1+\frac{v_{\text{wind}}}{c}}{1-\frac{v_{\text{wind}}}{c}}",
            font_size=52,
        )

        ratio_eq[0][1].set_color(RED)
        ratio_eq[0][2].set_color(RED)
        ratio_eq[0][4].set_color(BLUE)
        ratio_eq[0][5].set_color(BLUE)
        for i in range(11, 16):
            ratio_eq[0][i].set_color(ORANGE)
        for i in range(21, 26):
            ratio_eq[0][i].set_color(ORANGE)

        ratio_eq.move_to(doppler_eq)

        substitution_eq = MathTex(
            r"v_{\text{wind}} = c \cdot \frac{\left(\frac{f_{o}}{f_{s}}\right)^{2} - 1}{\left(\frac{f_{o}}{f_{s}}\right)^{2} + 1}",
            font_size=50,
        )

        substitution_eq[0][6].set_color(GREEN)
        substitution_eq[0][9].set_color(RED)
        substitution_eq[0][10].set_color(RED)
        substitution_eq[0][20].set_color(RED)
        substitution_eq[0][21].set_color(RED)
        substitution_eq[0][12].set_color(BLUE)
        substitution_eq[0][13].set_color(BLUE)
        substitution_eq[0][23].set_color(BLUE)
        substitution_eq[0][24].set_color(BLUE)
        for i in range(0,5):
            substitution_eq[0][i].set_color(ORANGE)

        substitution_eq.move_to(ratio_eq)

        freq_ratio = MathTex(
            r"v_{\text{wind}} = c \cdot \frac{\left(\frac{193.000004}{193.0}\right)^{2} - 1}{\left(\frac{193.000004}{193.0}\right)^{2} + 1}",
            font_size=44,
        )
        freq_ratio[0][6].set_color(GREEN)
        for i in range(9,19):
            freq_ratio[0][i].set_color(RED)
        for i in range(31,41):
            freq_ratio[0][i].set_color(RED)
        for i in range(20,25):
            freq_ratio[0][i].set_color(BLUE)
        for i in range(42,47):
            freq_ratio[0][i].set_color(BLUE)
        for i in range(0,5):
            freq_ratio[0][i].set_color(ORANGE)

        freq_ratio.next_to(substitution_eq, DOWN, buff=0.4).align_to(substitution_eq, LEFT)

        solve_eq = MathTex(
            r"v_{\text{wind}} \approx 6.2~\text{m/s}",
            font_size=48,
        )
        for i in range(0,5):
            solve_eq[0][i].set_color(ORANGE)
        solve_eq.next_to(freq_ratio, DOWN, buff=0.4).align_to(freq_ratio, LEFT)

        relativistic_note = Text(
            "For LiDAR, use the relativistic Doppler formula",
            font_size=28,
        )
        relativistic_note.next_to(doppler_eq, UP, buff=0.3).align_to(doppler_eq, LEFT)

        c_value = MathTex(r"c = 3.00\times10^{8}~\text{m/s}", font_size=42)
        c_value.set_color_by_tex(r"c", GREEN)
        c_value.next_to(freq_info, DOWN, buff=0.4).align_to(freq_info, LEFT)

        answer_box = SurroundingRectangle(solve_eq)

        self.play(Write(title))
        self.play(Create(ground))
        self.play(FadeIn(radar))
        self.play(FadeIn(cloud), FadeIn(cloud_label))

        self.play(GrowArrow(wind_arrow), FadeIn(wind_label))
        self.play(
            cloud.animate.shift(LEFT * 0.6),
            wind_arrow.animate.shift(LEFT * 0.6),
            wind_label.animate.shift(LEFT * 0.6),
            rate_func=linear,
            run_time=2,
        )

        transmit_arrow = Arrow(
            start=radar.get_center() + RIGHT * 0.3,
            end=cloud.get_center() + LEFT * 0.3,
            buff=0.15,
            color=BLUE,
        )
        return_arrow = Arrow(
            start=cloud.get_center() + LEFT * 0.3,
            end=radar.get_center() + RIGHT * 0.3,
            buff=0.15,
            color=YELLOW,
        )
        send_label = Text("Transmitted tone", font_size=28, color=BLUE)
        send_label.next_to(transmit_arrow, UP, buff=0.25)
        return_label = Text("Shifted echo", font_size=28, color=YELLOW)
        return_label.next_to(return_arrow, DOWN, buff=0.25)

        self.play(GrowArrow(transmit_arrow), FadeIn(send_label))
        self.play(GrowArrow(return_arrow), FadeIn(return_label))

        scene_elements = VGroup(
            wind_arrow,
            wind_label,
            transmit_arrow,
            return_arrow,
            send_label,
            return_label,
            cloud_label,
            cloud,
            radar,
            ground,
            title,
        )
        self.play(FadeOut(scene_elements))

        self.play(FadeIn(freq_info[0]))
        self.play(FadeIn(freq_info[1]))

        self.play(FadeIn(c_value))


        self.play(FadeIn(relativistic_note))
        self.play(Write(doppler_eq))      
        current_equation = doppler_eq
        self.wait(0.3)

        self.play(ReplacementTransform(current_equation, ratio_eq))
        current_equation = ratio_eq
        self.wait(0.3)

        self.play(ReplacementTransform(current_equation, substitution_eq))
        current_equation = substitution_eq
        self.wait(0.3)

        self.play(Write(freq_ratio))
        self.wait(0.3)
        self.play(Write(solve_eq))
        self.play(Create(answer_box))

        fade_list = [
            current_equation,
            freq_ratio,
            solve_eq,
            relativistic_note,
            freq_info,
            c_value,
            answer_box
        ]
        self.play(*[FadeOut(mob) for mob in fade_list])
        self.wait(0.5)
 
