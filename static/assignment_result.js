document.addEventListener("DOMContentLoaded", () => {
    const result = JSON.parse(localStorage.getItem("result"));
    const preferences_count = result.preferences_count;
    const students_in_course = result.students_in_course;
    const preference_assignment_count = result.preference_assignment_count;
    
    createStudentsPreference(preference_assignment_count);
    createAssignedStudents(students_in_course)
})

function createStudentsPreference(preference_assignment_count) {
    const canvas = document.getElementById("studentPref").getContext("2d")
    const data = [{
        label: 'Student Preferences',
        data: preference_assignment_count
    }]
    const chart = new Chart(canvas, {
        type: 'bar',
        data: {
            labels: ['1st', '2nd', '3rd', '4th'],
            datasets: data
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    })

}

function createAssignedStudents(students_in_course) {
    const canvas = document.getElementById("assignedStudents").getContext("2d")
    const values = Object.values(students_in_course)
    const min = Math.min(...values)
    const max = Math.max(...values)
    const data = {
        labels: Object.keys(students_in_course),
        datasets: [{
            label: 'Number of Students Assigned to Course',
            data: Object.values(students_in_course),
            backgroundColor: Object.values(students_in_course).map(value => getColor(value, min, max))
        }]
    }
    const chart = new Chart(canvas, {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            scales: {
                x: {
                    ticks: {
                        autoskip: false,
                        maxRotation: 45
                    }
                },
                y: {
                    beginAtZero: true
                }
            }
        }
    })
}

function getColor(value, min, max) {
    const ratio = (value-min)/(max-min);
    const red = Math.floor(175*ratio);
    const blue = Math.floor(255*(1-ratio));
    return `rgba(${red},150,${blue},0.4)`
}