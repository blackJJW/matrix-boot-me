import matplotlib.pyplot as plt
from PIL import Image
import os
import shutil

# ====== Configuration ====== #
OUTPUT_DIR = "hybrid_frames"
GIF_PATH = "hybrid_typing_intro.gif"
IMAGE_WIDTH = 8
IMAGE_HEIGHT = 6
FONT_SIZE = 12
FONT_COLOR = "#00FF00"
FONT_FAMILY = "monospace"
BG_COLOR = "black"
TYPING_SPEED = 65
ENCRYPT_SPEED = 80
SCRAMBLE_SPEED = 80
SHUTDOWN_SPEED = 180
FINAL_HOLD_COUNT = 10
FINAL_HOLD_DURATION = 250
MAX_VISIBLE_LINES = 24

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

# ====== Boot Sequence ====== #
boot_lines = [
    "$ ./start.sh",
    "",
    "[BOOT] Initializing neural shell...",
    "[SYS ] Authenticating identity: Jung Jin Woo",
    "[SYS ] Authenticating code name: blackJJW",
    "[IO  ] Injecting cognitive modules... success",
    "[MEM ] Mounting development stack: Full Stack, MLOps"
]
boot_text = []
for line in boot_lines:
    boot_text.append(line)
    render_frame(boot_text, TYPING_SPEED)

# ====== Encrypt Animation ====== #
encrypt_base = "[SEC ] Encrypting credentials..."
num_blocks = 12
boot_text_base = boot_lines.copy()

for i in range(1, num_blocks + 1):
    line = f"{encrypt_base} {'█ ' * i}".strip()
    render_frame(boot_text_base + [line], ENCRYPT_SPEED)

boot_text = boot_text_base + [f"{encrypt_base} {'█ ' * num_blocks}".strip()]

# ====== Continue Boot ====== #
boot_continue = [
    "[CORE] Launching autonomous agent...",
    "[✔] Consciousness online.",
    "[SYS ] Terminal ready.",
    ">>>",
    ""
]
for line in boot_continue:
    boot_text.append(line)
    render_frame(boot_text, TYPING_SPEED)

# ====== Typing Main Info ====== #
main_text = """
NAME    : Jung Jin Woo
JOB     : AI-focused Full Stack & MLOps Engineer
LOCATION: South Korea
RESUME  : github.com/blackJJW/resume
BLOG    : blackjjw.github.io
EMAIL   : jjinwoo92@gmail.com
""".strip("\n") + "\n"

for i in range(1, len(main_text) + 1):
    for blink in [True, False]:
        cursor = "_" if blink else " "
        full_text = "\n".join(boot_text) + "\n" + main_text[:i] + cursor
        render_frame(full_text.splitlines(), TYPING_SPEED)

# ====== Scramble Animation ====== #
scramble_base = "[SEC ] Scrambling credentials..."
scramble_blocks = 10
scramble_prefix = boot_text + main_text.splitlines() + ["", "[CORE] Disengaging autonomous agent..."]

for i in range(1, scramble_blocks + 1):
    line = f"{scramble_base} {'█ ' * i}".strip()
    clipped = (scramble_prefix + [line])[-MAX_VISIBLE_LINES:]
    render_frame(clipped, SCRAMBLE_SPEED)

scroll_base = scramble_prefix + [f"{scramble_base} {'█ ' * scramble_blocks}".strip()]

# ====== Shutdown Sequence ====== #
shutdown_lines = [
    "[MEM ] Unmounting development stack...",
    "[IO  ] Releasing cognitive modules...",
    "[SYS ] Closing terminal session...",
    "[SYS ] Identity: blackJJW signed out.",
    "[✔] Consciousness offline. Uplink terminated.",
    ">>>",
    ""
]
for i in range(1, len(shutdown_lines) + 1):
    visible = (scroll_base + shutdown_lines[:i])[-MAX_VISIBLE_LINES:]
    render_frame(visible, SHUTDOWN_SPEED)

# ====== Hold Final Screen ====== #
for _ in range(FINAL_HOLD_COUNT):
    images.append(images[-1].copy())
    durations.append(FINAL_HOLD_DURATION)

# ====== Save GIF ====== #
images[0].save(GIF_PATH, save_all=True,
               append_images=images[1:], duration=durations, loop=0)
print(f"Done: {GIF_PATH}")

# ====== Clean Up Frames ====== #
shutil.rmtree(OUTPUT_DIR)
print(f"Cleaned up frame directory: {OUTPUT_DIR}")