import codecs
import re

def process_catalog():
    filepath = 'products.html'
    try:
        with codecs.open(filepath, 'r', 'utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Delete everything from <div class="specs-grid reveal"> up to the end of the section that contains it.
    # since we want to keep the closing </div> of container and </section>
    content = re.sub(r'<div class="specs-grid reveal">.*?</div>\s*</section>', r'</div>\n    </section>', content, flags=re.DOTALL)

    # Now change all links that say "Datasheet" or "Know More" or similar to "More Details" pointing to specific pages.
    # We will do this explicitly for each.
    
    # PowerHub
    content = content.replace('<a href="contact.html#demo" class="btn btn--secondary">Datasheet</a>', 
                              '<a href="powerhub.html" class="btn btn--secondary">More Details</a>')
    
    # Mini
    content = content.replace('<a href="contact.html#preorder" class="btn btn--primary">Pre-Order Mini</a>',
                              '<a href="powerhubmini.html" class="btn btn--secondary">More Details</a>')
    # Actually wait. Just replacing "Datasheet" inside the Mini section is better. Wait, the exact HTML for Mini:
    # <a href="contact.html#preorder" class="btn btn--primary">Pre-Order Mini</a>
    # <a href="contact.html#demo" class="btn btn--secondary">Datasheet</a>
    
    # Let's replace the whole buttons section for each to be precise and clean.
    
    # Replace PowerHub buttons
    ph_btns_old = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="contact.html#preorder" class="btn btn--primary">Pre-Order PowerHub</a>
              <a href="contact.html#demo" class="btn btn--secondary">Datasheet</a>
            </div>'''
    ph_btns_new = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="powerhub.html" class="btn btn--primary">More Details</a>
            </div>'''
    content = content.replace(ph_btns_old, ph_btns_new)

    # Mini buttons
    mini_btns_old = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="contact.html#preorder" class="btn btn--primary">Pre-Order Mini</a>
              <a href="contact.html#demo" class="btn btn--secondary">Datasheet</a>
            </div>'''
    mini_btns_new = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="powerhubmini.html" class="btn btn--primary">More Details</a>
            </div>'''
    content = content.replace(mini_btns_old, mini_btns_new)

    # Pro buttons
    pro_btns_old = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="contact.html#quote" class="btn btn--primary">Request Quote</a>
              <a href="contact.html#demo" class="btn btn--secondary">Datasheet</a>
            </div>'''
    pro_btns_new = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="powerhubpro.html" class="btn btn--primary">More Details</a>
            </div>'''
    content = content.replace(pro_btns_old, pro_btns_new)
    
    # Rack buttons
    rack_btns_old = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="contact.html#knowmore" class="btn btn--primary">Know More</a>
            </div>'''
    rack_btns_new = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="powerrack.html" class="btn btn--primary">More Details</a>
            </div>'''
    content = content.replace(rack_btns_old, rack_btns_new)

    # Battery section buttons
    bat_btns_old = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="contact.html#knowmore" class="btn btn--primary btn--sm">Ask About Expansion</a>
              <a href="contact.html#preorder" class="btn btn--secondary btn--sm">Datasheet</a>
            </div>'''
    bat_btns_new = '''<div style="display:flex;gap:12px;margin-top:24px;flex-wrap:wrap;">
              <a href="powerhub.html#battery" class="btn btn--secondary btn--sm">More Details</a>
            </div>'''
    content = content.replace(bat_btns_old, bat_btns_new)


    custom_bess_html = """
    <!-- CUSTOM BESS -->
    <section class="section" id="custom-bess">
      <div class="container">
        <div class="section-header reveal">
          <div class="section-label">Industrial & Enterprise</div>
          <h2>Custom BESS Solutions</h2>
          <p>We design, engineer, and deploy battery energy storage systems from the ground up — built around your exact specification.</p>
        </div>
        <div class="specs-grid reveal" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
          <div class="specs-card" style="padding: 32px; background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); transition: transform 0.3s var(--ease), border-color 0.3s var(--ease);">
            <h3 style="font-size:1.3rem;">Drone Charging Stations</h3>
            <p style="color:var(--ink-secondary);font-size:1rem;margin-top:10px;">Off-grid and remote charging infrastructure for UAV fleets. Designed for rapid turnaround, weatherproof deployment, and solar replenishment.</p>
          </div>
          <div class="specs-card" style="padding: 32px; background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); transition: transform 0.3s var(--ease), border-color 0.3s var(--ease);">
            <h3 style="font-size:1.3rem;">Industrial ESS Deployments</h3>
            <p style="color:var(--ink-secondary);font-size:1rem;margin-top:10px;">Custom-engineered energy storage for manufacturing units and commercial facilities. Reduce peak demand, eliminate outages.</p>
          </div>
          <div class="specs-card" style="padding: 32px; background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); transition: transform 0.3s var(--ease), border-color 0.3s var(--ease);">
            <h3 style="font-size:1.3rem;">Off-grid Power Systems</h3>
            <p style="color:var(--ink-secondary);font-size:1rem;margin-top:10px;">Complete off-grid energy infrastructure for remote sites — construction, telecom towers, rural electrification, and field operations.</p>
          </div>
          <div class="specs-card" style="padding: 32px; background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); transition: transform 0.3s var(--ease), border-color 0.3s var(--ease);">
            <h3 style="font-size:1.3rem;">EV Charging Infrastructure</h3>
            <p style="color:var(--ink-secondary);font-size:1rem;margin-top:10px;">Battery-buffered EV charging solutions for locations with limited grid capacity. Deploy fast chargers anywhere without expensive grid upgrades.</p>
          </div>
        </div>
        <div style="margin-top:40px;" class="reveal">
          <a href="contact.html#quote" class="btn btn--primary">Discuss Custom Solutions</a>
        </div>
      </div>
    </section>
"""

    # Insert custom_bess_html just before FINAL CTA section
    cta_marker = "<!-- FINAL CTA -->"
    content = content.replace(cta_marker, custom_bess_html + "\n    " + cta_marker)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)
    print("products.html transformed successfully.")

if __name__ == '__main__':
    process_catalog()
