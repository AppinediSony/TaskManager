document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const toggleBtn = document.querySelector(".theme-toggle");

    if (!toggleBtn) return; // safety check

    // Load saved theme from localStorage
    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark");
    }

    // Toggle theme on button click
    toggleBtn.addEventListener("click", () => {
        body.classList.toggle("dark");
        const theme = body.classList.contains("dark") ? "dark" : "light";
        localStorage.setItem("theme", theme);
    });
});