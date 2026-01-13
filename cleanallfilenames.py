import os
import re
import string

def main():
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            # Skip this script if it's in the same folder
            if filename == os.path.basename(__file__):
                continue
                
            # Sanitize the filename
            new_name = sanitize_filename(filename)
                
            # If file has no extension but looks like HTML, add .html
            if '.' not in new_name:
                with open(filename, 'rb') as f:
                    start = f.read(200).decode('utf-8', errors='ignore')
                    if '<html' in start.lower() or '<!doctype' in start.lower():
                        new_name += '.html'
                    elif '<?xml' in start.lower():
                        new_name += '.xml'
            
            # If no change, skip
            if new_name == filename:
                # print(f'Skipping (no change): "{filename}"')
                continue
            
            # Avoid overwriting existing files
            # counter = 1
            # original_new_name = new_name
            # while os.path.exists(new_name):
            #     name, ext = os.path.splitext(original_new_name)
            #     new_name = f"{name}_{counter}{ext}"
            #     counter += 1

            print(f'Renaming: "{filename}" → "{new_name}"')
            os.rename(filename, new_name)

def sanitize_filename(filename):
    # More aggressive: remove control chars and non-printable Unicode
    # Keep only printable ASCII + space + common punctuation used in filenames
    cleaned = ''.join(
        c for c in filename
        if 32 <= ord(c) <= 126 or c in 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'
    )
    # Now apply safe chars filter
    safe_chars = "-_.()&+= %s%s" % (string.ascii_letters, string.digits)
    cleaned = ''.join(c if c in safe_chars else '_' for c in cleaned)
    cleaned = re.sub(r'_+', '_', cleaned).strip(' _')
    return cleaned or "unnamed_file"

if __name__ == "__main__":
    main()