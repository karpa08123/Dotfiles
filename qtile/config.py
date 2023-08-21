############################# IMPORTS ########################################
import dbus
import iwlib
import os
import subprocess
from libqtile import bar, layout, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration
##############################################################################

mod = "mod4"
terminal = "alacritty"

################################## KEYS ######################################
# A list of available commands that can be bound to keys can be found
# at https://docs.qtile.org/en/latest/manual/config/lazy.html

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows. Move windows to a unexisting place will generate new rows/columns
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    #Volume control
    Key((), "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 2%+")),
    Key((), "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 2%-")),
    Key((), "XF86AudioMute", lazy.spawn("amixer sset Master toggle")),
    #Debes averiguar como configurar la tecla para mutear el audio. idea: XF86

    #Brightness control
    Key((), "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key((), "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    #Print Screen
    Key((), "Print", lazy.spawn('scrot -s -f "%d-%m-%y_%H:%M:%S.png" -e "mv $f ~/Imágenes/Screenshots"')),

    #Mic mute
    Key((), "XF86AudioMicMute", lazy.spawn("amixer sset Capture toggle")),

    KeyChord([mod], "z", [
        Key([], "r", lazy.spawn("rofi -show drun"), desc="Spawn rofi in run mode"),
        Key([], "f", lazy.spawn("rofi -show filebrowser"), desc="Spawn rofi in file mode"),
        Key([], "c", lazy.spawn("rofi -show calc"), desc="Spawn rofi in calculator mode")
    ])

]

############################### GROUPS #######################################
groups = []

groups_names = ["1","2","3","4","5"]

group_labels = ["</>", "@", "CHAT", "FILES", "EXTRA"]
#group_labels = ["1", "2", "3", "4", "5"]


group_layouts = ["columns", "max", "max", "columns", "columns"]

for i in range(len(groups_names)):
    groups.append(
        Group(
            name=groups_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name),),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc="Move focused window to group {}".format(i.name),),

        ]
    )

############################# LAYOUTS ########################################
layout_theme={
    'border_width':2,
    'margin':8,
    'border_focus':"#cf000f",
    'border_normal':"#5c181d",
    'border_on_single':False
}

# nota 15/08/23 16:25 : Deberias experimentar con mas layouts diferentes. Suena muy interesante pero por ahora prefieres no hacerlo.
layouts = [
    layout.Columns(
        name='Columns',
        **layout_theme
        ),
    #layout.Floating(),
    layout.Max(name='Max')
]

widget_defaults = dict(
    font="Source Code Pro",
    fontsize=12,
    padding=3,
    opacity=0.0)
extension_defaults = widget_defaults.copy()

decor={
        'decorations':[
            PowerLineDecoration(#colour="#2e4b50",
                               #colour="#9c2932",
                               use_widget_background=True, 
                               path='forward_slash'
                               )
            ]}

######################### Bar ################################################
screens = [
    Screen(
        wallpaper='~/Imágenes/Wallpapers/Unmodified/animeLighthouse.png',
        wallpaper_mode='fill',

########################## WIDGETS ###########################################
        top=bar.Bar([
                widget.Image(filename='~/.config/qtile/manjaro.256x256.png',scale='false', margin=3,),
                widget.Sep(background='0a0914', linewidth=0,
                           decorations=[
                               PowerLineDecoration(
                                   path='rounded_right' 
                                   )
                               ]
                           ),
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
                widget.Sep(background='0a0914',
                           linewidth=0,
                           decorations=[
                               PowerLineDecoration(
                                   path='rounded_right',
                                   colour='9c2932'
                                   )
                               ]
                           ),
                widget.WiFiIcon(interface='wlp4s0',background='9c2932'),
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
##############################################################################

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'Qtile'
