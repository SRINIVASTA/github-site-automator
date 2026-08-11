# components/portfolios.py
from .base import get_header, get_footer

def layout_developer(prompt):
    return get_header("DevPortfolio Engine", dark_mode=True) + f"""
    <main class="max-w-4xl mx-auto px-6 py-20">
        <h1 class="text-4xl font-mono font-bold text-emerald-400">> build_developer_identity()</h1>
        <p class="text-slate-400 mt-4 max-w-xl font-mono text-sm">"{prompt}"</p>
    </main>
    """ + get_footer()

def layout_photography(prompt):
    return get_header("Visual Creator Matrix") + f"""
    <main class="max-w-6xl mx-auto px-6 py-16 text-center">
        <h1 class="text-3xl font-light uppercase tracking-widest text-slate-900">Captured Space Gallery</h1>
        <p class="text-slate-400 text-sm max-w-md mx-auto mt-2 italic">"{prompt}"</p>
    </main>
    """ + get_footer()

def layout_linktree(prompt):
    return get_header("Identity Hub Matrix", dark_mode=True) + f"""
    <main class="max-w-md mx-auto min-h-screen px-6 py-16 flex flex-col items-center">
        <h1 class="text-xl font-bold text-slate-100">@creative_identity</h1>
        <p class="text-xs text-slate-400 text-center mt-2 px-4 italic">"{prompt}"</p>
    </main>
    """ + get_footer()
