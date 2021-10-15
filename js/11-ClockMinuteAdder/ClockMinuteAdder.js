function clockMinuteAdder(time, minutesToAdd) {
    // Your code here:
    time = time.split(":");
    horaAct = Number(time[0]);
    minAct = Number(time[1]);
    var minAbsAct = horaAct * 60 + minAct;
    var nuevoMAA = minAbsAct + minutesToAdd;

    var min = nuevoMAA % 60;
    var hora = Math.floor(nuevoMAA / 60);

    if (hora > 12) {
        hora = hora - 12
    }

    resultado = "" + hora + ":" + min;
    return resultado;
}

function clockMinuteAdder2(time, min) {
    // Escribir la funcion

    let [hours, minutes] = time.split(':');

    minutes = min + parseInt(minutes);
    let newMinutes = minutes % 60;

    hours = parseInt(hours) + Math.floor(minutes / 60);
    let newHours = ((hours - 1) % 12) + 1 || 1;

    if (newHours < 10) newHours = `0${newHours}`;//tamb ternario
    if (newMinutes < 10) newMinutes = `0${newMinutes}`;

    return `${newHours}:${newMinutes}`;

};
console.log(clockMinuteAdder('12:05', 720));
console.log(clockMinuteAdder('01:30', 30));
console.log(clockMinuteAdder('09:00', 20));




console.log(clockMinuteAdder('09:00', 20));

console.log(clockMinuteAdder('11:00', 220));

console.log(clockMinuteAdder('05:00', 20));


module.exports = clockMinuteAdder
