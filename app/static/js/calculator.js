
document.addEventListener('DOMContentLoaded', function() {

    const calcHeader = document.querySelector('#calc-header');
    const taskText = document.querySelector('#task');
    const solutionText = document.querySelector('#solution');

    const calcKeyboardButtons = document.querySelectorAll('#calc-keyboard-button');

    const helpButton = document.querySelector('#help-button');

    const nameForm = document.querySelector('form');
    const userName = document.querySelector('#user-name');
    const userNameSubmit = document.querySelector('#user-name-submit');
    const sessionId = document.querySelector('#session-id');


    helpButton.onclick = function() {
        fetch("http://127.0.0.1:8000/help", {
            method: "GET",
            headers: {"Content-Type": "application/json"},
        })
        .then(response => response.json())
        .then(data => {
            alert(data.text);
        })
        .catch(error =>{
            alert(`api interacting error`);
            console.log('Error', error)
        });
    }

    async function outSolution(task){
        await fetch("http://127.0.0.1:8000/calc", {
            method: "POST",
            headers: {"Content-Type": "application/json", },
            body: JSON.stringify({'task': task, }),
        })
        .then(response => response.json())
        .then(data => {
            let solution = "= ";

            if (data.solution !== "the task is not correct") {
                solution += data.solution;
            }
            solutionText.innerHTML = solution;
        })
        .catch(error => {
            solutionText.innerHTML = `api interacting error`;
            console.log('Error', error);
        });
    }

    async function outUserName(){
        await fetch("http://127.0.0.1:8000/me", {
            method: "GET",
            headers: {"Content-Type": "application/json", },
        })
        .then(response => response.json())
        .then(data => {
            name = localStorage.getItem('user-name');
            calcHeader.innerHTML = "Calculator for " + name;
            sessionId.innerHTML = "session id - " + data.session ;
        })
        .catch(error => {
            sessionId.innerHTML = `api interacting error`;
            console.log('Error', error);
        });
    }

    async function regUserName(name){
        localStorage.setItem('user-name', name);
        await outUserName();
    }

    userNameSubmit.disabled = true;

    userName.onkeyup = () => {
        userNameSubmit.disabled = userName.value.length <= 0;
    }

    nameForm.onsubmit = function() {
        regUserName(userName.value)

        return false;
    }

    if (!localStorage.getItem('task')){
        localStorage.setItem('task', "enter the task");
    }

    taskText.innerHTML = localStorage.getItem('task');
    outSolution(localStorage.getItem('task'));

    if (!localStorage.getItem('user-name')){
        localStorage.setItem('user-name', "Not defined");
    }

    outUserName();

    calcKeyboardButtons.forEach(function(button) {
        button.onclick = function() {
            let action = button.dataset.key;
            let task = localStorage.getItem('task');

            if (action === "AC") {
                task = "enter the task";
            } else if (action === "C") {
                if (task !== "enter the task") {
                    if (task.length < 2 ) {
                        task = "enter the task";
                    } else {
                        task = task.slice(0, -1);
                    }
                }
            } else {
                if (task === "enter the task") {
                    task = action;
                } else {
                    task = task + action;
                }
            }

            localStorage.setItem('task', task);
            taskText.innerHTML = task;

            outSolution(task);
            outUserName();
        };
    });
})
