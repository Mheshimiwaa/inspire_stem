const randomNumber=Math.floor(Math.random()*100)+1;
console.log(randomNumber)
let attempt=0;

function checkguess(){
    const guess=parseint(document.getElementById("guessField").value)
    attempt++;
    if(isNaN(guess)||guess<1||guess>100){
    setMessage("Please enter a valid number between 1 and 100")
        return;

    }
    if (guess===randomNumber){
        setMessage("Congratulations! Guessed correctly!")
        document.getElementById("guessField").disabled=true;

    }else if(guess < randomNumber){
         setMessage("too low try again")
    }else if(guess > randomNumber){
    setmessage("too low high again")

} 
}
function setMessage(message){
    document.getElementById("message").textContent=message

}
