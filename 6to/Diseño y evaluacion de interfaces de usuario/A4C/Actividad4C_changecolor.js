document.addEventListener('DOMContentLoaded', function() {
    let currentSchemeIndex = 0;
    const colorSchemes = ["", "deuteranopia", "protanopia", "tritanopia"];

    const button = document.getElementById('colorSchemeBtn');
    if (button) {
        button.addEventListener('click', function() {
            currentSchemeIndex = (currentSchemeIndex + 1) % colorSchemes.length;
            document.body.className = colorSchemes[currentSchemeIndex];
            updateButtonText();
        });

        function updateButtonText() {
            const schemeNames = ["Estándar", "Deuteranopia", "Protanopia", "Tritanopia"];
            button.querySelector('a').innerText = "Diseño " + schemeNames[currentSchemeIndex];  // Asegúrate de que estás seleccionando el elemento correcto
        }

        updateButtonText(); // Set initial button text
    } else {
        console.error('Button not found');
    }
});
