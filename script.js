/* ============================================
   YOJANA GUIDE - Main JavaScript
   Government Schemes Information Portal
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Mobile Menu Toggle ---------- */
  const hamburger = document.querySelector('.hamburger');
  const mainNav = document.querySelector('.main-nav');
  const navOverlay = document.querySelector('.nav-overlay');

  if (hamburger) {
    hamburger.addEventListener('click', function () {
      mainNav.classList.toggle('open');
      if (navOverlay) navOverlay.classList.toggle('active');
      document.body.style.overflow = mainNav.classList.contains('open') ? 'hidden' : '';

      // Animate hamburger
      const spans = hamburger.querySelectorAll('span');
      if (mainNav.classList.contains('open')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });

    if (navOverlay) {
      navOverlay.addEventListener('click', function () {
        mainNav.classList.remove('open');
        navOverlay.classList.remove('active');
        document.body.style.overflow = '';
        const spans = hamburger.querySelectorAll('span');
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      });
    }
  }

  /* ---------- Active Navigation Highlighting ---------- */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-list a');
  navLinks.forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    }
  });

  /* ---------- Search Functionality ---------- */
  const searchInput = document.querySelector('.hero-search input');
  const searchBtn = document.querySelector('.hero-search button');

  function performSearch() {
    if (!searchInput) return;
    const query = searchInput.value.trim().toLowerCase();
    if (!query) return;

    const schemeCards = document.querySelectorAll('.scheme-card');
    let found = 0;

    schemeCards.forEach(function (card) {
      const title = card.querySelector('h3') ? card.querySelector('h3').textContent.toLowerCase() : '';
      const desc = card.querySelector('p') ? card.querySelector('p').textContent.toLowerCase() : '';
      const match = title.includes(query) || desc.includes(query);

      if (match) {
        card.style.display = '';
        card.style.border = '2px solid var(--accent-orange)';
        found++;
      } else {
        card.style.display = 'none';
      }
    });

    // Scroll to schemes section
    const schemesSection = document.querySelector('.schemes-grid');
    if (schemesSection) {
      schemesSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Reset if search is cleared
    if (query === '') {
      schemeCards.forEach(function (card) {
        card.style.display = '';
        card.style.border = '';
      });
    }
  }

  if (searchBtn) {
    searchBtn.addEventListener('click', function (e) {
      e.preventDefault();
      performSearch();
    });
  }

  if (searchInput) {
    searchInput.addEventListener('keypress', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        performSearch();
      }
    });

    // Reset on clearing search
    searchInput.addEventListener('input', function () {
      if (this.value.trim() === '') {
        const schemeCards = document.querySelectorAll('.scheme-card');
        schemeCards.forEach(function (card) {
          card.style.display = '';
          card.style.border = '';
        });
      }
    });
  }

  /* ---------- Back to Top Button ---------- */
  const backToTop = document.querySelector('.back-to-top');

  if (backToTop) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 400) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    });

    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---------- Reading Progress Bar ---------- */
  const progressBar = document.querySelector('.reading-progress');

  if (progressBar) {
    window.addEventListener('scroll', function () {
      const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (window.scrollY / docHeight) * 100;
      progressBar.style.width = scrolled + '%';
    });
  }

  /* ---------- Smooth Scroll for Anchor Links ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ---------- Contact Form Validation ---------- */
  const contactForm = document.getElementById('contactForm');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      let isValid = true;

      // Clear previous errors
      contactForm.querySelectorAll('.form-group').forEach(function (group) {
        group.classList.remove('error');
      });

      // Validate Name
      const nameField = document.getElementById('name');
      if (nameField && nameField.value.trim().length < 2) {
        showError(nameField, 'Please enter your full name (at least 2 characters).');
        isValid = false;
      }

      // Validate Email
      const emailField = document.getElementById('email');
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (emailField && !emailRegex.test(emailField.value.trim())) {
        showError(emailField, 'Please enter a valid email address.');
        isValid = false;
      }

      // Validate Subject
      const subjectField = document.getElementById('subject');
      if (subjectField && subjectField.value.trim().length < 3) {
        showError(subjectField, 'Please enter a subject (at least 3 characters).');
        isValid = false;
      }

      // Validate Message
      const messageField = document.getElementById('message');
      if (messageField && messageField.value.trim().length < 10) {
        showError(messageField, 'Please enter a message (at least 10 characters).');
        isValid = false;
      }

      if (isValid) {
        // Show success message
        const successMsg = document.querySelector('.success-message');
        if (successMsg) {
          successMsg.classList.add('show');
          contactForm.reset();
          setTimeout(function () {
            successMsg.classList.remove('show');
          }, 5000);
        }
      }
    });

    function showError(field, message) {
      const group = field.closest('.form-group');
      if (group) {
        group.classList.add('error');
        const errorEl = group.querySelector('.error-message');
        if (errorEl) errorEl.textContent = message;
      }
    }
  }

  /* ---------- Lazy Loading Placeholder ---------- */
  if ('IntersectionObserver' in window) {
    const lazyElements = document.querySelectorAll('[data-lazy]');
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('loaded');
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: '50px' });

    lazyElements.forEach(function (el) {
      observer.observe(el);
    });
  }

  /* ---------- Animate Elements on Scroll ---------- */
  if ('IntersectionObserver' in window) {
    const animateElements = document.querySelectorAll('.scheme-card, .category-card, .update-item, .about-feature-card, .team-card, .category-full-card');
    const animateObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          animateObserver.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px', threshold: 0.1 });

    animateElements.forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      animateObserver.observe(el);
    });
  }

});

  /* ---------- Dropdown menu on mobile ---------- */
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(function (toggle) {
    toggle.addEventListener('click', function (e) {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        const dropdownMenu = this.nextElementSibling;
        if (dropdownMenu) {
          dropdownMenu.classList.toggle('show');
          const arrow = this.querySelector('.arrow');
          if (arrow) {
            arrow.style.transform = dropdownMenu.classList.contains('show') ? 'rotate(180deg)' : '';
          }
        }
      }
    });
  });

/* ---------- Interactive Categories Filtering & Search ---------- */
window.activeCategory = null;

window.filterByCategory = function(catId, catName) {
  // Hide categories grid
  const catGrid = document.querySelector('.categories-page-grid');
  if (catGrid) catGrid.style.display = 'none';
  
  // Show active filter header and set title
  const filterHeader = document.getElementById('active-filter-header');
  const filterTitle = document.getElementById('filter-title');
  if (filterHeader && filterTitle) {
    filterHeader.style.display = 'flex';
    filterTitle.textContent = catName + ' Schemes';
  }
  
  // Show schemes results section
  const resultsSec = document.getElementById('schemes-results-section');
  if (resultsSec) resultsSec.style.display = 'block';
  
  // Save active category globally
  window.activeCategory = catId;
  
  // Filter the cards
  window.filterSchemes();
  
  // Scroll to top of section
  const mainContent = document.getElementById('main-content');
  if (mainContent) {
    mainContent.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
};

window.showCategoryGrid = function() {
  // Hide schemes results section and header
  const resultsSec = document.getElementById('schemes-results-section');
  const filterHeader = document.getElementById('active-filter-header');
  if (resultsSec) resultsSec.style.display = 'none';
  if (filterHeader) filterHeader.style.display = 'none';
  
  // Show categories grid
  const catGrid = document.querySelector('.categories-page-grid');
  if (catGrid) catGrid.style.display = '';
  
  // Reset active category
  window.activeCategory = null;
  
  // Reset search input
  const searchInput = document.getElementById('categories-search-input');
  if (searchInput) searchInput.value = '';
  
  // Show all cards for next time
  const schemeCards = document.querySelectorAll('#schemes-list-container .scheme-card');
  schemeCards.forEach(card => card.style.display = 'block');
};

window.filterSchemes = function() {
  const searchInput = document.getElementById('categories-search-input');
  const query = searchInput ? searchInput.value.trim().toLowerCase() : '';
  const schemeCards = document.querySelectorAll('#schemes-list-container .scheme-card');
  
  schemeCards.forEach(function(card) {
    const cardCat = card.getAttribute('data-category');
    const title = card.querySelector('h3').textContent.toLowerCase();
    const desc = card.querySelector('p').textContent.toLowerCase();
    
    // Category match
    const categoryMatch = !window.activeCategory || cardCat === window.activeCategory;
    
    // Search query match
    const searchMatch = !query || title.includes(query) || desc.includes(query);
    
    if (categoryMatch && searchMatch) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
};

// Add live search handling when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  const categoriesSearchInput = document.getElementById('categories-search-input');
  const categoriesSearchBtn = document.getElementById('categories-search-btn');
  
  if (categoriesSearchInput) {
    categoriesSearchInput.addEventListener('input', function() {
      const query = this.value.trim().toLowerCase();
      
      if (query) {
        // If searching, hide categories grid and show results
        const catGrid = document.querySelector('.categories-page-grid');
        if (catGrid) catGrid.style.display = 'none';
        
        const resultsSec = document.getElementById('schemes-results-section');
        if (resultsSec) resultsSec.style.display = 'block';
        
        const filterHeader = document.getElementById('active-filter-header');
        const filterTitle = document.getElementById('filter-title');
        if (filterHeader && filterTitle) {
          filterHeader.style.display = 'flex';
          if (!window.activeCategory) {
            filterTitle.textContent = 'Search Results';
          }
        }
      } else {
        // If search is cleared and no category is selected, show categories grid
        if (!window.activeCategory) {
          window.showCategoryGrid();
        }
      }
      window.filterSchemes();
    });
  }
  
  if (categoriesSearchBtn && categoriesSearchInput) {
    categoriesSearchBtn.addEventListener('click', function(e) {
      e.preventDefault();
      window.filterSchemes();
    });
  }

  // Handle auto-filtering by category on page load if query param or hash exists
  const params = new URLSearchParams(window.location.search);
  const cat = params.get('cat') || window.location.hash.substring(1);
  if (cat) {
    const cards = document.querySelectorAll('.category-full-card');
    let catName = cat.charAt(0).toUpperCase() + cat.slice(1);
    for (const card of cards) {
      const onclickAttr = card.getAttribute('onclick');
      if (onclickAttr && onclickAttr.includes(`'${cat}'`)) {
        const matches = onclickAttr.match(/'([^']+)'\s*,\s*'([^']+)'/);
        if (matches && matches[2]) {
          catName = matches[2];
          break;
        }
      }
    }
    setTimeout(() => {
      window.filterByCategory(cat, catName);
    }, 50);
  }
});
