from time import sleep
import os
import re

from terminaltexteffects.engine.terminal import Terminal
from terminaltexteffects.effects import effect_rain, effect_beams, effect_middleout

effect_map = {
    'rain': effect_rain.Rain,
    'beams': effect_beams.Beams,
    'middleout': effect_middleout.MiddleOut
}
frame_files = [f for f in os.listdir() if f.endswith('.txt')]
frame_files.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))

for frame_file in frame_files:
    # rest of the code

    effect_name = frame_file.split('_')[0]
    with open(frame_file, 'r') as file:
        content = file.read()
        effect_class = effect_map.get(re.split(r'\s+', content.lower())[0])
        content = re.sub(r'^\w+', lambda x: ' ' * len(x.group()), content)

        if effect_class:
            effect = effect_class(content)

            effect.terminal_config.frame_rate = 120
            effect.terminal_config.canvas_width = 80
            effect.terminal_config.canvas_height = 32

            effect.effect_config.merge = True

        # effect.terminal.move_cursor_to_top()
        # with effect.terminal_output() as terminal:
        terminal = Terminal(effect.input_data, effect.terminal_config)
        # terminal.move_cursor_to_top()
        for frame in effect:
            terminal.print(frame)

        sleep(2)
