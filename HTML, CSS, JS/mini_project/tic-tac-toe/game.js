let allbox = document.querySelectorAll(".bt");
let reset = document.querySelector("#reset");
let msg_box = document.querySelector(".msg-box");
let text = document.querySelector("#text");
let new_game = document.querySelector("#new-game");

const winnerpattern = [
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],
    [6,7,8],
];

let turn0 = true;
let count = 0;


for (let box of allbox){
    
    box.addEventListener("click" , () =>{
        count++;
        if(turn0 === true){
            box.innerText = "O";
            turn0 = false;
        }
        else{
            box.innerText = "X";
            turn0 = true;
        }
        box.disabled = true;
        checkwinner();
    })
}

const checkwinner = () => {
    let winnerfound = false;
    for(let pattern of winnerpattern){
        let pos1val = allbox[pattern[0]].innerText;
        let pos2val = allbox[pattern[1]].innerText;
        let pos3val = allbox[pattern[2]].innerText;

        if(pos1val != "" && pos2val != "" && pos3val != ""){
            if(pos1val === pos2val && pos2val === pos3val){
                console.log("winner");
                showwinner(pos1val);
                box_disable();
                winnerfound = true;
                break;
            } 
            else if(count === 9 && winnerfound === false){
                text.innerText = "It's a draw";
                msg_box.classList.remove("hide");
            }
        }
    }
    
}
const drawfunc = () => {
    if(count === 9){
        text.innerText = "It's a draw";
    }
}


const showwinner = (winner) =>{
    text.innerText = `Congratulations, The winner is ${winner}`;
    msg_box.classList.remove("hide");

}
const box_disable = () => {
    for(box of allbox){
        box.disabled = true;
    }
    
}

new_game.addEventListener("click",() => {
    turn0 = true;
    count = 0;
    for(box of allbox){
        box.innerText = "";
    }
    msg_box.classList.add("hide");
    
    for(box of allbox){
        box.disabled = false;
    }
})

reset.addEventListener("click",() => {
    turn0 = true;
    count = 0;
    for(box of allbox){
        box.innerText = "";
    }
    msg_box.classList.add("hide");
    
    for(box of allbox){
        box.disabled = false;
    }
})