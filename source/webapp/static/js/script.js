let add = document.getElementById('add');
let subtract = document.getElementById('subtract');
let multiply = document.getElementById('multiply');
let divide = document.getElementById('divide');
let container = document.getElementById('container');
let error = document.createElement('h3');
let result = document.createElement('h3');
error.style.color = 'red';
error.style.marginTop = '50px';
result.style.color = 'green';
result.style.marginTop = '50px';

async function makeRequest(url, method = 'GET') {
    let response = await fetch(url, {method});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}


async function onClick(event) {
    event.preventDefault();
    target = event.target;
    target.style.backgroundColor ='green';
    let urlCalc = target.dataset.adres;
    let A = document.getElementById('A').value;
    let B = document.getElementById('B').value;
    let url = `http://localhost:8000/${urlCalc}?A=${A}&B=${B}`;
    let response = await makeRequest(url);
    if (response.result) {
        result.innerText = `Результат: ${response.result}` ;
        container.appendChild(result);
    }
    if (response.error) {
        error.innerText = response.error;
        container.appendChild(error);
    }
}


add.addEventListener("click", onClick);
subtract.addEventListener("click", onClick);
multiply.addEventListener("click", onClick);
divide.addEventListener("click", onClick);



