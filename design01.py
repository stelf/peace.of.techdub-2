from terminaltexteffects.effects import effect_rain
effect = effect_rain.Rain("your text here")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)
