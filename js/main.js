/* ═══════════════════════════════════════════
   SYUNIQE ENERGIES — MAIN JAVASCRIPT
   Premium interactions, finder logic, animations
   ═══════════════════════════════════════════ */

/* ───── APPLICATION STATE ───── */
const appState = {
  step: 0,
  useCase: "home",
  solar: "yes",
  priority: "price",
  hours: 4,
  customWatts: 0,
  appliances: {
    fan: 0, light: 0, tv: 0, router: 0, laptop: 0, fridge: 0,
    cctv: 0, desktop: 0, speaker: 0, microwave: 0, projector: 0, oxygen: 0
  }
};

const applianceCatalog = {
  fan: { label: "Fan", watts: 75 },
  light: { label: "LED Light", watts: 12 },
  tv: { label: "TV", watts: 120 },
  router: { label: "Wi-Fi Router", watts: 20 },
  laptop: { label: "Laptop", watts: 90 },
  fridge: { label: "Refrigerator", watts: 180 },
  cctv: { label: "CCTV", watts: 40 },
  desktop: { label: "Desktop PC", watts: 180 },
  speaker: { label: "Speaker / PA", watts: 150 },
  microwave: { label: "Microwave", watts: 1000 },
  projector: { label: "Projector", watts: 220 },
  oxygen: { label: "Oxygen Concentrator", watts: 350 }
};

const products = {
  mini: {
    key: "mini", name: "PowerHub Mini",
    type: "Personal backup / travel / creators",
    capacityWh: 512, outputW: 600, surgeW: 1200, solarW: 200,
    cycle: "3000+ cycles", price: "₹29,999+", cta: "Pre-Order Mini",
    image: "assets/powerhub-mini.png",
    bestFor: ["travel", "camping", "creators", "students"]
  },
  core: {
    key: "core", name: "PowerHub",
    type: "Homes / professionals / all-rounder",
    capacityWh: 1024, outputW: 1200, surgeW: 2400, solarW: 400,
    cycle: "3500+ cycles", price: "₹69,999+", cta: "Pre-Order PowerHub",
    image: "assets/powerhub-core.png",
    bestFor: ["home", "shop", "office", "school", "resort"]
  },
  pro: {
    key: "pro", name: "PowerHub Pro",
    type: "Heavy appliances / events / remote operations",
    capacityWh: 2048, outputW: 2400, surgeW: 4800, solarW: 800,
    cycle: "4000+ cycles", price: "Request Quote", cta: "Request Quote",
    image: "assets/powerhub-pro.png",
    bestFor: ["event", "field", "medical", "resort", "business"]
  },
  rack: {
    key: "rack", name: "PowerRack",
    type: "B2B / NGOs / telecom / infrastructure",
    capacityWh: 5000, outputW: 5000, surgeW: 10000, solarW: 5000,
    cycle: "Modular system", price: "Request Quote", cta: "Talk to B2B Team",
    image: "assets/powerrack.png",
    bestFor: ["infrastructure", "ngo", "school", "facility", "telecom", "b2b"]
  }
};

/* ───── NAVIGATION ───── */
function initNav() {
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".navbar");
  if (!toggle || !nav) return;
  toggle.addEventListener("click", () => nav.classList.toggle("open"));

  // Close menu on link click (mobile)
  nav.querySelectorAll(".nav-links a, .nav-actions a").forEach(link => {
    link.addEventListener("click", () => nav.classList.remove("open"));
  });
}

/* ───── DYNAMIC ISLAND HEADER SCROLL EFFECT ───── */
function initHeaderScroll() {
  const navbar = document.querySelector(".navbar");
  if (!navbar) return;
  
  let ticking = false;
  window.addEventListener("scroll", () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        navbar.classList.toggle("scrolled", window.scrollY > 20);
        ticking = false;
      });
      ticking = true;
    }
  });
}

/* ───── SCROLL REVEAL ANIMATIONS ───── */
function initReveal() {
  const reveals = document.querySelectorAll(".reveal");
  if (!reveals.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.08,
    rootMargin: "0px 0px -40px 0px"
  });

  reveals.forEach(el => observer.observe(el));
}

/* ───── FINDER: CHOICE CARDS ───── */
function initChoices() {
  document.querySelectorAll("[data-choice-group]").forEach(btn => {
    btn.addEventListener("click", () => {
      const group = btn.dataset.choiceGroup;
      document.querySelectorAll(`[data-choice-group="${group}"]`).forEach(el => el.classList.remove("active"));
      btn.classList.add("active");
      appState[group] = btn.dataset.choiceValue;
    });
  });
}

/* ───── FINDER: APPLIANCE COUNTERS ───── */
function initAppliances() {
  document.querySelectorAll(".appliance").forEach(card => {
    const key = card.dataset.appliance;
    if (!key) return;
    const minus = card.querySelector("[data-minus]");
    const plus = card.querySelector("[data-plus]");
    const count = card.querySelector("[data-count]");

    function update(delta) {
      const next = Math.max(0, (appState.appliances[key] || 0) + delta);
      appState.appliances[key] = next;
      count.textContent = next;
      // Visual feedback
      card.style.borderColor = next > 0 ? "var(--brand)" : "";
    }

    if (minus) minus.addEventListener("click", () => update(-1));
    if (plus) plus.addEventListener("click", () => update(1));
  });
}

/* ───── FINDER: HOURS PICKER ───── */
function initHours() {
  const hourValue = document.querySelector("[data-hours-value]");
  const minus = document.querySelector("[data-hours-minus]");
  const plus = document.querySelector("[data-hours-plus]");
  if (!hourValue || !minus || !plus) return;

  function render() {
    hourValue.textContent = `${appState.hours}h`;
  }

  minus.addEventListener("click", () => {
    appState.hours = Math.max(1, appState.hours - 1);
    render();
  });
  plus.addEventListener("click", () => {
    appState.hours = Math.min(24, appState.hours + 1);
    render();
  });
  render();
}

/* ───── FINDER: COMPUTATION ───── */
function computeLoad() {
  let totalWatts = 0;
  Object.entries(appState.appliances).forEach(([key, qty]) => {
    totalWatts += applianceCatalog[key].watts * qty;
  });
  totalWatts += Number(appState.customWatts || 0);
  return totalWatts;
}

function recommendProduct() {
  const watts = computeLoad();
  const requiredWh = watts * appState.hours;
  const useCase = appState.useCase;

  if (useCase === "b2b" || requiredWh > 3500 || watts > 3000) {
    return { product: products.rack, watts, requiredWh };
  }
  if (watts > 1300 || requiredWh > 1700 || ["resort", "event", "medical", "field"].includes(useCase)) {
    return { product: products.pro, watts, requiredWh };
  }
  if (watts > 550 || requiredWh > 700 || ["home", "shop", "school", "office"].includes(useCase)) {
    return { product: products.core, watts, requiredWh };
  }
  return { product: products.mini, watts, requiredWh };
}

function renderSummary() {
  const customInput = document.querySelector("#customWatts");
  appState.customWatts = Number(customInput?.value || 0);

  const { product, watts, requiredWh } = recommendProduct();

  const setNode = (sel, val) => {
    const el = document.querySelector(sel);
    if (el) el.textContent = val;
  };
  const setAttr = (sel, attr, val) => {
    const el = document.querySelector(sel);
    if (el) el[attr] = val;
  };

  setNode("[data-summary-load]", `${(watts / 1000).toFixed(2)} kW`);
  setNode("[data-summary-backup]", `${appState.hours} Hours`);
  setNode("[data-summary-capacity]", `${(requiredWh / 1000).toFixed(2)} kWh`);
  setNode("[data-summary-product]", product.name);
  setNode("[data-summary-desc]", product.type);
  setAttr("[data-summary-image]", "src", product.image);
  setNode("[data-summary-price]", product.price);
  setNode("[data-summary-output]", `${product.outputW}W / ${product.surgeW}W surge`);
  setNode("[data-summary-solar]", `Up to ${product.solarW}W input`);
  setNode("[data-summary-cycle]", product.cycle);
  setNode("[data-summary-cta]", product.cta);

  const reasons = {
    mini: "Ideal for lighter loads, travel, creators, and compact backup needs.",
    core: "Best for Indian homes, small shops, and everyday backup during outages.",
    pro: "Recommended for heavy loads, event operations, resort use, and remote work sites.",
    rack: "Built for custom B2B, infrastructure, large backup demands, and modular scaling."
  };
  setNode("[data-summary-reason]", reasons[product.key] || reasons.core);
}

/* ───── FINDER: STEP NAVIGATION ───── */
function showStep(index, direction) {
  const steps = [...document.querySelectorAll(".finder-step")];
  const dots = [...document.querySelectorAll(".step-dot")];
  const connectors = [...document.querySelectorAll(".step-connector")];
  const stepLabel = document.querySelector(".finder-step-label");
  if (!steps.length) return;

  const prevStep = appState.step;
  appState.step = Math.max(0, Math.min(index, steps.length - 1));
  const goingBack = direction === 'back' || (direction === undefined && appState.step < prevStep);
  
  // Animate steps
  steps.forEach((step, i) => {
    if (i === appState.step) {
      step.classList.remove("slide-back");
      if (goingBack) step.classList.add("slide-back");
      step.classList.add("active");
      step.style.animation = "none";
      step.offsetHeight; // Force reflow
      step.style.animation = "";
    } else {
      step.classList.remove("active", "slide-back");
    }
  });

  // Update step dots
  dots.forEach((dot, i) => {
    dot.classList.remove("active", "done");
    if (i === appState.step) dot.classList.add("active");
    else if (i < appState.step) dot.classList.add("done");
  });

  // Update connectors
  connectors.forEach((conn, i) => {
    conn.classList.toggle("done", i < appState.step);
  });

  // Update step label
  const labels = ["Scenario", "Appliances", "Backup Hours", "Charging", "Priority", "Result"];
  if (stepLabel) {
    stepLabel.textContent = `Step ${appState.step + 1} of ${steps.length} — ${labels[appState.step] || ''}`;
  }

  if (appState.step === steps.length - 1) renderSummary();
}

function initFinderNav() {
  document.querySelectorAll("[data-next]").forEach(btn => {
    btn.addEventListener("click", () => showStep(appState.step + 1, 'forward'));
  });
  document.querySelectorAll("[data-prev]").forEach(btn => {
    btn.addEventListener("click", () => showStep(appState.step - 1, 'back'));
  });
}

/* ───── CONTACT PAGE: TABS ───── */
function initContactTabs() {
  const tabs = document.querySelectorAll(".contact-tab");
  const panels = document.querySelectorAll(".contact-panel");
  if (!tabs.length || !panels.length) return;

  function switchTab(tabName) {
    tabs.forEach(t => t.classList.toggle("active", t.dataset.tab === tabName));
    panels.forEach(p => {
      const isTarget = p.dataset.panel === tabName;
      p.classList.toggle("active", isTarget);
      // Re-trigger animation
      if (isTarget) {
        p.style.animation = "none";
        p.offsetHeight;
        p.style.animation = "";
      }
    });
  }

  tabs.forEach(tab => {
    tab.addEventListener("click", () => switchTab(tab.dataset.tab));
  });

  // Handle hash-based deep linking
  function handleHash() {
    const hash = window.location.hash.replace("#", "");
    if (hash && document.querySelector(`[data-panel="${hash}"]`)) {
      switchTab(hash);
      // Smooth scroll to form section
      setTimeout(() => {
        const section = document.getElementById("contact-forms");
        if (section) section.scrollIntoView({ behavior: "smooth", block: "start" });
      }, 100);
    }
  }

  handleHash();
  window.addEventListener("hashchange", handleHash);
}

/* ───── SMOOTH ANCHOR SCROLLING ───── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (href === "#") return;
      
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const headerHeight = document.querySelector(".site-header")?.offsetHeight || 80;
        const top = target.getBoundingClientRect().top + window.scrollY - headerHeight - 20;
        window.scrollTo({ top, behavior: "smooth" });
        
        // Update URL hash without jump
        history.pushState(null, null, href);
      }
    });
  });
}

/* ───── AMBIENT CLOUDS MOUSE EFFECT ───── */
function initAmbientClouds() {
  const hero = document.querySelector(".hero");
  const cloudTeal = document.querySelector(".cloud-teal");
  const cloudBlue = document.querySelector(".cloud-blue");
  if (!hero || !cloudTeal || !cloudBlue) return;

  // Cloud size is ~50vw, so center offset = 25vw
  const cloudHalfSizeVw = 25;

  // Current and target positions
  let tealX = 0, tealY = 0, blueX = window.innerWidth, blueY = window.innerHeight;
  let targetX = window.innerWidth / 2, targetY = window.innerHeight / 2;

  function lerp(a, b, t) { return a + (b - a) * t; }

  function animate() {
    // Teal follows cursor closely (80% lerp speed)
    tealX = lerp(tealX, targetX, 0.08);
    tealY = lerp(tealY, targetY, 0.08);

    // Blue follows with an offset and slower (lagging effect)
    blueX = lerp(blueX, targetX, 0.04);
    blueY = lerp(blueY, targetY, 0.04);

    // Position clouds so their center aligns with cursor
    const cloudHalf = window.innerWidth * cloudHalfSizeVw / 100;
    cloudTeal.style.transform = `translate(${tealX - cloudHalf}px, ${tealY - cloudHalf}px)`;
    cloudBlue.style.transform = `translate(${blueX - cloudHalf + 80}px, ${blueY - cloudHalf + 60}px)`;

    requestAnimationFrame(animate);
  }

  hero.addEventListener("mousemove", (e) => {
    const rect = hero.getBoundingClientRect();
    targetX = e.clientX - rect.left;
    targetY = e.clientY - rect.top;
  });

  // Reset clouds when mouse leaves
  hero.addEventListener("mouseleave", () => {
    targetX = hero.offsetWidth / 2;
    targetY = hero.offsetHeight / 2;
  });

  animate();
}



/* ───── INIT ───── */
document.addEventListener("DOMContentLoaded", () => {
  initNav();
  initHeaderScroll();
  initReveal();
  initChoices();
  initAppliances();
  initHours();
  initFinderNav();
  initContactTabs();
  initSmoothScroll();
  initAmbientClouds();
  
  // Init finder if present
  if (document.querySelector(".finder-step")) {
    showStep(0);
  }
});
