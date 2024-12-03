var $Temp = $('#Temperatura');  // asignamos el objeto Temperatura a una variable nueva
var $Hum = $('#Humedad'); // asignamos el objeto  Humedad a una variable nueva
var temp = 0;
var hum = 0;
var particle = new Particle();
var token;
particle.login({ username: 'correo', password: 'contraseña' }).then(
    function (data) {
        token = data.body.access_token;
    },
    function (err) {
        console.log('Could not log in.', err);
    }
);
setInterval(function () {

    particle.getVariable({ deviceId: '26003c001947313037363132', name: 'TEMP', auth: token }).then(function (data) {

        console.log('Device variable retrieved successfully:', data);
        temp = data.body.result;

    }, function (err) {
        console.log('An error occurred while getting attrs:', err);
    });
    particle.getVariable({ deviceId: '26003c001947313037363132', name: 'HUM', auth: token }).then(function (data) {

        console.log('Device variable retrieved successfully:', data);
        hum = data.body.result;

    }, function (err) {
        console.log('An error occurred while getting attrs:', err);
    });
    hum = hum.toFixed(2);
    temp = temp.toFixed(2);
    $Hum.text(hum + " %");
    $Temp.text(temp + " °C");
}, 2000);
