from manim import *
from manim.opengl import *

# Pyglet key constants
from pyglet.window import key

config.renderer = 'opengl'
config.write_to_movie = False
config.preview = True

class KeyboardScene(Scene):
    def construct(self):
        # we're using self so it's available throughout the scene
        self.circle = Circle(color=BLUE)

        self.play(Write(self.circle))

        self.interactive_embed()

        self.play(FadeOut(self.circle))

    def on_key_press(self, symbol, modifiers):
        """Called each time a key is pressed."""
        # grow the circle when plus is pressed
        if symbol == key.SPACE:
            self.play(self.circle.animate.scale(2))

        # shrink it when minus is pressed
        elif symbol == key.MINUS:
            self.play(self.circle.animate.scale(1 / 2))

        # so we can still use the default controls
        super().on_key_press(symbol, modifiers)