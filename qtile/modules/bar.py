import dbus
import iwlib
import os
import subprocess
from libqtile import bar, layout, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration, BorderDecoration


decor={
        'decorations':[
            PowerLineDecoration(#colour="#2e4b50",
                               #colour="#9c2932",
                               use_widget_background=True, 
                               path='forward_slash'
                               )
            ]}

def init_og_screen():
    return [
            Screen(top=bar.Bar(
                [
                    widget.GroupBox(highlight_method='line',
                                    background='9c2932',
                                    highlight_color=['cf3540','cf3540'],
                                    ),

                    widget.CurrentLayout(background='9c2932'),

                    widget.Sep(background='9c2932', linewidth=0,
                            decorations=[
                                PowerLineDecoration(
                                    path='rounded_left',
                                    colour='9c2932'
                                    )
                                ]
                            ),

                    widget.WindowTabs(background='0a0914'),

                    widget.KeyboardLayout(
                        configured_keyboards=['us','es'],
                        background='0a0914',
                            foreground='ffffff'
                    ), #it's hided bc this ^^^^

                    widget.Systray(background='0a0914'),

                    widget.Sep(background='0a0914',
                            linewidth=0,
                            decorations=[
                                PowerLineDecoration(
                                    path='rounded_right',
                                    colour='9c2932'
                                    )
                                ]
                            ),

                    widget.WiFiIcon(interface='wlp4s0',
                                    background='9c2932',
                    ),
                    widget.Sep(background='9c2932', linewidth=0, **decor),
                    widget.UPowerWidget(background='cf3540'),
                    widget.Sep(background='cf3540', linewidth=0, **decor),
                    widget.Volume(step=2,fmt='vol: {}',background='9c2932'),
                    widget.Sep(background='9c2932', linewidth=0, **decor),
                    widget.Clock(format="%a, %b %d - %H:%M",background='cf3540'),
                    ],
                24,
            ),
        ),
    ]

def init_second_screen():
    return [
            Screen(top=bar.Bar(
                [
                    widget.GroupBox(highlight_method='line',
                                    background='0a0914',
                                    highlight_color=['cf3540','cf3540'],
                                    ),

                    widget.CurrentLayout(background='0a0914'),

                    widget.Spacer(length=6),

                    widget.WindowTabs(background='0a0914'),

                    widget.KeyboardLayout(
                        configured_keyboards=['us','es'],
                        background='0a0914',
                            foreground='ffffff'
                    ),

                    widget.Systray(background='0a0914'),

                    widget.Spacer(length=6),

                    widget.WiFiIcon(interface='wlp4s0',
                                    background='0a0914',
                                    decorations=[
                                        BorderDecoration(
                                        colour = 'cf4540',
                                        border_width = [0, 0, 2, 0]
                                    )]
                    ),

                    widget.UPowerWidget(background='0a0914',
                                    decorations=[
                                BorderDecoration(
                                    colour = 'cf4540',
                                    border_width = [0, 0, 2, 0]
                                )]),
                    widget.Spacer(length=6),

                    widget.Volume(step=2,fmt='vol: {}',background='0a0914',
                                decorations=[
                                BorderDecoration(
                                    colour = 'cf4540',
                                    border_width = [0, 0, 2, 0]
                                )]),
                    widget.Spacer(length=6),

                    widget.Clock(format="%a, %b %d - %H:%M",background='0a0914',
                                decorations=[
                                BorderDecoration(
                                    colour = 'cf4540',
                                    border_width = [0, 0, 2, 0]
                                )
                                ]),
                    ],
                24,
            ),
        ),
    ]

#screens = init_og_screen()
screens = init_second_screen()
