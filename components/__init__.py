# components/__init__.py

from .business import layout_restaurant, layout_real_estate, layout_gym
from .portfolios import layout_developer, layout_photography, layout_linktree
from .ecommerce import layout_single_product, layout_digital_store
from .utilities import layout_saas, layout_event_rsvp

def route_prompt_to_template(prompt):
    p = prompt.lower()
    
    # 1. Business & Service
    if any(k in p for k in ["restaurant", "food", "cafe", "bistro", "menu"]): return layout_restaurant(prompt)
    if any(k in p for k in ["real estate", "house", "apartment", "property"]): return layout_real_estate(prompt)
    if any(k in p for k in ["gym", "fitness", "workout", "trainer"]): return layout_gym(prompt)
    
    # 2. Portfolios
    if any(k in p for k in ["developer", "programmer", "software portfolio"]): return layout_developer(prompt)
    if any(k in p for k in ["photography", "designer", "gallery"]): return layout_photography(prompt)
    if any(k in p for k in ["linktree", "bio", "social links"]): return layout_linktree(prompt)
    
    # 3. E-Commerce
    if any(k in p for k in ["drop store", "single product", "backpack", "watch"]): return layout_single_product(prompt)
    if any(k in p for k in ["digital store", "e-book", "license store"]): return layout_digital_store(prompt)
    
    # 4. Utilities & Interactive
    if any(k in p for k in ["saas", "dashboard", "ai product"]): return layout_saas(prompt)
    if any(k in p for k in ["rsvp", "event", "wedding", "summit"]): return layout_event_rsvp(prompt)
    
    return layout_saas(prompt)  # Default Fallback
