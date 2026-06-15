# 🎭 ImgSpy

`ImgSpy` is a 100% free, open-source terminal-based digital image forensics and Open-Source Intelligence (OSINT) metadata metadata extraction framework built strictly for **Linux Operating Systems**. By utilizing raw binary image stream parsing, it automates the evaluation of EXIF (Exchangeable Image File Format) directory paths across individual image specimens or entire local folder directories to harvest device configurations and precise physical tracking coordinates.

Developed by **Unknownx007**.

---

## ⚙️ Operational Mechanics

1. **Binary Container Extraction:** Bypasses visual graphic layers to open and process raw binary structures across standard formats (`.jpg`, `.jpeg`, `.png`, `.tiff`, `.webp`).
2. **EXIF Tag Decoding:** Maps numerical hardware indices back to recognizable forensic metadata targets (Camera Make, Device Model, Accurate Timestamps, Execution Software).
3. **Geometric Coordinate Parsing:** Collects raw degrees/minutes/seconds rational tuples hidden inside the `GPSInfo` metadata structure and dynamically computes precise decimal degree coordinates.
4. **Active Intelligence Mapping:** Automatically calculates localized tracking coordinates to generate an active, clickable Google Maps routing hyperlink for immediate geographic validation.
5. **Directory Workspace Sweeping:** Integrates a recursive, non-disruptive folder parsing loop that automatically skips corrupted assets or scrubbed graphic layers to aggregate matching hits into forensic text reports.

---

## 🔍 Deep Dive: The WhatsApp Document Exploit Vector

Many modern messaging platforms (like WhatsApp, Facebook, or Instagram) automatically scrub or erase EXIF metadata strings when a user uploads a photo directly from their gallery. This privacy-sanitization layer is designed to prevent open-source intelligence operations from tracking their users.

However, a major **operational vulnerability** exists in how these chat applications process files:

* **The Document Loophole:** When a smartphone user sends an image over WhatsApp utilizing the **"Send Document"** or **"Uncompressed File"** option, the application drops its image optimization and compression engines entirely. It treats the graphic block as an untouched, raw binary archive document.
* **HD Transmissions (50/50 Ceilings):** Utilizing the newer "HD Quality" gallery sharing options preserves high-density pixel resolutions but leaves metadata sanitization locked behind volatile, OS-dependent server policies. 
* **The Exploit Result:** Images distributed as documents keep 100% of their hidden EXIF directory trees completely intact. Anyone who receives that document can run `ImgSpy` over it to extract the target's exact hardware profiles, time footprints, and physical geographic location coordinates without the target's consent.

---

## 📦 Workspace Installation Guide

Because this application relies strictly on a lightweight standard library wrapper, it installs and executes with 100% compilation stability on modern environments:

```bash
# 1. Clone this competitive suite repository
git clone https://github.com/Unknownx007/ImgSpy
cd ImgSpy

# 2. Configure and isolate the python virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Pull required microservice modules securely
pip install -r requirements.txt

# 4. Initialize the command-line control panel
python3 imgspy.py
```

---

## 🚀 Usage Guide

1. Run the tool to initialize the high-contrast purple selection matrix.
2. Select **Option 1** to audit a single uncompressed document file, or **Option 2** to type a directory path and automatically process a mass folder of images.
3. Observe the live console logs as `ImgSpy` strips away empty formats and isolates active metadata profiles.
4. Copy the auto-generated **Google Maps Link** or view the comprehensive text document profile generated inside **`forensic_report.txt`** to secure your evidence metrics.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more details.
