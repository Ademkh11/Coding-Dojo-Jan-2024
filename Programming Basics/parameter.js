function greetPerson(Adem){
    console.log("Goodday" + " " + "Adem");
}
greetPerson("Adem")
function getCurrentTime(){
    var now = new Date()
    var hours = now.getHours
    var minutes = now.getMinutes
    minutes=(minutes < 10)? '0' + minutes : minutes;
    return hours + 'H'+ minutes + 'Min';

}console.log(getCurrentTime());
function CountDooku(Doku){
    console.log("im comming for you, Dooku")
}CountDooku("im comming for you, Dooku")
//i've worked on this assignment with the help of my cohort mate