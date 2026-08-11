# components/utilities.py
from .base import get_header, get_footer

def layout_saas(prompt):
    return get_header("SaaS Framework Engine", dark_mode=True) + f"""
    <header class="py-24 text-center max-w-4xl mx-auto px-4">
        <h1 class="text-5xl font-black tracking-tight mb-6">Automate Systems In Real Time</h1>
        <p class="text-slate-400 text-sm italic">"{prompt}"</p>
    </header>
    """ + get_footer()

def layout_event_rsvp(prompt):
    return get_header("Summit & Event Portal") + f"""
    <main class="max-w-2xl mx-auto px-6 py-20 text-center">
        <h1 class="text-4xl font-extrabold text-slate-900 mb-4">Global Tech Summit 2026</h1>
        <p class="text-slate-500 text-sm italic">"{prompt}"</p>
    </main>
    """ + get_footer()
