document.addEventListener("DOMContentLoaded", () => {
    const result = JSON.parse(localStorage.getItem("result"));

    if (result.status !== "Optimal") {
        alert(result.status);
        window.location.href = "/scheduling/input"
        return;
    }
    
    const p = document.getElementById("salary")
    const salary = document.createElement("p");
    salary.textContent = result.objective;
    p.appendChild(salary);

    const schedule = {};
    assignment = result.data || [];

    assignment.forEach(row => {
        const {day, id, shift} = row;

        if (!schedule[id]) schedule[id] = {};

        if (!schedule[id][day]) schedule[id][day] = [];

        schedule[id][day].push(shift)
    });
    
    printEmployees(schedule);
    

});

function printEmployees(schedule) {
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    const headerRow = document.getElementById("schedule-header")
    days.forEach(day => {
        const th = document.createElement("th");
        th.textContent = day;
        headerRow.appendChild(th);
    })

    const tbody = document.getElementById("schedule-body")
    const e_id = Object.keys(schedule)
    e_id.forEach(id => {
        const tr = document.createElement("tr");

        // first column
        const id_col = document.createElement("td");
        id_col.textContent = id
        tr.appendChild(id_col);

        // insert shifts
        days.forEach(day => {
            const td = document.createElement("td")
            const employees = schedule?.[id]?.[day] || [];
            td.textContent = employees.join(", ");
            tr.appendChild(td);
        });
        tbody.appendChild(tr)
    });

};