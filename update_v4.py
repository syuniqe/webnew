import codecs
import re

def main():
    # 1. Update css/styles.css
    with codecs.open('css/styles.css', 'r', 'utf-8') as f:
        css = f.read()
    
    # Fix flip cards
    css = css.replace('.flip-card-front, .flip-card-back {\n  position: absolute;',
                      '.flip-card-front, .flip-card-back {\n  position: absolute;\n  top: 0;\n  left: 0;')
    
    # Add back link CSS
    if '.back-link' not in css:
        back_css = "\n.back-link { display: inline-flex; align-items: center; gap: 6px; font-weight: 600; font-size: 0.9rem; color: var(--ink-secondary); padding: 8px 16px; border-radius: 99px; background: var(--surface); border: 1px solid var(--line); transition: all 0.3s ease; text-decoration: none; }\n.back-link:hover { color: var(--brand); border-color: var(--brand); transform: translateX(-4px); }\n"
        css += back_css

    # Rework Timeline to glowing minimal circuit line
    new_timeline_css = """
/* Glowing Tech Timeline Redesign */
.glowing-timeline {
  display: flex;
  flex-direction: column;
  position: relative;
  padding: 40px 0;
  margin-top: 20px;
}
.glowing-timeline::before {
  content: "";
  position: absolute;
  top: 0; bottom: 0;
  left: 50%;
  width: 2px;
  background: var(--line-strong);
  transform: translateX(-50%);
  z-index: 0;
}
/* Active glow tracker line */
.glowing-timeline::after {
  content: "";
  position: absolute;
  top: 0; height: 100%;
  left: 50%;
  width: 2px;
  background: var(--brand);
  transform: translateX(-50%);
  z-index: 1;
  box-shadow: 0 0 15px var(--brand);
  opacity: 0.8;
  mask-image: linear-gradient(to bottom, black 25%, transparent 75%);
  -webkit-mask-image: linear-gradient(to bottom, black 25%, transparent 75%);
  animation: glowPulse 4s infinite alternate;
}
@keyframes glowPulse {
  0% { opacity: 0.5; box-shadow: 0 0 10px var(--brand); }
  100% { opacity: 1; box-shadow: 0 0 25px var(--brand); }
}

.gt-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 60px;
  position: relative;
  z-index: 2;
}
.gt-item:last-child { margin-bottom: 0; }
.gt-item:nth-child(even) { flex-direction: row-reverse; }

.gt-node {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 20px; height: 20px;
  border-radius: 50%;
  background: var(--dark-bg);
  border: 4px solid var(--brand-light);
  box-shadow: 0 0 15px var(--brand);
  transition: all 0.3s ease;
}
.gt-item:hover .gt-node {
  background: var(--brand);
  transform: translateX(-50%) scale(1.3);
  box-shadow: 0 0 30px var(--brand);
}

.gt-content {
  width: calc(50% - 40px);
  padding: 32px;
  background: var(--surface);
  border-radius: var(--radius-sm);
  border: 1px solid var(--line);
  box-shadow: var(--shadow-sm);
  position: relative;
  transition: all 0.4s var(--ease);
}
.gt-item:hover .gt-content {
  border-color: var(--brand);
  box-shadow: var(--shadow-md), 0 0 0 1px var(--brand-glow);
  transform: translateY(-4px);
}
.gt-item:nth-child(odd) .gt-content { text-align: right; border-right: 3px solid transparent; }
.gt-item:nth-child(even) .gt-content { text-align: left; border-left: 3px solid transparent; }

.gt-item:nth-child(odd):hover .gt-content { border-right-color: var(--brand); }
.gt-item:nth-child(even):hover .gt-content { border-left-color: var(--brand); }

.gt-date { display: inline-block; font-family: monospace; font-size: 0.95rem; color: var(--brand); font-weight: 700; margin-bottom: 12px; background: var(--brand-subtle); padding: 4px 12px; border-radius: 99px; }
.gt-content h4 { font-size: 1.35rem; color: var(--ink); margin-bottom: 8px; }
.gt-content p { color: var(--ink-secondary); font-size: 1.05rem; }

@media (max-width: 768px) {
  .glowing-timeline::before, .glowing-timeline::after { left: 30px; }
  .gt-node { left: 30px; }
  .gt-item, .gt-item:nth-child(even) { flex-direction: row; }
  .gt-content { width: calc(100% - 70px); margin-left: auto; text-align: left !important; }
  .gt-item:nth-child(odd):hover .gt-content { border-right-color: transparent; border-left-color: var(--brand); }
}
"""
    # Replace parallax timeline section with glowing timeline CSS
    # Since I appended it last time, I can find /* Circular Timeline Parallax */ and replace to end
    parallax_comment = "/* Circular Timeline Parallax */"
    if parallax_comment in css:
        css = css.split(parallax_comment)[0] + new_timeline_css
    else:
        css += new_timeline_css
    
    with codecs.open('css/styles.css', 'w', 'utf-8') as f:
        f.write(css)
    print("Updated styles.css")

    # 2. Update about.html
    try:
        with codecs.open('about.html', 'r', 'utf-8') as f:
            about = f.read()
            
        glowing_timeline_html = """
        <div class="glowing-timeline reveal">
          <div class="gt-item">
            <div class="gt-node"></div>
            <div class="gt-content">
              <span class="gt-date">JAN 2025</span>
              <h4>Ideation & gap analysis</h4>
              <p>Identified portability, weight, and usability gaps in existing backup systems.</p>
            </div>
          </div>
          
          <div class="gt-item">
            <div class="gt-node"></div>
            <div class="gt-content">
              <span class="gt-date">MAR - MAY 2025</span>
              <h4>Early prototyping</h4>
              <p>Demo prototypes built. Battery architecture and power management validated.</p>
            </div>
          </div>
          
          <div class="gt-item">
            <div class="gt-node"></div>
            <div class="gt-content">
              <span class="gt-date">JUN - JUL 2025</span>
              <h4>Incorporation & pre-incubation</h4>
              <p>Company incorporated. IIM Bangalore pre-incubation support secured.</p>
            </div>
          </div>
          
          <div class="gt-item">
            <div class="gt-node"></div>
            <div class="gt-content">
              <span class="gt-date">AUG - SEP 2025</span>
              <h4>MVP build & optimization</h4>
              <p>MVP prototype built and refined through structured field feedback.</p>
            </div>
          </div>
          
          <div class="gt-item">
            <div class="gt-node"></div>
            <div class="gt-content">
              <span class="gt-date">LATE 2025</span>
              <h4>Certification focus</h4>
              <p>BIS and IEC testing initiated. Production-readiness planning underway.</p>
            </div>
          </div>
          
          <div class="gt-item">
            <div class="gt-node"></div>
            <div class="gt-content">
              <span class="gt-date">2026</span>
              <h4>Institutional pilots & rollout</h4>
              <p>First deployments with schools, institutions, and early adopters across India.</p>
            </div>
          </div>
        </div>
        """
        
        # Replace the <div class="parallax-timeline reveal"> block
        new_about = re.sub(r'<div class="parallax-timeline reveal">.*?</div>\s*</div>\s*</section>',
                           glowing_timeline_html + '\n      </div>\n    </section>', about, flags=re.DOTALL)
        
        with codecs.open('about.html', 'w', 'utf-8') as f:
            f.write(new_about)
        print("Updated about.html timeline")
    except Exception as e:
        print("Error updating about.html:", e)

    # 3. Add back button to product pages
    product_pages = ['powerhub.html', 'powerhubmini.html', 'powerhubpro.html', 'powerrack.html']
    back_button_html = '<a href="products.html" class="back-link" style="margin-bottom: 24px;">\n          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>\n          Back to Catalog\n        </a>\n        '
    
    for page in product_pages:
        try:
            with codecs.open(page, 'r', 'utf-8') as f:
                content = f.read()
            if "Back to Catalog" not in content:
                content = content.replace('<div class="section-label">Products</div>', 
                                          back_button_html + '<div class="section-label">Products</div>')
                with codecs.open(page, 'w', 'utf-8') as f:
                    f.write(content)
                print(f"Added back button to {page}")
        except Exception as e:
            print(f"Error touching {page}: {e}")

if __name__ == '__main__':
    main()
