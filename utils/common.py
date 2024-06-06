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