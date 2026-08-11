# components/business.py
from .base import get_header, get_footer

def layout_restaurant(prompt):
    return get_header("Bistro & Gourmet Experience", dark_mode=True) + f"""
    <nav class="p-6 bg-slate-900 border-b border-slate-800 flex justify-between items-center sticky top-0 z-50">
        <span class="text-2xl font-serif text-amber-500 font-bold">L'Étoile Bistro</span>
        <button class="bg-amber-500 text-slate-950 font-bold px-6 py-2 rounded-full hover:bg-amber-400 transition">Book a Table</button>
    </nav>
    <header class="py-24 text-center max-w-3xl mx-auto px-4">
        <span class="text-amber-500 tracking-widest text-xs uppercase font-bold">Culinary Mastery</span>
        <h1 class="text-5xl font-serif font-black mt-2 mb-6">Exquisite Dining Redefined</h1>
        <p class="text-slate-400 italic">"{prompt}"</p>
    </header>
    <section class="max-w-5xl mx-auto px-6 py-12 grid md:grid-cols-2 gap-8">
        <div class="bg-slate-900 p-6 rounded-2xl border border-slate-800">
            <h3 class="text-xl font-serif font-bold text-amber-500 mb-4">Signature Degustation</h3>
            <div class="flex justify-between border-b border-slate-800 pb-2 mb-4"><span>Truffle Ribeye Filet</span><span class="text-amber-400">$64</span></div>
            <div class="flex justify-between border-b border-slate-800 pb-2"><span>Pan-Seared Sea Bass</span><span class="text-amber-400">$48</span></div>
        </div>
    </section>
    """ + get_footer()

def layout_real_estate(prompt):
    return get_header("Luxury Real Estate Showcase") + f"""
    <nav class="p-6 bg-white shadow-sm flex justify-between items-center">
        <span class="text-xl font-bold tracking-tight text-slate-900">VERTEX RESIDENCES</span>
    </nav>
    <div class="py-24 text-center bg-slate-100">
        <h1 class="text-4xl font-extrabold mb-4">The Pinnacle of Modern Architecture</h1>
        <p class="text-slate-600 text-sm italic">"{prompt}"</p>
    </div>
    """ + get_footer()

def layout_gym(prompt):
    return get_header("Iron Forge Fitness Studio", dark_mode=True) + f"""
    <header class="py-20 text-center bg-gradient-to-b from-red-950/40 to-slate-950 px-4">
        <h1 class="text-6xl font-black tracking-tighter uppercase mt-4 mb-4">Forge Your Ultimate Body</h1>
        <p class="text-slate-400 max-w-xl mx-auto italic">"{prompt}"</p>
    </header>
    """ + get_footer()
