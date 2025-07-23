import matplotlib.pyplot as plt
from PIL import Image
import os
import shutil

# ====== Configuration ====== #
OUTPUT_DIR = "frames"
GIF_PATH = "output.gif"
IMAGE_WIDTH = 5
IMAGE_HEIGHT = 2
FONT_SIZE = 10
FONT_COLOR = "#00FF00"
FONT_FAMILY = "monospace"
BG_COLOR = "black"
TYPING_SPEED = 40
ENCRYPT_SPEED = 120
SCRAMBLE_SPEED = 120
SHUTDOWN_SPEED = 180
FINAL_HOLD_COUNT = 10
FINAL_HOLD_DURATION = 250
MAX_VISIBLE_LINES = 10

# ====== Message Constants ====== #
BOOT_LINES = [
    "$ ./start.sh",
    "",
    "[BOOT] Initializing neural shell...",
    "[SYS ] Authenticating identity: Jung Jin Woo",
    "[SYS ] Authenticating code name: blackJJW",
    "[IO  ] Injecting cognitive modules... success",
    "[MEM ] Mounting development stack: Full Stack, MLOps"
]

ENCRYPT_BASE = "[SEC ] Encrypting credentials..."

CONTINUE_LINES = [
    "[CORE] Launching autonomous agent...",
    "[✔] Consciousness online.",
    "[SYS ] Terminal ready.",
    ">>>",
    ""
]

MAIN_INFO = '''
NAME    : Jung Jin Woo
JOB     : AI-focused Full Stack & MLOps Engineer
LOCATION: South Korea
RESUME  : github.com/blackJJW/resume
BLOG    : blackjjw.github.io
EMAIL   : jjinwoo92@gmail.com
'''.strip("\n") + "\n\n"

DISENGAGE_LINE = "[CORE] Disengaging autonomous agent..."

SCRAMBLE_BASE = "[SEC ] Scrambling credentials..."

SHUTDOWN_LINES = [
    "[MEM ] Unmounting development stack...",
    "[IO  ] Releasing cognitive modules...",
    "[SYS ] Closing terminal session...",
    "[SYS ] Identity: blackJJW signed out.",
    "[✔] Consciousness offline. Uplink terminated.",
    ">>>",
    ""
]

# ====== Setup ====== #
os.makedirs(OUTPUT_DIR, exist_ok=True)
images, durations = [], []
frame_idx = 0

# ====== Frame Renderer ====== #
def render_frame(text_lines, duration):
    global frame_idx
    fig, ax = plt.subplots(figsize=(IMAGE_WIDTH, IMAGE_HEIGHT))
    fig.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.10)
    ax.set_facecolor(BG_COLOR)
    fig.patch.set_facecolor(BG_COLOR)
    ax.axis('off')
    ax.text(0, 1, "\n".join(text_lines), va='top', ha='left',
            fontsize=FONT_SIZE, fontfamily=FONT_FAMILY, color=FONT_COLOR, transform=ax.transAxes)
    path = os.path.join(OUTPUT_DIR, f"frame_{frame_idx:03}.png")
    plt.savefig(path, dpi=100)
    images.append(Image.open(path))
    durations.append(duration)
    plt.close()
    frame_idx += 1

# ====== Animation Helpers ====== #
def render_accumulating_lines(base, lines, speed):
    for line in lines:
        base.append(line)
        render_frame(base[-MAX_VISIBLE_LINES:], speed)

def render_block_animation(prefix, base_lines, block_count, speed):
    for i in range(1, block_count + 1):
        line = f"{prefix} {'█ ' * i}".strip()
        render_frame((base_lines + [line])[-MAX_VISIBLE_LINES:], speed)
    return (base_lines + [f"{prefix} {'█ ' * block_count}".strip()])[-MAX_VISIBLE_LINES:]

def render_typing_animation(base_lines, text, speed):
    for i in range(1, len(text) + 1):
        for blink in [True, False]:
            cursor = "|" if blink else " "
            full_text = "\n".join(base_lines) + "\n" + text[:i] + cursor
            render_frame(full_text.splitlines()[-MAX_VISIBLE_LINES:], speed)

def render_scroll_sequence(prefix, lines, speed):
    scroll_base = prefix.copy()
    for i in range(len(lines)):
        scroll_base.append(lines[i])
        visible = scroll_base[-MAX_VISIBLE_LINES:]
        render_frame(visible, speed)

# ====== Boot Sequence ====== #
def main():
    boot_text = []
    render_accumulating_lines(boot_text, BOOT_LINES, TYPING_SPEED)

    boot_text = render_block_animation(ENCRYPT_BASE, BOOT_LINES.copy(), 10, ENCRYPT_SPEED)

    render_accumulating_lines(boot_text, CONTINUE_LINES, TYPING_SPEED)

    render_typing_animation(boot_text, MAIN_INFO, TYPING_SPEED)

    scramble_prefix = (
        boot_text
        + MAIN_INFO.splitlines()
        + ["", DISENGAGE_LINE]
    )
    scramble_prefix = scramble_prefix[-MAX_VISIBLE_LINES:]  # ensure scroll starts from bottom
    scrambled_text = render_block_animation(SCRAMBLE_BASE, scramble_prefix, 10, SCRAMBLE_SPEED)
    scrambled_text = scrambled_text[-MAX_VISIBLE_LINES:]

    render_scroll_sequence(scrambled_text, SHUTDOWN_LINES, SHUTDOWN_SPEED)

    for _ in range(FINAL_HOLD_COUNT):
        images.append(images[-1].copy())
        durations.append(FINAL_HOLD_DURATION)

    images[0].save(GIF_PATH, save_all=True,
                   append_images=images[1:], duration=durations, loop=0)
    print(f"Done: {GIF_PATH}")

    shutil.rmtree(OUTPUT_DIR)
    print(f"Cleaned up frame directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
