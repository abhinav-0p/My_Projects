let rock = document.querySelector("#rock");
let paper = document.querySelector("#paper");
let scissor = document.querySelector("#scissor");

let playerscore = document.querySelector("#playerscore");
let compscore = document.querySelector("#compscore");
let msg_box = document.querySelector("#msg-box");
let computerchoice = document.querySelector(".computerchoice");
let move = document.querySelector("#move");
let drawscore = document.querySelector("#drawscore");

let wincount = 0;
let compwin = 0;
let draw = 0;

const randomnum = () => {
    choice = ["Rock","Paper","Scissor"];
    compchoice = choice[Math.floor(Math.random() * choice.length)];
}

rock.addEventListener("click" , () => {
    r = "Rock";
    randomnum();
    if(compchoice === "Scissor" ){
        wincount++;
        move.innerText = " Congrats,You win!";
        playerscore.innerText = `Player : ${wincount}`;
        computerchoice.innerHTML = `<img src="scissor2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;
        move.style.color = "rgb(90, 253, 2)";
    }
    else if(compchoice === "Paper") {
        compwin++;
        move.innerText = " Computer jii win!";
        compscore.innerText = `Computer : ${compwin}`;
        move.style.color = "rgb(253, 253, 2)";

        computerchoice.innerHTML = `<img src="paper2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;
    }
    else{
        draw++;
        move.innerText = "It's a draw!";
        drawscore.innerText = `Draw : ${draw}`;
        move.style.color = "rgb(255, 255, 255)";

        computerchoice.innerHTML = `<img src="rock2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;
    }
})

paper.addEventListener("click" , () => {
    p = "Paper";
    randomnum();
    if(compchoice === "Rock" ){
        wincount++;
        move.innerText = " Congrats,You win!";
        playerscore.innerText = `Player : ${wincount}`;
        move.style.color = "rgb(90, 253, 2)";
        computerchoice.innerHTML = `<img src="rock2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;

    }
    else if(compchoice === "Scissor") {
        compwin++;
        move.innerText = " Computer jii win!";
        compscore.innerText = `Computer : ${compwin}`;
        move.style.color = "rgb(253, 253, 2)";
        computerchoice.innerHTML = `<img src="scissor2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;


    }
    else{
        draw++;
        move.innerText = "It's a draw!";
        drawscore.innerText = `Draw : ${draw}`;
        move.style.color = "rgb(255, 255, 255)";
        computerchoice.innerHTML = `<img src="paper2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;

    }
})

scissor.addEventListener("click" , () => {
    s = "Scissor";
    randomnum();
    if(compchoice === "Paper" ){
        wincount++;
        move.innerText = " Congrats,You win!";
        playerscore.innerText = `Player : ${wincount}`;
        move.style.color = "rgb(90, 253, 2)";
        computerchoice.innerHTML = `<img src="paper2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;

    }
    else if(compchoice === "Rock") {
        compwin++;
        move.innerText = " Computer jii win!";
        compscore.innerText = `Computer : ${compwin}`;
        move.style.color = "rgb(253, 253, 2)";
        computerchoice.innerHTML = `<img src="rock2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;

    }
    else{
        draw++;
        move.innerText = "It's a draw!";
        drawscore.innerText = `Draw : ${draw}`;
        move.style.color = "rgb(255, 255, 255)";
        computerchoice.innerHTML = `<img src="scissor2.png.jpg" style="width: 100%; height: 100%; object-fit: contain;">`;
    }
})