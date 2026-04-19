document.addEventListener("DOMContentLoaded", () => {
    const result = JSON.parse(localStorage.getItem("result"));
    console.log(result.data);

    if (result.status !== "Optimal") {
        alert(result.status);
        window.location.href = "/scheduling/input"
        return;
    }

    const schedule = {};
    assignment = result.data || [];

    assignment.forEach(row => {
        const {day, id, shift} = row;

        if (!schedule[day]) schedule[day] = {};

        if (!schedule[day][shift]) schedule[day][shift] = [];

        schedule[day][shift].push(id)
    });

    // create shift header
    const shifts = ["Account opening",
        "Credit card application",
        "Loan Application",
        "Mortgage Consultation",
        "Retirement planning",
        "Financial advising",
        "Wealth management"
    ];
    const headerRow = document.getElementById("schedule-header")
    shifts.forEach(shift => {
        const th = document.createElement("th");
        th.textContent = shift;
        headerRow.appendChild(th);
    })

    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

    const tbody = document.getElementById("schedule-body")
    days.forEach(day => {
        const tr = document.createElement("tr");

        // first column
        const day_label = document.createElement("td");
        day_label.textContent = day;
        tr.appendChild(day_label);

        // insert employees
        shifts.forEach(shift => {
            const td = document.createElement("td")
            const employees = schedule?.[day]?.[shift] || [];
            td.textContent = employees.join(", ");
            tr.appendChild(td);
        });
        tbody.appendChild(tr)
    });

});