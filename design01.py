#!/usr/bin/python3


# fonts used:
#
# Render font is IBM Plex Mono
# Rendered in alacritty
# ASCII Fonts: DiamFont

from time import sleep
import os
import re
import random

from terminaltexteffects.engine.terminal import Terminal
from terminaltexteffects.effects import effect_rain, effect_beams, effect_middleout, effect_binarypath
from terminaltexteffects.utils.graphics import Color
from terminaltexteffects.utils.graphics import Gradient
from terminaltexteffects.utils.easing import (
    out_quad, out_cubic, in_out_quad
)

effect_map = {
    'beams': lambda prompt_text:
        (lambda effect: (
            setattr(effect.effect_config, 'beam_gradient_stops', (Color("00ffff"), Color("ff00ff"))),
            setattr(effect.effect_config, 'beam_gradient_steps', (4, 6, 10)),
            setattr(effect.effect_config, 'final_gradient_stops', (Color("4080ff"), Color("aa40ff"), Color("FFFF55"))),
            setattr(effect.effect_config, 'final_gradient_steps', (2,3,8)),
            setattr(effect.effect_config, 'final_wipe_speed', 3),
            effect
        )[-1])(effect_beams.Beams(prompt_text)),

    'rain': lambda prompt_text: 
        (lambda effect: (
            setattr(effect.effect_config, 'rain_colors', (Color("00ff88"), Color("eeff00"), Color("ff00ff"))),
            setattr(effect.effect_config, 'rain_symbols', (".", ",", ":", "|", "*")),
            setattr(effect.effect_config, 'final_gradient_stops', (Color("0044ff"), Color("00ffff"), Color("ffAAff"))),
            setattr(effect.effect_config, 'final_gradient_steps', (15, 25, 2)),
            setattr(effect.effect_config, 'easing', out_quad),
            effect
        )[-1])(effect_rain.Rain(prompt_text)),


    'middleout': lambda prompt_text:
        (lambda effect: (
            setattr(effect.effect_config, 'starting_color', Color("ffffff")),
            setattr(effect.effect_config, 'final_gradient_stops', (Color("ff00ff"), Color("00ffff"), Color("ffff00"))),
            setattr(effect.effect_config, 'final_gradient_steps', (10, 8, 20)),
            setattr(effect.effect_config, 'expand_direction', 'horizontal'),
            setattr(effect.effect_config, 'center_movement_speed', 0.4),
            setattr(effect.effect_config, 'full_movement_speed', 0.5),
            setattr(effect.effect_config, 'center_easing', out_cubic),
            setattr(effect.effect_config, 'full_easing', in_out_quad),
            effect
        )[-1])(effect_middleout.MiddleOut(prompt_text)),

    'binarypath': lambda prompt_text:
        (lambda effect: (
            setattr(effect.effect_config, 'final_gradient_stops', (Color("00ff00"), Color("00ffff"), Color("ff00ff"))),
            setattr(effect.effect_config, 'final_gradient_steps', (10, 15)),
            setattr(effect.effect_config, 'binary_colors', (Color("e6e6e6"), Color("99cc99"), Color("99cccc"))),
            setattr(effect.effect_config, 'movement_speed', 1),
            setattr(effect.effect_config, 'active_binary_groups', 1.7),
            effect
        )[-1])(effect_binarypath.BinaryPath(prompt_text))
}


frame_files = [f for f in os.listdir() if f.endswith('.txt')]
frame_files.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))

for frame_file in frame_files:
    effect_name = frame_file.split('_')[0]
    with open(frame_file, 'r', encoding='utf-8') as file:
        content = file.read()
        effect_class = effect_map.get(re.split(r'\s+', content.lower())[0])
        effect_pause = int(re.split(r'\s+', content.lower())[1])
        content = re.sub(r'^\w+\s+\d+',
                         lambda x: ' ' * len(x.group()), content)

        if effect_class:
            effect = effect_class(content)

            effect.terminal_config.frame_rate = 120
            effect.terminal_config.canvas_width = 96
            effect.terminal_config.canvas_height = 55

            effect.effect_config.merge = True


        # effect.terminal.move_cursor_to_top()
        # with effect.terminal_output() as terminal:
        terminal = Terminal(effect.input_data, effect.terminal_config)
        terminal.prep_canvas()
        # terminal.move_cursor_to_top()
        for frame in effect:
            terminal.print(frame)

        sleep(effect_pause)

sleep(3)
