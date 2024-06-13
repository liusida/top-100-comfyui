import re
from datetime import datetime, timedelta, timezone
from jinja2 import Environment, FileSystemLoader, select_autoescape

def format_updated_at_date(date_str):
    date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return date_obj.strftime('%Y-%m-%d')

# Set up Jinja2 environment
env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html', 'xml', 'md'])
)

def load_template(template_name):
    return env.get_template(f'{template_name}.md.j2')

def get_human_readable_star_count(star_count):
    if star_count < 1000:
        str_star_count = f"{star_count}"
    else:
        str_star_count = f"{star_count / 1000:.1f}k"
    return str_star_count

def valid_filename(filename):
    # Remove invalid file name characters
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    # Replace other potentially problematic characters with underscore
    filename = re.sub(r'[\s]', "_", filename)
    # Avoid names typical for system devices like 'CON', 'PRN', etc.
    reserved_names = {"CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"}
    if filename.upper() in reserved_names:
        filename = "_" + filename
    # Ensure the filename length is not too long
    filename = filename[:255]
    return filename

def valid_search_query(string):
    string = re.sub(r'\((.*?)\)', r'\1', string)  # Remove content within parentheses
    string = string.replace('+', '')  # Remove the '+' character
    return string