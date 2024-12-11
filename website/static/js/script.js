document.addEventListener("DOMContentLoaded", function () {
    const hiddenToggle = document.querySelector(".hidden");
    const navList = document.querySelector(".nav-list");

    // Function to handle showing/hiding the menu based on screen size
    function adjustMenuDisplay() {
        if (window.innerWidth > 1000) {
            // Ensure the nav-list is always visible on larger screens
            navList.style.display = "flex";
            navList.classList.remove("show"); // Remove the "show" class on large screens
        } else {
            // On smaller screens, hide the nav list by default and allow toggling
            if (!navList.classList.contains("show")) {
                navList.style.display = "none";
            }
        }
    }

    // Initial check when the page loads
    adjustMenuDisplay();

    // Listen for the resize event to adjust the menu on window resize
    window.addEventListener("resize", adjustMenuDisplay);

    // Toggle the menu when clicking the hamburger icon
    hiddenToggle.addEventListener("click", function () {
        if (navList.style.display === "block") {
            navList.style.display = "none";
            navList.classList.remove("show");
        } else {
            navList.style.display = "block";
            navList.classList.add("show");
        }
    });
});
