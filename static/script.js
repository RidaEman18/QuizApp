document.addEventListener("DOMContentLoaded", function () {
    const bar = document.querySelector(".quiz-progress-fill");

    if (bar) {
        bar.style.width = bar.dataset.progress + "%";
    }
});