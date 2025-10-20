from manim import *

# Color palette inspired by the provided reference image
DARK_NAVY = "#05021f"
DEEP_INDIGO = "#0b1551"
MID_BLUE = "#172874"
ACCENT_PERIWINKLE = "#5e6fc8"
STRIPE_BLUE = "#2e3a7a"


def create_urban_night_background() -> VGroup:
    """Return a stylised background that borrows the blues and diagonal accent from the reference image."""
    frame_width = config.frame_width
    frame_height = config.frame_height

    base_rect = Rectangle(width=frame_width * 1.4, height=frame_height * 1.4)
    base_rect.set_fill(color=[DARK_NAVY, DEEP_INDIGO], opacity=1)
    base_rect.set_stroke(width=0)
    base_rect.set_z_index(-20)

    horizon_overlay = Rectangle(width=frame_width * 1.4, height=frame_height * 0.55)
    horizon_overlay.set_fill(color=[DEEP_INDIGO, MID_BLUE], opacity=0.95)
    horizon_overlay.set_stroke(width=0)
    horizon_overlay.align_to(base_rect, DOWN)
    horizon_overlay.set_z_index(-19)

    accent_triangle = Polygon(
        np.array([-frame_width * 0.52, -frame_height * 0.5, 0]),
        np.array([-frame_width * 0.52, frame_height * 0.05, 0]),
        np.array([-frame_width * 0.18, -frame_height * 0.5, 0]),
    )
    accent_triangle.set_fill(color=ACCENT_PERIWINKLE, opacity=0.85)
    accent_triangle.set_stroke(width=0)
    accent_triangle.set_z_index(-18)

    stripe_group = VGroup()
    stripe_width = frame_width * 0.32
    stripe_height = frame_height * 0.08
    for i in range(4):
        stripe = Rectangle(width=stripe_width, height=stripe_height)
        stripe.set_fill(color=STRIPE_BLUE, opacity=0.85)
        stripe.set_stroke(width=0)
        stripe.set_z_index(-17)
        stripe.align_to(base_rect, DOWN + LEFT)
        stripe.shift(RIGHT * stripe_width * 0.78 * i + UP * stripe_height * 0.8)
        stripe_group.add(stripe)

    return VGroup(base_rect, horizon_overlay, accent_triangle, stripe_group)


class DopplerEquation(Scene):
    def construct(self):
        self.camera.background_color = DARK_NAVY
        background = create_urban_night_background()
        self.add(background)
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
        equation.scale(0.9)

        panel_width = 4.0
        panel_height = 2.4
        stationary_panel = RoundedRectangle(width=panel_width, height=panel_height, corner_radius=0.25)
        stationary_panel.set_stroke(color=ACCENT_PERIWINKLE, width=2)
        stationary_panel.set_fill(color=DEEP_INDIGO, opacity=0.7)

        stationary_title = Text("Stationary source", font_size=24)
        stationary_title.next_to(stationary_panel, UP, buff=0.5)

        stationary_source = Dot(color=YELLOW).scale(1.2)
        stationary_source.move_to(stationary_panel.get_center() + DOWN * 0.1)

        stationary_waves = VGroup()
        for radius in [0.5, 0.9, 1.3]:
            wave = Circle(radius=radius)
            wave.set_stroke(color=ACCENT_PERIWINKLE, width=3, opacity=0.75)
            wave.move_to(stationary_source.get_center())
            stationary_waves.add(wave)

        observer_distance = 1.4
        stationary_left_observer = Dot(color=GREEN).scale(1.0)
        stationary_left_observer.move_to(stationary_source.get_center() + LEFT * observer_distance)
        stationary_right_observer = stationary_left_observer.copy()
        stationary_right_observer.move_to(stationary_source.get_center() + RIGHT * observer_distance)

        stationary_caption = Text("Waves spread evenly → same pitch", font_size=20, color=GREEN)
        stationary_caption.next_to(stationary_panel, DOWN, buff=0.4)

        moving_panel = stationary_panel.copy()

        moving_title = Text("Source moving right", font_size=24)
        moving_title.next_to(moving_panel, UP, buff=0.5)

        moving_source = Dot(color=YELLOW).scale(1.2)
        moving_source.move_to(moving_panel.get_center() + DOWN * 0.1 + LEFT * 0.35)

        moving_waves = VGroup()
        for index, radius in enumerate([0.5, 0.9, 1.3]):
            wave = Circle(radius=radius)
            wave.set_stroke(color=ACCENT_PERIWINKLE, width=3, opacity=0.75)
            wave.move_to(moving_source.get_center() + LEFT * 0.3 * index)
            moving_waves.add(wave)

        front_observer = Dot(color=BLUE).scale(1.0)
        front_observer.move_to(moving_source.get_center() + RIGHT * 1.8)
        rear_observer = Dot(color=GREEN).scale(1.0)
        rear_observer.move_to(moving_source.get_center() + LEFT * 2.0)

        approaching_label = Text("Approaching → higher pitch", font_size=20, color=BLUE)
        receding_label = Text("Receding → lower pitch", font_size=20, color=GREEN)
        observer_labels = VGroup(receding_label, approaching_label)
        observer_labels.arrange(RIGHT, buff=0.6)
        observer_labels.next_to(moving_panel, DOWN, buff=0.4)

        velocity_arrow = Arrow(
            start=moving_source.get_center() + LEFT * 1.1,
            end=moving_source.get_center() + RIGHT * 1.1,
            buff=0.2,
            color=YELLOW,
        )
        velocity_arrow.shift(UP * 0.7)
        velocity_label = Text("Source motion", font_size=20, color=YELLOW)
        velocity_label.next_to(velocity_arrow, UP, buff=0.04)

        stationary_inner = VGroup(
            stationary_title,
            stationary_source,
            stationary_waves,
            stationary_left_observer,
            stationary_right_observer,
            stationary_caption,
        )
        stationary_inner.scale(0.8, about_point=stationary_panel.get_center())

        moving_inner = VGroup(
            moving_title,
            moving_source,
            moving_waves,
            front_observer,
            rear_observer,
            observer_labels,
            velocity_arrow,
            velocity_label,
        )
        moving_inner.scale(0.8, about_point=moving_panel.get_center())

        stationary_group = VGroup(
            stationary_panel,
            stationary_title,
            stationary_source,
            stationary_waves,
            stationary_left_observer,
            stationary_right_observer,
            stationary_caption,
        )
        moving_group = VGroup(
            moving_panel,
            moving_title,
            moving_source,
            moving_waves,
            front_observer,
            rear_observer,
            observer_labels,
            velocity_arrow,
            velocity_label,
        )

        visual_group = VGroup(stationary_group, moving_group)
        visual_group.arrange(RIGHT, buff=0.9, aligned_edge=DOWN)
        visual_group.shift(DOWN * 0.2)

        self.play(Write(title))

        self.play(FadeIn(stationary_panel), FadeIn(stationary_title))
        self.play(FadeIn(stationary_source))
        self.play(LaggedStart(*[Create(wave) for wave in stationary_waves], lag_ratio=0.15, run_time=1.2))
        self.play(FadeIn(VGroup(stationary_left_observer, stationary_right_observer)))
        self.play(FadeIn(stationary_caption))
        self.wait(0.3)

        self.play(FadeIn(moving_panel), FadeIn(moving_title))
        self.play(FadeIn(moving_source))
        self.play(GrowArrow(velocity_arrow), FadeIn(velocity_label))
        self.play(LaggedStart(*[Create(wave) for wave in moving_waves], lag_ratio=0.1, run_time=1.2))
        self.play(FadeIn(VGroup(front_observer, rear_observer)))
        self.play(FadeIn(observer_labels))
        self.wait(1)



        

        self.play(FadeOut(visual_group), Write(equation))
        self.wait(1)

        

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

        self.wait(1)

        self.play(ShrinkToCenter(numerator_brace), FadeOut(numerator_text), ShrinkToCenter(denominator_brace), FadeOut(denominator_text))

        light_title = Text('Doppler Effect (For Light)', font_size=60)

        light_title.to_edge(UP)
        equation.next_to(light_title, DOWN, buff=1.2)

        self.play(ReplacementTransform(title,light_title))



        light_equation = MathTex(r"\lambda_{o}=\lambda_{s}\sqrt{\frac{1+\frac{v}{c}}{1-\frac{v}{c}}}",font_size=66)
        light_equation[0][0].set_color(RED)

        light_equation[0][3].set_color(RED)

        light_equation[0][9].set_color(BLUE)
        light_equation[0][15].set_color(BLUE)
        light_equation[0][11].set_color(ORANGE)
        light_equation[0][17].set_color(ORANGE)

        self.play(ReplacementTransform(equation,light_equation))
        self.wait(1)
        self.play(light_equation.animate.to_edge(LEFT, buff=1.2))

        observer_text = Text("Velocity of the source (v)", font_size=32)
        sol_explain = Text("Speed of light (c)", font_size=32)

        labels_group = VGroup(observer_text, sol_explain)
        labels_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        labels_group.next_to(light_equation, RIGHT, buff=0.8)

        observer_arrow = Arrow(
            start=observer_text.get_left() + RIGHT * 0.15,
            end=light_equation[0][9].get_center(),
            buff=0.1,
        )
        sol_arrow = Arrow(
            start=sol_explain.get_left() + RIGHT * 0.15,
            end=light_equation[0][17].get_center(),
            buff=0.1,
        )
        self.play(FadeIn(observer_text),FadeIn(sol_explain),Create(observer_arrow),Create(sol_arrow))

        self.wait(1)

        self.play(FadeOut(light_equation),FadeOut(light_title),FadeOut(observer_arrow),FadeOut(observer_text),FadeOut(sol_arrow),FadeOut(sol_explain))
        
class WindSpeedExample(Scene):
    def construct(self):
        self.camera.background_color = DARK_NAVY
        background = create_urban_night_background()
        self.add(background)
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

        freq_readings = VGroup(
            MathTex(r"f_{\text{sent}} = 193.0~\text{THz}", font_size=44),
            MathTex(r"f_{\text{return}} = 193.000004~\text{THz}", font_size=44),
        )
        freq_readings.arrange(DOWN, aligned_edge=LEFT, buff=0.3)

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

        c_value = MathTex(r"c = 3.00\times10^{8}~\text{m/s}", font_size=42)
        c_value.set_color_by_tex(r"c", GREEN)

        freq_column = VGroup(freq_readings, c_value)
        freq_column.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        freq_column.to_edge(RIGHT).shift(UP * 0.6)

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

        answer_box = SurroundingRectangle(solve_eq)

        info_group = VGroup(freq_column, relativistic_note)


        self.play(Write(title))
        self.play(Create(ground))
        self.play(FadeIn(radar))
        self.play(FadeIn(cloud), FadeIn(cloud_label))

        self.wait(1)

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

        self.wait(1)

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
        )
        self.play(FadeOut(scene_elements))

        self.play(FadeIn(freq_readings[0]))
        self.play(FadeIn(freq_readings[1]))
        self.play(FadeIn(c_value))
        self.play(FadeIn(relativistic_note))
        self.wait(1)
        self.play(Write(doppler_eq))    
        self.wait(1)  


        current_equation = doppler_eq
        self.wait(0.3)

        self.play(ReplacementTransform(current_equation, ratio_eq))
        self.wait(1)
        current_equation = ratio_eq

        self.play(ReplacementTransform(current_equation, substitution_eq))
        current_equation = substitution_eq
        self.wait(1)

        self.play(Write(freq_ratio))
        self.wait(1)
        self.play(Write(solve_eq))
        self.play(Create(answer_box))

        self.wait(1)

        fade_list = [
            current_equation,
            freq_ratio,
            solve_eq,
            answer_box,
            title
        ]
        self.play(*[FadeOut(mob) for mob in fade_list])
        self.play(FadeOut(info_group))
        self.wait(0.5)
 
