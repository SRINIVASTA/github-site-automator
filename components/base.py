# components/base.py

def get_header(title, dark_mode=False):
    bg_class = "bg-slate-950 text-white" if dark_mode else "bg-slate-50 text-slate-800"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cloudflare.com">
</head>
<body class="{bg_class} font-sans scroll-smooth">"""

def get_footer():
    return """<footer class="bg-slate-900 text-slate-400 text-center py-12 text-sm border-t border-slate-800">
        <p>&copy; 2026 AutoSite Engine. Created automatically from prompt metadata structures.</p>
    </footer>
</body>
</html>"""
