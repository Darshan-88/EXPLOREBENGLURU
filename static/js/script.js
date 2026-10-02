document.addEventListener("DOMContentLoaded", () => {
    const slides = [...document.querySelectorAll(".hero-slide")];
    const dots = [...document.querySelectorAll(".hero-dots button")];
    const pills = [...document.querySelectorAll(".category-pill")];
    const cards = [...document.querySelectorAll(".place-card")];
    const count = document.getElementById("resultCount");
    const emptyState = document.getElementById("emptyState");
    const menuToggle = document.getElementById("menuToggle");
    const mainNav = document.getElementById("mainNav");

    let currentSlide = 0;
    let timer;

    function showSlide(index) {
        currentSlide = index;
        slides.forEach((slide, i) => slide.classList.toggle("active", i === index));
        dots.forEach((dot, i) => dot.classList.toggle("active", i === index));
    }

    function nextSlide() {
        showSlide((currentSlide + 1) % slides.length);
    }

    function startSlider() {
        clearInterval(timer);
        timer = setInterval(nextSlide, 4500);
    }

    dots.forEach(dot => {
        dot.addEventListener("click", () => {
            showSlide(Number(dot.dataset.slide));
            startSlider();
        });
    });

    startSlider();

    function filterPlaces(category) {
        let visible = 0;

        cards.forEach(card => {
            const cardCategory = card.dataset.category;
            const name = card.dataset.name;

            // Category aliases make the navigation intuitive.
            const matches =
                category === "all" ||
                cardCategory === category ||
                (category === "food" && (name.includes("mg road") || name.includes("church street") || name.includes("commercial street"))) ||
                (category === "party" && (name.includes("church street") || name.includes("mg road") || name.includes("ub city"))) ||
                (category === "shopping" && (name.includes("commercial street") || name.includes("mg road") || name.includes("ub city"))) ||
                (category === "hills" && name.includes("nandi")) ||
                (category === "temples" && name.includes("iskcon"));

            card.style.display = matches ? "" : "none";
            if (matches) visible++;
        });

        count.textContent = category === "all"
            ? `Showing all ${visible} places`
            : `Showing ${visible} place${visible === 1 ? "" : "s"} in ${category}`;

        emptyState.classList.toggle("show", visible === 0);
    }

    pills.forEach(pill => {
        pill.addEventListener("click", () => {
            pills.forEach(p => p.classList.remove("active"));
            pill.classList.add("active");
            filterPlaces(pill.dataset.category);
            document.getElementById("places").scrollIntoView({ behavior: "smooth", block: "start" });
        });
    });

    document.querySelectorAll("[data-filter]").forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();
            const category = link.dataset.filter;
            const pill = document.querySelector(`.category-pill[data-category="${category}"]`);

            if (pill) {
                pills.forEach(p => p.classList.remove("active"));
                pill.classList.add("active");
            }

            filterPlaces(category);
            document.getElementById("places").scrollIntoView({ behavior: "smooth" });

            mainNav.classList.remove("open");
        });
    });

    menuToggle.addEventListener("click", () => {
        mainNav.classList.toggle("open");
    });
});
