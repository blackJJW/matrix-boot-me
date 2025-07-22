# MATRIX-BOOT-ME

> 💻 A Matrix-style boot sequence generator written in Python — perfect for intros, resumes, or terminal-style animations.

![sample](sample/hybrid_typing_intro.gif)

---

## ✨ Overview

`MATRIX-BOOT-ME` is a simple Python script that generates a boot-sequence-style animated GIF — inspired by classic terminal aesthetics and *The Matrix*.  
It simulates a futuristic neural system startup and shutdown, complete with personalized identity, tech stack, and contact info — typed out character by character.

---

## 🧰 Requirements

Install the required packages with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the script:

```bash
python main.py
```

The generated animation will be saved as:

```txt
hybrid_typing_intro.gif
```

---

## ⚙️ Customization

You can easily configure the following in `main.py`:

### 🔹 Boot / Shutdown Messages

Modify the `boot_lines`, `boot_continue`, and `shutdown_lines` lists to customize the startup and shutdown sequences.

### 🔹 Personal Information

Edit the `main_text` block to include your name, title, links, contact details, or anything else you’d like to type out character by character.

### 🔹 Encryption / Scrambling Animation

Adjust `encrypt_base`, `scramble_base`, `num_blocks`, or even replace the animation style with your own.

### 🔹 Typing & Animation Speeds

Customize frame delays using constants like:

- `TYPING_SPEED`  
- `ENCRYPT_SPEED`  
- `SCRAMBLE_SPEED`  
- `SHUTDOWN_SPEED`  
- `FINAL_HOLD_DURATION`

### 🔹 Visual Style

Tweak the visual presentation via:

- `FONT_COLOR`, `BG_COLOR`, `FONT_SIZE`, `FONT_FAMILY`  
- Terminal size: `IMAGE_WIDTH`, `IMAGE_HEIGHT`  
- Line limit: `MAX_VISIBLE_LINES`

### 🔹 GIF Output & Frame Handling

Change the output filename via `GIF_PATH`, or disable cleanup by commenting out the `shutil.rmtree()` call at the end of the script.

## 📄 License

MIT License
