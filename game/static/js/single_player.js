const img_set_arr = ['../static/images/stone_game_img.png', '../static/images/paper_game_img.png', '../static/images/scissor_game_img.png'];
let i = 0;
const img  = document.getElementById('change-img');
let x;
let ans;

function startGame()
{
    img.src = '../static/images/stone_game_img.png';
    x = setInterval(changeImage, 300);
    ans = Math.floor(Math.random() * 3);
    setTimeout(gameResult, 10000);
}

function changeImage()
{
    img.src = img_set_arr[(i + 1) % 3];
    i = i + 1;
}

function gameResult()
{
    console.warn(img.src);
    img.src = ans;
    clearInterval(x);
}