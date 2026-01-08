// Load reusable header and footer components
async function loadHeader() {
  try {
    const response = await fetch('static/elements/header.html');
    const html = await response.text();
    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
      headerPlaceholder.innerHTML = html;
    }
  } catch (error) {
    console.error('Error loading header:', error);
  }
}

async function loadFooter() {
  try {
    const response = await fetch('static/elements/footer.html');
    const html = await response.text();
    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
      footerPlaceholder.innerHTML = html;
    }
  } catch (error) {
    console.error('Error loading footer:', error);
  }
}

// Load timeline and phase sections if needed (currently not used after data-driven cards)
async function loadTimeline() {
  try {
    const response = await fetch('static/elements/timeline.html');
    const html = await response.text();
    const timelinePlaceholder = document.getElementById('timeline-placeholder');
    if (timelinePlaceholder) {
      timelinePlaceholder.innerHTML = html;
    }
  } catch (error) {
    console.error('Error loading timeline:', error);
  }
}

async function loadPhases() {
  try {
    const phases = ['ideation', 'research', 'concepting', 'validation', 'planning'];
    for (const phase of phases) {
      const response = await fetch(`static/elements/phase-${phase}.html`);
      const html = await response.text();
      const phasePlaceholder = document.getElementById(`${phase}-placeholder`);
      if (phasePlaceholder) {
        phasePlaceholder.innerHTML = html;
      }
    }
  } catch (error) {
    console.error('Error loading phases:', error);
  }
}

// Load all components when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  loadHeader();
  loadFooter();
  // loadTimeline();
  // loadPhases();
});
