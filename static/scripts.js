document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const button = document.querySelector("button");

    if (form && button) {
        form.addEventListener("submit", function () {
            button.innerHTML = "🤖 Analyzing...";
            button.disabled = true;
        });
    }

});
