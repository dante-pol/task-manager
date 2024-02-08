console.log("script is work");
// проверка подключения скрипта

let numberTask = 0;
let text = document.getElementById('new_task_txt')    
let data_end = document.getElementById('new_task_done')
let today = new Date();
let dd = String(today.getDate()).padStart(2, '0');
let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
let yyyy = today.getFullYear();
today = mm + '/' + dd + '/' + yyyy;
const tasklist = document.getElementById('tasks_list')


//Создание новой задачи
document.getElementById("new_task_btn").onclick = function add_new_task() {
    let result = eel.create_task(text, today, data_end);
    if(result=='True'){
        alert('Задача успешно создана')
        numberTask ++
    }else{
        alert('result')
    }
}


//Цикл по отображению текущих задач
for(numberTask; numberTask > 0; numberTask--) {
    let li = document.createElement('li');
    li.innerHTML = eel.get_one_task(numberTask)
    tasklist.appendChild(li);
}
