// 
/*Data Types:
1.string
2.integers/numbers 
3.Booleans 
4.Arrays
5.
*/

//on click events
//element selectors
let name="Mike";
let height=50
function submit(){
    var input=document.getElementById("inputField").value
    var input=parseInt(input);//data type conversion
    var input=input+1
    
console.log(input)
}
let adult=true;//boolean
let fruit=[ 'kiwi','pineapple','apple',30,false]//array/lists
let person={
    Firstname:'Ada',
    Lastname:'LoveLace',
    age:18,
    address:{
        country:'Sudan',
        city:'Khartoum',
        street:'Bani bani',
    },
    children:['kelly','Mary']
    }
function saveItem(){
    var input=document.getElementById("inputField").value
    localStorage.setItem('inputitem',input);
    showWelcomeMessage(input)
}
function showWelcomeMessage(input){
    var messageElement=document.getElementById("showmessage")
    messageElement.textcontent="we have your input as"+input;
}

var storedItem=local.getItem('inputitem');
if(storedItem){
    showWelcomeMessage(storedItem)
}
