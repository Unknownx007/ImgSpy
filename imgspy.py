import os
import sys
import re
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Terminal ANSI Color Escape Constants
C_RESET = "\033[0m"
C_BOLD  = "\033[1m"
C_RED   = "\033[91m"
C_GREEN = "\033[92m"
C_YEL   = "\033[93m"
C_PURP  = "\033[95m"
C_CYAN  = "\033[96m"

class ImgSpyEngine:
    def __init__(self):
        self.log_file = "forensic_report.txt"

    def display_banner(self, mode_msg=""):
        """Renders the high-visibility, bright color-coded custom ASCII logo banner canvas."""
        os.system("clear")
        print(f"{C_PURP}{C_BOLD}")
        print(r"  _____                 _____")
        print(r" |_   _|               / ____|")
        print(r"   | |  _ __ ___   __ _| (___  _ __  _   _")
        print(r"   | | | '_ ` _ \ / _` |\___ \| '_ \| | | |")
        print(r"  _| |_| | | | | | (_| |____) | |_) | |_| |")
        print(r" |_____|_| |_| |_|\__, |_____/| .__/ \__, |")
        print(r"                   __/ |      | |     __/ |")
        print(r"                  |___/       |_|    |___/X")
        print(f"       [ Automated Digital Image Forensics & OSINT Engine v1.0 ]")
        print(f"       [               Engineered by Unknownx007               ]{C_RESET}")
        print(f"{C_PURP}=================================================================={C_RESET}")
        
        print(f"{C_YEL}{C_BOLD}[💡 FORENSIC AWARENESS NOTES]{C_RESET}")
        print(f"{C_YEL}Images sent as 'Documents' or 'HD Files' on messaging apps bypass standard")
        print(f"privacy sanitization layers, leaking precise GPS and system markers. Always")
        print(f"scrub metadata strings prior to distributing uncompressed target media!{C_RESET}")
        print(f"{C_PURP}=================================================================={C_RESET}")
        if mode_msg:
            print(f"{C_CYAN}[*] ACTIVE PROFILE: {mode_msg}{C_RESET}")
            print(f"{C_PURP}=================================================================={C_RESET}")
        print("\n")

    def log_write(self, text):
        """Strips terminal color codes and saves clear text lines to the forensic report file."""
        clean_text = re.sub(r'\033\[[0-9;]*m', '', text)
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(clean_text + "\n")

    def convert_to_degrees(self, value):
        """Converts raw EXIF GPS rational tuples into decimal degree values."""
        try:
            d = float(value[0])
            m = float(value[1])
            s = float(value[2])
            return d + (m / 60.0) + (s / 3600.0)
        except Exception:
            return None

    def extract_exif_metadata(self, image_path):
        """Extracts hidden device parameters and GPS coordinates from a target image file."""
        if not os.path.exists(image_path):
            print(f"{C_RED}[!] Targeted image asset path does not exist: {image_path}{C_RESET}")
            return False

        try:
            img = Image.open(image_path)
            exif_data = img._getexif()
        except Exception as e:
            # Silently pass corrupted graphics or formats that don't support EXIF
            return False

        if not exif_data:
            return False

        parsed_metadata = {}
        gps_info = {}

        # Map standard numerical EXIF markers back to recognizable string tags
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if tag_name == "GPSInfo":
                for gps_id in value:
                    gps_tag = GPSTAGS.get(gps_id, gps_id)
                    gps_info[gps_tag] = value[gps_id]
            else:
                parsed_metadata[tag_name] = value

        # Isolate and log the specific image name block header to separate reporting data
        file_name = os.path.basename(image_path)
        out_header = f"\n📦 FORENSIC AUDIT RECORD FOR ASSET TARGET: {file_name}\n" + "-"*65
        print(f"{C_YEL}{out_header}{C_RESET}"); self.log_write(out_header)

        # Output baseline hardware camera parameters inside yellow labels
        meta_keys = ["Make", "Model", "DateTime", "Software", "ExposureTime", "ISOSpeedRatings"]
        for key in meta_keys:
            if key in parsed_metadata:
                out = f" [▶] Hardware Metric -> {key}: {parsed_metadata[key]}"
                print(f"{C_CYAN}{out}{C_RESET}"); self.log_write(out)

        # Process and decode precise geometric GPS metadata coordinates if present
        if gps_info and "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
            lat = self.convert_to_degrees(gps_info["GPSLatitude"])
            lon = self.convert_to_degrees(gps_info["GPSLongitude"])
            
            # Adjust mapping signs depending on directional coordinate hemisphere markers
            lat_ref = gps_info.get("GPSLatitudeRef", "N")
            lon_ref = gps_info.get("GPSLongitudeRef", "E")
            
            if lat_ref != "N" and lat: lat = -lat
            if lon_ref != "E" and lon: lon = -lon

            if lat and lon:
                out_coord = f" [🚨 GPS GEOMETRIC HIT] Latitude: {lat:.6f} | Longitude: {lon:.6f}"
                gmaps_url = f"https://google.com{lat:.6f},{lon:.6f}"
                out_link  = f" [🌐 SATELLITE MAP LINK] Google Maps Target Route: {gmaps_url}"
                
                print(f"{C_GREEN}{out_coord}{C_RESET}"); self.log_write(out_coord)
                print(f"{C_GREEN}{out_link}{C_RESET}"); self.log_write(out_link)
        else:
            out_none = " [i] Status: Graphics layer verified but contains no physical tracking parameters."
            print(f"{C_RESET}{out_none}"); self.log_write(out_none)

        return True

    def process_single_file_interface(self):
        self.display_banner("SINGLE IMAGE SPECIMEN EXTRACTION")
        target_file = input("[+] Enter absolute path to your target image (e.g., target.jpg): ").strip()
        
        self.display_banner("ANALYZING TARGET GEOMETRIC MARKERS")
        status = self.extract_exif_metadata(target_file)
        if not status:
            print(f"{C_RED}[!] Targeted asset holds no valid metadata registry headers.{C_RESET}\n")

    def process_directory_batch_interface(self):
        self.display_banner("DIRECTORY REGISTRY BULK BATCH SWEEP")
        target_dir = input("[+] Enter location path to target folder containing images: ").strip()
        
        if not os.path.isdir(target_dir):
            print(f"\n{C_RED}[!] Target path is not a valid directory registry workspace link.{C_RESET}\n")
            time.sleep(2)
            return

        self.display_banner(f"EXECUTING METADATA CRAWL OVER WORKSPACE: {target_dir}")
        print(f"{C_YEL}[*] Automated sweep initiated. Filtering files and processing directories...{C_RESET}\n")
        
        valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.webp')
        processed_count = 0
        hit_count = 0

        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.lower().endswith(valid_extensions):
                    full_path = os.path.join(root, file)
                    status = self.extract_exif_metadata(full_path)
                    processed_count += 1
                    if status:
                        hit_count += 1

        print(f"\n{C_PURP}=================================================================={C_RESET}")
        print(f"{C_GREEN}[✅] Sweep complete! Audited {processed_count} files. Extracted data from {hit_count} images.{C_RESET}")
        print(f"{C_GREEN}[✅] Comprehensive forensics profile report saved to: {os.path.abspath(self.log_file)}{C_RESET}")
        print(f"{C_PURP}=================================================================={C_RESET}\n")

    def main_menu(self):
        # Clean session text remnants before writing fresh analysis entries
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
            
        while True:
            self.display_banner("READY")
            print(f"{C_BOLD}💻 FORENSIC ARCHITECTURE SELECTION MATRIX:{C_RESET}")
            print(f" [{C_GREEN}1{C_RESET}] AUDIT TARGET: Scan a single uncompressed image specimen file")
            print(f" [{C_GREEN}2{C_RESET}] WORKSPACE BATCH: Scan an entire directory folder for metadata profiles")
            print(f" [{C_GREEN}3{C_RESET}] EXIT INDUSTRIAL FRAMEWORK")
            print("-" * 65)
            
            choice = input("[+] Enter action index selection (1-3): ").strip()
            if choice == "1":
                self.process_single_file_interface()
                input("\n[+] Press Enter to return to main choice dashboard matrix...")
            elif choice == "2":
                self.process_directory_batch_interface()
                input("\n[+] Press Enter to return to main choice dashboard matrix...")
            elif choice == "3":
                print(f"\n{C_GREEN}[*] Closing active image file sockets... Goodbye.{C_RESET}\n")
                break

if __name__ == "__main__":
    engine = ImgSpyEngine()
    engine.main_menu()
