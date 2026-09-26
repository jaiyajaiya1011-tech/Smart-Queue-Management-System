document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll("button");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            button.style.transform = "scale(0.97)";

            setTimeout(function () {
                button.style.transform = "scale(1)";
            }, 100);
        });
    });

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function (event) {

            const inputs = form.querySelectorAll(
                "input[required], select[required]"
            );

            let valid = true;

            inputs.forEach(function (input) {
                if (input.value.trim() === "") {
                    valid = false;
                    input.style.borderColor = "#b00020";
                } else {
                    input.style.borderColor = "#ccc";
                }
            });

            if (!valid) {
                event.preventDefault();
                alert("Please fill in all required fields.");
            }
        });
    });

    const inputs = document.querySelectorAll("input, select");

    inputs.forEach(function (input) {
        input.addEventListener("input", function () {
            if (input.value.trim() !== "") {
                input.style.borderColor = "#ccc";
            }
        });
    });

    const callNextButton = document.querySelector(".call-btn");

    if (callNextButton) {
        callNextButton.addEventListener("click", function (event) {
            const confirmed = confirm(
                "Are you sure you want to call the next token?"
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    }

    const queueTable = document.querySelector("table");

    if (queueTable) {
        const rows = queueTable.querySelectorAll("tbody tr");

        rows.forEach(function (row) {
            row.addEventListener("mouseenter", function () {
                row.style.backgroundColor = "#f7f3f3";
            });

            row.addEventListener("mouseleave", function () {
                row.style.backgroundColor = "";
            });
        });
    }

    const dashboard =
        document.querySelector(".cards") ||
        document.querySelector(".stats");

    if (dashboard) {
        setTimeout(function () {
            location.reload();
        }, 10000);
    }

});