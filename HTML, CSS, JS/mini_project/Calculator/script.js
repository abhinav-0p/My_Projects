let display = document.querySelector(".display");
let expression = "";

const appendvalue = (value) =>{
    expression = expression + value;
    display.innerText = expression;
}

const lastclear = () =>{
    expression = expression.slice(0, -1);
    display.innerText = expression;
}

const allclear = () => {
    expression = "";
    display.innerText = expression;
}

const calculate = () => {
    try{
        expression = eval(expression);
        display.innerText = expression;
    }
    catch(error){
        display.innerText = "invalid error!";
    }
    
}