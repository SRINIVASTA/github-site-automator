# components/ecommerce.py
from .base import get_header, get_footer

def layout_single_product(prompt):
    return get_header("Exclusive Drop Store") + f"""
    <main class="max-w-5xl mx-auto px-6 py-20 text-center">
        <h1 class="text-4xl font-black text-slate-900 mb-4">AeroStrand Minimalist Backpack</h1>
        <p class="text-slate-600 text-sm italic">"{prompt}"</p>
    </main>
    """ + get_footer()

def layout_digital_store(prompt):
    return get_header("Nexus Digital Warehouse", dark_mode=True) + f"""
    <header class="py-20 text-center max-w-3xl mx-auto px-4">
        <h1 class="text-4xl font-extrabold mb-4 bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">Digital Assets Marketplace</h1>
        <p class="text-slate-400 text-sm italic">"{prompt}"</p>
    </header>
    """ + get_footer()
