// Inicializa el objeto Particle para interactuar con el Photon
const particle = new Particle();
const deviceId = 'id';  // ID de mi photonsito
let token;  // Token de autenticación, realmente no se que hace el token, supongo que me deja pasar o algo asi xD

// Estos son los valores que necesito jalar para despues actualizar valores
const currentValueElement = document.getElementById('current-value');
const particleValueElement = document.getElementById('particle-value');
const valueInput = document.getElementById('value-input');
const valueSlider = document.getElementById('value-slider');
const messageElement = document.getElementById('message');

// Función para actualizar el valor mostrado en la interfaz y enviar el dato al Photon
function updateValue(newValue) {
    newValue = Math.min(Math.max(newValue, 5), 20);  // Restringe el valor entre 5 y 20 muy necesario
    currentValueElement.textContent = newValue;
    valueInput.value = newValue;
    valueSlider.value = newValue;

    // Mensaje si se alcanza el límite de valores
    if (newValue === 5) {
        showMessage("Perdon! El valor minimo es 5");
    } else if (newValue === 20) {
        showMessage("El valor maximo es 20, Lo siento!");
    } else {
        showMessage("");  // Limpia el mensaje, para que no se vea todo el tiempo, obvio
    }

    // envia el valor al photon y si viene o no la funcion, entonces muestra (O no) un mensaje!
    if (token) {
        particle.callFunction({
            deviceId: deviceId,
            name: 'TMS_2',
            argument: newValue.toString(),
            auth: token
        }).then(
            function(data) {
                console.log('funcion jalada:', data);
            },
            function(err) {
                console.log('Oh no:', err);
                showMessage("O no funciona particle o esta apagado el photon, espero que sea la segunda");
            }
        );
    }
}

// Demuestra mi esquizofrenia
function showMessage(message) {
    messageElement.textContent = message;
}

// Maneja los botones de incrementar y decrementar el valor
document.getElementById('decrease').addEventListener('click', () => {
    updateValue(parseInt(currentValueElement.textContent) - 1);
});

document.getElementById('increase').addEventListener('click', () => {
    updateValue(parseInt(currentValueElement.textContent) + 1);
});

// actualiza el valor con el spinner (nunca sabre como se escribe)
valueInput.addEventListener('input', (event) => {
    updateValue(parseInt(event.target.value));
});

valueSlider.addEventListener('input', (event) => {
    updateValue(parseInt(event.target.value));
});

// manea los botones con cantidades grandes, tipo +5 y asi
document.querySelectorAll('.button-group .btn').forEach((button) => {
    button.addEventListener('click', () => {
        updateValue(parseInt(currentValueElement.textContent) + parseInt(button.dataset.value));
    });
});

// Autenticación (me pregunto si soy el unico que cambia esto para que no salga mi contraseña del github XD)
particle.login({username: 'tucorreoparticle', password: 'tucontraseñaparticle'})
    .then(
        function(data) {
            token = data.body.access_token;

            // Suscripción a las actualizaciones del Photon
            particle.getEventStream({ deviceId: deviceId, name: 'TMS_2', auth: token })
                .then(function(stream) {
                    stream.on('event', function(data) {
                        // Actualiza el valor proveniente del Photon
                        particleValueElement.textContent = data.data;
                    });
                });
        },
        function (err) {
            console.log('No pude autenticarme', err);
        }
    );
